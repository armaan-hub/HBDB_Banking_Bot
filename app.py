import streamlit as st
import pandas as pd
from mistralai import Mistral
import os

# Set page config
st.set_page_config(page_title="HBDB Banking Bot", layout="wide", initial_sidebar_state="expanded")

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 2rem;
    }
    .bot-message {
        background-color: #f5f5f5;
        margin-right: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Mistral client
try:
    api_key = st.secrets["MISTRAL_API_KEY"]
except (KeyError, FileNotFoundError):
    api_key = "rKAog5VOtjTBkMAXkr1OXNcBgNn97dzY"

client = Mistral(api_key=api_key)

# Load FAQ data
@st.cache_data
def load_faq_data():
    csv_path = "hbdb_banking_faqs.csv"
    df = pd.read_csv(csv_path)
    return df

# Create FAQ context
@st.cache_data
def create_faq_context(df):
    context = "You are a helpful HBDB banking assistant. Here is the banking FAQ knowledge base:\n\n"
    for idx, row in df.iterrows():
        context += f"Q: {row['Question']}\nA: {row['Answer']}\n\n"
    return context

# Main app
st.title("🏦 HBDB Banking Bot")
st.markdown("---")

try:
    # Load FAQ data
    df = load_faq_data()
    faq_context = create_faq_context(df)
    
    # Sidebar
    with st.sidebar:
        st.header("📋 About")
        st.write("This banking bot uses Mistral Large AI to answer your banking questions based on HBDB's FAQ database.")
        
        st.header("📊 FAQ Statistics")
        st.metric("Total FAQs", len(df))
        
        st.header("🔄 Session Info")
        if st.button("Clear Chat History"):
            st.session_state.messages = []
            st.rerun()
    
    # Initialize session state for messages
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    user_input = st.chat_input("Ask me anything about HBDB banking services...")
    
    if user_input:
        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Prepare messages for API
        messages = [
            {"role": "system", "content": faq_context},
        ]
        
        # Add conversation history
        for msg in st.session_state.messages:
            messages.append({"role": msg["role"], "content": msg["content"]})
        
        # Get response from Mistral
        try:
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""
                
                # Stream the response
                with client.chat.stream(
                    model="mistral-large-latest",
                    messages=messages,
                    temperature=0.7,
                    max_tokens=1024
                ) as response:
                    for chunk in response:
                        if chunk.data.choices[0].delta.content:
                            full_response += chunk.data.choices[0].delta.content
                            message_placeholder.markdown(full_response + "▌")
                    
                    message_placeholder.markdown(full_response)
                
                # Add assistant message to session state
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        
        except Exception as e:
            st.error(f"Error getting response: {str(e)}")
            st.info("Please check your API key and internet connection.")
    
except FileNotFoundError:
    st.error("❌ FAQ file not found. Please ensure 'hbdb_banking_faqs.csv' is in the same directory as this app.")
except Exception as e:
    st.error(f"An error occurred: {str(e)}")
    st.info(f"Error details: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #888;'>
        <p>HBDB Banking Bot v1.0 | Powered by Mistral Large AI</p>
    </div>
""", unsafe_allow_html=True)
