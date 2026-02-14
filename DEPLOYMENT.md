# HBDB Banking Bot - Deployment Guide

## 🚀 Local Access (Now Running)

Your Banking Bot is **currently running locally** and can be accessed at:

### Local URLs:
- **Local URL**: [http://localhost:8501](http://localhost:8501)
- **Network URL**: [http://192.168.1.139:8501](http://192.168.1.139:8501)

Use the Network URL to share with others on the same network.

---

## 🌐 Deploy to Streamlit Cloud (For Public Access)

To get a public Streamlit link that anyone can access from anywhere:

### Step 1: Prepare Your Repository

```powershell
# Navigate to the Banking folder
cd "C:\Users\armaa\OneDrive - The Era Corporations\Study\AI Class\Data Science Class\19. 14-Dec-2026\Banking"

# Initialize Git repository
git init
git add .
git commit -m "HBDB Banking Bot - Initial commit"
git branch -M main
```

### Step 2: Push to GitHub

1. Create a new repository on [GitHub](https://github.com/new)
2. Name it something like `hbdb-banking-bot`
3. Make it **Public** (required for free tier)
4. Run these commands:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/hbdb-banking-bot.git
git push -u origin main
```

### Step 3: Deploy to Streamlit Cloud

1. Go to [https://share.streamlit.io/](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click **"New app"**
4. Select:
   - **Repository**: `YOUR_USERNAME/hbdb-banking-bot`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Deploy"**

### Step 4: Set Environment Variables

In the Streamlit Cloud dashboard:
1. Go to Settings ⚙️
2. Click **"Secrets"**
3. Add your API key:
```
MISTRAL_API_KEY = "rKAog5VOtjTBkMAXkr1OXNcBgNn97dzY"
```
4. Save

### Step 5: Update app.py for Cloud

Replace the hardcoded API key in `app.py` (line 22) with:
```python
api_key = st.secrets["MISTRAL_API_KEY"]
```

After deployment, you'll get a public URL like: **`https://your-username-hbdb-banking-bot.streamlit.app`**

---

## 📦 Project Files

All necessary files are in: `C:\Users\armaa\OneDrive - The Era Corporations\Study\AI Class\Data Science Class\19. 14-Dec-2026\Banking\`

```
Banking/
├── app.py                      # Main Streamlit app
├── hbdb_banking_faqs.csv      # FAQ database (50+ Q&As)
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── deploy.py                   # Deployment helper script
├── .streamlit/
│   └── config.toml            # Streamlit configuration
└── DEPLOYMENT.md              # This file
```

---

## ✅ Features Included

✓ **50+ FAQ Database** - Based on HBDB banking services  
✓ **Real-time Streaming** - Responses stream as they're generated  
✓ **Mistral Large AI** - Powered by state-of-the-art language model  
✓ **Chat History** - Maintains conversation context  
✓ **Professional UI** - Beautiful Streamlit interface  
✓ **Production Ready** - All error handling included  

---

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **App won't start** | Check all files are in the Banking folder |
| **API errors** | Verify your Mistral API key is correct |
| **Slow responses** | Normal - API calls take 2-5 seconds |
| **CSV not found** | Ensure `hbdb_banking_faqs.csv` is in the same folder as app.py |
| **Port 8501 in use** | Run with `streamlit run app.py --server.port 8502` |

---

## 📞 Support Links

- **Streamlit Docs**: https://docs.streamlit.io/
- **Mistral AI Docs**: https://docs.mistral.ai/
- **Streamlit Cloud**: https://share.streamlit.io/

---

## 🎯 Next Steps

1. ✅ **Local Testing** - Access at http://localhost:8501
2. **GitHub Setup** - Push to GitHub (see Step 2)
3. **Cloud Deployment** - Deploy to Streamlit Cloud (see Step 3)
4. **Share** - Get public URL and share with others

---

**Last Updated**: February 14, 2026
**Status**: ✅ Running locally
**Model**: Mistral Large
