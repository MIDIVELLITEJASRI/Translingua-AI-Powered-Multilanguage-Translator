import streamlit as st
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Streamlit app
st.title("Translingua - Language Translator")

# Input text
text = st.text_area("Enter the text you want to translate:")

# Language selection
languages = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Chinese (Simplified)": "zh-cn",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "Urdu": "ur",
    "Malayalam": "ml",
    "Marati": "mr",
    "Nepali": "ne",
    "Bengali": "bn",
    "Chinese": "zh-cn",
    "dutch": "nl",
    "Greek": "el",
    "Gujarathi": "gu",
    "Italian": "it",
    "Indonesian": "id",
    "Kannada": "kn",
    "Korean": "ko",
    "Latin": "la",
    "Punjabi": "pa",
    "Thai": "th",
    "Turkish": "tr",
    "Persian": "fa",
}

target_language = st.selectbox("Select target language:", list(languages.keys()))

# Translate button
if st.button("Translate"):
    if text:
        try:
            # Perform translation
            translated = translator.translate(text, dest=languages[target_language])
            st.success("Translation:")
            st.write(translated.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to translate.")

# Run the app
if __name__ == "__main__":
    st.write("Welcome to Translingua! Enter text and select a language to translate.")
