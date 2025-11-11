import streamlit as st
from datetime import datetime

# ------------------ Page Configuration ------------------
st.set_page_config(page_title="Food Redistribution System", page_icon="🍱", layout="wide")

# ------------------ Sidebar Theme Toggle ------------------
st.sidebar.title("🎨 Theme Settings")
theme = st.sidebar.radio("Choose Theme:", ["🌞 Light Theme", "🌙 Dark Theme"])

# ------------------ Dynamic CSS based on Theme ------------------
if theme == "🌞 Light Theme":
    bg_color = "#f8fff9"
    text_color = "#0b6e4f"
    button_bg = "#0b6e4f"
    button_hover = "#10a56d"
    quote_color = "#2e8b57"
else:
    bg_color = "#1a1a1a"
    text_color = "#c9ffd7"
    button_bg = "#10a56d"
    button_hover = "#0b6e4f"
    quote_color = "#91ffb3"

# ------------------ Custom CSS ------------------
st.markdown(f"""
    <style>
    body {{
        background-color: {bg_color};
    }}
    .main-title {{
        color: {text_color};
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-top: 20px;
    }}
    .subtext {{
        color: {text_color};
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }}
    .stButton>button {{
        background-color: {button_bg};
        color: white;
        font-weight: 600;
        border-radius: 10px;
        padding: 10px 25px;
        border: none;
    }}
    .stButton>button:hover {{
        background-color: {button_hover};
        color: white;
    }}
    .quote {{
        font-style: italic;
        text-align: center;
        color: {quote_color};
        margin-top: 20px;
    }}
    </style>
""", unsafe_allow_html=True)

# ------------------ Main Header ------------------
st.markdown('<h1 class="main-title">🍽️ Food Redistribution System</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Reducing food waste and feeding the hungry — together we make a difference!</p>', unsafe_allow_html=True)

# ------------------ Hero Image ------------------
st.image(
    "https://img.freepik.com/free-photo/top-view-food-donation-box_23-2148733850.jpg",
    caption="Together, we can end hunger one meal at a time.",
    use_container_width=True
)

st.markdown('<p class="quote">"Don’t waste food — feed someone in need."</p>', unsafe_allow_html=True)

# ------------------ Sidebar Navigation ------------------
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🍴 Donate Food", "🎯 View Donations", "📦 Recipient Request", "👩‍💼 Admin Dashboard"])

# ------------------ Global Data Storage (Temporary) ------------------
if 'donations' not in st.session_state:
    st.session_state['donations'] = []

# ------------------ Home Page ------------------
if page == "🏠 Home":
    st.header("Welcome to Food Redistribution Platform 🌱")
    st.write("""
    This platform helps connect **donors** who have extra food with **recipients** who need it.
    Together, we can reduce food wastage and fight hunger.
    """)

    st.image(
        "https://cdn.pixabay.com/photo/2017/05/07/08/56/volunteers-2294361_1280.jpg",
        use_container_width=True
    )
    st.markdown('<p class="quote">"Sharing food is sharing love."</p>', unsafe_allow_html=True)

# ------------------ Donate Food ------------------
elif page == "🍴 Donate Food":
    st.header("🍛 Donate Surplus Food")

    donor_name = st.text_input("Your Name / Organization")
    food_type = st.selectbox("Food Type", ["Vegetarian", "Non-Vegetarian", "Both"])
    quantity = st.text_input("Food Quantity (e.g., 10 plates, 5kg rice)")
    location = st.text_input("Pickup Location")
    contact = st.text_input("Contact Number")
    expiry = st.date_input("Food Expiry / Safe Until Date", datetime.now())

    if st.button("Submit Donation"):
        if donor_name and food_type and quantity and location and contact:
            new_donation = {
                "Donor": donor_name,
                "Type": food_type,
                "Quantity": quantity,
                "Location": location,
                "Contact": contact,
                "Expiry": str(expiry)
            }
            st.session_state['donations'].append(new_donation)
            st.success("✅ Thank you for your generous donation! Your food has been added to the list.")
        else:
            st.error("⚠️ Please fill out all fields before submitting.")

# ------------------ View Donations ------------------
elif page == "🎯 View Donations":
    st.header("📋 Available Food Donations")

    if len(st.session_state['donations']) == 0:
        st.info("No donations available yet. Please check back later.")
    else:
        for i, donation in enumerate(st.session_state['donations']):
            with st.expander(f"🍱 Donation #{i+1} — {donation['Donor']}"):
                st.write(f"**Type:** {donation['Type']}")
                st.write(f"**Quantity:** {donation['Quantity']}")
                st.write(f"**Location:** {donation['Location']}")
                st.write(f"**Contact:** {donation['Contact']}")
                st.write(f"**Expiry:** {donation['Expiry']}")

# ------------------ Recipient Request ------------------
elif page == "📦 Recipient Request":
    st.header("🤝 Recipient Food Request")

    recipient_name = st.text_input("Recipient Name / Organization")
    need = st.text_area("Describe your food requirement")
    phone = st.text_input("Contact Number")

    if st.button("Send Request"):
        if recipient_name and need and phone:
            st.success(f"✅ Request submitted successfully by {recipient_name}! We’ll connect you with nearby donors soon.")
        else:
            st.error("⚠️ Please complete all fields.")

# ------------------ Admin Dashboard ------------------
elif page == "👩‍💼 Admin Dashboard":
    st.header("📊 Admin Dashboard")
    st.write("Monitor all food donations and requests in one place.")

    total_donations = len(st.session_state['donations'])
    st.metric("Total Donations", total_donations)

    if total_donations > 0:
        st.write("### 🧾 Donation Records:")
        for i, donation in enumerate(st.session_state['donations']):
            st.write(f"{i+1}. **{donation['Donor']}** donated {donation['Quantity']} ({donation['Type']}) from {donation['Location']} 📞 {donation['Contact']}")

    st.markdown('<p class="quote">"Together, we can end hunger one meal at a time."</p>', unsafe_allow_html=True)
