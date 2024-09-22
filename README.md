# 📝 To-Do List Application with Flask, GraphQL, Keycloak & Stripe 🌟

Welcome to the **To-Do List** project! This web application allows users to manage tasks with a beautiful and intuitive interface. Powered by **Flask** for the backend and **GraphQL** for efficient data management, this app incorporates **Keycloak** for robust user authentication and **Stripe** for handling payments to unlock premium features.

## 🔑 Key Features

### ✅ Core Features
- **User Authentication**: Secure login via **Keycloak**, ensuring all to-do actions are authenticated.
- **To-Do Management**: Create, view, edit, and delete your to-do items, each with a title, description, and scheduled time.
- **GraphQL API**: Use GraphQL for smooth and flexible queries and mutations, providing only the data you need.

### 🌟 Premium Features (Pro License)
- **Image Upload**: Users with a **Pro license** can upload images to their to-do items.
- **Stripe Integration**: Seamless payment integration using **Stripe** (test mode) to upgrade users to Pro.

---

## 🚀 Project Overview

This project consists of two main components:

### Backend (Flask + GraphQL)
The backend is powered by **Flask**, with **GraphQL** providing the API for data manipulation. It also integrates **Keycloak** for authentication and **Stripe** for handling payments. SQLAlchemy is used for managing the database, and **Flask-Migrate** handles migrations.

### Frontend (React)
The frontend is a **React** application that allows users to interact with the backend via the GraphQL API. Users can log in, manage their to-do items, and upgrade to a Pro account.

---

## 🛠️ Tech Stack

- **Backend**: Flask, GraphQL, SQLAlchemy, Keycloak, Stripe
- **Frontend**: React
- **Authentication**: Keycloak (JWT-based)
- **Payments**: Stripe (test mode)
- **Database**: SQLite (default), PostgreSQL/MySQL (optional)

---

## 🏗️ Setup Instructions

### Prerequisites

1. **Python 3.7+** installed
2. **Node.js** and **npm** for the React frontend
3. **Keycloak** for authentication (setup guide below)
4. **Stripe account** for payment integration

### 1. Clone the Repository

```bash
git clone https://github.com/Aniketpagare1/To-do-flask.git
cd To-do-flask
