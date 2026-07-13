import os
import threading
import requests
import streamlit as st
from supabase import create_client

# --- 1. INITIALIZE DATABASE & EMAIL ENGINE INITIALS ---
SUPABASE_URL = "https://hsswbfymhvertfhdgueg.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhzc3diZnltaHZlcnRmaGRndWVnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc4MjIwODg4OSwiZXhwIjoyMDk3Nzg0ODg5fQ.61Y4kuYAk_LWa4d5_LYSZl8Wx4C_NnP3iMOyZjMg7vE"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

EMAILJS_SERVICE_ID = "service_hzctvxf"
EMAILJS_TEMPLATE_ID = "template_c5fgogi"
EMAILJS_PUBLIC_KEY = "qZRu7AJ6k_hMVbZlq"

LOGO_URL = "https://hsswbfymhvertfhdgueg.supabase.co/storage/v1/object/sign/Eduvic/Eduvic.jpeg?token=eyJraWQiOiJzdG9yYWdlLXVybC1zaWduaW5nLWtleV85ODEzNDhlNS05NjMyLTRjMjMtOTEzNi1kZWNlODAyYzEwY2QiLCJhbGciOiJIUzI1NiJ9.eyJ1cmwiOiJFZHV2aWMvRWR1dmljLmpwZWciLCJzY29wZSI6ImRvd25sb2FkIiwiaWF0IjoxNzgzOTQ2NjI1LCJleHAiOjE4MTU0ODI2MjV9.IwDW2MuRdgwxqgx4hiWrDm-WdkdIlk_CE-3L8oVU1AE"


# --- 2. ASYNCHRONOUS EMAIL SENDER HELPER ---
def send_async_email(recipient, name, date, time):
    url = "https://api.emailjs.com/api/v1.0/email/send"
    payload = {
        "service_id": EMAILJS_SERVICE_ID,
        "template_id": EMAILJS_TEMPLATE_ID,
        "user_id": EMAILJS_PUBLIC_KEY,
        "template_params": {
            "user_email": recipient,
            "name": name,
            "date": date,
            "time": time
        }
    }
    try:
        response = requests.post(url, json=payload)
        print(f"DEBUG: Web Portal EmailJS Status: {response.status_code}")
    except Exception as e:
        print(f"Web Portal Email Thread Exception Error: {e}")


# --- 3. STREAMLIT PAGE & WELCOME STATE CONTROL ---
st.set_page_config(page_title="Eduvic Travels - Booking Portal", page_icon="🌟", layout="wide")

if "modal_cleared" not in st.session_state:
    st.session_state.modal_cleared = False

