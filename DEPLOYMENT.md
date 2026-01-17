# Deploying to Streamlit Cloud

## Step-by-Step Guide

### 1. Push Your Code to GitHub

First, make sure your code is on GitHub:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit your changes
git commit -m "Initial commit with Streamlit app"

# Create a repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

**Important:** Make sure you have a `.gitignore` file that excludes:
- `__pycache__/` folders
- `.env` file (contains sensitive API keys)
- Any other sensitive files

### 2. Set Up Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select your repository: `YOUR_USERNAME/YOUR_REPO_NAME`
5. Set the **Main file path** to: `main.py`
6. Click **"Deploy!"**

### 3. Configure Environment Variables

Since your app uses `load_dotenv()`, you need to add your environment variables in Streamlit Cloud:

1. In your Streamlit Cloud app dashboard, click **"Settings"** (⚙️ icon)
2. Go to **"Secrets"** tab
3. Add your environment variables in TOML format:

```toml
OPENAI_API_KEY = "your-api-key-here"
# Add any other API keys or environment variables you need
```

### 4. Wait for Deployment

Streamlit Cloud will:
- Install dependencies from `requirements.txt`
- Deploy your app
- Give you a public URL (e.g., `https://yourapp.streamlit.app`)

### 5. Access Your App

Once deployed, you'll get a URL like:
```
https://YOUR_APP_NAME.streamlit.app
```

## Requirements

Your `requirements.txt` should include all dependencies. Current dependencies:
- crewai
- crewai-tools
- python-dotenv
- yfinance
- streamlit

## Troubleshooting

- **Build fails**: Check that all dependencies are in `requirements.txt`
- **App errors**: Check the logs in Streamlit Cloud dashboard
- **API keys not working**: Make sure secrets are set correctly in Streamlit Cloud settings
- **Import errors**: Ensure all your Python files are in the repository

## Notes

- Streamlit Cloud automatically redeploys when you push to your main branch
- Free tier has some limitations (app sleeps after inactivity)
- Make sure your `.env` file is in `.gitignore` to keep secrets safe
