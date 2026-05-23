import os
import time
import json
import requests
import streamlit as st
import streamlit.components.v1 as components

# Set page configurations
st.set_page_config(
    page_title="ScriptVibe AI - YouTube Studio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for Dark Futuristic Cyber-Neon Theme
cyber_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css');

/* Ambient Moving Background & General Styling */
@keyframes ambient-glow {
    0% { background-position: 0% 0%, 100% 100%, 0 0, 0 0; }
    50% { background-position: 50% 100%, 50% 0%, 0 0, 0 0; }
    100% { background-position: 0% 0%, 100% 100%, 0 0, 0 0; }
}

.stApp {
    background-color: #030611 !important;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(168, 85, 247, 0.12) 0%, transparent 45%),
        radial-gradient(circle at 90% 80%, rgba(0, 240, 255, 0.1) 0%, transparent 50%),
        linear-gradient(rgba(255, 255, 255, 0.003) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 255, 255, 0.003) 1px, transparent 1px) !important;
    background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px !important;
    background-attachment: fixed !important;
    color: #f1f5f9 !important;
    font-family: 'Outfit', sans-serif !important;
    animation: ambient-glow 25s ease infinite !important;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: rgba(3, 6, 17, 0.5);
}
::-webkit-scrollbar-thumb {
    background: rgba(0, 240, 255, 0.25);
    border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgba(0, 240, 255, 0.5);
}

/* Header Container */
.header-container {
    text-align: center;
    padding: 35px 25px;
    margin-bottom: 30px;
    background: linear-gradient(135deg, rgba(13, 20, 44, 0.6) 0%, rgba(6, 9, 22, 0.8) 100%);
    border: 1px solid rgba(0, 240, 255, 0.18);
    border-radius: 20px;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6), 
                0 0 30px rgba(0, 240, 255, 0.05),
                inset 0 1px 2px rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(16px);
    position: relative;
    overflow: hidden;
}

.header-container::before {
    content: "";
    position: absolute;
    top: 0; left: 0; width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #00f0ff, #ff007f, #00f0ff, transparent);
    animation: scan 5s linear infinite;
}

@keyframes scan {
    0% { transform: translateX(-100%); }
    100% { transform: translateX(100%); }
}

.header-title {
    font-family: 'Outfit', sans-serif !important;
    font-size: 3.2rem;
    font-weight: 900;
    margin: 0;
    background: linear-gradient(90deg, #00f0ff, #ff007f, #a855f7, #00f0ff);
    background-size: 300% 100%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 5px;
    animation: gradient-glow 8s ease infinite;
    text-shadow: 0 0 40px rgba(0, 240, 255, 0.15);
}

@keyframes gradient-glow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.header-subtitle {
    color: #94a3b8;
    font-size: 0.92rem;
    margin-top: 10px;
    letter-spacing: 4px;
    text-transform: uppercase;
    font-weight: 700;
    text-shadow: 0 0 8px rgba(0, 240, 255, 0.15);
}

/* Floating status badge */
.cyber-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(57, 255, 20, 0.08);
    border: 1px solid rgba(57, 255, 20, 0.25);
    color: #39ff14;
    font-size: 0.68rem;
    font-weight: 800;
    font-family: 'JetBrains Mono', monospace;
    padding: 4px 10px;
    border-radius: 20px;
    margin-top: 12px;
    letter-spacing: 1px;
    box-shadow: 0 0 10px rgba(57, 255, 20, 0.1);
}
.cyber-badge-dot {
    width: 6px;
    height: 6px;
    background-color: #39ff14;
    border-radius: 50%;
    animation: pulse-green 1.5s infinite;
}
@keyframes pulse-green {
    0% { transform: scale(0.9); opacity: 0.5; box-shadow: 0 0 0 0 rgba(57, 255, 20, 0.4); }
    70% { transform: scale(1.1); opacity: 1; box-shadow: 0 0 0 4px rgba(57, 255, 20, 0); }
    100% { transform: scale(0.9); opacity: 0.5; box-shadow: 0 0 0 0 rgba(57, 255, 20, 0); }
}

/* Card metrics */
.meta-block-card {
    background: rgba(13, 17, 33, 0.5) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 16px !important;
    padding: 24px !important;
    margin-bottom: 24px !important;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
    backdrop-filter: blur(8px) !important;
    transition: all 0.3s ease !important;
}
.meta-block-card:hover {
    border-color: rgba(168, 85, 247, 0.25) !important;
    box-shadow: 0 12px 40px rgba(168, 85, 247, 0.08) !important;
    transform: translateY(-2px) !important;
}

.meta-title {
    font-size: 0.9rem !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    color: #a855f7 !important;
    margin-bottom: 16px !important;
    display: flex !important;
    align-items: center !important;
    gap: 10px !important;
    border-bottom: 1px solid rgba(255,255,255,0.06) !important;
    padding-bottom: 10px !important;
    text-shadow: 0 0 10px rgba(168, 85, 247, 0.25) !important;
}

.title-option-item {
    background: rgba(255,255,255,0.015);
    border: 1px solid rgba(255,255,255,0.04);
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 14px;
    transition: all 0.25s ease;
}
.title-option-item:hover {
    background: rgba(0, 240, 255, 0.02);
    border-color: rgba(0, 240, 255, 0.2);
    padding-left: 22px;
}

.title-num {
    font-family: 'JetBrains Mono', monospace;
    color: #00f0ff;
    font-weight: 900;
    font-size: 1.1rem;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.3);
}

.title-text {
    font-weight: 600;
    color: #ffffff;
    font-size: 0.98rem;
}

.thumbnail-idea-text {
    font-family: 'Outfit', sans-serif;
    font-size: 1.4rem;
    font-weight: 900;
    color: #f59e0b;
    text-shadow: 0 0 15px rgba(245, 158, 11, 0.25);
    background: rgba(245, 158, 11, 0.03);
    border: 1px dashed rgba(245, 158, 11, 0.3);
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.meta-seo-desc {
    color: #cbd5e1;
    line-height: 1.7;
    font-style: italic;
    background: rgba(255,255,255,0.015);
    border-left: 4px solid #ff007f;
    padding: 14px 20px;
    border-radius: 0 10px 10px 0;
    margin: 0;
}

.hashtags-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
}

.tag-item {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    background: rgba(168, 85, 247, 0.05);
    border: 1px solid rgba(168, 85, 247, 0.15);
    padding: 6px 14px;
    border-radius: 20px;
    color: #d8b4fe;
    transition: all 0.2s ease;
}
.tag-item:hover {
    background: rgba(168, 85, 247, 0.15);
    border-color: rgba(168, 85, 247, 0.4);
    color: #f3e8ff;
    transform: translateY(-1px);
}

