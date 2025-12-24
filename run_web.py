"""
Streamlit Web App Runner
Simple entry point for the modular web package
"""

import sys
from pathlib import Path

# Add the current directory to Python path to ensure packages can be imported
if str(Path(__file__).parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).parent))

from web import main

if __name__ == "__main__":
    main()