# --- 4. CORPORATE MINIMALIST CSS INJECTION ---
custom_css = """
<style>
    /* REMOVE ALL DEFAULT STREAMLIT CHROMIUM WRAPPERS */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display: none;}

    /* Deep Corporate Backdrop Zone */
    .stApp {
        background-color: #0A192F !important;
    }

    /* Stretched Minimalist White Card Block with Sharp Structural Edges */
    .block-container {
        max-width: 850px !important;
        background-color: #FFFFFF !important;
        padding: 4rem 4.5rem !important;
        border-radius: 4px !important; 
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4) !important;
        margin: auto !important;
        margin-top: 5rem !important;
        margin-bottom: 5rem !important;
        border-top: 6px solid #FF6600 !important; 

        /* Smooth fade-in transition when portal loads */
        animation: fadeIn 0.6s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Style Corporate Input Fields to be Sharp and Clean */
    input, select, div[data-baseweb="select"] {
        border-radius: 2px !important;
        border: 1px solid #CCD6F6 !important;
    }

    /* Text Layer Font Hierarchy Rules */
    h1 {
        color: #0A2540 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px !important;
    }

    h3, label, .stWidgetLabel p {
        color: #0A2540 !important;
        font-weight: 600 !important;
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
    }

    /* Precision Cut Sharp Corporate Call-to-Action Button */
    div.stButton > button:first-child {
        background-color: #FF6600 !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 0.75rem 2rem !important;
        border-radius: 4px !important; 
        transition: background-color 0.2s ease, transform 0.1s ease !important;
    }

    div.stButton > button:first-child:hover {
        background-color: #E65C00 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- 5. INTERACTIVE WELCOME MODAL OVERLAY ---
if not st.session_state.modal_cleared:
    @st.dialog("WELCOME TO EDUVIC TRAVELS", width="large")
    def show_welcome_modal():
        col_m_logo, _ = st.columns([1, 3])
        with col_m_logo:
            st.image(LOGO_URL, width=130)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(
            "<h2 style='color:#0A2540; text-align:left; font-weight:700; margin-top:0;'>Travel From Within to Beyond Borders</h2>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='color:#555555; font-size:1.1rem;'>Access our live scheduling engine to seamlessly book your expert travel consultation session.</p>",
            unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("PROCEED TO PORTAL", use_container_width=True):
            st.session_state.modal_cleared = True
            st.rerun()


    show_welcome_modal()
    st.stop()

# --- 6. CORE PORTAL WEB INTERFACE (ACTIVE VIEWPORT) ---
col_logo, _ = st.columns([1, 4])
with col_logo:
    st.image(LOGO_URL, width=140)

st.title("Appointment Scheduling Portal")
st.markdown(
    "<p style='color:#666666; font-size:1.05rem; margin-top:-10px;'>Select an open calendar date and window below to complete secure consultation booking.</p>",
    unsafe_allow_html=True)
st.markdown("<hr style='border-top: 1px solid #EAEAEA; margin-bottom:2.5rem;'>", unsafe_allow_html=True)


# --- 7. FETCH AVAILABLE SLOTS FROM SUPABASE ---
@st.cache_data(ttl=5)
def fetch_available_slots():
    try:
        response = supabase.table("slot").select("id, appointment_date, appointment_time").eq("is_booked", 0).execute()
        return response.data if response.data else []
    except Exception as e:
        st.error(f"Error fetching database rows: {e}")
        return []


all_slots = fetch_available_slots()

if not all_slots:
    st.warning("⚠️ No slots are currently available for booking. Please contact our support team or check back later!")
else:
    # --- 8. MINIMALIST TWO-COLUMN TIMELINE UI ---
    unique_dates = sorted(list(set([slot["appointment_date"] for slot in all_slots])))

    col1, col2 = st.columns(2)

    with col1:
        selected_date = st.selectbox("📅 Step 1: Choose a Date", unique_dates)

    filtered_slots = [s for s in all_slots if s["appointment_date"] == selected_date]
    time_options = [s["appointment_time"] for s in filtered_slots]

    with col2:
        selected_time = st.selectbox("⏰ Step 2: Choose an Available Time", time_options)

    chosen_slot_id = next(s["id"] for s in filtered_slots if s["appointment_time"] == selected_time)

    st.markdown(
        "<br><h3 style='font-size:1.3rem; border-left: 4px solid #FF6600; padding-left:10px;'>Step 3: Enter Your Contact Details</h3>",
        unsafe_allow_html=True)

    # Added explicit value='' and exact key references
    client_name = st.text_input("Full Name", value="", key="client_name_input")
    client_email = st.text_input("Email Address", value="", key="client_email_input")
    client_phone = st.text_input("WhatsApp Phone Number (e.g., +234...)", value="", key="client_phone_input")

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 9. DATA SUBMISSION & DATABASE WRITING ---
    if st.button("Confirm Appointment", use_container_width=True, key="submit_booking_btn"):
        # Explicitly pull fresh strings out of the backend session state dictionary
        name_val = st.session_state.client_name_input.strip()
        email_val = st.session_state.client_email_input.strip()
        phone_val = st.session_state.client_phone_input.strip()

        if not name_val or not email_val or not phone_val:
            st.error("❌ Please complete all fields before clicking submit.")
        elif "@" not in email_val or "." not in email_val:
            st.error("❌ Please provide a structurally valid email address.")
        else:
            with st.spinner("Processing booking request..."):
                try:
                    supabase.table("bookings").insert({
                        "client_name": name_val,
                        "client_email": email_val,
                        "appointment_date": selected_date,
                        "appointment_time": selected_time,
                        "whatsapp_number": phone_val
                    }).execute()

                    supabase.table("slot").update({"is_booked": 1}).eq("id", chosen_slot_id).execute()

                    # Fire Email Thread
                    threading.Thread(
                        target=send_async_email,
                        args=(email_val, name_val, selected_date, selected_time)
                    ).start()

                    st.success(
                        f"🎉 Success! Your appointment on {selected_date} at {selected_time} is locked in. A confirmation email has been dispatched.")
                    st.balloons()
                    st.cache_data.clear()

                except Exception as e:
                    st.error(f"Database sync operation rejected: {e}")