/* Custom Highlight Rules for Script Stage Directions */
.stage-direction {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
    margin-left: 8px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.dir-pause {
    background: rgba(245, 158, 11, 0.12) !important;
    border: 1px solid rgba(245, 158, 11, 0.3) !important;
    color: #f59e0b !important;
}

.dir-smile {
    background: rgba(34, 197, 94, 0.12) !important;
    border: 1px solid rgba(34, 197, 94, 0.3) !important;
    color: #22c55e !important;
}

.dir-camera {
    background: rgba(0, 240, 255, 0.12) !important;
    border: 1px solid rgba(0, 240, 255, 0.3) !important;
    color: #00f0ff !important;
}

.dir-action {
    background: rgba(168, 85, 247, 0.12) !important;
    border: 1px solid rgba(168, 85, 247, 0.3) !important;
    color: #a855f7 !important;
}

.timestamp {
    background: rgba(255, 0, 127, 0.1);
    border: 1px solid rgba(255, 0, 127, 0.25);
    color: #ff007f;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.78rem;
    font-weight: bold;
    padding: 2px 8px;
    border-radius: 4px;
    margin-right: 8px;
    display: inline-flex;
    align-items: center;
    gap: 4px;
}

.script-document {
    background: rgba(10, 15, 30, 0.45) !important;
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 16px !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.05) !important;
    overflow: hidden !important;
    backdrop-filter: blur(12px) !important;
    margin-top: 20px !important;
}

.script-row {
    display: flex !important;
    gap: 24px !important;
    padding: 22px 24px !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04) !important;
    transition: all 0.25s ease !important;
}
.script-row:hover {
    background: rgba(0, 240, 255, 0.02) !important;
}
.script-row:last-child {
    border-bottom: none !important;
}

.script-timecode-col {
    flex: 0 0 110px !important;
    display: flex !important;
    justify-content: flex-start !important;
    align-items: flex-start !important;
}

.timecode-pill {
    background: rgba(255, 0, 127, 0.08) !important;
    border: 1px solid rgba(255, 0, 127, 0.25) !important;
    color: #ff007f !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.8rem !important;
    font-weight: 700 !important;
    padding: 4px 10px !important;
    border-radius: 6px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    box-shadow: 0 0 10px rgba(255, 0, 127, 0.05) !important;
}

.script-content-col {
    flex: 1 !important;
}

.speaker-header {
    display: flex !important;
    align-items: center !important;
    gap: 12px !important;
    margin-bottom: 8px !important;
    flex-wrap: wrap !important;
}

.speaker-name {
    color: #ff007f !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 800 !important;
    font-size: 0.95rem !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
    text-shadow: 0 0 10px rgba(255, 0, 127, 0.15) !important;
}

.speaker-stage-dirs {
    display: inline-flex !important;
    gap: 6px !important;
    flex-wrap: wrap !important;
}

.dialogue-text {
    color: #cbd5e1 !important;
    font-size: 1.05rem !important;
    line-height: 1.75 !important;
}

.dialogue-text strong {
    color: #ffffff !important;
    font-weight: 700 !important;
}

.script-section-header {
    background: linear-gradient(90deg, rgba(0, 240, 255, 0.08) 0%, rgba(168, 85, 247, 0.02) 100%) !important;
    border-bottom: 1px solid rgba(0, 240, 255, 0.18) !important;
    color: #00f0ff !important;
    padding: 16px 24px !important;
    font-size: 1.15rem !important;
    font-weight: 800 !important;
    text-transform: uppercase !important;
    letter-spacing: 2px !important;
    margin: 0 !important;
    display: block !important;
    text-shadow: 0 0 15px rgba(0, 240, 255, 0.35) !important;
}

.script-divider {
    border: 0 !important;
    height: 1px !important;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.05), transparent) !important;
    margin: 0 !important;
}

/* Streamlit specific input and area tweaks */
div[data-testid="stForm"] {
    border: 1px solid rgba(255, 255, 255, 0.06) !important;
    border-radius: 16px !important;
    background-color: rgba(8, 12, 28, 0.45) !important;
    backdrop-filter: blur(20px) !important;
    box-shadow: 0 12px 36px rgba(0, 0, 0, 0.4), inset 0 1px 1px rgba(255, 255, 255, 0.05) !important;
    padding: 24px !important;
}

div[data-testid="stForm"] label, div[data-testid="stForm"] legend {
    color: #94a3b8 !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.5px !important;
}

div[data-testid="stTextInput"] > div, 
div[data-testid="stTextArea"] > div,
div[data-testid="stSelectbox"] > div {
    background-color: rgba(4, 6, 14, 0.8) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 10px !important;
    transition: all 0.3s ease !important;
}
div[data-testid="stTextInput"] > div:hover, 
div[data-testid="stTextArea"] > div:hover,
div[data-testid="stSelectbox"] > div:hover {
    border-color: rgba(0, 240, 255, 0.3) !important;
}
div[data-testid="stTextInput"] > div:focus-within, 
div[data-testid="stTextArea"] > div:focus-within,
div[data-testid="stSelectbox"] > div:focus-within {
    border-color: #00f0ff !important;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.25) !important;
}

div[data-testid="stTextInput"] input, 
div[data-testid="stTextArea"] textarea,
div[data-testid="stSelectbox"] div[role="combobox"] {
    color: #f1f5f9 !important;
    font-size: 0.95rem !important;
    font-family: 'Outfit', sans-serif !important;
    background-color: transparent !important;
}

/* Styled Form Generate Button */
div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(135deg, #00f0ff 0%, #a855f7 50%, #ff007f 100%) !important;
    background-size: 200% auto !important;
    border: none !important;
    color: #ffffff !important;
    font-weight: 800 !important;
    font-size: 1rem !important;
    letter-spacing: 2px !important;
    border-radius: 12px !important;
    padding: 14px 28px !important;
    box-shadow: 0 4px 15px rgba(0, 240, 255, 0.25), 
                0 0 30px rgba(168, 85, 247, 0.15) !important;
    transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1) !important;
    text-shadow: 0 1px 2px rgba(0,0,0,0.3) !important;
    height: auto !important;
}
div[data-testid="stFormSubmitButton"] button:hover {
    background-position: right center !important;
    box-shadow: 0 6px 20px rgba(0, 240, 255, 0.4), 
                0 0 40px rgba(255, 0, 127, 0.3) !important;
    transform: translateY(-2px) scale(1.01) !important;
}
div[data-testid="stFormSubmitButton"] button:active {
    transform: translateY(1px) scale(0.99) !important;
}

