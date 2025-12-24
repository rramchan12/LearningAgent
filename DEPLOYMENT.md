# Deploy to Streamlit Cloud (Free!)

This guide will help you deploy your Learning Agent so it's accessible from anywhere on the internet.

## Prerequisites

1. GitHub account
2. GitHub Personal Access Token (you already have this!)
3. 10 minutes of time

---

## Step 1: Create GitHub Repository

### Option A: Using GitHub Desktop (Easiest)
1. Download GitHub Desktop: https://desktop.github.com
2. Open GitHub Desktop
3. File → Add Local Repository → Choose `Q:\workspace\LearningAgent`
4. Click "Create Repository"
5. Click "Publish Repository"
   - Name: `cbse-learning-agent`
   - Description: "AI-powered learning assistant for CBSE Std 9"
   - ⚠️ **UNCHECK "Keep this code private"** if you want free hosting (or check for private)
6. Click "Publish Repository"

### Option B: Using Git Command Line
```bash
cd Q:\workspace\LearningAgent

# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - CBSE Learning Agent"

# Create repository on GitHub and push
# Follow: https://github.com/new
# Then run the commands GitHub shows you
```

### ⚠️ IMPORTANT: Make sure `.env` is NOT uploaded!
Check your GitHub repository - you should NOT see:
- ❌ `.env` file with your token
- ✅ `.env.example` is OK to see

If you see `.env` with your token:
1. Delete it from GitHub immediately
2. Generate a NEW GitHub token (old one is compromised)

---

## Step 2: Deploy to Streamlit Cloud

### 1. Go to Streamlit Cloud
Visit: https://share.streamlit.io/

### 2. Sign in with GitHub
Click "Sign in with GitHub" and authorize Streamlit.

### 3. Deploy New App
1. Click "New app" button (top right)
2. Fill in the form:
   - **Repository:** Select `your-username/cbse-learning-agent`
   - **Branch:** `main` (or `master`)
   - **Main file path:** `run_web.py`
3. Click "Advanced settings" (optional)
   - Python version: 3.9 or 3.10

### 4. Add Secrets
**This is CRITICAL - Your GitHub Token!**

1. Click on "Advanced settings" → "Secrets"
2. Paste this TOML format:
   ```toml
   GITHUB_TOKEN = "ghp_your_actual_github_token_here"
   ```
   Replace `ghp_your_actual_github_token_here` with your real token!

3. Click "Save"

### 5. Deploy!
1. Click "Deploy!" button
2. Wait 2-5 minutes for deployment
3. Your app will be live at: `https://your-username-cbse-learning-agent.streamlit.app`

---

## Step 3: Share with Your Son!

Once deployed, you'll get a URL like:
```
https://rramchandran-cbse-learning-agent.streamlit.app
```

Share this link! Your son can:
- Access from any device (laptop, tablet, phone)
- Use anywhere with internet
- Get automatic diagram generation
- Have persistent conversations

---

## Updating Your App

When you make changes locally:

### Using GitHub Desktop:
1. Make your code changes
2. Open GitHub Desktop
3. Write commit message
4. Click "Commit to main"
5. Click "Push origin"
6. Streamlit Cloud auto-updates in ~1 minute!

### Using Command Line:
```bash
git add .
git commit -m "Updated feature X"
git push
```

Streamlit Cloud detects changes and redeploys automatically!

---

## Cost

**100% FREE** if:
- Repository is public
- Moderate usage (perfect for family use)

**Private repositories:**
- Free for 1 private app
- $20/month for unlimited private apps

---

## Troubleshooting

### "Error: GITHUB_TOKEN not found"
- Go to your app on Streamlit Cloud
- Click Settings > Secrets
- Make sure your token is there in correct format:
  ```toml
  GITHUB_TOKEN = "ghp_..."
  ```

### App won't start / ModuleNotFoundError
- **IMPORTANT:** Make sure Main file path is set to `run_web.py` (NOT `streamlit_app.py` or `web/app.py`)
- Check "Manage app" → "Logs" to see errors
- Make sure `requirements.txt` is complete
- Verify Python version is 3.9 or 3.10
- To fix: Go to app settings → Change "Main file path" to `run_web.py` → Reboot app

### Diagram generation fails
- Check the "diagrams" folder is being created
- May need to adjust file paths for cloud environment

### GitHub Token expired
- Generate new token: https://github.com/settings/tokens
- Update in Streamlit Cloud secrets
- App will restart automatically

---

## Security Notes

1. **NEVER commit `.env` file** - Already in `.gitignore`
2. **Use Streamlit Secrets** for tokens - Not environment variables
3. **Token scope** - GitHub Models needs no special scopes
4. **Rotate tokens** - Generate new ones every 90 days

---

## Mobile Access

The Streamlit app works great on mobile!
- Responsive design
- Touch-friendly
- Works on iOS and Android
- Can add to home screen as PWA

---

## Next Steps (Optional)

1. **Custom Domain:** Point your own domain to Streamlit app
2. **Authentication:** Add password protection (Streamlit built-in)
3. **Analytics:** Track usage with Streamlit metrics
4. **More Features:** Add calculator, quiz mode, progress tracking

---

## Need Help?

- Streamlit Docs: https://docs.streamlit.io
- Streamlit Community: https://discuss.streamlit.io
- My GitHub: (your repository URL)

Happy Learning!
