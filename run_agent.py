"""
CBSE Std 9 Learning Agent - Command Line Runner
Simple entry point for the modular agent package
"""

import asyncio
from agent import LearningAgent
from tools import get_tool_functions, DIAGRAM_TOOLS, cleanup_old_diagrams


async def main():
    """Run the learning agent in terminal"""
    print("=" * 60)
    print("CBSE Std 9 Learning Agent")
    print("AI Tutor with Autonomous Diagram Generation")
    print("=" * 60)
    print()
    
    # Clean up old diagrams
    cleanup_old_diagrams(max_age_seconds=3600)
    
    # Initialize agent with tools
    print("Initializing agent...")
    tool_functions = get_tool_functions()
    agent = LearningAgent(
        tool_functions=tool_functions,
        diagram_tools=DIAGRAM_TOOLS
    )
    print("Agent ready! (Type 'quit' to exit, 'clear' to reset)\n")
    
    while True:
        try:
            # Get user input
            question = input("\nYou: ").strip()
            
            if not question:
                continue
            
            if question.lower() in ['quit', 'exit', 'bye']:
                print("\nGoodbye! Keep learning!")
                break
            
            if question.lower() == 'clear':
                agent.clear_history()
                cleanup_old_diagrams(max_age_seconds=0)
                print("Conversation cleared!\n")
                continue
            
            # Get response
            print("\nAgent: ", end="", flush=True)
            
            async for chunk in agent.chat_stream(question):
                print(chunk, end="", flush=True)
            
            print()  # New line after response
            
        except KeyboardInterrupt:
            print("\n\nGoodbye! Keep learning!")
            break
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    asyncio.run(main())
