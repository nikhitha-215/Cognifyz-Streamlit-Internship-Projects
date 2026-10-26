import streamlit as st

# Page setup
st.set_page_config(page_title="Python Developer Assessment", page_icon="💻", layout="centered")

# Corporate Light Theme & CSS to hide header anchor links entirely
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #1e293b;
    }
    h1, h2, h3 {
        color: #0f172a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Completely hide heading link icons */
    h3 a, .stMarkdown h3 a, .element-container a {
        display: none !important;
    }
    .question-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        padding: 10px 24px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💻 Python Developer Assessment")
st.write("Complete the technical assessment below to evaluate your core Python knowledge.")

# Comprehensive Question Bank (10 Questions)
question_bank = [
    {
        "q": "What keyword is used to define a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "q": "Which data type is used to store True or False values?",
        "options": ["int", "bool", "string", "float"],
        "answer": "bool"
    },
    {
        "q": "What symbol is used for single-line comments in Python?",
        "options": ["//", "/*", "#", "<!--"],
        "answer": "#"
    },
    {
        "q": "Which function outputs text to the console in Python?",
        "options": ["echo()", "print()", "write()", "display()"],
        "answer": "print()"
    },
    {
        "q": "Which operator is used for exponentiation in Python?",
        "options": ["^", "**", "pow", "exp"],
        "answer": "**"
    },
    {
        "q": "What is the correct file extension for Python files?",
        "options": [".pt", ".pyt", ".py", ".python"],
        "answer": ".py"
    },
    {
        "q": "Which collection is ordered, changeable, and allows duplicate members?",
        "options": ["Tuple", "Set", "Dictionary", "List"],
        "answer": "List"
    },
    {
        "q": "Which statement is used to handle runtime exceptions in Python?",
        "options": ["try-except", "catch-throw", "error-handle", "do-catch"],
        "answer": "try-except"
    },
    {
        "q": "What does the `len()` function return when passed a list?",
        "options": ["The total number of elements", "The memory size in bytes", "The maximum value", "The data type"],
        "answer": "The total number of elements"
    },
    {
        "q": "Which method is used to add an item to the end of a list?",
        "options": ["add()", "push()", "append()", "insert()"],
        "answer": "append()"
    }
]

if "submitted" not in st.session_state:
    st.session_state.submitted = False

with st.form("assessment_form"):
    user_answers = {}
    
    for idx, item in enumerate(question_bank):
        st.markdown(f"""
            <div class="question-card">
                <h3 style="font-size: 1.15rem; margin-bottom: 12px;">Q{idx + 1}. {item["q"]}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        # index=None ensures no option is pre-selected
        choice = st.radio(
            f"Select option for question {idx+1}:", 
            item["options"], 
            index=None,
            key=f"q_{idx}", 
            label_visibility="collapsed"
        )
        user_answers[idx] = choice
        
        # Inline feedback after submission
        if st.session_state.submitted:
            correct_ans = item["answer"]
            if choice == correct_ans:
                st.success(f"Correct! The right answer is '{correct_ans}'.")
            elif choice is None:
                st.warning(f"No answer selected. The correct answer was '{correct_ans}'.")
            else:
                st.error(f"Incorrect. Your answer: '{choice}' | Correct answer: '{correct_ans}'.")
        
        st.markdown("<br>", unsafe_allow_html=True)

    submit_btn = st.form_submit_button("Submit Assessment")

if submit_btn:
    st.session_state.submitted = True
    st.rerun()

# Score summary banner after submission
if st.session_state.submitted:
    score = sum(1 for idx, item in enumerate(question_bank) if user_answers.get(idx) == item["answer"])
    st.markdown("---")
    st.subheader(f"Assessment Result: {score} / {len(question_bank)} Correct")
    
    if st.button("🔄 Retake Assessment"):
        st.session_state.submitted = False
        st.rerun()