/* Custom Tabs styling */
div[data-testid="stTabBar"] {
    background-color: rgba(8, 12, 28, 0.6) !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px !important;
    padding: 6px !important;
    backdrop-filter: blur(10px) !important;
    margin-bottom: 20px !important;
    display: flex !important;
    gap: 8px !important;
}

div[data-testid="stTabBar"] button {
    flex: 1 !important;
    background-color: transparent !important;
    border: none !important;
    color: #94a3b8 !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.5px !important;
    padding: 10px 16px !important;
    border-radius: 8px !important;
    transition: all 0.3s ease !important;
    text-transform: uppercase !important;
}

div[data-testid="stTabBar"] button:hover {
    color: #00f0ff !important;
    background-color: rgba(255, 255, 255, 0.03) !important;
}

div[data-testid="stTabBar"] button[aria-selected="true"] {
    background: linear-gradient(135deg, rgba(0, 240, 255, 0.15) 0%, rgba(168, 85, 247, 0.1) 100%) !important;
    border: 1px solid rgba(0, 240, 255, 0.3) !important;
    color: #ffffff !important;
    box-shadow: 0 4px 15px rgba(0, 240, 255, 0.15) !important;
    text-shadow: 0 0 10px rgba(0, 240, 255, 0.4) !important;
}

div[data-testid="stTabBar"] div[data-baseweb="tab-highlight-bar"] {
    display: none !important;
}

/* Styled empty states */
.empty-state-box {
    text-align: center;
    padding: 60px 40px;
    color: #94a3b8;
    border: 1px dashed rgba(0, 240, 255, 0.25);
    border-radius: 16px;
    background: radial-gradient(circle at 50% 50%, rgba(13, 17, 33, 0.4) 0%, rgba(5, 7, 17, 0.7) 100%);
    box-shadow: inset 0 0 20px rgba(0, 240, 255, 0.03);
    margin: 25px 0;
    transition: all 0.3s ease;
}
.empty-state-box:hover {
    border-color: rgba(0, 240, 255, 0.5);
    box-shadow: inset 0 0 30px rgba(0, 240, 255, 0.06), 0 8px 32px rgba(0, 0, 0, 0.4);
}
.empty-state-icon {
    margin-bottom: 20px;
    animation: float 4s ease-in-out infinite;
}
@keyframes float {
    0% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-8px) rotate(2deg); }
    100% { transform: translateY(0px) rotate(0deg); }
}
.empty-state-title {
    font-size: 1.4rem;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 10px;
    letter-spacing: 0.5px;
}
.empty-state-desc {
    max-width: 440px;
    margin: 0 auto;
    font-size: 0.92rem;
    line-height: 1.6;
    color: #94a3b8;
}
</style>
"""
st.markdown(cyber_css, unsafe_allow_html=True)

# Render main Header Logo
header_html = """
<div class="header-container">
    <h1 class="header-title">⚡ SCRIPT-VIBE AI ⚡</h1>
    <p class="header-subtitle">Viral YouTube Script Studio & Teleprompter</p>
    <div class="cyber-badge"><span class="cyber-badge-dot"></span> SYSTEM ONLINE</div>
