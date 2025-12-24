"""
CBSE Std 9 Learning Assistant Agent
Core agent implementation with autonomous diagram generation
"""

import os
import json
from typing import List, Dict
from dotenv import load_dotenv
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

# CBSE Std 9 specific system prompt
LEARNING_AGENT_PROMPT = """You are a friendly and patient learning tutor for a 13-year-old CBSE Standard 9 student.

**Your Teaching Style:**
- Use simple, age-appropriate language
- Break down complex concepts into easy steps
- Give real-world examples that relate to a teenager's life
- Encourage questions and curiosity
- Be patient and supportive, never condescending
- Use analogies and visuals (describe them) when helpful

**AGENTIC CAPABILITIES - YOU CAN GENERATE DIAGRAMS!**
You have special powers to create visual diagrams! When explaining concepts that benefit from visualization, YOU SHOULD AUTOMATICALLY use these tools:

1. **plot_quadratic_function** - For quadratic equations, parabolas (e.g., y = x² - 5x + 6)
2. **plot_linear_function** - For linear equations, slopes (e.g., y = 2x + 3)
3. **draw_cell_diagram** - For plant/animal cell structure
4. **plot_motion_graph** - For physics motion, speed, velocity
5. **draw_triangle** - For geometry, triangle types

**When to Generate Diagrams (IMPORTANT):**
- Math: When discussing equations, graphs, functions, geometry
- Biology: When explaining cells, their parts
- Physics: When explaining motion, graphs of movement (distance-time, velocity-time)
- Geometry: When discussing shapes, triangles

**IMPORTANT:** Only use tools for topics they're designed for. If a student asks about something you don't have a tool for (like capacitors, circuits, atoms), politely explain that you can describe it with words but don't have a diagram tool for that specific topic yet.

After generating a diagram, tell the student: "I've created a visual diagram for you! Check the 'diagrams' folder to see: [filename]"

**CBSE Std 9 Subjects You Help With:**
1. **Mathematics**: Algebra, Geometry, Trigonometry, Statistics, Coordinate Geometry
2. **Science**: Physics (Motion, Force, Gravitation), Chemistry (Matter, Atoms), Biology (Cells, Tissues)
3. **Social Science**: History, Geography, Civics, Economics
4. **English**: Grammar, Literature, Writing skills
5. **Hindi**: Grammar, Literature (if asked)

**Teaching Approach:**
1. First, understand what the student needs help with
2. Check their current understanding level
3. Decide if a diagram would help - if yes, generate it!
4. Explain the concept step-by-step
5. Reference the diagram if you created one
6. Provide examples
7. Ask if they need clarification
8. Offer practice questions when appropriate
9. Celebrate their understanding!

**Writing Math Equations (IMPORTANT for Web Display):**
When writing mathematical equations in your responses:
- Use LaTeX format for complex equations: $equation$ for inline, $$equation$$ for display
- For simple superscripts: write x² as $x^2$, x³ as $x^3$
- For fractions: write $\frac{numerator}{denominator}$
- For square roots: write $\sqrt{number}$
- Examples:
  * "The equation $x^2 - 5x + 6 = 0$" instead of "The equation x² - 5x + 6 = 0"
  * "Using the formula $a = \frac{v - u}{t}$" instead of "Using the formula a = (v - u) / t"
  * "Newton's Second Law: $F = ma$"
  * "Energy equation: $E = mc^2$"

**Important Rules:**
- Never just give direct answers to homework - guide them to discover
- Show step-by-step working for math/science problems
- Connect new concepts to what they already know
- Make learning fun and engaging
- If a topic is outside Std 9 syllabus, gently mention it but still help
- PROACTIVELY generate diagrams when they would help understanding!

Remember: Your goal is to help them UNDERSTAND, not just memorize! Use your diagram powers wisely!"""


