import streamlit as st
import random

# पेज सेटअप
st.set_page_config(page_title="For Navya ❤️", page_icon="🌹")

# सेशन स्टेट्स
if 'no_count' not in st.session_state:
    st.session_state.no_count = 0
if 'is_forgiven' not in st.session_state:
    st.session_state.is_forgiven = False
if 'heart_type' not in st.session_state:
    st.session_state.heart_type = None

no_messages = [
    "No 😠", "Sach mai? 🥺", "Phir soch lo... 🤔", 
    "Phir ek bar phir se... 🧐", "Sorry na bebe... Plzzz? 🎀", "Otheeeeee... ❤️"
]

# --- CSS: बैकग्राउंड और एनीमेशन ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(to bottom, #ffdde1, #ee9ca7); }
    .stButton>button { border-radius: 30px; border: 2px solid #ff4b4b; background-color: white; color: #ff4b4b; font-weight: bold; width: 100%; }
    
    @keyframes fall {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .heart {
        position: fixed; top: -10%; user-select: none; pointer-events: none; z-index: 9999;
        animation: fall 3s linear forwards;
    }
    .love-text {
        text-align: center; color: white; font-size: 40px; font-weight: bold; text-shadow: 2px 2px #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

def get_heart_html(heart_symbol):
    heart_html = ""
    for _ in range(40): 
        left = random.randint(0, 100)
        duration = random.uniform(1.5, 3.5)
        delay = random.uniform(0, 1)
        size = random.randint(20, 50)
        heart_html += f'<div class="heart" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s; font-size:{size}px;">{heart_symbol}</div>'
    return heart_html

# --- UI लॉजिक ---

if not st.session_state.is_forgiven:
    # एनीमेशन दिखाना अगर कोई बटन दबाया गया हो
    if st.session_state.heart_type:
        st.markdown(get_heart_html(st.session_state.heart_type), unsafe_allow_html=True)
        st.session_state.heart_type = None # रिसेट

    st.markdown("<h1 style='text-align: center; color: white;'>Hi Navya... ❤️</h1>", unsafe_allow_html=True)
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes, Maaf kiya! 😍"):
            st.session_state.is_forgiven = True
            st.rerun()

    with col2:
        if st.session_state.no_count < len(no_messages):
            current_text = no_messages[st.session_state.no_count]
            if st.button(current_text):
                if "Otheeeeee" in current_text:
                    st.session_state.is_forgiven = True
                    st.session_state.heart_type = "❤️" # यहाँ लाल दिल सेट किया
                else:
                    st.session_state.no_count += 1
                    st.session_state.heart_type = "💔" # बाकी सब पर टूटे दिल
                st.rerun()
        else:
            st.write("Ab toh maaf kar do please... 🥺")

else:
    # --- माफ़ी के बाद का जश्न ---
    st.markdown(get_heart_html("❤️"), unsafe_allow_html=True)
    st.balloons()
    st.markdown("<div class='love-text'>I LOVE U NAVYA SO MUCH ❤️</div>", unsafe_allow_html=True)
    
    # एनिमेटेड वीडियो ऑटो-प्ले
    try:
        video_file = open('navya_video.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes, autoplay=True, loop=True)
    except FileNotFoundError:
        st.info("Aryan ❤️ Navya: Waiting for the sunset... ✨")

    st.markdown("<h3 style='text-align: center; color: white;'>Hamesha ke liye saath! ✨</h3>", unsafe_allow_html=True)