</div>
"""
st.markdown(header_html, unsafe_allow_html=True)

# Initialize Session States
if "script_markdown" not in st.session_state:
    st.session_state.script_markdown = ""
if "metadata_markdown" not in st.session_state:
    st.session_state.metadata_markdown = ""
if "raw_api_response" not in st.session_state:
    st.session_state.raw_api_response = ""
if "gemini_key" not in st.session_state:
    st.session_state.gemini_key = os.environ.get("GEMINI_API_KEY", "")

# TOP SECTION: Parameters expander (Full width)
has_script = bool(st.session_state.script_markdown)
with st.expander("🛠️ STUDIO CONFIGURATION & PARAMETERS", expanded=not has_script):
    with st.form("parameters_form"):
        # API Key config
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            value=st.session_state.gemini_key,
            placeholder="AI Key (stored temporarily in memory)",
            help="Your API Key is kept locally and is never sent to any third-party."
        )
        st.session_state.gemini_key = api_key
        
        # Topic input
        topic = st.text_area(
            "Video Concept / Topic *",
            placeholder="Describe what your video is about... (e.g. Why RAG is the future of AI, or 5 common coding mistakes that ruin careers)",
            height=130
        )
        
        # Grid parameters in 3 columns
        col_opt_1, col_opt_2, col_opt_3 = st.columns(3)
        with col_opt_1:
            niche = st.selectbox(
                "Niche",
                ["Tech & AI", "Education & Science", "Personal Finance & Business", "Lifestyle & Travel", "Health & Fitness", "Motivation & Psychology", "Entertainment & Gaming"]
            )
            target_audience = st.selectbox(
                "Target Audience",
                ["Tech Enthusiasts & Developers", "General Audience / Beginners", "Students & Lifelong Learners", "Business Professionals & Investors", "Teenagers & Gen-Z"]
            )
        with col_opt_2:
            tone = st.selectbox(
                "Script Tone",
                ["Engaging & Fast-paced", "Educational & Clear", "Storytelling & Dramatic", "Serious & Authoritative", "Casual & Funny"]
            )
            hook_style = st.selectbox(
                "First 5s Hook Style",
                ["Shocking fact or statistic", "Bold controversial statement", "Direct question to the viewer", "A relatable pain point or problem"]
            )
        with col_opt_3:
            video_length = st.selectbox(
                "Video Length target",
                ["1 to 2 Minutes", "3 to 5 Minutes", "5 to 8 Minutes", "8 to 12 Minutes"]
            )
            language = st.selectbox(
                "Language",
                ["English", "Spanish", "Hindi", "French", "German", "Portuguese"]
            )
            
        # Submit Button
        generate_btn = st.form_submit_button("⚡ GENERATE VIRAL SCRIPT", use_container_width=True)

# Parse output helper functions
def parse_stage_directions(text):
    import re
    def replace_dir(match):
        direction = match.group(1)
        dir_lower = direction.lower()
        if "pause" in dir_lower or "slow" in dir_lower:
            color_class = "dir-pause"
            icon = "fa-hourglass-half"
        elif "smile" in dir_lower or "laugh" in dir_lower or "warm" in dir_lower:
            color_class = "dir-smile"
            icon = "fa-face-smile"
        elif "camera" in dir_lower or "look" in dir_lower or "eye" in dir_lower:
            color_class = "dir-camera"
            icon = "fa-video"
        else:
            color_class = "dir-action"
            icon = "fa-person-running"
        return f'<span class="stage-direction {color_class}"><i class="fa-solid {icon}"></i> {direction}</span>'
    return re.sub(r'\(([^)]+)\)', replace_dir, text)

def parse_script_markdown_to_html(markdown_str):
    if not markdown_str:
        return ""
    
    import re
    lines = markdown_str.split("\n")
    html = '<div class="script-document">'
    
    current_timestamp = None
    current_stage_dirs = []
    
    def render_dialogue_row(speaker, text, timestamp, stage_dirs):
        # Format stage directions: remove single asterisks wrapping stage directions first
        text = re.sub(r'\*\s*(\([^)]+\))\s*\*|\*(\([^)]+\))\*', r'\1', text)
        text = parse_stage_directions(text)
        
        # Format bold text
        text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
        
        # Render stage directions HTML
        s_dirs_html = ""
        if stage_dirs:
            s_dirs_html = '<div class="speaker-stage-dirs">' + " ".join(stage_dirs) + '</div>'
            
        # Render timestamp HTML
        ts_html = ""
        if timestamp:
            ts_html = f'<span class="timecode-pill"><i class="fa-regular fa-clock"></i> {timestamp}</span>'
            
        return f"""
        <div class="script-row">
            <div class="script-timecode-col">{ts_html}</div>
            <div class="script-content-col">
                <div class="speaker-header">
                    <span class="speaker-name"><i class="fa-solid fa-microphone-lines"></i> {speaker}</span>
                    {s_dirs_html}
                </div>
                <div class="dialogue-text">{text}</div>
            </div>
        </div>
        """

    for line in lines:
        l = line.strip()
        if not l:
            continue
            
        # 1. Heading Parser
        if l.startswith("####") or l.startswith("###") or l.startswith("##") or l.startswith("#"):
            title = l.replace("#", "").strip()
            html += f'<div class="script-section-header">{title}</div>'
            continue
            
        # 2. Divider Parser
        if l == "---" or l == "***":
            html += '<hr class="script-divider">'
            continue
            
        # 3. Timestamp Parser
        ts_match = re.match(r'^\[([0-9:]{5})\]$', l)
        if ts_match:
            current_timestamp = ts_match.group(1)
            continue
            
        # 4. Independent Stage Directions Line
        if re.match(r'^(\([^)]+\)\s*)+$', l):
            parsed = parse_stage_directions(l)
            current_stage_dirs.append(parsed)
            continue
            
        # 5. Dialogue Line
        speaker_match = re.match(r'^\*\*([^*]+):\*\*\s*(.*)$', l) or re.match(r'^([A-Z\s]{3,}):\s*(.*)$', l)
        if speaker_match:
            speaker = speaker_match.group(1).replace(":", "").strip()
            dialogue = speaker_match.group(2).strip()
            
            html += render_dialogue_row(speaker, dialogue, current_timestamp, current_stage_dirs)
            # Reset
            current_timestamp = None
            current_stage_dirs = []
        else:
            # If it's a general line (narrative or dialogue without speaker tag)
            host_match = re.match(r'^HOST:\s*(.*)$', l, re.IGNORECASE)
            if host_match:
                dialogue = host_match.group(1).strip()
                html += render_dialogue_row("HOST", dialogue, current_timestamp, current_stage_dirs)
            else:
                # Standard narrative or continuation line
                html += render_dialogue_row("HOST", l, current_timestamp, current_stage_dirs)
                
            # Reset
            current_timestamp = None
            current_stage_dirs = []
            
    html += '</div>'
    return html

def parse_metadata_to_kpis(meta_str):
    if not meta_str:
        return ""
    lines = meta_str.split("\n")
    titles = []
    thumbnail = ""
    desc = ""
    tags = []
    
    for line in lines:
        l = line.strip()
        if not l:
            continue
            
        if l.startswith("1. ") or l.startswith("2. ") or l.startswith("3. ") or l.startswith("Option"):
            titles.append(l.replace("1.", "").replace("2.", "").replace("3.", "").replace("Option", "").strip())
        elif "thumbnail" in l.lower():
            thumbnail = l.split(":")[-1].strip() if ":" in l else l
        elif "description" in l.lower():
            desc = l.split(":")[-1].strip() if ":" in l else l
        elif "#" in l:
            import re
            found = re.findall(r'#[a-zA-Z0-9]+', l)
            if found:
                tags.extend(found)
                
    html = ""
    # Rendering HTML cards
    if titles:
        opts = "".join([f'<div class="title-option-item"><span class="title-num">0{idx+1}</span><span class="title-text">{t}</span></div>' for idx, t in enumerate(titles[:3])])
        html += f'<div class="meta-block-card"><div class="meta-title">Video Title Suggestions</div>{opts}</div>'
    if thumbnail:
        html += f'<div class="meta-block-card"><div class="meta-title">Thumbnail Text Idea</div><div class="thumbnail-idea-text">{thumbnail}</div></div>'
    if desc:
        html += f'<div class="meta-block-card"><div class="meta-title">SEO Optimized Description</div><p class="meta-seo-desc">{desc}</p></div>'
    if tags:
        tg_html = "".join([f'<span class="tag-item">{tag}</span>' for tag in tags])
        html += f'<div class="meta-block-card"><div class="meta-title">Search Tags</div><div class="hashtags-grid">{tg_html}</div></div>'
        
    if not html:
        html = f"<div class='meta-block-card'>{meta_str}</div>"
    return html

# Embedded HTML/JS Teleprompter Template Component
TELEPROMPTER_IFRAME_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@500;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            background-color: #020308;
            color: rgba(255, 255, 255, 0.45);
            font-family: 'Outfit', sans-serif;
            margin: 0;
            padding: 0;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            height: 100vh;
        }
        .toolbar {
            display: flex;
            gap: 15px;
            align-items: center;
            background: rgba(9, 12, 21, 0.9);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(0, 240, 255, 0.2);
            padding: 12px 20px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
            z-index: 10;
        }
        .btn {
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            cursor: pointer;
            padding: 8px 16px;
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.85rem;
            transition: all 0.3s cubic-bezier(0.165, 0.84, 0.44, 1);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .btn-play {
            background: #00f0ff;
            color: #000;
            border-color: #00f0ff;
        }
        .btn-play:hover {
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.5);
            transform: translateY(-1px);
        }
        .btn-reset {
            background: rgba(255, 255, 255, 0.05);
            color: #e2e8f0;
        }
        .btn-reset:hover {
            background: rgba(255, 255, 255, 0.12);
            border-color: rgba(255, 255, 255, 0.2);
            color: #ffffff;
        }
        .btn-reset.active {
            background: rgba(168, 85, 247, 0.2);
            border-color: #a855f7;
            color: #ffffff;
            box-shadow: 0 0 12px rgba(168, 85, 247, 0.3);
        }
        .btn-rec {
            background: rgba(255, 255, 255, 0.05);
            color: #e2e8f0;
        }
        .btn-rec:hover {
            background: rgba(239, 68, 68, 0.15);
            border-color: rgba(239, 68, 68, 0.3);
        }
        .btn-rec.active {
            background: rgba(239, 68, 68, 0.2);
            border-color: #ef4444;
            color: #ffffff;
            box-shadow: 0 0 12px rgba(239, 68, 68, 0.4);
        }
        .rec-dot {
            width: 8px;
            height: 8px;
            background-color: #94a3b8;
            border-radius: 50%;
            transition: all 0.3s;
        }
        .btn-rec.active .rec-dot {
            background-color: #ef4444;
            animation: blink 1.2s infinite;
        }
        @keyframes blink {
            0% { opacity: 0.3; }
            50% { opacity: 1; }
            100% { opacity: 0.3; }
        }
        .rec-timer {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
            color: #ef4444;
            font-weight: 700;
            margin-left: auto;
            display: none;
            align-items: center;
            gap: 8px;
            background: rgba(239, 68, 68, 0.08);
            border: 1px solid rgba(239, 68, 68, 0.2);
            padding: 6px 12px;
            border-radius: 6px;
        }
        .rec-timer i {
            font-size: 8px;
            animation: blink 1.2s infinite;
        }
        .rec-timer.visible {
            display: flex;
        }
        .ctrl-group {
            display: flex;
            align-items: center;
            gap: 10px;
            font-size: 0.8rem;
            color: #94a3b8;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .ctrl-group input[type="range"] {
            -webkit-appearance: none;
            width: 90px;
            height: 4px;
            border-radius: 2px;
            background: rgba(255, 255, 255, 0.1);
            outline: none;
            cursor: pointer;
        }
        .ctrl-group input[type="range"]::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: #00f0ff;
            box-shadow: 0 0 8px rgba(0, 240, 255, 0.5);
            transition: transform 0.1s;
        }
        .ctrl-group input[type="range"]::-webkit-slider-thumb:hover {
            transform: scale(1.2);
        }
        .ctrl-group span {
            color: #00f0ff;
            font-family: 'JetBrains Mono', monospace;
            min-width: 38px;
        }
        .prompter-screen {
            flex: 1;
            position: relative;
            background: #020308;
            overflow: hidden;
        }
        .focus-box {
            position: absolute;
            left: 0;
            top: 50%;
            transform: translateY(-50%);
            width: 100%;
            height: 80px;
            background: linear-gradient(180deg, rgba(0, 240, 255, 0.04) 0%, rgba(0, 240, 255, 0.0) 100%);
            border-top: 1.5px dashed rgba(0, 240, 255, 0.3);
            border-bottom: 1.5px dashed rgba(0, 240, 255, 0.3);
            pointer-events: none;
            z-index: 2;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.05);
        }
        .focus-box::after {
            content: "FOCUS ZONE";
            position: absolute;
            right: 20px;
            top: 6px;
            font-size: 0.6rem;
            color: rgba(0, 240, 255, 0.4);
            font-weight: 800;
            letter-spacing: 1.5px;
        }
        .scroll-canvas {
            width: 100%;
            height: 100%;
            overflow-y: auto;
            padding: 50vh 40px; /* Offset scrolling past mid focus */
            box-sizing: border-box;
            text-align: center;
            scroll-behavior: smooth;
            transition: transform 0.3s;
        }
        .scroll-canvas::-webkit-scrollbar {
            display: none;
        }
        .scroll-canvas.mirrored {
            transform: scaleX(-1);
        }
        .paragraph {
            margin-bottom: 2.2rem;
            font-weight: 700;
            line-height: 1.6;
            transition: all 0.3s ease;
        }
        .paragraph.active {
            color: #ffffff;
            text-shadow: 0 0 15px rgba(255,255,255,0.4);
            transform: scale(1.03);
        }
        .stage-direction {
            font-family: 'Outfit', sans-serif;
            font-size: 0.65em;
            font-weight: 700;
            padding: 3px 8px;
            border-radius: 6px;
            margin-left: 8px;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }
        .dir-pause {
            background: rgba(255, 189, 0, 0.12) !important;
            border: 1px solid rgba(255, 189, 0, 0.3) !important;
            color: #ffbd00 !important;
        }
        .dir-smile {
            background: rgba(57, 255, 20, 0.12) !important;
            border: 1px solid rgba(57, 255, 20, 0.3) !important;
            color: #39ff14 !important;
        }
        .dir-camera {
            background: rgba(0, 240, 255, 0.12) !important;
            border: 1px solid rgba(0, 240, 255, 0.3) !important;
            color: #00f0ff !important;
        }
        .dir-action {
            background: rgba(157, 78, 221, 0.12) !important;
            border: 1px solid rgba(157, 78, 221, 0.3) !important;
            color: #9d4edd !important;
        }
        .timestamp {
            background: rgba(255, 0, 127, 0.12);
            border: 1px solid rgba(255, 0, 127, 0.3);
            color: #ff007f;
            font-size: 0.65em;
            padding: 2px 6px;
            border-radius: 4px;
            margin-right: 6px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="toolbar">
        <button id="play-btn" class="btn btn-play"><i class="fa-solid fa-play"></i> Play</button>
        <button id="reset-btn" class="btn btn-reset"><i class="fa-solid fa-backward-step"></i> Reset</button>
        <button id="mirror-btn" class="btn btn-reset"><i class="fa-solid fa-arrows-left-right"></i> Mirror</button>
        <button id="rec-btn" class="btn btn-rec"><span class="rec-dot"></span> Practice REC</button>
        
        <div class="ctrl-group">
            <label><i class="fa-solid fa-gauge-high"></i> Speed</label>
            <input type="range" id="speed" min="1" max="10" value="3">
            <span id="speed-val">3</span>
        </div>
        
        <div class="ctrl-group">
            <label><i class="fa-solid fa-text-height"></i> Size</label>
            <input type="range" id="size" min="20" max="60" value="32">
            <span id="size-val">32px</span>
        </div>

        <div id="rec-timer" class="rec-timer">
            <i class="fa-solid fa-circle"></i> <span id="timer-val">00:00</span>
        </div>
    </div>
    
    <div class="prompter-screen">
        <div class="focus-box"></div>
        <div id="canvas" class="scroll-canvas"></div>
    </div>

    <script>
        const scriptData = %SCRIPT_DATA_JSON%;
        const canvas = document.getElementById('canvas');
        const playBtn = document.getElementById('play-btn');
        const resetBtn = document.getElementById('reset-btn');
        const mirrorBtn = document.getElementById('mirror-btn');
        const recBtn = document.getElementById('rec-btn');
        const recTimer = document.getElementById('rec-timer');
        const timerVal = document.getElementById('timer-val');
        const speedInput = document.getElementById('speed');
        const sizeInput = document.getElementById('size');
        const speedVal = document.getElementById('speed-val');
        const sizeVal = document.getElementById('size-val');

        let isRunning = false;
        let scrollTimer = null;
        let isMirrored = false;
        let isRecording = false;
        let recInterval = null;
        let recSeconds = 0;

        // Load Script content
        function loadScript() {
            canvas.innerHTML = '';
            if(!scriptData) {
                canvas.innerHTML = '<div style="color: #94a3b8; font-size: 20px;">Awaiting generated script...</div>';
                return;
            }
            const lines = scriptData.split('\\n');
            lines.forEach(line => {
                const trimmed = line.trim();
                if(!trimmed || trimmed.startsWith('#') || trimmed.startsWith('---') || trimmed.startsWith('===') || trimmed.startsWith('* ') || trimmed.startsWith('- ')) return;
                
                const div = document.createElement('div');
                div.className = 'paragraph';
                div.style.fontSize = sizeInput.value + 'px';
                
                let text = trimmed;
                
                // Remove speaker prefix like **HOST:** or HOST:
                text = text.replace(/^\\*\\*HOST:\\*\\*\\\\s*/i, '');
                text = text.replace(/^HOST:\\\\s*/i, '');
                
                // Clean any other raw bold markers
                text = text.replace(/\\*\\*([^*]+)\\*\\*/g, '$1');
                
                // Parse stage directions
                text = text.replace(/\\(([^)]+)\\)/g, (match, direction) => {
                    const dir_lower = direction.toLowerCase();
                    let cls = 'dir-action';
                    let icon = 'fa-person-running';
                    if (dir_lower.includes('pause') || dir_lower.includes('slow')) {
                        cls = 'dir-pause';
                        icon = 'fa-hourglass-half';
                    } else if (dir_lower.includes('smile') || dir_lower.includes('laugh') || dir_lower.includes('warm')) {
                        cls = 'dir-smile';
                        icon = 'fa-face-smile';
                    } else if (dir_lower.includes('camera') || dir_lower.includes('look') || dir_lower.includes('eye')) {
                        cls = 'dir-camera';
                        icon = 'fa-video';
                    }
                    return `<span class="stage-direction ${cls}"><i class="fa-solid ${icon}"></i> ${direction}</span>`;
                });
                // Parse timestamps
                text = text.replace(/\\[([0-9:]{5})\\]/g, '<span class="timestamp"><i class="fa-regular fa-clock"></i> $1</span>');
                
                div.innerHTML = text;
                canvas.appendChild(div);
            });
            resetPrompter();
        }

        function resetPrompter() {
            pause();
            canvas.scrollTop = 0;
            updateHighlights();
            if (isRecording) {
                startTimer();
            }
        }

        function play() {
            isRunning = true;
            playBtn.innerHTML = '<i class="fa-solid fa-pause"></i> Pause';
            playBtn.style.background = '#ff007f';
            playBtn.style.color = '#fff';
            playBtn.style.borderColor = '#ff007f';
            
            const spd = parseInt(speedInput.value);
            scrollTimer = setInterval(() => {
                canvas.scrollTop += spd * 0.4;
                updateHighlights();
            }, 16);
        }

        function pause() {
            isRunning = false;
            playBtn.innerHTML = '<i class="fa-solid fa-play"></i> Play';
            playBtn.style.background = '#00f0ff';
            playBtn.style.color = '#000';
            playBtn.style.borderColor = '#00f0ff';
            
            if(scrollTimer) {
                clearInterval(scrollTimer);
                scrollTimer = null;
            }
        }

        function updateHighlights() {
            const paras = canvas.querySelectorAll('.paragraph');
            if(paras.length === 0) return;
            const canvasRect = canvas.getBoundingClientRect();
            const focusY = canvasRect.top + (canvasRect.height / 2);
            
            let minDistance = Infinity;
            let closest = null;
            
            paras.forEach(p => {
                const pRect = p.getBoundingClientRect();
                const centerY = pRect.top + (pRect.height / 2);
                const dist = Math.abs(centerY - focusY);
                if(dist < minDistance) {
                    minDistance = dist;
                    closest = p;
                }
            });
            
            paras.forEach(p => p.classList.remove('active'));
            if(closest) closest.classList.add('active');
        }

        playBtn.addEventListener('click', () => {
            if(isRunning) pause(); else play();
        });
        resetBtn.addEventListener('click', resetPrompter);

        mirrorBtn.addEventListener('click', () => {
            isMirrored = !isMirrored;
            if (isMirrored) {
                canvas.classList.add('mirrored');
                mirrorBtn.classList.add('active');
            } else {
                canvas.classList.remove('mirrored');
                mirrorBtn.classList.remove('active');
            }
        });

        recBtn.addEventListener('click', () => {
            isRecording = !isRecording;
            if (isRecording) {
                recBtn.classList.add('active');
                recTimer.classList.add('visible');
                startTimer();
            } else {
                recBtn.classList.remove('active');
                recTimer.classList.remove('visible');
                stopTimer();
            }
        });

        function startTimer() {
            recSeconds = 0;
            timerVal.textContent = "00:00";
            clearInterval(recInterval);
            recInterval = setInterval(() => {
                recSeconds++;
                const mins = Math.floor(recSeconds / 60).toString().padStart(2, '0');
                const secs = (recSeconds % 60).toString().padStart(2, '0');
                timerVal.textContent = mins + ':' + secs;
            }, 1000);
        }

        function stopTimer() {
            clearInterval(recInterval);
            recInterval = null;
            recSeconds = 0;
            timerVal.textContent = "00:00";
        }
        
        speedInput.addEventListener('input', (e) => {
            speedVal.textContent = e.target.value;
            if(isRunning) { pause(); play(); }
        });

        sizeInput.addEventListener('input', (e) => {
            sizeVal.textContent = e.target.value + 'px';
            const paras = canvas.querySelectorAll('.paragraph');
            paras.forEach(p => p.style.fontSize = e.target.value + 'px');
        });

        // Initialize script
        loadScript();
    </script>
</body>
</html>
"""

