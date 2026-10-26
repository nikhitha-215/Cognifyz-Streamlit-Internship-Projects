import streamlit as st

# Page setup
st.set_page_config(page_title="Cognifyz Portfolio Hub", page_icon="🏆", layout="wide")

# Enterprise Clean White Theme with subtle dotted grid and zero wrapper boxes
st.markdown("""
    <style>
    .stApp, .main {
        background-color: #ffffff !important;
        background-image: radial-gradient(#e2e8f0 1px, transparent 1px);
        background-size: 24px 24px;
        color: #0f172a !important;
    }
    h1, h2, h3, h4, p, label, span {
        color: #0f172a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .project-row {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        padding: 18px 22px;
        border-radius: 10px;
        margin-bottom: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
    }
    .metric-box {
        background-color: #f8fafc;
        border: 1px solid #cbd5e1;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    /* Fixed code block styling for high contrast and full visibility */
    pre, code {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 6px;
        font-weight: 600;
    }
    .stButton>button {
        background-color: #2563eb !important;
        color: #ffffff !important;
        font-weight: 600;
        border-radius: 6px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🏆 Cognifyz Internship Portfolio Hub")
st.markdown("Master control dashboard showcasing your complete suite of enterprise Python Streamlit web applications.")
st.markdown("---")

# Quick Stats Overview
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
        <div class="metric-box">
            <h4 style="color: #64748b !important; margin: 0; font-size: 0.85rem;">TOTAL MODULES</h4>
            <h2 style="color: #0f172a !important; margin: 5px 0 0 0;">6 Projects</h2>
        </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="metric-box">
            <h4 style="color: #64748b !important; margin: 0; font-size: 0.85rem;">PROJECT STATUS</h4>
            <h2 style="color: #16a34a !important; margin: 5px 0 0 0;">100% Completed</h2>
        </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
        <div class="metric-box">
            <h4 style="color: #64748b !important; margin: 0; font-size: 0.85rem;">FRAMEWORK</h4>
            <h2 style="color: #2563eb !important; margin: 5px 0 0 0;">Streamlit Python</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 📁 Project Directory: `C:\\Users\\Nikhitha\\Desktop\\Cognifyz_Projects`")
st.markdown("<br>", unsafe_allow_html=True)

# List of all completed tasks
tasks = [
    {
        "id": "Task 1", 
        "name": "Interactive Quiz Game", 
        "file": "task1_quiz_game.py", 
        "desc": "Dynamic trivia evaluation with real-time scoring and instant feedback."
    },
    {
        "id": "Task 2", 
        "name": "Number Pattern Generator", 
        "file": "task2_number_patterns.py", 
        "desc": "Customizable mathematical pyramid and sequence rendering engine."
    },
    {
        "id": "Task 3", 
        "name": "Enterprise Task Management Suite", 
        "file": "task3_crud_app.py", 
        "desc": "Full CRUD task management with search filters, priority levels, and live metrics."
    },
    {
        "id": "Task 4", 
        "name": "Thermal Engineering Suite", 
        "file": "task4_temp_converter.py", 
        "desc": "Precision temperature conversion matrix with thermal state analysis and session history."
    },
    {
        "id": "Task 5", 
        "name": "Password Security Suite", 
        "file": "task5_password_checker.py", 
        "desc": "Cryptographic strength heuristic evaluator and secure randomized key generator."
    },
    {
        "id": "Task 6", 
        "name": "Cognifyz Portfolio Hub", 
        "file": "task6_portfolio_hub.py", 
        "desc": "Centralized master dashboard summarizing all internship deliverables."
    }
]

for t in tasks:
    st.markdown(f"""
        <div class="project-row">
            <div>
                <h4 style="margin: 0; color: #0f172a;"><b>{t['id']}:</b> {t['name']}</h4>
                <p style="margin: 4px 0 0 0; color: #475569; font-size: 0.95rem;">{t['desc']} &nbsp;|&nbsp; <code>{t['file']}</code></p>
            </div>
            <div>
                <span style="background: #dcfce7; color: #166534; padding: 5px 12px; border-radius: 6px; font-weight: 600; font-size: 0.85rem;">Deployed ✅</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("### 🚀 Quick Execution Guide")
st.markdown("To run any individual project in your terminal, use the following command structure:")
st.code("python -m streamlit run task1_quiz_game.py", language="bash")