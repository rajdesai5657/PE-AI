import streamlit as st
import random

# --- Page Config ---
st.set_page_config(page_title="Travel Destination Expert System", page_icon="✈️", layout="centered")

# --- Custom Styling ---
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f6d365 0%, #fda085 100%);
    color: #000000;
}
h1, h2, h3 {
    text-align: center;
    color: #003366;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 10em;
    border: none;
    font-size: 16px;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# --- Title Section ---
st.title("✈️ Travel Destination Expert System")
st.markdown("<h4 style='text-align:center;'>Find your perfect travel destination based on your preferences 🌴</h4>", unsafe_allow_html=True)
st.write("---")

# --- User Inputs ---
st.subheader("🧭 Tell us about your travel preferences")

budget = st.selectbox("💰 What is your budget level?", ["Low", "Medium", "High"])
climate = st.selectbox("☀️ Preferred climate?", ["Cold", "Moderate", "Hot"])
activity = st.selectbox("🎢 What type of activities do you enjoy?", 
                        ["Adventure", "Relaxation", "Cultural", "Nature", "Party"])
travel_type = st.selectbox("🧳 Who are you traveling with?", 
                           ["Solo", "Friends", "Family", "Partner"])
duration = st.slider("📅 Trip duration (in days)", 2, 20, 7)

# --- Rule-based Recommendation Logic ---
destinations = []

# Budget and Climate Based
if budget == "Low":
    if climate == "Cold":
        destinations += ["Shimla, India", "Kathmandu, Nepal"]
    elif climate == "Moderate":
        destinations += ["Goa, India", "Bali, Indonesia"]
    else:
        destinations += ["Bangkok, Thailand", "Dubai, UAE"]

elif budget == "Medium":
    if climate == "Cold":
        destinations += ["Switzerland", "Kashmir, India"]
    elif climate == "Moderate":
        destinations += ["Singapore", "Malaysia"]
    else:
        destinations += ["Greece", "Morocco"]

else:  # High budget
    if climate == "Cold":
        destinations += ["Finland", "Canada"]
    elif climate == "Moderate":
        destinations += ["Japan", "Italy"]
    else:
        destinations += ["Maldives", "Hawaii"]

# Activity Filters
if activity == "Adventure":
    destinations += ["New Zealand", "Rishikesh, India", "Costa Rica"]
elif activity == "Relaxation":
    destinations += ["Bali, Indonesia", "Maldives", "Goa, India"]
elif activity == "Cultural":
    destinations += ["Rome, Italy", "Kyoto, Japan", "Varanasi, India"]
elif activity == "Nature":
    destinations += ["Kerala, India", "Switzerland", "Norway"]
elif activity == "Party":
    destinations += ["Ibiza, Spain", "Las Vegas, USA", "Goa, India"]

# --- Recommendation Result ---
if st.button("🌎 Get My Travel Recommendation"):
    suggestion = random.choice(destinations)
    st.write("---")
    st.markdown(f"<h3 style='text-align:center;'>🏖️ Your Ideal Destination is:</h3>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align:center; color:#2b9348;'>{suggestion}</h2>", unsafe_allow_html=True)
    
    # --- Custom Advice Section ---
    st.markdown("### ✨ Travel Tips")
    st.markdown("""
    - Always pack according to weather forecasts.  
    - Try local food and respect local traditions.  
    - Keep your important documents safe.  
    - Travel light and carry reusable items.  
    - Capture memories, not just photos 📸.
    """)
    
    # --- Fun Message ---
    st.success("Have a safe and joyful trip! 🌏💼")

# --- Footer ---
st.write("---")
st.caption("Thank you 🌸 | Travel Destination Expert System | 2025")
