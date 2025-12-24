# Modular Architecture

The codebase has been refactored into a clean, modular structure:

## Package Structure

```
LearningAgent/
├── agent/                  # Core agent logic
│   ├── __init__.py
│   └── learning_agent.py  # LearningAgent class, system prompt
│
├── tools/                  # Diagram generation tools
│   ├── __init__.py
│   └── diagram_tools.py   # All diagram functions, cleanup utility
│
├── web/                    # Streamlit web interface
│   ├── __init__.py
│   └── app.py            # Web UI, chat interface
│
├── diagrams/              # Temporary folder (auto-cleaned)
│
├── run_agent.py           # CLI runner: python run_agent.py
├── run_web.py             # Web runner: streamlit run run_web.py
│
└── legacy files/          # Deprecated (use above instead)
    ├── learning_agent.py  → use agent/learning_agent.py
    ├── diagram_tools.py   → use tools/diagram_tools.py
    └── streamlit_app.py   → use web/app.py
```

## Usage

### Command Line Interface
```bash
python run_agent.py
```

### Web Interface
```bash
streamlit run run_web.py
# or
python run_web.py
```

### Import in Your Code
```python
# Agent
from agent import LearningAgent, LEARNING_AGENT_PROMPT

# Tools
from tools import (
    DIAGRAM_TOOLS,
    get_tool_functions,
    cleanup_old_diagrams,
    plot_quadratic_function,
    draw_cell_diagram,
)

# Web app
from web import main
```

## Diagrams Cleanup

The `diagrams/` folder is temporary and automatically cleaned:
- **On app start**: Removes diagrams older than 1 hour
- **On clear conversation**: Removes all diagrams
- **Manual cleanup**: Use `cleanup_old_diagrams(max_age_seconds=3600)`

## Benefits of Modular Structure

- **Separation of concerns**: Agent, tools, and UI are independent  
- **Easy testing**: Test each package separately  
- **Reusability**: Import agent in other projects  
- **Maintainability**: Changes in one package don't affect others  
- **Scalability**: Add new packages (e.g., evaluation, memory) easily

## Development

Each package has a clear responsibility:

- **agent/**: Contains the AI logic, conversation management, tool execution
- **tools/**: Pure functions for diagram generation, no agent dependencies
- **web/**: UI layer, depends on agent and tools but isolated from core logic

## Documentation

- **README.md**: General project information
- **SETUP.md**: Quick start guide
- **DEPLOYMENT.md**: Cloud deployment instructions
- **QUICKSTART.md**: Local testing guide
- **ARCHITECTURE.md**: This file (modular structure explanation)
