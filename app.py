import streamlit as st
import requests

# Page Config
st.set_page_config(
    page_title="RAYYAN.AI | Full-Stack AI Engineer Portfolio & SaaS Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------------------
# HIGH-CONTRAST LUXURY GLASSMORPHISM + ROBOT AVATAR CHATBOT CSS
# -------------------------------------------------------------
st.markdown("""
<style>
    /* Dark Deep Theme Background */
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(15, 12, 41) 0%, rgb(24, 19, 58) 50%, rgb(10, 10, 26) 100%);
        color: #f8fafc !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Glassmorphic Container Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(168, 85, 247, 0.3);
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 24px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease-in-out;
    }
    
    .glass-card:hover {
        border: 1px solid rgba(56, 189, 248, 0.6);
        box-shadow: 0 8px 32px 0 rgba(56, 189, 248, 0.25);
    }
    
    /* Header Neon Text */
    .hero-title {
        background: linear-gradient(135deg, #c084fc 0%, #38bdf8 50%, #4ade80 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3.2rem !important;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 4px;
    }
    
    .hero-subtitle {
        color: #facc15 !important;
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 25px;
        text-shadow: 0 0 12px rgba(250, 204, 21, 0.3);
    }

    /* High Contrast Text Styles */
    .contrast-body {
        color: #f8fafc !important;
        font-size: 1.05rem;
        line-height: 1.7;
    }

    .contrast-highlight {
        color: #38bdf8 !important;
        font-weight: 700;
    }

    /* High Contrast Skill Tags */
    .skill-tag {
        background: rgba(56, 189, 248, 0.2);
        color: #38bdf8 !important;
        border: 1px solid #38bdf8;
        padding: 8px 16px;
        border-radius: 12px;
        font-size: 0.9rem;
        font-weight: 700;
        display: inline-block;
        margin: 5px;
        box-shadow: 0 0 10px rgba(56, 189, 248, 0.2);
    }

    /* Status Badges */
    .badge-online {
        background: rgba(74, 222, 128, 0.2);
        color: #4ade80 !important;
        border: 1px solid #4ade80;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 700;
        display: inline-block;
    }

    .badge-offline {
        background: rgba(248, 113, 113, 0.2);
        color: #f87171 !important;
        border: 1px solid #f87171;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 700;
        display: inline-block;
    }
    
    /* Custom Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(10, 10, 26, 0.85) !important;
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(168, 85, 247, 0.3);
    }

    /* Modern Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #a855f7 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        border: 1px solid #c084fc !important;
        border-radius: 12px !important;
        padding: 10px 20px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        box-shadow: 0 4px 20px rgba(168, 85, 247, 0.5) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 28px rgba(56, 189, 248, 0.8) !important;
        border-color: #38bdf8 !important;
    }

    /* -------------------------------------------------------------
       PERFECT FIXED BOTTOM-RIGHT ROBOT AVATAR FLOATING WIDGET
    ------------------------------------------------------------- */
    div[data-testid="stVerticalBlock"] > div:has(div.floating-chat-anchor) {
        position: fixed !important;
        bottom: 25px !important;
        right: 25px !important;
        width: 380px !important;
        max-width: 88vw !important;
        z-index: 999999 !important;
    }

    div[data-testid="stExpander"] {
        border: none !important;
        background: transparent !important;
        box-shadow: none !important;
    }

    div[data-testid="stExpander"] details {
        border: none !important;
        background: rgba(15, 10, 35, 0.96) !important;
        backdrop-filter: blur(25px) !important;
        -webkit-backdrop-filter: blur(25px) !important;
        border-radius: 20px !important;
        border: 2px solid #a855f7 !important;
        box-shadow: 0 12px 40px rgba(168, 85, 247, 0.6) !important;
        overflow: hidden !important;
    }

    div[data-testid="stExpander"] details summary {
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        padding: 12px 18px !important;
        background: linear-gradient(135deg, #a855f7 0%, #2563eb 100%) !important;
        color: #ffffff !important;
        font-weight: 800 !important;
        border-radius: 18px !important;
        cursor: pointer !important;
    }

    /* ROBOT AVATAR CIRCLE WHEN CLOSED */
    div[data-testid="stExpander"] details:not([open]) {
        width: 70px !important;
        height: 70px !important;
        margin-left: auto !important;
        border-radius: 50% !important;
        border: 2px solid #38bdf8 !important;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.8) !important;
        animation: robot-pulse 2s infinite alternate;
        background: radial-gradient(circle, #38bdf8 0%, #0f172a 100%) !important;
    }

    div[data-testid="stExpander"] details:not([open]) summary {
        border-radius: 50% !important;
        width: 100% !important;
        height: 100% !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        background: transparent !important;
    }

    div[data-testid="stExpander"] details:not([open]) summary p {
        display: none !important;
    }

    /* High-Tech Robot Icon replacing grey badge */
    div[data-testid="stExpander"] details:not([open]) summary::after {
        content: "🤖";
        font-size: 2.2rem;
    }

    @keyframes robot-pulse {
        0% { box-shadow: 0 0 15px rgba(168, 85, 247, 0.6); transform: scale(1); }
        100% { box-shadow: 0 0 30px rgba(56, 189, 248, 0.95); transform: scale(1.05); }
    }

    .chat-guard-badge {
        font-size: 0.78rem;
        background: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        border: 1px solid #38bdf8;
        padding: 3px 8px;
        border-radius: 6px;
        display: inline-block;
        margin-bottom: 8px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

BACKEND_URL = "http://127.0.0.1:8000"

# Health Check with Backend
backend_online = False
try:
    res = requests.get(f"{BACKEND_URL}/", timeout=3)
    if res.status_code == 200:
        backend_online = True
except Exception:
    backend_online = False

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='color: #c084fc; font-weight:800; font-size: 1.8rem;'>⚡ RAYYAN.AI</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #38bdf8; font-size: 0.95rem; font-weight: 700;'>Created by Rayyan | 9th Grade Full-Stack AI Engineer</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h3 style='color: #f8fafc;'>🖥 Engine Status</h3>", unsafe_allow_html=True)
    if backend_online:
        st.markdown("<span class='badge-online'>● FastAPI Engine: ONLINE</span>", unsafe_allow_html=True)
    else:
        st.markdown("<span class='badge-offline'>○ FastAPI Engine: OFFLINE</span>", unsafe_allow_html=True)
        st.markdown("<p style='color: #facc15; font-size:0.85rem; margin-top:5px;'>Run `uv run python main.py` in Terminal 1</p>", unsafe_allow_html=True)

# Main Hero Header
st.markdown("<h1 class='hero-title'>Rayyan | Full-Stack AI Agent Developer</h1>", unsafe_allow_html=True)
st.markdown("<p class='hero-subtitle'>⚡ 9th Grade Software & AI Agent Developer | Web Development with Advanced AI</p>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 1: RAYYAN'S PERSONAL PORTFOLIO & TECH STACK
# -------------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #38bdf8; font-weight:800; font-size:1.5rem; margin-bottom: 12px;'>👨‍💻 About Me & Engineering Stack</h3>", unsafe_allow_html=True)

col_a, col_b = st.columns([2, 1])

with col_a:
    st.markdown("""
    <div class='contrast-body'>
    <span class='contrast-highlight'>Asalamualikum</span>, I'm <span class='contrast-highlight'>Rayyan</span>! I am a passionate <span class='contrast-highlight'>Full-Stack AI Developer</span> currently studying in <span class='contrast-highlight'>9th Grade</span> and specializing in <span class='contrast-highlight'>Web Development with Advanced AI</span>.<br><br>
    I build autonomous AI agent systems, full-stack microservices using <span class='contrast-highlight'>FastAPI</span>, and interactive web applications with <span class='contrast-highlight'>Streamlit</span>.<br><br>
    
    • <b>Core Focus:</b> Decoupled Dual-Server Architecture, Agentic Workflows, Structured Outputs & AI Guardrails.<br>
    • <b>Development Setup:</b> Windows Workstation, <code>uv</code> Package Manager, OpenRouter API Integration.
    </div>
    """, unsafe_allow_html=True)

with col_b:
    st.markdown("<h4 style='color: #c084fc; font-weight:800;'>🚀 Technical Stack</h4>", unsafe_allow_html=True)
    st.markdown("""
    <span class='skill-tag'>Python 3.12</span>
    <span class='skill-tag'>FastAPI</span>
    <span class='skill-tag'>Streamlit</span>
    <span class='skill-tag'>OpenAI Agents SDK</span>
    <span class='skill-tag'>OpenRouter</span>
    <span class='skill-tag'>Pydantic</span>
    <span class='skill-tag'>Uvicorn</span>
    <span class='skill-tag'>uv</span>
    """, unsafe_allow_html=True)

st.markdown("---")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Education", "9th Grade Student")
m2.metric("Specialization", "Advanced AI Agents")
m3.metric("Architecture", "Dual-Server Decoupled")
m4.metric("SDK Stack", "FastAPI + Streamlit")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------------------
# SECTION 2: LIVE AI PORTFOLIO & RESUME EVALUATOR PORTAL
# -------------------------------------------------------------
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("<h3 style='color: #c084fc; font-weight:800; font-size:1.5rem; margin-bottom: 15px;'>🚀 Live SaaS Portal: AI Portfolio Evaluator</h3>", unsafe_allow_html=True)

DEFAULT_ROLE = "Full-Stack AI Developer / Agent Engineer"
DEFAULT_BIO = (
    "Rayyan - 9th Grade Student & AI Developer.\n"
    "Skills: Python, FastAPI, Streamlit, OpenAI Agents SDK, OpenRouter, REST APIs, Git, AsyncOpenAI.\n"
    "Projects:\n"
    "- Decoupled Dual-Server Portfolio & Resume Evaluator App\n"
    "- Mini-Devin AI Engineer Agent\n"
    "- Voice-Activated Desktop & Web Calculators\n"
    "- Streamlit Guardrails Application"
)

target_role = st.text_input("Target Designation / Role", value=DEFAULT_ROLE)
skills_bio = st.text_area("Candidate Bio, Technical Skills & Major Projects", value=DEFAULT_BIO, height=180)

col_btn1, col_btn2 = st.columns([2, 1])
with col_btn1:
    analyze_btn = st.button("⚡ Run Autonomous AI Evaluation")
with col_btn2:
    if st.button("🔄 Reset Fields"):
        st.rerun()

st.markdown("</div>", unsafe_allow_html=True)

if analyze_btn:
    if not skills_bio.strip():
        st.warning("Please enter skills or bio details!")
    elif not backend_online:
        st.error("⚠️ Cannot connect to FastAPI Backend! Please start Terminal 1 first: `uv run python main.py`")
    else:
        with st.spinner("AI Agent is analyzing profile against requirements..."):
            try:
                # TIMEOUT SET TO 45 SECONDS TO PREVENT TIME OUT ERRORS
                response = requests.post(
                    f"{BACKEND_URL}/analyze",
                    json={"target_role": target_role, "skills_and_bio": skills_bio},
                    timeout=45
                )
                if response.status_code == 200:
                    data = response.json()
                    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                    st.markdown("<h3 style='color: #38bdf8; font-weight:800;'>📊 Agent Evaluation Report</h3>", unsafe_allow_html=True)
                    score = data.get("overall_score", 0)
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.metric("Overall Match Score", f"{score} / 100")
                        st.progress(score / 100)
                    with col2:
                        st.markdown(f"<p style='color:#f8fafc; font-size:1.05rem;'><b>Executive Summary:</b><br>{data.get('summary', '')}</p>", unsafe_allow_html=True)
                    st.markdown("</div>", unsafe_allow_html=True)
                else:
                    st.error(f"Backend Returned Error: {response.text}")
            except requests.exceptions.Timeout:
                st.error("⌛ Request Timed Out! Model server slow tha. Phir se 'Run Autonomous AI Evaluation' click karein ya OpenRouter model check karein.")
            except Exception as e:
                st.error(f"Communication Error: {e}")

# -------------------------------------------------------------
# SECTION 3: FLOATING ROBOT AVATAR CHATBOT WIDGET
# -------------------------------------------------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "Asalamualikum! I am Rayyan's Dedicated AI Assistant. Ask me anything about Rayyan or this platform!"}
    ]

with st.container():
    st.markdown('<div class="floating-chat-anchor"></div>', unsafe_allow_html=True)
    
    with st.expander("🤖 Chat with RAYYAN.AI", expanded=False):
        st.markdown("<span class='chat-guard-badge'>🛡️ Guardrailed AI Assistant</span>", unsafe_allow_html=True)
        
        chat_box = st.container(height=260)
        with chat_box:
            for msg in st.session_state.chat_history:
                if msg["role"] == "user":
                    st.markdown(f"<div style='text-align: right; margin-bottom: 6px;'><span style='background: rgba(56, 189, 248, 0.25); border: 1px solid #38bdf8; color: #f8fafc; padding: 5px 10px; border-radius: 10px; font-size:0.85rem; display: inline-block;'>{msg['content']}</span></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div style='text-align: left; margin-bottom: 6px;'><span style='background: rgba(192, 132, 252, 0.25); border: 1px solid #c084fc; color: #f8fafc; padding: 5px 10px; border-radius: 10px; font-size:0.85rem; display: inline-block;'>🤖 {msg['content']}</span></div>", unsafe_allow_html=True)

        with st.form(key="floating_chat_form", clear_on_submit=True):
            user_msg = st.text_input("Ask about Rayyan...", placeholder="e.g. What are Rayyan's skills?", label_visibility="collapsed")
            submit_chat = st.form_submit_button("Send 🚀")
            
            if submit_chat and user_msg.strip():
                st.session_state.chat_history.append({"role": "user", "content": user_msg})
                
                if backend_online:
                    try:
                        # INCREASED TIMEOUT TO 30 SECONDS FOR CHAT
                        chat_res = requests.post(f"{BACKEND_URL}/chat", json={"message": user_msg}, timeout=30)
                        if chat_res.status_code == 200:
                            bot_reply = chat_res.json().get("response", "No response received.")
                        else:
                            bot_reply = f"Error: {chat_res.text}"
                    except requests.exceptions.Timeout:
                        bot_reply = "⌛ Request timed out! Response lene mein zyada time laga. Dobara message bhejen."
                    except Exception as e:
                        bot_reply = f"Connection Failed: {e}"
                else:
                    bot_reply = "⚠️ Backend server offline hai! Terminal 1 par `uv run python main.py` start karein."
                    
                st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
                st.rerun()