# Handle Script Generation Click
if generate_btn:
    if not api_key:
        st.error("⚠️ Please enter a Google Gemini API Key in the form configuration.")
    elif not topic:
        st.warning("⚠️ Please provide a Video Topic first.")
    else:
        # Dynamic progression stages
        status_bar = st.empty()
        status_bar.info("🔮 1/4 Ingesting topic and audience context...")
        time.sleep(0.7)
        status_bar.info("🚀 2/4 Synthesizing hook structure...")
        time.sleep(0.7)
        status_bar.info("🎨 3/4 Generating main retention content body...")
        time.sleep(0.7)
        status_bar.info("⚡ 4/4 Structuring video metadata and SEO tags...")
        
        systemPrompt = f"""You are an expert YouTube script writer with 10+ years of experience creating viral, high-retention, and deeply engaging video content. You have studied the top 1000 YouTube channels and you understand exactly what makes a viewer watch till the end, click like, comment, and subscribe.

Write a complete, professional, ready-to-record YouTube script in {language} for the niche: "{niche}".
Write in a conversational, friendly, and natural speaking style.
Target Audience: "{target_audience}"
Tone: "{tone}"
Approximate Video Length target: "{video_length}"

════════════════════════════════════════
SCRIPT STRUCTURE REQUIREMENTS - FOLLOW EXACTLY
════════════════════════════════════════

Your response MUST be divided into two main parts clearly marked with headers:
"=== SCRIPT METADATA ===" and "=== SCRIPT CONTENT ==="

PART 1: METADATA
Provide the following values exactly within the metadata markers:
- Video Title (give 3 highly engaging options)
- Thumbnail Text Suggestion (short, high impact, max 4 words)
- Description (first 2 lines optimized for SEO)
- 10 Hashtags

PART 2: SCRIPT CONTENT
Follow the exact sections below. IMPORTANT: Prefix every single spoken line with **HOST:** in bold (e.g. **HOST:** Have you ever felt...) to clearly indicate who is speaking. Do not add speaker tags to stage directions or timestamps.

SECTION 1 — HOOK (First 5 Seconds)
- 2 to 3 extremely powerful lines
- Choose hook style: {hook_style}
- The viewer must feel they CANNOT skip this video.
- No introduction of yourself here, just pure hook.

SECTION 2 — INTRO (5 to 30 Seconds)
- Welcome the viewer back to the channel.
- Clearly state what this video is about and what they will gain.
- Add a curiosity gap like "and I will also reveal something at the end that most people do not know".
- Ask them to stay till the end.

SECTION 3 — MAIN CONTENT (Body)
- Divide the topic into 3 to 5 clear sections.
- Each section must have:
  * A bold heading or title (e.g. ### SECTION TITLE)
  * A simple and conversational explanation
  * A real-world example, story, or analogy
  * Stage directions like (pause) or (look directly at camera)
  * A one-line transition to the next section
- Use the word YOU frequently to make it personal.
- Each section must end with a mini cliffhanger to the next.

SECTION 4 — GOLDEN NUGGET (Surprise Value)
- Reveal a secret tip, hack, or insight that 99% of people do not know.
- Make it the most memorable and high-value part of the script.

SECTION 5 — CALL TO ACTION (CTA)
- Ask to LIKE if helpful, COMMENT with a specific question related to the topic, SUBSCRIBE and turn on the bell, and SHARE with one friend.
- CTA should feel natural and conversational.

SECTION 6 — OUTRO (Last 20 to 30 Seconds)
- Thank the viewer by name style like "hey you watching this".
- Give a powerful closing line.
- Recommend the next video they should watch and why.
- End with your channel sign-off line.

════════════════════════════════════════
CRITICAL STYLE & RETENTION RULES
════════════════════════════════════════
- Write in short sentences. Maximum 15 words per sentence. This is an ABSOLUTE REQUIREMENT. Every single sentence MUST be 15 words or fewer.
- Use contractions (don't, you're, we've, it's, etc.) consistently. Make sure the speaker never says formal expressions like "we are" or "you will" or "do not" in speech unless they want extreme emphasis. Make it sound 100% like natural spoken speech.
- Start sentences with AND or BUT occasionally for natural pacing.
- Avoid filler words like basically, literally, actually, just.
- Add a re-engagement line every 60 seconds of script (e.g., "Now here is where it gets really interesting", "Wait, before I move on, you need to hear this", "And this next part changed everything for me").
- Stage directions to use in round brackets and italics: (pause), (smile), (look directly at camera), (slow down here), (show graphic or b-roll), (emphasize this word), (lean forward), (raise eyebrows). Add timestamps in brackets like [00:00], [00:30] at the start of major segments."""

        userPrompt = f"Topic: {topic}"

        try:
            # Define model candidate list
            model_candidates = [
                "gemini-3.5-flash",
                "gemini-2.5-flash",
                "gemini-flash-latest",
                "gemini-pro-latest",
                "gemini-2.0-flash"
            ]
            generated_text = None
            errors = []

            # Try official SDK first
            try:
                from google import genai
                for model_name in model_candidates:
                    try:
                        client = genai.Client(api_key=api_key)
                        response = client.models.generate_content(
                            model=model_name,
                            contents=[systemPrompt, userPrompt],
                        )
                        if response.text:
                            generated_text = response.text
                            break
                    except Exception as e:
                        errors.append(f"SDK ({model_name}): {str(e)}")
            except Exception as import_err:
                errors.append(f"SDK import failed: {str(import_err)}")

            # If SDK fails, fall back to REST API
            if not generated_text:
                for model_name in model_candidates:
                    if generated_text:
                        break
                    for api_ver in ["v1", "v1beta"]:
                        try:
                            payload = {
                                "contents": [
                                    {
                                        "role": "user",
                                        "parts": [
                                            {"text": systemPrompt},
                                            {"text": userPrompt}
                                        ]
                                    }
                                ],
                                "generationConfig": {
                                    "temperature": 0.75,
                                    "maxOutputTokens": 2500
                                }
                            }
                            url = f"https://generativelanguage.googleapis.com/{api_ver}/models/{model_name}:generateContent?key={api_key}"
                            resp = requests.post(url, json=payload, timeout=30)
                            if resp.status_code == 200:
                                data = resp.json()
                                generated_text = data["candidates"][0]["content"]["parts"][0]["text"]
                                break
                            else:
                                err_msg = resp.json().get("error", {}).get("message", f"HTTP {resp.status_code}")
                                errors.append(f"REST ({model_name} {api_ver}): {err_msg}")
                        except Exception as rest_err:
                            errors.append(f"REST ({model_name} {api_ver}): {str(rest_err)}")

            if not generated_text:
                # Attempt to list available models for debug
                sdk_models = []
                try:
                    from google import genai
                    client = genai.Client(api_key=api_key)
                    sdk_models = [m.name for m in client.models.list()]
                except Exception as list_err:
                    sdk_models = [f"Failed to list: {str(list_err)}"]
                
                raise Exception(" | ".join(errors) + f" | Available Models: {', '.join(sdk_models)}")
            
            # Split metadata & script content
            if "=== SCRIPT METADATA ===" in generated_text and "=== SCRIPT CONTENT ===" in generated_text:
                m_start = generated_text.find("=== SCRIPT METADATA ===") + len("=== SCRIPT METADATA ===")
                m_end = generated_text.find("=== SCRIPT CONTENT ===")
                st.session_state.metadata_markdown = generated_text[m_start:m_end].trim() if hasattr(str, 'trim') else generated_text[m_start:m_end].strip()
                
                s_start = m_end + len("=== SCRIPT CONTENT ===")
                st.session_state.script_markdown = generated_text[s_start:].strip()
            else:
                # Splitting fallback
                s_idx = generated_text.find("SECTION 1")
                if s_idx != -1:
                    st.session_state.metadata_markdown = generated_text[:s_idx].strip()
                    st.session_state.script_markdown = generated_text[s_idx:].strip()
                else:
                    st.session_state.script_markdown = generated_text
                    st.session_state.metadata_markdown = "No metadata separated. See Raw display tab."
                    
            st.session_state.raw_api_response = generated_text
            status_bar.success("🎉 Script Synthesized Successfully!")
            
        except Exception as e:
            status_bar.error(f"⚠️ Generation Failed: {str(e)}")

