# Quick Start - Test Locally First!

## Step 1: Test Locally (RIGHT NOW!)

The Streamlit server is starting. You should see a browser open automatically at:
```
http://localhost:8501
```

If it doesn't open automatically, manually go to: **http://localhost:8501**

### What You'll See:
- Web interface with chat
- Diagrams displayed inline
- Chat history
- Responsive design (works on phone too!)

### Test It:
Try asking: "Explain the quadratic equation x² - 5x + 6 = 0"
You should see it generate a diagram automatically!

---

## Step 2: Share on Your Home Network

Once it's running locally, anyone on your Wi-Fi can access it!

### Find Your Local IP:
```powershell
ipconfig
```
Look for "IPv4 Address" under your Wi-Fi adapter (usually 192.168.x.x)

### Share URL:
Give this URL to your son:
```
http://192.168.x.x:8501
```
(Replace x.x with your actual IP numbers)

He can access it from:
- His laptop
- Tablet
- Phone
- Any device on same Wi-Fi!

---

## Step 3: Deploy to Cloud (Next!)

When you're ready to make it accessible from anywhere (even outside home):

### Follow: [DEPLOYMENT.md](DEPLOYMENT.md)

Quick summary:
1. Upload to GitHub (5 min)
2. Connect to Streamlit Cloud (2 min)
3. Add your GitHub token to secrets (1 min)
4. Get public URL to share!

Total time: ~10 minutes

---

## Stopping the Server

To stop the local server:
- Press `Ctrl+C` in the terminal

---

## Tips for Testing

### Good Questions to Try:
- "What's a quadratic equation?"
- "Show me a plant cell"
- "Explain velocity vs time graph"
- "What's a right triangle?"
- "Help me with this problem: x² - 4x + 3 = 0"

### Features to Test:
- Automatic diagram generation
- Multi-turn conversation
- Clear conversation button
- Mobile responsiveness (check on phone!)
- Diagram display

---

## Next Steps

1. **Test locally now** - Use http://localhost:8501
2. **Share on home network** - Use http://YOUR_IP:8501
3. **Deploy to cloud** - Follow [DEPLOYMENT.md](DEPLOYMENT.md)
4. **Share with your son** - Give him the URL!

---

Enjoy!
