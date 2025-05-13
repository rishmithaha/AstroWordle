import streamlit as st
import random

if "secret_word" not in st.session_state:
    with open("wordlist.txt", "r") as f:
        st.session_state.word_list = [word.strip() for word in f if len(word.strip()) == 5]
    st.session_state.secret_word = random.choice(st.session_state.word_list).lower()
    st.session_state.attempts = 0
    st.session_state.max_attempts = 7
    st.session_state.feedback = []
    st.session_state.game_over = False
    st.session_state.score_astro = 800

st.title("AstroWordle")
st.write(f"### Attempt {st.session_state.attempts} / {st.session_state.max_attempts}")

if not st.session_state.game_over:
    guess = st.text_input("Enter a 5-letter word", max_chars=5).lower()
    if st.button("Submit Guess") and len(guess) == 5:
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
            st.success("CONGRATULATIONS! You guessed the word.")
            st.session_state.game_over = True
        elif st.session_state.attempts >= st.session_state.max_attempts:
            st.error(f"GAME OVER! The word was '{st.session_state.secret_word.upper()}'")
            st.session_state.game_over = True
    elif st.button("Submit Guess") and len(guess) != 5:
        st.warning("Please enter a 5-letter word!")

for row in st.session_state.feedback:
    st.write(" ".join([f"{color}{char}" for color, char in row]))

if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.clear()
        st.experimental_rerun()

st.markdown(f"**Current Score:** {st.session_state.score_astro}")
