# CBSE Std 9 Learning Assistant

## Backstory

My son is fascinated by LLMs and loves experimenting with AI. However, I quickly realized that:

- **Learning-optimized AI models aren't free** - Services like ChatGPT's tutoring mode or specialized educational AI tools come with subscription costs
- **Generic LLMs don't prioritize learning** - Standard system prompts aren't designed to encourage understanding, break down concepts, or teach step-by-step
- **He needed something tailored** - A patient tutor specifically built for CBSE Standard 9 curriculum (age 13)

So I built this AI agent for him - a completely free, learning-focused tutor that uses GitHub Models and is designed from the ground up to teach, not just answer.

## About This App

This is an **AI Learning Agent** (not just a chatbot) specifically designed for CBSE Standard 9 students. It combines:

**1. Learning-First System Prompt**
- Age-appropriate language (13-year-old friendly)
- Encourages understanding over memorization
- Breaks complex concepts into simple steps
- Connects new topics to what students already know
- Patient and encouraging teaching style

**2. Autonomous Agent Capabilities**
- **Thinks independently**: Decides when visual aids would help learning
- **Uses tools**: Automatically generates diagrams (graphs, cell structures, motion charts)
- **Takes action**: Creates and saves visualization files
- **Explains work**: Shows reasoning and guides discovery

**3. Cost-Effective & Open**
- Completely free using GitHub Models (gpt-4.1-mini)
- No subscription or credit card required
- Open source - modify the system prompt for your needs
- Self-hostable for privacy

## What It Does

**Covers all CBSE Std 9 Subjects:**
- Mathematics (Algebra, Geometry, Trigonometry, Statistics)
- Science (Physics, Chemistry, Biology)
- Social Science (History, Geography, Civics, Economics)
- English (Grammar, Literature, Writing)
- Hindi (Grammar, Literature)

