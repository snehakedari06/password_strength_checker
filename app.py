import streamlit as st
import re
from nltk.corpus import words
import nltk

# Download NLTK word corpus
nltk.download('words')
word_list = set(words.words())

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")

    if any(word in password.lower() for word in word_list):
        feedback.append("Avoid using common dictionary words.")

    return strength, feedback

st.title("Password Strength Checker")

password = st.text_input("Enter your password:")
if st.button("Check Strength"):
    strength, feedback = check_password_strength(password)
    st.write(f"Strength: {strength}/4")
    st.write("\n".join(feedback))
