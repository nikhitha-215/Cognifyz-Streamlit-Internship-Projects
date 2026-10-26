import streamlit as st
import random
import string

# Page setup
st.set_page_config(page_title="Password Security Suite", page_icon="🔐", layout="wide")

# Clean styling with zero wrapper boxes and native widget visibility
st.markdown("""
    <style>
    .stApp, .main {
        background-color: #ffffff !important;
        color: #0f172a !important;
    }
    h1, h2, h3, h4, p, label, span {
        color: #0f172a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stButton>button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 6px;
        padding: 8px 16px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔐 Enterprise Password Security Suite")
st.markdown("Evaluate password strength or generate secure randomized keys.")
st.markdown("---")

col_left, col_right = st.columns(2, gap="large")

with col_left:
    st.markdown("### 🔍 Strength Analyzer")
    pwd_input = st.text_input("Enter Password to Test", type="password", placeholder="Type password here...")
    analyze_btn = st.button("Analyze Strength")
    
    if analyze_btn:
        if not pwd_input:
            st.markdown("<p style='color: #dc2626; font-weight: 600; margin-top: 10px;'>Please enter a password first.</p>", unsafe_allow_html=True)
        else:
            score = 0
            feedback = []
            
            if len(pwd_input) >= 8: score += 1
            else: feedback.append("• Minimum length of 8 characters required.")
            
            if len(pwd_input) >= 12: score += 1
            
            if any(c.isupper() for c in pwd_input): score += 1
            else: feedback.append("• Include uppercase letters (A-Z).")
                
            if any(c.islower() for c in pwd_input): score += 1
            else: feedback.append("• Include lowercase letters (a-z).")
                
            if any(c.isdigit() for c in pwd_input): score += 1
            else: feedback.append("• Include numeric digits (0-9).")
                
            if any(c in string.punctuation for c in pwd_input): score += 1
            else: feedback.append("• Include special symbols (!@#$%^&*).")

            if score <= 2:
                rating = "🔴 Weak Security"
                color = "#dc2626"
            elif score <= 4:
                rating = "🟡 Moderate Security"
                color = "#d97706"
            else:
                rating = "🟢 Strong Enterprise-Grade"
                color = "#16a34a"

            st.markdown(f"<p style='font-size: 1.1rem; font-weight: 600; color: {color} !important; margin-top: 15px;'>Rating: {rating}</p>", unsafe_allow_html=True)
            st.progress(score / 6)
            
            if feedback:
                st.markdown("<p style='font-weight: 600; margin-top: 10px;'>Recommendations:</p>", unsafe_allow_html=True)
                for tip in feedback:
                    st.markdown(f"<p style='margin: 3px 0; color: #475569;'>{tip}</p>", unsafe_allow_html=True)
            else:
                st.markdown("<p style='color: #16a34a; font-weight: 600; margin-top: 10px;'>✨ Excellent! This password meets all security criteria.</p>", unsafe_allow_html=True)

with col_right:
    st.markdown("### ⚡ Secure Generator")
    gen_length = st.slider("Password Length", min_value=8, max_value=32, value=16)
    
    use_upper = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
    use_lower = st.checkbox("Include Lowercase Letters (a-z)", value=True)
    use_digits = st.checkbox("Include Digits (0-9)", value=True)
    use_symbols = st.checkbox("Include Symbols (!@#$)", value=True)
    
    generate_btn = st.button("Generate Secure Password")
    
    if generate_btn:
        char_pool = ""
        if use_upper: char_pool += string.ascii_uppercase
        if use_lower: char_pool += string.ascii_lowercase
        if use_digits: char_pool += string.digits
        if use_symbols: char_pool += string.punctuation
        
        if not char_pool:
            st.markdown("<p style='color: #dc2626; font-weight: 600; margin-top: 10px;'>Please select at least one character set.</p>", unsafe_allow_html=True)
        else:
            generated_pwd = "".join(random.choice(char_pool) for _ in range(gen_length))
            st.markdown(f"""
                <div style="background: #f8fafc; padding: 12px; border: 1px solid #cbd5e1; border-radius: 8px; margin-top: 15px; text-align: center;">
                    <span style="font-size: 1.1rem; font-family: monospace; font-weight: 600; color: #0f172a;">{generated_pwd}</span>
                </div>
            """, unsafe_allow_html=True)
            st.markdown("<p style='color: #16a34a; font-weight: 600; margin-top: 8px;'>Secure password generated successfully!</p>", unsafe_allow_html=True)