**Teaching Approach:**
- Guides students to discover answers (doesn't just give them)
- Shows step-by-step working for math and science
- Provides real-world examples relevant to teenagers
- Remembers conversation context across multiple questions
- Creates diagrams automatically when they aid understanding

**Visual Learning - Autonomous Diagram Generation:**

The agent **automatically decides** when to create visual aids:
- Quadratic & linear function graphs (for algebra)
- Plant & animal cell diagrams (for biology)
- Motion graphs: distance-time, velocity-time (for physics)
- Geometric shapes and triangles (for geometry)

## Modular Architecture

```
LearningAgent/
├── agent/              # Core agent logic
├── tools/              # Diagram generation tools  
├── web/                # Streamlit web interface
├── diagrams/           # Temporary folder (auto-cleaned)
├── run_agent.py        # CLI runner
├── run_web.py          # Web runner
└── requirements.txt
```

**Benefits:**
- Separation of concerns
- Easy testing & reusability
- Clean imports & dependencies
- Scalable structure

See [ARCHITECTURE.md](ARCHITECTURE.md) for details.

## Quick Start

### Prerequisites
- Python 3.9 or higher
- GitHub Personal Access Token
- Internet connection

### Installation

**1. Install dependencies**
```bash
pip install -r requirements.txt
```

**2. Get GitHub Token**
1. Go to https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Give it a name like "Learning Agent"
4. **No special scopes needed**
5. Copy the token

**3. Configure Environment**
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your token
GITHUB_TOKEN=ghp_your_token_here
```

## Usage

### Option 1: Command Line (Terminal)
```bash
python run_agent.py
```
- Simple text interface
- See diagrams created in `diagrams/` folder
- Type 'quit' to exit, 'clear' to reset

### Option 2: Web Interface (Browser)
```bash
streamlit run run_web.py
```
Or the simpler:
```bash
python run_web.py
```
Then open http://localhost:8501 in your browser

**Features:**
- Beautiful chat interface
- Inline diagram display
- Mobile-friendly
- Clear conversation button
- Math equation rendering

### Option 3: Import in Your Code
```python
from agent import LearningAgent
from tools import get_tool_functions, DIAGRAM_TOOLS

# Initialize agent
tool_functions = get_tool_functions()
agent = LearningAgent(
    tool_functions=tool_functions,
    diagram_tools=DIAGRAM_TOOLS
)

# Chat
import asyncio

async def chat():
    async for chunk in agent.chat_stream("Explain x² - 5x + 6 = 0"):
        print(chunk, end="", flush=True)

asyncio.run(chat())
```

## Deployment to Cloud

Deploy to Streamlit Cloud for free internet access from anywhere!

See [DEPLOYMENT.md](DEPLOYMENT.md) for complete instructions.

**Quick steps:**
1. Push code to GitHub
2. Connect Streamlit Cloud to your repo
3. Add GITHUB_TOKEN to Streamlit secrets
4. Deploy!

Your app will be live at: `https://your-username-learning-agent.streamlit.app`

## Documentation

- **[SETUP.md](SETUP.md)** - Detailed setup guide
- **[QUICKSTART.md](QUICKSTART.md)** - Quick testing guide
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Cloud deployment
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - Modular structure explanation

## Diagrams Folder

The `diagrams/` folder is **temporary** and automatically cleaned:
- On app start: Removes diagrams older than 1 hour
- On clear conversation: Removes all diagrams
- Manual: Use `cleanup_old_diagrams(max_age_seconds=3600)`

No need to worry about disk space!

## Development

**Project Structure:**
```python
# Agent package - Core logic
from agent import LearningAgent, LEARNING_AGENT_PROMPT

# Tools package - Diagram generation
from tools import (
    plot_quadratic_function,
    draw_cell_diagram,
    plot_motion_graph,
    DIAGRAM_TOOLS,
    get_tool_functions,
    cleanup_old_diagrams
)

# Web package - UI
from web import main
```

**Run tests:**
```bash
python example_usage.py
```How Students Should Use It

**For Understanding Concepts:**
- "Explain photosynthesis in simple words"
- "What's the difference between speed and velocity?"
- "How does the French Revolution connect to what we learned before?"

**For Homework Help:**
- "I have this problem: x² - 5x + 6 = 0. How do I approach it?"
- "Can you show me step-by-step how to solve this?"
- "I got this answer, can you check if my approach is correct?"

**For Clarification:**
- "I still don't understand, can you explain it differently?"
- "Can you give me a real-world example?"
- "What if the numbers were different?"

**Note:** The agent will automatically create diagrams when it thinks visuals will help you understand better!cally, but you can explicitly ask  
- **Step-by-step**: "Show me step-by-step" for detailed explanations  
- *Why This Approach?

**Problem with Generic LLMs:**
- They're designed for general conversation, not teaching
- System prompts aren't optimized for step-by-step learning
- No age-appropriate language targeting
- Can't generate visual learning aids autonomously
- Premium "tutor modes" require expensive subscriptions

**This Solution:**
- System prompt **specifically designed for learning** - encourages understanding, not memorization
- **Agent capabilities** - autonomously creates diagrams when helpful
- **Free forever** - uses GitHub Models (no credit card needed)
- **Customizable** - modify the teaching style in the system prompt
- **Privacy-friendly** - self-host if desired

## Technology Stack

**AI Model:** gpt-4.1-mini via GitHub Models
- Free with GitHub Personal Access Token
- Fast response times
- Excellent reasoning for math & science
- No credit card or subscription required

**Why GitHub Models?**
- CCustomization

The key to this working well is the **system prompt** in `agent/learning_agent.py`. You can:

- Adjust the teaching style (more formal/casual)
- Change age-appropriate language
- Add/remove subject focus areas
- Modify when diagrams are generated
- Customize the personality of the tutor

Feel free to experiment with the prompt to suit your child's learning style!

## Future Ideas

- Add more diagram types (circuits, chemistry structures, atoms)
- Calculator tool for quick computations
- Quiz generation for practice
- Progress tracking across sessions
- Hindi medium support
- CFor Parents & Educators

This project demonstrates that:
- You **don't need expensive subscriptions** for AI-powered learning
- A well-crafted **system prompt matters more** than using premium models
- **Open source + free models** can deliver excellent educational experiences
- **Agentic capabilities** (tool use) make learning more visual and engaging

If this helps your child learn, consider:
- Customizing the system prompt for their specific needs
- Adding more diagram types for their weak areas
- Deploying it for easy access from any device
- Contributing improvements back to the community

## Contributing

Built this for my son, sharing it with the community. Feel free to:
- Add new diagram generation tools
- Improve the teaching system prompt
- Add support for more curricula (not just CBSE)
- Enhance the UI/UX
- Share your modifications

## License

MIT License - Free to use, modify, and share for educational purposes.

---

**A father's weekend project | Built for CBSE Std 9 students | Powered by GitHub Models (free tier)
- Old files are deprecated but still work
- Use new modular imports (see ARCHITECTURE.md)

## Future Enhancements

- Add more diagram types (circuits, chemistry)
- Calculator tool for quick math
- Quiz generation for practice
- Progress tracking
- Multi-language support (Hindi medium)
- Code executor for programming concepts
- Export conversations as PDF

## Technical Details

**Python Version:** 3.9+  
**Framework:** OpenAI SDK (AsyncOpenAI)  
**Model:** gpt-4.1-mini via GitHub Models  
**UI:** Streamlit  
**Visualization:** Matplotlib, Pillow  
**Agent Pattern:** Autonomous tool use with function calling  

## Contributing

This is a learning project! Feel free to:
- Add new diagram types
- Improve system prompts
- Add more subjects
- Enhance UI
- Report issues

## License

MIT License - Feel free to use and modify for your learning needs!

---

**Made for CBSE Std 9 students | Powered by GitHub Models**
