# 🏦 HBDB Banking Bot

A conversational AI chatbot for HBDB banking services built with Streamlit and powered by Mistral Large AI.

## Features

- 💬 Interactive chat interface
- 📚 FAQ knowledge base integration
- 🚀 Real-time streaming responses
- 📊 Session statistics
- 🔄 Chat history management

## Prerequisites

- Python 3.8+
- Mistral AI API Key
- pip package manager

## Installation

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Verify the CSV file is present:**
   - Ensure `hbdb_banking_faqs.csv` is in the same directory as `app.py`

## Running the Application

1. **Navigate to the Banking folder:**
```bash
cd "C:\\Users\\armaa\\OneDrive - The Era Corporations\\Study\\AI Class\\Data Science Class\\19. 14-Dec-2026\\Banking"
```

2. **Run the Streamlit app:**
```bash
streamlit run app.py
```

3. **Access the app:**
   - Local URL: `http://localhost:8501`
   - You can share the public URL if deployed to Streamlit Cloud

## Deployment to Streamlit Cloud

### Option 1: Using Streamlit Cloud (Free Hosting)

1. **Create a GitHub repository** with your app files:
   - `app.py`
   - `requirements.txt`
   - `hbdb_banking_faqs.csv`

2. **Push to GitHub:**
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

3. **Deploy to Streamlit Cloud:**
   - Go to [https://share.streamlit.io/](https://share.streamlit.io/)
   - Click "New app"
   - Select your GitHub repo, branch, and app file
   - Deploy!

4. **Set environment variables:**
   - In Streamlit Cloud dashboard, go to "Settings"
   - Add your Mistral API key as an environment variable

### Option 2: Local Streamlit Link

To create a shareable local link:
```bash
streamlit run app.py --logger.level=error
```

## Configuration

### API Key Security

The app uses your Mistral API key. For production:

1. **Use environment variables:**
   - Create a `.env` file:
   ```
   MISTRAL_API_KEY=your_key_here
   ```
   - Update `app.py` to use: `api_key = os.getenv("MISTRAL_API_KEY")`

2. **Use Streamlit secrets:**
   - Create `.streamlit/secrets.toml`:
   ```toml
   MISTRAL_API_KEY = "your_key_here"
   ```
   - Update `app.py` to use: `api_key = st.secrets["MISTRAL_API_KEY"]`

## API Details

- **Model:** Mistral Large (Latest)
- **API Base:** Mistral AI
- **Temperature:** 0.7
- **Max Tokens:** 1024

## Troubleshooting

| Issue | Solution |
|-------|----------|
| CSV file not found | Ensure `hbdb_banking_faqs.csv` is in the same directory as `app.py` |
| API key error | Verify the Mistral API key is correct |
| No responses | Check internet connection and API quota |
| Slow responses | This is normal due to API response time; responses are streamed |

## File Structure

```
Banking/
├── app.py                      # Main Streamlit application
├── requirements.txt            # Python dependencies
├── hbdb_banking_faqs.csv      # FAQ knowledge base
└── README.md                   # This file
```

## FAQ Access

The chatbot has access to 50+ frequently asked questions about HBDB banking services, including:
- Account opening and management
- Banking products
- Online and mobile banking
- Loans and mortgages
- Cards and payments
- Customer service

## Support

For issues or questions:
- Check the sidebar information in the app
- Verify your Mistral API key and quota
- Ensure all files are in the correct directory

## License

This project uses the Mistral Large AI model. Refer to [Mistral AI Terms](https://mistral.ai/) for usage terms.

---

**Created:** February 2026
**Model:** Mistral Large
**Framework:** Streamlit
