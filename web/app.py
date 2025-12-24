"""
Streamlit Web Interface for CBSE Std 9 Learning Assistant
Access from any browser - works on desktop, tablet, phone!
"""

import streamlit as st
import asyncio
import os
from pathlib import Path
from PIL import Image
import re

# Import from modular packages
from agent import LearningAgent
from tools import cleanup_old_diagrams, get_tool_functions, DIAGRAM_TOOLS


# Page configuration
st.set_page_config(
    page_title="CBSE Std 9 Learning Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better appearance and math rendering
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .user-message {
        background-color: #e3f2fd;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .assistant-message {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .stButton>button {
        width: 100%;
    }
    /* Better math rendering */
    .katex {
        font-size: 1.2em !important;
    }
    code {
        background-color: #f0f0f0;
        padding: 2px 6px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables"""
    if 'agent' not in st.session_state:
        st.session_state.agent = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'initialized' not in st.session_state:
        st.session_state.initialized = False


async def get_agent_response(agent, question):
    """Get response from agent (async)"""
    response_text = ""
    diagrams = []
    
    async for chunk in agent.chat_stream(question):
        response_text += chunk
        
        # Check if chunk mentions diagram creation
        if "Creating diagram:" in chunk or "Diagram created successfully:" in chunk:
            # Extract diagram path if present
            if "Q:" in chunk or "diagrams/" in chunk:
                paths = re.findall(r'(?:Q:\\workspace\\LearningAgent\\)?diagrams[/\\][\w\-\.]+\.png', chunk)
                diagrams.extend(paths)
    
    return response_text, diagrams


def display_diagram(diagram_path):
    """Display a generated diagram"""
    try:
        # Normalize path
        if not diagram_path.startswith('Q:'):
            diagram_path = Path("diagrams") / Path(diagram_path).name
        else:
            diagram_path = Path(diagram_path)
        
        if diagram_path.exists():
            image = Image.open(diagram_path)
            st.image(image, caption=diagram_path.name, use_container_width=True)
        else:
            st.warning(f"Diagram not found: {diagram_path}")
    except Exception as e:
        st.error(f"Error displaying diagram: {e}")


def enhance_math_rendering(content: str) -> str:
    """Enhance markdown content with better LaTeX math rendering"""
    # Handle inline equations like x² with proper superscript
    content = re.sub(r'x²', r'$x^2$', content)
    content = re.sub(r'x³', r'$x^3$', content)
    content = re.sub(r'(\d+)²', r'$\1^2$', content)
    content = re.sub(r'(\d+)³', r'$\1^3$', content)
    
    # Common math patterns
    content = re.sub(r'F = ma', r'$F = ma$', content)
    content = re.sub(r'E = mc²', r'$E = mc^2$', content)
    content = re.sub(r'a = \(v - u\) / t', r'$a = \frac{v - u}{t}$', content)
    
    return content


def main():
    """Main application"""
    init_session_state()
    
    # Clean up old diagrams on startup (keep last 1 hour)
    if not st.session_state.initialized:
        cleanup_old_diagrams(max_age_seconds=3600)
    
    # Sidebar
    with st.sidebar:
        st.markdown("## CBSE Learning Assistant")
        st.markdown("---")
        
        st.markdown("### About")
        st.info("""
        Your AI-powered learning buddy for CBSE Standard 9!
        
        **Features:**
        - All subjects: Math, Science, Social Science, English
        - Age-appropriate explanations
        - Automatic diagram generation
        - Step-by-step guidance
        """)
        
        st.markdown("---")
        st.markdown("### Supported Diagrams")
        st.markdown("""
        - Math equations & graphs
        - Cell structures
        - Motion graphs
        - Geometric shapes
        """)
        
        st.markdown("---")
        if st.button("Clear Conversation", use_container_width=True):
            st.session_state.messages = []
            if st.session_state.agent:
                st.session_state.agent.clear_history()
            # Clean up diagrams when clearing conversation
            cleanup_old_diagrams(max_age_seconds=0)
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Tips")
        st.markdown("""
        - Be specific with questions
        - Ask for examples
        - Request step-by-step explanations
        - The agent will create diagrams automatically!
        """)
    
    # Main content
    st.markdown('<div class="main-header">CBSE Std 9 Learning Assistant</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">AI Agent with Autonomous Diagram Generation</div>', unsafe_allow_html=True)
    
    # Initialize agent
    if not st.session_state.initialized:
        try:
            with st.spinner("Initializing AI Agent..."):
                # Get tool functions and diagram tool definitions
                tool_functions = get_tool_functions()
                
                # Create agent with tools
                st.session_state.agent = LearningAgent(
                    tool_functions=tool_functions,
                    diagram_tools=DIAGRAM_TOOLS
                )
                st.session_state.initialized = True
                st.success("Agent ready! Ask me anything about CBSE Std 9 subjects!")
        except ValueError as e:
            st.error(f"❌ {str(e)}")
            st.info("""
            **Setup Required:**
            1. Get GitHub Personal Access Token from: https://github.com/settings/tokens
            2. Add to Streamlit secrets (Settings → Secrets in Streamlit Cloud)
            3. Or add to `.env` file locally
            """)
            st.stop()
        except Exception as e:
            st.error(f"❌ Error initializing agent: {e}")
            st.stop()
    
    # Chat container
    chat_container = st.container()
    
    # Display chat history
    with chat_container:
        for message in st.session_state.messages:
            if message["role"] == "user":
                with st.chat_message("user"):
                    st.markdown(message["content"])
            else:
                with st.chat_message("assistant"):
                    # Enhanced markdown rendering with LaTeX support
                    content = enhance_math_rendering(message["content"])
                    st.markdown(content, unsafe_allow_html=True)
                    
                    # Display diagrams if any
                    if "diagrams" in message and message["diagrams"]:
                        st.markdown("**Generated Diagrams:**")
                        cols = st.columns(len(message["diagrams"]))
                        for idx, diagram in enumerate(message["diagrams"]):
                            with cols[idx]:
                                display_diagram(diagram)
    
    # Input area
    if prompt := st.chat_input("Ask me anything about CBSE Std 9 subjects..."):
        # Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Run async function
                    response, diagrams = asyncio.run(
                        get_agent_response(st.session_state.agent, prompt)
                    )
                    
                    # Display response with enhanced math rendering
                    response_display = enhance_math_rendering(response)
                    st.markdown(response_display, unsafe_allow_html=True)
                    
                    # Display diagrams if generated
                    if diagrams:
                        st.markdown("**Generated Diagrams:**")
                        cols = st.columns(len(diagrams))
                        for idx, diagram in enumerate(diagrams):
                            with cols[idx]:
                                display_diagram(diagram)
                    
                    # Add to message history
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "diagrams": diagrams
                    })
                    
                except Exception as e:
                    error_msg = f"❌ Error: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": error_msg,
                        "diagrams": []
                    })
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        Powered by GitHub Models (gpt-4.1-mini) | Built for learning
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