class LearningAgent:
    """CBSE Learning Agent with autonomous diagram generation capabilities"""
    
    def __init__(self, tool_functions: dict = None, diagram_tools: list = None):
        """
        Initialize the learning agent
        
        Args:
            tool_functions: Dict mapping tool names to function implementations
            diagram_tools: List of tool definitions for OpenAI function calling
        """
        # Get GitHub token from environment
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            raise ValueError(
                "GITHUB_TOKEN not found! Please:\n"
                "1. Copy .env.example to .env\n"
                "2. Get your GitHub token from: https://github.com/settings/tokens\n"
                "3. Add it to the .env file"
            )
        
        # Connect to GitHub Models
        self.client = AsyncOpenAI(
            base_url="https://models.github.ai/inference",
            api_key=github_token,
        )
        
        self.model = "openai/gpt-4.1-mini"  # Fast, smart, affordable
        self.conversation_history: List[Dict[str, str]] = [
            {"role": "system", "content": LEARNING_AGENT_PROMPT}
        ]
        
        # Tool functions and definitions
        self.tool_functions = tool_functions or {}
        self.diagram_tools = diagram_tools or []
    
    async def _execute_tool(self, tool_name: str, tool_args: dict) -> str:
        """Execute a tool function and return the result"""
        try:
            if tool_name in self.tool_functions:
                result = self.tool_functions[tool_name](**tool_args)
                return f"Diagram created successfully: {result}"
            else:
                return f"❌ Unknown tool: {tool_name}"
        except Exception as e:
            return f"❌ Error creating diagram: {str(e)}"
    
    async def chat(self, user_message: str) -> str:
        """Send a message and get response (non-streaming)"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Get response with tool calling enabled
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            tools=self.diagram_tools if self.diagram_tools else None,
            tool_choice="auto" if self.diagram_tools else None,
            temperature=0.7,
            max_tokens=2000,
        )
        
        assistant_message = response.choices[0].message
        tool_calls = assistant_message.tool_calls
        
        # If agent wants to use tools, execute them
        if tool_calls:
            # Add assistant's tool call to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in tool_calls
                ]
            })
            
            # Execute each tool
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                
                print(f"\nAgent is creating a diagram: {tool_name}...", flush=True)
                result = await self._execute_tool(tool_name, tool_args)
                
                # Add tool result to history
                self.conversation_history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
            
            # Get final response after tool execution
            final_response = await self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=0.7,
                max_tokens=2000,
            )
            
            final_content = final_response.choices[0].message.content
            self.conversation_history.append({
                "role": "assistant",
                "content": final_content
            })
            
            return final_content
        else:
            # No tools used, just return the response
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message.content
            })
            return assistant_message.content
    
    async def chat_stream(self, user_message: str):
        """Send a message and get streaming response with tool support"""
        # Add user message to history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # First, check if tools are needed (non-streaming call)
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=self.conversation_history,
            tools=self.diagram_tools if self.diagram_tools else None,
            tool_choice="auto" if self.diagram_tools else None,
            temperature=0.7,
            max_tokens=2000,
        )
        
        assistant_message = response.choices[0].message
        tool_calls = assistant_message.tool_calls
        
        # If agent wants to use tools
        if tool_calls:
            # Add assistant's tool call to history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in tool_calls
                ]
            })
            
            # Execute tools
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)
                
                yield f"\n\nCreating diagram: {tool_name}...\n"
                result = await self._execute_tool(tool_name, tool_args)
                yield f"{result}\n\n"
                
                # Add tool result to history
                self.conversation_history.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result
                })
            
            # Get final response with streaming
            try:
                stream = await self.client.chat.completions.create(
                    model=self.model,
                    messages=self.conversation_history,
                    temperature=0.7,
                    max_tokens=2000,
                    stream=True,
                )
                
                full_response = ""
                async for chunk in stream:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        full_response += content
                        yield content
                
                # Add complete response to history
                self.conversation_history.append({
                    "role": "assistant",
                    "content": full_response
                })
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                yield error_msg
                self.conversation_history.append({
                    "role": "assistant",
                    "content": error_msg
                })
        else:
            # No tools, just stream the response
            full_response = assistant_message.content
            
            # Add to history
            self.conversation_history.append({
                "role": "assistant",
                "content": full_response
            })
            
            # Yield the response
            yield full_response
    
    def clear_history(self):
        """Clear conversation history (keep system prompt)"""
        self.conversation_history = [
            {"role": "system", "content": LEARNING_AGENT_PROMPT}
        ]
