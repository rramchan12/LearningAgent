# Quick Start Guide

## Step-by-Step Setup (5 minutes)

### Step 1: Install Python Dependencies

Open PowerShell in this folder and run:

```powershell
pip install agent-framework-azure-ai --pre
pip install openai python-dotenv
```

⚠️ **Important**: The `--pre` flag is required while Agent Framework is in preview.

Or simply install all from requirements.txt:
```powershell
pip install -r requirements.txt
```

---

### Step 2: Get Your GitHub Personal Access Token (PAT)

#### Why do I need this?
GitHub Models provides free AI models, but needs a token to identify your account.

#### How to get it:

1. **Go to GitHub**: https://github.com/settings/tokens

2. **Click**: "Generate new token (classic)"

3. **Fill in**:
   - Note: `Learning Agent` (or any name)
   - Expiration: `90 days` (or choose your preference)
   - **Scopes**: No special scopes needed! Just generate.

4. **Generate token** and **COPY IT** (you won't see it again!)

   It looks like: `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

### Step 3: Configure Your Token

**Option A: Using .env file (Recommended)**

```powershell
# Copy the example file
copy .env.example .env
```

Then edit `.env` file and replace `your_github_token_here` with your actual token:

```
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**Option B: Set Environment Variable (Temporary)**

In PowerShell:
```powershell
$env:GITHUB_TOKEN="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

Note: This only works for the current PowerShell session.

---

### Step 4: Run the Learning Agent

```powershell
python learning_agent.py
```

You should see:
```
============================================================
CBSE Std 9 Learning Assistant
============================================================
Hi! I'm your learning buddy for CBSE Standard 9.
Ask me anything about Math, Science, Social Science, or English!

Type 'exit' or 'quit' to end the session.
============================================================

You: _
```

---

## Try Sample Conversations

Run pre-built examples to see the agent in action:

```powershell
python examples.py
```

Choose from:
1. Math - Quadratic Equations
2. Physics - Newton's Law
3. Biology - Cell Structure
4. History - French Revolution
5. Homework Guidance

---

## Usage Tips

### Good Questions:
✅ "Explain photosynthesis in simple words"  
✅ "How do I solve quadratic equations?"  
✅ "What's the difference between speed and velocity?"  
✅ "Help me understand the French Revolution"  

### Follow-up Questions:
✅ "Can you give another example?"  
✅ "What if the numbers were different?"  
✅ "I still don't get it, can you explain again?"  
✅ "Show me step-by-step"  

### For Homework:
✅ "I have this problem: [paste problem]. How do I approach it?"  
✅ "What formula should I use for this?"  
✅ "Can you check my working?"  

---

## Troubleshooting

### ❌ Error: "GITHUB_TOKEN not found"

**Solution**: Make sure you created the `.env` file and added your token.

Check:
```powershell
cat .env
```

Should show:
```
GITHUB_TOKEN=ghp_...
```

---

### ❌ Error: "Invalid authentication credentials"

**Reasons**:
1. Token expired - Generate a new one
2. Token copied incorrectly - Check for extra spaces
3. No internet connection

**Solution**: 
- Generate a new token from https://github.com/settings/tokens
- Update `.env` file

---

### ❌ Error: "Module not found: agent_framework"

**Solution**: Install with the `--pre` flag:
```powershell
pip install agent-framework-azure-ai --pre
```

---

### ⏰ Agent is slow to respond

This is normal! The free tier has rate limits during high usage. The agent is "thinking" - good responses take time.

---

## Advanced: Switching Models

Want to use a different model? Edit `learning_agent.py`:

```python
# Current (gpt-4.1-mini - fast & smart)
model_id="openai/gpt-4.1-mini"

# Alternative options:
model_id="openai/o3-mini"           # Better for math reasoning
model_id="openai/gpt-5-mini"        # Newer, slightly better
model_id="microsoft/phi-4"          # Microsoft's efficient model
```

Available models: https://github.com/marketplace/models

---

## Project Structure

```
LearningAgent/
├── learning_agent.py    # Main agent code
├── examples.py          # Sample conversations
├── requirements.txt     # Python dependencies
├── .env.example         # Environment template
├── .env                 # Your token (DO NOT COMMIT!)
├── README.md            # Full documentation
└── SETUP.md            # This file
```

---

## Next Steps

1. Try the agent with a simple question
2. Run examples: `python examples.py`
3. Have your son ask real homework questions
4. Experiment with different subjects

---

## Need Help?

- **GitHub Models**: https://github.com/marketplace/models
- **Agent Framework**: https://github.com/microsoft/agent-framework
- **Token Issues**: https://github.com/settings/tokens

---

**Happy Learning!**
