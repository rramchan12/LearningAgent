"""
Example: How to use the modular Learning Agent
"""

import asyncio
from agent import LearningAgent
from tools import get_tool_functions, DIAGRAM_TOOLS, cleanup_old_diagrams


async def example_basic_usage():
    """Basic usage example"""
    print("=" * 60)
    print("Example 1: Basic Agent Usage")
    print("=" * 60)
    
    # Initialize agent with tools
    tool_functions = get_tool_functions()
    agent = LearningAgent(
        tool_functions=tool_functions,
        diagram_tools=DIAGRAM_TOOLS
    )
    
    # Ask a question
    question = "Explain the quadratic equation x² - 5x + 6 = 0"
    print(f"\nQuestion: {question}")
    print("\nResponse:")
    
    async for chunk in agent.chat_stream(question):
        print(chunk, end="", flush=True)
    
    print("\n")


async def example_diagram_generation():
    """Example with diagram generation"""
    print("=" * 60)
    print("Example 2: Autonomous Diagram Generation")
    print("=" * 60)
    
    tool_functions = get_tool_functions()
    agent = LearningAgent(
        tool_functions=tool_functions,
        diagram_tools=DIAGRAM_TOOLS
    )
    
    # Question that should trigger diagram
    question = "Show me a plant cell diagram"
    print(f"\nQuestion: {question}")
    print("\nResponse:")
    
    async for chunk in agent.chat_stream(question):
        print(chunk, end="", flush=True)
    
    print("\n")


async def example_cleanup():
    """Example of cleaning up diagrams"""
    print("=" * 60)
    print("Example 3: Cleanup Old Diagrams")
    print("=" * 60)
    
    # Clean diagrams older than 10 seconds (for testing)
    print("\nCleaning up old diagrams...")
    cleanup_old_diagrams(max_age_seconds=10)
    print("Cleanup complete!")


async def main():
    """Run all examples"""
    await example_basic_usage()
    await example_diagram_generation()
    await example_cleanup()


if __name__ == "__main__":
    asyncio.run(main())
