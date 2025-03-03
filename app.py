import streamlit as st

st.set_page_config(page_title= "Growth Mindset Challenge" , page_icon ="★")
st.title("🌱Growth Mindset AI Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Journey!")
st.write("Face challenges, learn from mistakes, and unlock your true potential! This AI-powered app helps you cultivate a growth mindset through self-reflection, exciting challenges, and rewarding achievements🌟")

st.header("💡 Today's Growth Mindset Quote")
st.write("Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful .– Albert Schweitzer")

st.header("🧠 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")


if user_input:
    st.success(f"⚡ You're facing: {user_input}. Keep pushing forwards to your goal! 💡")
else:
    st.warning("Tell us about your challenge to get started!")

    #Reflexing

st.header("💭 Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow! Share your difficulties. 💪")

    #Achievements

st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎉 Amazing! You achieved: {achievement}")
else:
    st.info("Big or small , every achievement counts! Share one now 😊")


    #Footer

    st.write("- - -")
    st.write("Believe in your journey—every challenge shapes your growth. ✨🌿")
    st.write(" **©️ Created By Haram Adnan**")
