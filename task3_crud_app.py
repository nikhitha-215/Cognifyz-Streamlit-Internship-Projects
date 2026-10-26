import streamlit as st

# Page setup
st.set_page_config(page_title="Task Manager", page_icon="📋", layout="wide")

# Styling with explicit contrast fixes for sidebar text and main content
st.markdown("""
    <style>
    .stApp {
        background-color: #f8fafc;
        color: #0f172a;
    }
    /* Force sidebar text and labels to be clearly visible */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        color: #ffffff !important;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] h4, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #0f172a !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .metric-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        text-align: center;
    }
    .task-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 15px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    .stButton>button {
        background-color: #2563eb;
        color: white;
        font-weight: 600;
        border-radius: 6px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("📋 Task Manager Dashboard")
st.markdown("Manage your tasks easily with Create, Read, Update, and Delete functions.")

# Initialize database in session state with simple everyday tasks
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Buy groceries", "desc": "Milk, eggs, bread, and fruits.", "priority": "Medium", "completed": False},
        {"id": 2, "title": "Complete Python homework", "desc": "Finish writing the Streamlit single-file scripts.", "priority": "High", "completed": True},
        {"id": 3, "title": "Call the plumber", "desc": "Fix the kitchen sink leak.", "priority": "Low", "completed": False}
    ]

if "next_id" not in st.session_state:
    st.session_state.next_id = 4

# --- METRICS BAR ---
total_tasks = len(st.session_state.tasks)
completed_tasks = sum(1 for t in st.session_state.tasks if t["completed"])
pending_tasks = total_tasks - completed_tasks

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #64748b !important; margin: 0; font-size: 0.9rem;">TOTAL TASKS</h4>
            <h2 style="color: #0f172a !important; margin: 5px 0 0 0;">{total_tasks}</h2>
        </div>
    """, unsafe_allow_html=True)
with col_m2:
    st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #64748b !important; margin: 0; font-size: 0.9rem;">COMPLETED</h4>
            <h2 style="color: #16a34a !important; margin: 5px 0 0 0;">{completed_tasks}</h2>
        </div>
    """, unsafe_allow_html=True)
with col_m3:
    st.markdown(f"""
        <div class="metric-card">
            <h4 style="color: #64748b !important; margin: 0; font-size: 0.9rem;">PENDING</h4>
            <h2 style="color: #ca8a04 !important; margin: 5px 0 0 0;">{pending_tasks}</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- SIDEBAR: CREATE & FILTER CONTROLS ---
with st.sidebar:
    st.markdown("### 🛠️ Control Panel")
    
    st.markdown("#### ➕ Add New Task")
    with st.form("create_form", clear_on_submit=True):
        new_title = st.text_input("Task Title")
        new_desc = st.text_area("Description")
        new_priority = st.selectbox("Priority Level", ["Low", "Medium", "High"])
        
        submitted = st.form_submit_button("Add Task")
        if submitted:
            if new_title.strip():
                st.session_state.tasks.append({
                    "id": st.session_state.next_id,
                    "title": new_title,
                    "desc": new_desc,
                    "priority": new_priority,
                    "completed": False
                })
                st.session_state.next_id += 1
                st.success("Task added successfully!")
                st.rerun()
            else:
                st.error("Title cannot be blank.")
    
    st.markdown("---")
    st.markdown("#### 🔍 Filter Tasks")
    search_query = st.text_input("Search by keyword")
    status_filter = st.selectbox("Status", ["All", "Pending", "Completed"])
    priority_filter = st.selectbox("Priority", ["All", "High", "Medium", "Low"])

# --- MAIN WORKSPACE ---
st.markdown("### 🗂️ Task List")

# Filter logic
filtered_tasks = st.session_state.tasks
if search_query:
    filtered_tasks = [t for t in filtered_tasks if search_query.lower() in t["title"].lower() or search_query.lower() in t["desc"].lower()]
if status_filter == "Pending":
    filtered_tasks = [t for t in filtered_tasks if not t["completed"]]
elif status_filter == "Completed":
    filtered_tasks = [t for t in filtered_tasks if t["completed"]]
if priority_filter != "All":
    filtered_tasks = [t for t in filtered_tasks if t["priority"] == priority_filter]

if not filtered_tasks:
    st.info("No matching tasks found.")
else:
    for idx, task in enumerate(filtered_tasks):
        status_icon = "✅" if task["completed"] else "⏳"
        status_text = "Completed" if task["completed"] else "Pending"
        
        bg_badge = "#dcfce7" if task["completed"] else "#fef9c3"
        txt_badge = "#166534" if task["completed"] else "#854d0e"
        prio_color = "#dc2626" if task["priority"] == "High" else ("#d97706" if task["priority"] == "Medium" else "#2563eb")
        
        st.markdown(f"""
            <div class="task-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <h4 style="margin: 0; color: #0f172a;">{status_icon} {task['title']}</h4>
                    <div>
                        <span style="font-size: 0.8rem; padding: 3px 8px; border-radius: 4px; background: #e2e8f0; color: {prio_color}; font-weight: 600; margin-right: 6px;">
                            {task['priority']}
                        </span>
                        <span style="font-size: 0.8rem; padding: 3px 8px; border-radius: 4px; background: {bg_badge}; color: {txt_badge}; font-weight: 600;">
                            {status_text}
                        </span>
                    </div>
                </div>
                <p style="margin: 8px 0 0 0; color: #475569; font-size: 0.95rem;">{task['desc'] if task['desc'] else 'No description.'}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Action buttons
        col_btn1, col_btn2, col_btn3, col_space = st.columns([1.2, 1.2, 1, 2])
        
        with col_btn1:
            toggle_label = "Mark Pending" if task["completed"] else "Mark Complete"
            if st.button(toggle_label, key=f"toggle_{task['id']}"):
                task["completed"] = not task["completed"]
                st.rerun()
                
        with col_btn2:
            edit_key = f"edit_mode_{task['id']}"
            if edit_key not in st.session_state:
                st.session_state[edit_key] = False
                
            if st.button("Edit", key=f"btn_edit_{task['id']}"):
                st.session_state[edit_key] = not st.session_state[edit_key]
                st.rerun()
                
        with col_btn3:
            if st.button("Delete", key=f"delete_{task['id']}"):
                st.session_state.tasks = [t for t in st.session_state.tasks if t["id"] != task["id"]]
                st.rerun()