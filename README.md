# ✈️ Eduvic Booking System

> A secure, full-stack appointment scheduling and reservation management portal built for modern travel consultancy workflows.

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?style=flat&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL-green?style=flat&logo=supabase&logoColor=white)](https://supabase.com/)
[![Render](https://img.shields.io/badge/Hosted-Render-purple?style=flat&logo=render&logoColor=white)](https://render.com/)

---

## 📋 Overview

**Eduvic Booking System** is a standalone, web-based appointment portal designed to streamline client intake and reservation management for **Eduvic Global International Educational Services Ltd.** 

Instead of manual scheduling, this platform provides a dedicated web interface where clients can seamlessly submit travel consultancy details, while securely logging and centralizing appointment tracking in a relational cloud database.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask (Micro-web framework)
* **Database & Auth:** Supabase (PostgreSQL relational database)
* **Frontend:** HTML5, CSS3, Responsive UI Layouts
* **Deployment & Hosting:** Render Platform

---

## 🚀 Key Features

* **Automated Client Intake:** Clean web interface enabling users to submit consultation requests and preferred appointment schedules.
* **Relational Database Backend:** Fully integrated with Supabase PostgreSQL to securely store, track, and manage client data and reservation states in real time.
* **Session & State Management:** Handles user requests smoothly with structured error handling and fast routing.
* **Cloud Native Deployment:** Continuously hosted and optimized for high uptime on the Render platform.

---

## 📂 Project Architecture

```text
eduvic-booking-system/
│
├── static/              # CSS stylesheets, images, and static assets
├── templates/           # HTML frontend views / booking forms
├── app.py               # Main Flask application routes and logic
├── database.py          # Supabase PostgreSQL connection & query handlers
├── requirements.txt     # Python project dependencies
└── README.md            # Project documentation
