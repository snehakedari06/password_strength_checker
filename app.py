import streamlit as st
import re
from nltk.corpus import words
import nltk
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


st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")
st.title("🔒 Password Strength Checker")
st.markdown("""
### Instructions:
- Enter a password in the input field below.
- Click the "Check Strength" button.
- The app will evaluate your password's strength and provide suggestions to improve it.
""")

password = st.text_input("Enter your password:", type="password")
if st.button("Check Strength"):
    if not password:
        st.error("Please enter a password to check!")
    else:
        strength, feedback = check_password_strength(password)
        st.write(f"### Strength: {strength}/4")

        
        st.progress(strength / 4)

        if feedback:
            st.markdown("### Suggestions to Improve:")
            for tip in feedback:
                st.write(f"- ⚠️ {tip}")
        else:
            st.success("🎉 Your password is strong!")
st.sidebar.markdown("### Try These Examples:")
st.sidebar.button("Example 1: `Pass123!`")
st.sidebar.button("Example 2: `weakpassword`")
st.sidebar.button("Example 3: `Strong!Pass2023`")
