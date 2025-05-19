# AstroWordle  
*A Space-Themed Wordle Game built with Streamlit*

## 🌟 About AstroWordle
**AstroWordle** is a visually enhanced, interactive word-guessing game built using [Streamlit](https://streamlit.io/). Inspired by the original **Wordle**, this galactic twist features a score system, stylish color-coded feedback, and a custom background that immerses you in a cosmic experience!

## 🌐 Try it here: [https://wordle-aztura.streamlit.app/](https://wordle-aztura.streamlit.app/)

## 🎮 Features

- 🔠 **Guess the 5-letter secret word** in **7 attempts**
- 🎨 **Color-coded feedback** for each guess:
  - 🟩 Green — correct letter in the correct position  
  - 🟨 Yellow — correct letter in the wrong position  
  - ⬜ White — incorrect letter  
- 🔢 **Scoring system**:
  - Starts at 800  
  - Deducts 100 points per incorrect guess  
- 🔁 **Play Again** option for quick resets  
- 💾 Uses `st.session_state` to manage game state

## 🎨 Visual & Styling

- Custom Dreamscape font
- Space-themed background image (set via base64)
- Colored letter feedback using HTML/CSS instead of emojis

## 📁 File Structure
astrowordle/
├── wordle.py # Main Streamlit app file
├── wordlist.txt # List of valid 5-letter words (one per line)
├── background.png # Background image used in the app
└── fonts/
└── dreamscape.ttf # Custom font used for UI

## 📜 Requirements

- Python 3.7 or higher  
- Streamlit ≥ 1.20  
- A `wordlist.txt` file with valid 5-letter words (one per line)

## 👩‍💻 Author

Made with ❤️ by **Rishmitha**  
Open to feedback, issues, or feature suggestions!

## 📄 License
This project is licensed under the **MIT License**.
