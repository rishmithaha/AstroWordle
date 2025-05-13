# 🪐 AstroWordle - A Space-Themed Wordle Game with Streamlit

AstroWordle is a fun, web-based word guessing game built with [Streamlit](https://streamlit.io/). Inspired by the viral game **Wordle**, this version adds a unique scoring system, attempt limits, and an interactive interface — perfect for word enthusiasts and stargazers alike!

---

## 🎮 Features

- 🔠 **Guess the 5-letter secret word** in **7 attempts**
- ✅ **Emoji-based feedback**:
  - 🟩 Correct letter in the correct position
  - 🟨 Correct letter in the wrong position
  - ⬜ Letter not in the word
- 🧠 **Score starts at 800**, loses 100 points per guess
- 🔁 **Play Again** option resets the game
- 🧾 State preserved using `st.session_state`

---

## 📁 File Structure

wordle-streamlit/
- wordle.py # Main Streamlit app file
- wordlist.txt # List of valid 5-letter words (one per line)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wordle-streamlit.git
cd wordle-streamlit
```

### 2. Install Requirements
Create a virtual environment (optional but recommended), then install:

```bash
pip install streamlit
```
### 3. Run the App
```bash
streamlit run wordle.py
```
### 📜 Requirements

- Python 3.7 or higher  
- Streamlit ≥ 1.20  
- A `wordlist.txt` file containing 5-letter words (one per line)

### 👩‍💻 Author

Made with ❤️ by Rishmitha  
Feel free to contribute or suggest features via issues or pull requests!

### 📄 License
This project is licensed under the MIT License.
