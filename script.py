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
SECOND_EMAILJS_TEMPLATE_ID = "template_slfpy9c"
SECOND_EMAILJS_SERVICE_ID = "service_us6etit"
SECOND_EMAILJS_PUBLIC_KEY = "GHxJqyiZqMz3TP7Y4"

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
        print(f"DEBUG: Web Portal EmailJS Status for {recipient}: {response.status_code}")
    except Exception as e:
        print(f"Web Portal Email Thread Exception Error for {recipient}: {e}")


def second_mail(recipient,name, date, time):
    url = "https://api.emailjs.com/api/v1.0/email/send"
    payload = {
        "service_id": SECOND_EMAILJS_SERVICE_ID,
        "template_id": SECOND_EMAILJS_TEMPLATE_ID,
        "user_id": SECOND_EMAILJS_PUBLIC_KEY,
        "template_params": {
            "recipient" email,
            "name": name,
            "date": date,
            "time": time
        }
    }
    try:
        response = requests.post(url, json=payload)
        print(f"DEBUG: Web Portal EmailJS Status for {recipient}: {response.status_code}")
    except Exception as e:
        print(f"Web Portal Email Thread Exception Error for {recipient}: {e}")





# --- Dual Notification Dispatcher ---
def dispatch_all_notifications(client_email, client_name, date, time, phone):
    send_async_email(client_email, client_name, date, time)
    admin_subject = f"🚨 NEW BOOKING: {client_name} ({phone})"
    second_mail("eduvicgloballtravels@gmail.com", admin_subject, date, time)


# --- 3. STREAMLIT PAGE & WELCOME STATE CONTROL ---
st.set_page_config(page_title="Eduvic Travels - Booking Portal", page_icon="🌟", layout="wide")

if "modal_cleared" not in st.session_state:
    st.session_state.modal_cleared = False