# RIGHT COLUMN: Display Workspaces
# BOTTOM SECTION: Display Workspaces (Full width)
st.subheader("🖥️ Script Studio Workspace")

# Render main tabs
tab_studio, tab_teleprompter, tab_raw, tab_meta = st.tabs([
    "📄 Studio View",
    "📺 Teleprompter",
    "📝 Raw Markdown",
    "📊 Video Metadata"
])

# Active Workspace check
has_script = bool(st.session_state.script_markdown)

with tab_studio:
    if has_script:
        # Action Toolbar
        col_bar_1, col_bar_2 = st.columns([5, 1.2])
        with col_bar_1:
            st.markdown("<div style='display: flex; align-items: center; gap: 8px; margin-top: 8px;'><span style='width: 8px; height: 8px; background: #00f0ff; border-radius: 50%; box-shadow: 0 0 8px #00f0ff;'></span> <span style='font-size: 0.85rem; font-weight: 700; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase;'>Script Draft Active</span></div>", unsafe_allow_html=True)
        with col_bar_2:
            # Clean topic for filename export
            import re
            fn_topic = re.sub(r'[^a-zA-Z0-9]', '_', topic[:15]).lower() if topic else 'script'
            st.download_button(
                label="📥 Export MD",
                data=f"{st.session_state.metadata_markdown}\n\n# SCRIPT CONTENT\n\n{st.session_state.script_markdown}",
                file_name=f"scriptvibe_{fn_topic}.md",
                mime="text/markdown",
                use_container_width=True
            )
        
        # Formatted script body
        script_html = parse_script_markdown_to_html(st.session_state.script_markdown)
        st.markdown(script_html, unsafe_allow_html=True)
    else:
        st.markdown(
            """<div class="empty-state-box">
                <div class="empty-state-icon">
                    <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="studioGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#00f0ff"/>
                                <stop offset="100%" stop-color="#ff007f"/>
                            </linearGradient>
                        </defs>
                        <path d="M15 10l4.553-2.276A1 1 0 0121 8.618v6.764a1 1 0 01-1.447.894L15 14v-4zM3 8a2 2 0 012-2h8a2 2 0 012 2v8a2 2 0 01-2 2H5a2 2 0 01-2-2V8z" stroke="url(#studioGrad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="empty-state-title">Create Your Next Viral Video</div>
                <div class="empty-state-desc">Enter your Gemini API key and concept parameters above, then click Generate to create your ready-to-record script.</div>
            </div>""",
            unsafe_allow_html=True
        )
        
