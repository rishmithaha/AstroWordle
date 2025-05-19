import streamlit as st
import random
import base64

from pathlib import Path

st.set_page_config(page_title="AstroWordle", page_icon="🪐", layout="centered")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

local_css("style.css")
set_png_as_page_bg("background.png")

if "secret_word" not in st.session_state:
    with open("wordlist.txt", "r") as f:
        st.session_state.word_list = [word.strip() for word in f if len(word.strip()) == 5]
    st.session_state.secret_word = random.choice(st.session_state.word_list).lower()
    st.session_state.attempts = 0
    st.session_state.max_attempts = 7
    st.session_state.feedback = []
    st.session_state.game_over = False
    st.session_state.score_astro = 800

st.markdown('<div class="astro-title">AstroWordle 🪐</div>', unsafe_allow_html=True)
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
                feedback = [("", "")] * 5
                secret_chars = list(secret)
                used = [False] * 5

                for i in range(5):
                    if guess[i] == secret[i]:
                        feedback[i] = ("green", guess[i].upper())
                        used[i] = True

                for i in range(5):
                    if feedback[i][0] == "":
                        if guess[i] in secret_chars:
                            for j in range(5):
                                if secret[j] == guess[i] and not used[j]:
                                    feedback[i] = ("yellow", guess[i].upper())
                                    used[j] = True
                                    break
                        if feedback[i][0] == "":
                            feedback[i] = ("red", guess[i].upper())
                return feedback

            feedback = get_feedback(guess, st.session_state.secret_word)
            st.session_state.feedback.append(feedback)

            if guess == st.session_state.secret_word:
                st.success("🛸 CONGRATULATIONS! You guessed the word.")
                st.session_state.game_over = True
            elif st.session_state.attempts >= st.session_state.max_attempts:
                st.error(f"💥 GAME OVER! The word was '{st.session_state.secret_word.upper()}'")
                st.session_state.game_over = True

color_map = {
    "green": "#4CAF50",   # Correct letter & position
    "yellow": "#FFD700",  # Correct letter, wrong position
    "white": "#888888"    # Incorrect letter
}

for row in st.session_state.feedback:
    rendered_row = "".join([
        f"<span style='background-color:{color_map[color]}; color:white; padding:10px 14px; margin:3px; border-radius:5px; font-size:24px; display:inline-block;'>{char}</span>"
        for color, char in row
    ])
    st.markdown(f"<div style='text-align:center;'>{rendered_row}</div>", unsafe_


if st.session_state.game_over:
    if st.button("Play Again", key="play_again_button"):
        st.session_state.clear()
        st.experimental_rerun()

st.markdown(f"<div class='score'>Current Score: {st.session_state.score_astro}</div>", unsafe_allow_html=True)