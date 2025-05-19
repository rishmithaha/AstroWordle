import streamlit as st
import random

# Load secret word only once
if "secret_word" not in st.session_state:
    with open("wordlist.txt", "r") as f:
        st.session_state.word_list = [word.strip() for word in f if len(word.strip()) == 5]
    st.session_state.secret_word = random.choice(st.session_state.word_list).lower()
    st.session_state.attempts = 0
    st.session_state.max_attempts = 7
    st.session_state.feedback = []
    st.session_state.game_over = False
    st.session_state.score_astro = 800

# Page setup
st.set_page_config(
    page_title="AstroWordle",
    page_icon="🪐",
    layout="centered",
)

import base64
from pathlib import Path

# Encode the local image file to base64
def get_base64_bg(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

bg_base64 = get_base64_bg("bg.png")

# ---- Custom Styling ----
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron&display=swap');

        html, body {{
            height: 100%;
            margin: 0;
        }}

        /* Background Image */
        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background-image: url("data:image/png;base64,{bg_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            z-index: -3;
        }}

        /* Dark Overlay */
        body::after {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            height: 100%;
            width: 100%;
            background: rgba(0, 0, 0, 0.6);
            z-index: -2;
        }}

        /* Stars animation */
        body::before {{
            animation: stars 60s linear infinite;
        }}

        @keyframes stars {{
            0% {{ background-position: 0 0; }}
            100% {{ background-position: 10000px 0; }}
        }}

        /* Typography and layout */
        html, body, [class*="css"] {{
            font-family: 'Orbitron', sans-serif;
            color: white;
        }}

        h1 {{
            font-size: 64px;
            text-shadow: 2px 2px 8px #00ffff;
            letter-spacing: 2px;
            animation: fadeIn 1.5s ease-out;
        }}

        .stTextInput>div>div>input {{
            background-color: #1e1e2f;
            color: white;
            font-size: 18px;
            border: 2px solid #4b0082;
            border-radius: 10px;
            box-shadow: 0 0 8px #00ffff;
        }}

        .stButton>button {{
            background-color: #1f1f2e;
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-weight: bold;
            transition: 0.3s;
            border: 2px solid #ffffff;
            box-shadow: 0 0 8px #00ffff;
        }}

        .stButton>button:hover {{
            background-color: #4b0082;
            border-color: cyan;
            color: cyan;
            box-shadow: 0 0 16px cyan;
        }}

        .feedback-box {{
            font-size: 28px;
            margin-bottom: 8px;
            text-shadow: 0 0 6px #ff00ff;
        }}

        .score {{
            font-size: 20px;
            font-weight: bold;
            color: #FFD700;
            text-shadow: 0 0 6px #FFD700;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(-10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
""", unsafe_allow_html=True)

# ---- Main UI ----
st.title("AstroWordle 🪐")
st.markdown(f"### Attempt {st.session_state.attempts} / {st.session_state.max_attempts}")

if not st.session_state.game_over:
    guess = st.text_input("Enter a 5-letter word", max_chars=5).lower()
    if st.button("Submit Guess", key="submit_guess_button"):
        if len(guess) != 5:
            st.warning("Please enter a 5-letter word!")
        else:
            st.session_state.attempts += 1
            st.session_state.score_astro -= 100

            def get_feedback(guess, secret):
                feedback = []
                for i in range(5):
                    if guess[i] == secret[i]:
                        feedback.append(("🟩", guess[i].upper()))
                    elif guess[i] in secret:
                        feedback.append(("🟨", guess[i].upper()))
                    else:
                        feedback.append(("⬜", guess[i].upper()))
                return feedback

            feedback = get_feedback(guess, st.session_state.secret_word)
            st.session_state.feedback.append(feedback)

            if guess == st.session_state.secret_word:
                st.success("🛸 CONGRATULATIONS! You guessed the word.")
                st.session_state.game_over = True
            elif st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f"💥 GAME OVER! The word was '{st.session_state.secret_word.upper()}'")
                st.session_state.game_over = True

# Feedback Display
for row in st.session_state.feedback:
    st.markdown(f"<div class='feedback-box'>{' '.join([f'{color}{char}' for color, char in row])}</div>", unsafe_allow_html=True)

# Play Again Option
if st.session_state.game_over:
    if st.button("Play Again", key="play_again_button"):
        st.session_state.clear()
        st.experimental_rerun()

# Score Display
st.markdown(f"<div class='score'>🌌 Current Score: {st.session_state.score_astro}</div>", unsafe_allow_html=True)