with tab_teleprompter:
    if has_script:
        # Convert raw script text to JSON string to load in prompter iframe
        js_script_json = json.dumps(st.session_state.script_markdown)
        iframe_html = TELEPROMPTER_IFRAME_TEMPLATE.replace("%SCRIPT_DATA_JSON%", js_script_json)
        components.html(iframe_html, height=540)
    else:
        st.markdown(
            """<div class="empty-state-box">
                <div class="empty-state-icon">
                    <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="prompterGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#a855f7"/>
                                <stop offset="100%" stop-color="#00f0ff"/>
                            </linearGradient>
                        </defs>
                        <rect x="2" y="3" width="20" height="14" rx="2" stroke="url(#prompterGrad)" stroke-width="2"/>
                        <path d="M6 8h12M6 12h12M12 17v4" stroke="url(#prompterGrad)" stroke-width="2" stroke-linecap="round"/>
                    </svg>
                </div>
                <div class="empty-state-title">No Script Loaded</div>
                <div class="empty-state-desc">Once you generate a script, this canvas will load the active reading lines for immediate recording.</div>
            </div>""",
            unsafe_allow_html=True
        )
        
with tab_raw:
    if has_script:
        st.code(st.session_state.raw_api_response, language="markdown")
    else:
        st.markdown(
            """<div class="empty-state-box">
                <div class="empty-state-icon">
                    <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="rawGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#ff007f"/>
                                <stop offset="100%" stop-color="#a855f7"/>
                            </linearGradient>
                        </defs>
                        <path d="M16 18l6-6-6-6M8 6l-6 6 6 6m4-14l-4 16" stroke="url(#rawGrad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="empty-state-title">Awaiting API Output</div>
                <div class="empty-state-desc">Raw API markdown outputs will appear here.</div>
            </div>""",
            unsafe_allow_html=True
        )
        
with tab_meta:
    if has_script:
        meta_html = parse_metadata_to_kpis(st.session_state.metadata_markdown)
        st.markdown(meta_html, unsafe_allow_html=True)
    else:
        st.markdown(
            """<div class="empty-state-box">
                <div class="empty-state-icon">
                    <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="metaGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" stop-color="#f59e0b"/>
                                <stop offset="100%" stop-color="#ff007f"/>
                            </linearGradient>
                        </defs>
                        <path d="M3 3v18h18M18.7 8l-5.1 5.2-2.8-2.7L7 14.3" stroke="url(#metaGrad)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <div class="empty-state-title">No Metadata Configured</div>
                <div class="empty-state-desc">Click generate above to see suggestion titles, search hashtags, SEO descriptions, and thumbnail text recommendations.</div>
            </div>""",
            unsafe_allow_html=True
        )
