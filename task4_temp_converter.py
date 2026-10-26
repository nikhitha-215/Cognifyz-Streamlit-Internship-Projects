import streamlit as st
from datetime import datetime

# Page setup
st.set_page_config(page_title="Thermal Conversion Suite", page_icon="🌡️", layout="wide")

# Enterprise Clean White Theme with subtle background pattern
st.markdown("""
    <style>
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #ffffff !important;
        background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
        background-size: 24px 24px;
        color: #0f172a !important;
    }
    h1, h2, h3, h4, p, label, span {
        color: #0f172a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Sleek container box for results or prompts */
    .result-box {
        background-color: #f8fafc !important;
        border: 2px solid #2563eb !important;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
        text-align: center;
    }
    input, div[data-baseweb="select"] > div {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-color: #cbd5e1 !important;
    }
    .stButton>button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 6px;
        padding: 10px 24px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize history log in session state
if "conv_history" not in st.session_state:
    st.session_state.conv_history = []

st.title("🌡️ Enterprise Thermal Engineering Suite")
st.markdown("Advanced temperature conversion matrix equipped with state analytics and session history logging.")
st.markdown("---")

col_left, col_right = st.columns([1.2, 1], gap="large")

with col_left:
    st.markdown("### ⚙️ Conversion Parameters")
    temp_value = st.number_input("Input Thermal Value", value=25.0, format="%.4f")
    unit_from = st.selectbox("Source Scale", ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    convert_btn = st.button("Compute Conversions")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 📐 Applied Formulas")
    st.markdown("- **°C to °F:** $(C \\times \\frac{9}{5}) + 32$")
    st.markdown("- **°C to K:** $C + 273.15$")
    st.markdown("- **°F to °C:** $(F - 32) \\times \\frac{5}{9}$")

with col_right:
    st.markdown("### 📊 Conversion Matrix")
    
    if convert_btn:
        celsius, fahrenheit, kelvin = 0.0, 0.0, 0.0
        
        if unit_from == "Celsius (°C)":
            celsius = temp_value
            fahrenheit = (temp_value * 9/5) + 32
            kelvin = temp_value + 273.15
        elif unit_from == "Fahrenheit (°F)":
            celsius = (temp_value - 32) * 5/9
            fahrenheit = temp_value
            kelvin = celsius + 273.15
        elif unit_from == "Kelvin (K)":
            if temp_value < 0:
                st.error("❌ Invalid thermal state: Temperature cannot fall below absolute zero (0 K).")
                st.stop()
            celsius = temp_value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            kelvin = temp_value

        state_desc = "Normal Ambient"
        if celsius <= 0:
            state_desc = "❄️ Freezing / Sub-zero"
        elif celsius >= 100:
            state_desc = "🔥 Boiling Point Reached"

        # Render results inside the single unified result box
        st.markdown(f"""
            <div class='result-box' style='text-align: left;'>
                <p style='font-size: 1.15rem; margin: 10px 0; color: #0f172a !important;'><b>Celsius:</b> {celsius:.2f} °C</p>
                <p style='font-size: 1.15rem; margin: 10px 0; color: #0f172a !important;'><b>Fahrenheit:</b> {fahrenheit:.2f} °F</p>
                <p style='font-size: 1.15rem; margin: 10px 0; color: #0f172a !important;'><b>Kelvin:</b> {kelvin:.2f} K</p>
                <hr style='border: 0; border-top: 1px solid #cbd5e1; margin: 15px 0;'>
                <p style='font-size: 1rem; color: #2563eb !important;'><b>Thermal State Analysis:</b> {state_desc}</p>
            </div>
        """, unsafe_allow_html=True)
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.conv_history.insert(0, {
            "Time": timestamp,
            "Input": f"{temp_value} {unit_from.split()[0]}",
            "Celsius": f"{celsius:.2f}°C",
            "Fahrenheit": f"{fahrenheit:.2f}°F",
            "Kelvin": f"{kelvin:.2f}K"
        })
    else:
        # Single clean prompt card instead of st.info()
        st.markdown("""
            <div class='result-box'>
                <p style='color: #64748b !important; margin: 10px 0;'>Configure your parameters on the left and click <b>Compute Conversions</b>.</p>
            </div>
        """, unsafe_allow_html=True)

# --- SESSION HISTORY LOG ---
if st.session_state.conv_history:
    st.markdown("<br><hr><br>", unsafe_allow_html=True)
    st.markdown("### 🕒 Session Conversion History")
    
    for item in st.session_state.conv_history:
        st.markdown(f"""
            <div style="background: #f8fafc; padding: 12px 16px; border: 1px solid #e2e8f0; border-radius: 8px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #64748b;">[{item['Time']}]</span>
                <span style="color: #0f172a; font-weight: 600;">Input: {item['Input']}</span>
                <span style="color: #2563eb;">➡️ {item['Celsius']} | {item['Fahrenheit']} | {item['Kelvin']}</span>
            </div>
        """, unsafe_allow_html=True)
        
    if st.button("Clear History Log"):
        st.session_state.conv_history = []
        st.rerun()