# --- 4. DYNAMIC NATIVE THEME CONFIGURATION (CSS Variables) ---
custom_css = """
<style>
    /* Define dynamic color variables based on system preference */
    :root {
        --bg-color: #F4F6F9;
        --card-bg: #FFFFFF;
        --text-color: #0A2540;
        --sub-text: #555555;
        --input-border: #CCD6F6;
        --input-focus: #FF6600;
        --hr-color: #EAEAEA;
        --footer-bg: #0A2540;
        --footer-text: #CCD6F6;
    }

    @media (prefers-color-scheme: dark) {
        :root {
            --bg-color: #0A192F;
            --card-bg: #172A45;
            --text-color: #F8F9FA;
            --sub-text: #8892B0;
            --input-border: #233554;
            --input-focus: #FF6600;
            --hr-color: #233554;
            --footer-bg: #0B1E36;
            --footer-text: #8892B0;
        }
    }

    /* REMOVE ALL DEFAULT STREAMLIT CHROMIUM WRAPPERS */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stAppDeployButton {display: none;}

    /* Dynamic Base Page Backdrop */
    .stApp {
        background-color: var(--bg-color) !important;
        transition: background-color 0.3s ease-in-out;
    }

    /* Sharp Structural Card Layout Block */
    .block-container {
        max-width: 850px !important;
        background-color: var(--card-bg) !important;
        padding: 4rem 4.5rem !important;
        border-radius: 4px !important; 
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.18) !important;
        margin: auto !important;
        margin-top: 5rem !important;
        margin-bottom: 5rem !important;
        border-top: 6px solid #FF6600 !important; 
        transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        animation: fadeIn 0.6s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* 📱 RESPONSIVE BREAKPOINTS FOR MOBILE SCREENS */
    @media (max-width: 768px) {
        .block-container {
            padding: 2rem 1.5rem !important;
            margin-top: 1.5rem !important;
            margin-bottom: 1.5rem !important;
        }
    }

    /* 🎯 HIGH SPECIFICITY TARGET FOR THE STREAMLIT DIALOG DIALOG OVERLAYS */
    div[data-testid="stModal"] div[role="dialog"] {
        background-color: var(--card-bg) !important;
        color: var(--text-color) !important;
        border: 1px solid var(--input-border) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
        transition: background-color 0.3s ease-in-out;
    }
    
    div[data-testid="stModal"] div[role="dialog"] h2, 
    div[data-testid="stModal"] div[role="dialog"] p, 
    div[data-testid="stModal"] div[role="dialog"] span,
    div[data-testid="stModal"] div[role="dialog"] div {
        color: var(--text-color) !important;
    }

    /* Sharpened & Responsive Input styling with Orange Focus highlights */
    input, select, div[data-baseweb="select"] {
        border-radius: 4px !important;
        border: 1px solid var(--input-border) !important;
        background-color: var(--card-bg) !important;
        color: var(--text-color) !important;
        transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out !important;
    }
    
    input:focus, select:focus {
        border-color: var(--input-focus) !important;
        box-shadow: 0 0 0 2px rgba(255, 102, 0, 0.15) !important;
    }

    /* Text Layer Font Hierarchy Rules */
    h1 {
        color: var(--text-color) !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.5px !important;
    }

    h2, h3, label, .stWidgetLabel p {
        color: var(--text-color) !important;
        font-weight: 600 !important;
        font-family: 'Helvetica Neue', Arial, sans-serif !important;
    }

    /* Dynamic divider styling */
    hr {
        border-top: 1px solid var(--hr-color) !important;
    }

    /* 🌟 UNIVERSAL STYLING FOR ALL MAIN ACTION BUTTONS (Signature Orange) */
    div.stButton button {
        background-color: #FF6600 !important;
        color: white !important;
        border: none !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        padding: 0.75rem 2rem !important;
        border-radius: 4px !important; 
        transition: background-color 0.2s cubic-bezier(0.4, 0, 0.2, 1), transform 0.1s ease !important;
        box-shadow: 0 4px 10px rgba(255, 102, 0, 0.2) !important;
    }

    div.stButton button:hover {
        background-color: #E65C00 !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 6px 14px rgba(255, 102, 0, 0.3) !important;
    }
    
    div.stButton button:active {
        transform: translateY(1px) !important;
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
            "<h2 style='text-align:left; font-weight:700; margin-top:0;'>Travel From Within to Beyond Borders</h2>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:1.1rem;'>Access our live scheduling engine to seamlessly book your expert travel consultation session.</p>",
            unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("PROCEED TO PORTAL", use_container_width=True, key="modal_proceed_btn"):
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
    "<p style='font-size:1.05rem; margin-top:-10px;'>Select an open calendar date and window below to complete secure consultation booking.</p>",
    unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)


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

    col_s1, col_s2 = st.columns(2)

    with col_s1:
        selected_date = st.selectbox("📅 Step 1: Choose a Date", unique_dates)

    filtered_slots = [s for s in all_slots if s["appointment_date"] == selected_date]
    time_options = [s["appointment_time"] for s in filtered_slots]

    with col_s2:
        selected_time = st.selectbox("⏰ Step 2: Choose an Available Time", time_options)

    chosen_slot_id = next(s["id"] for s in filtered_slots if s["appointment_time"] == selected_time)

    st.markdown(
        "<br><h3 style='font-size:1.3rem; border-left: 4px solid #FF6600; padding-left:10px;'>Step 3: Enter Your Contact Details</h3>",
        unsafe_allow_html=True)

    client_name = st.text_input("Full Name", value="", key="client_name_input")
    client_email = st.text_input("Email Address", value="", key="client_email_input")
    client_phone = st.text_input("WhatsApp Phone Number (e.g., +234...)", value="", key="client_phone_input")

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 9. DATA SUBMISSION & DATABASE WRITING ---
    if st.button("Confirm Appointment", use_container_width=True, key="submit_booking_btn"):
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

                    # Fire Concurrent Background Email Thread (To Client & workdoxa@gmail.com)
                    threading.Thread(
                        target=dispatch_all_notifications,
                        args=(email_val, name_val, selected_date, selected_time, phone_val)
                    ).start()

                    st.success(
                        f"🎉 Success! Your appointment on {selected_date} at {selected_time} is locked in. A confirmation email has been dispatched.")
                    st.balloons()
                    st.cache_data.clear()

                except Exception as e:
                    st.error(f"Database sync operation rejected: {e}")

# --- 10. PROFESSIONAL CORPORATE FOOTER WITH INQUIRIES NUMBER & SLEEK DARK BG ---
st.markdown("<br><hr>", unsafe_allow_html=True)
st.markdown(
    """
    <div class="booking-footer" style="background-color: var(--footer-bg); text-align: center; padding: 25px 20px; border-radius: 6px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: background-color 0.3s ease;">
        <p style="margin: 0 0 10px 0; font-size: 0.95rem; color: var(--footer-text); font-weight: 500;">
            For further inquiries, please contact us at <a href="tel:08126669153" style="color: #FF6600; text-decoration: none; font-weight: bold;">08126669153</a>
        </p>
        <p style="margin: 0; font-size: 0.9rem; color: var(--footer-text); font-weight: 500; opacity: 0.95;">
            © 2026 <strong>Eduvic Travels</strong>. All rights reserved.
        </p>
        <p style="margin: 10px 0 0 0; font-size: 0.8rem; color: #FF6600; font-weight: bold; letter-spacing: 0.5px;">
            TRAVEL FROM WITHIN TO BEYOND BORDERS
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
