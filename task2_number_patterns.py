import streamlit as st

# Page setup
st.set_page_config(page_title="Advanced Pattern Studio", page_icon="🔢", layout="centered")

# Corporate Light Theme & Styling
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
    .studio-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 24px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🔢 Advanced Number Pattern Studio")
st.write("Explore algorithmic pattern generation using nested loops with multiple geometric configurations.")

# Controls Section
with st.container():
    st.markdown("<div class='studio-card'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        pattern_type = st.selectbox(
            "Select Pattern Algorithm:",
            [
                "Symmetric Number Pyramid",
                "Right-Angled Triangle",
                "Inverted Number Pyramid",
                "Floyd's Triangle Sequence"
            ]
        )
        
    with col2:
        rows = st.slider("Select Number of Rows:", min_value=2, max_value=12, value=5)
    st.markdown("</div>", unsafe_allow_html=True)

# Pattern Generation Logic
output_lines = []
algorithm_code = ""

if pattern_type == "Symmetric Number Pyramid":
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        asc = "".join(str(j % 10) for j in range(1, i + 1))
        desc = "".join(str(j % 10) for j in range(i - 1, 0, -1))
        output_lines.append(spaces + asc + desc)
    algorithm_code = f"""# Symmetric Number Pyramid Logic
for i in range(1, {rows} + 1):
    spaces = " " * ({rows} - i)
    asc = "".join(str(j) for j in range(1, i + 1))
    desc = "".join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + asc + desc)"""

elif pattern_type == "Right-Angled Triangle":
    for i in range(1, rows + 1):
        line = "".join(str(j % 10) for j in range(1, i + 1))
        output_lines.append(line)
    algorithm_code = f"""# Right-Angled Triangle Logic
for i in range(1, {rows} + 1):
    line = "".join(str(j) for j in range(1, i + 1))
    print(line)"""

elif pattern_type == "Inverted Number Pyramid":
    for i in range(rows, 0, -1):
        spaces = " " * (rows - i)
        line = "".join(str(j % 10) for j in range(1, i + 1)) + "".join(str(j % 10) for j in range(i - 1, 0, -1))
        output_lines.append(spaces + line)
    algorithm_code = f"""# Inverted Number Pyramid Logic
for i in range({rows}, 0, -1):
    spaces = " " * ({rows} - i)
    line = "".join(str(j) for j in range(1, i + 1)) + "".join(str(j) for j in range(i - 1, 0, -1))
    print(spaces + line)"""

elif pattern_type == "Floyd's Triangle Sequence":
    num = 1
    for i in range(1, rows + 1):
        row_vals = []
        for j in range(1, i + 1):
            row_vals.append(f"{num:<3}")
            num += 1
        output_lines.append(" ".join(row_vals))
    algorithm_code = f"""# Floyd's Triangle Sequence Logic
num = 1
for i in range(1, {rows} + 1):
    row_vals = []
    for j in range(1, i + 1):
        row_vals.append(str(num))
        num += 1
    print(" ".join(row_vals))"""

pattern_result = "\n".join(output_lines)

# Display Output and Code Tabs
st.markdown("### 📊 Pattern Output Preview")
st.code(pattern_result, language="text")

st.markdown("### 💻 Underlying Python Algorithm")
st.code(algorithm_code, language="python")