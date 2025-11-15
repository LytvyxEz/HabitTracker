# 🌟 Habit Tracker 3.0 — Microservice Edition

A **production-grade habit tracking system** built with a modern Python backend stack.
This project demonstrates **clean architecture, microservices, event‑driven communication, background processing, caching, and real‑world integrations**.


---

## 🚀 Features

### ✅ **FastAPI Monolith (Core API)**

* JWT Authentication (access & refresh tokens)
* Habit CRUD
* Habit check-ins with daily/weekly/monthly frequency
* Streaks and progress calculations
* Analytics service (summary, progress, recommendations)
* Redis caching
* Celery worker for background jobs
* Celery beat for reminders & daily analytics
* SQLAlchemy ORM + PostgreSQL
* DAO + Service Layer architecture
* Publish habit events to RabbitMQ

---

### 📨 **Notification Microservice**

* RabbitMQ consumer (async)
* Telegram Bot notifications (aiogram)
* Message templates & formatting
* Retry logic
* Redis for rate-limiting and chat session mapping
* Event-driven design:

  * `notifications.habit.reminder`
  * `notifications.habit.check`
  * `notifications.analytics.ready`

---

## 🧩 Architecture Overview

```
                ┌──────────────────────────┐
                │ FastAPI Monolith (API)   │
                │  - Habits                │
                │  - Auth                  │
                │  - Analytics             │
                └─────────┬────────────────┘
                          │  publish events
                          ▼
                ┌──────────────────────────┐
                │        RabbitMQ          │
                │      (Event Bus)         │
                └─────────┬────────────────┘
                          │ consume events
                          ▼
        ┌──────────────────────────────────────────┐
        │      Notification Microservice           │
        │  - Telegram bot                          │
        │  - Consumer                              │
        │  - Templates / Retry                     │
        └──────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
/project
│
├── monolith/                      # FastAPI + Celery + PostgreSQL + Redis
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/
│   │   │   ├── habits/
│   │   │   ├── analytics/
│   │   │   └── health/
│   │   ├── core/
│   │   ├── db/
│   │   ├── services/
│   │   ├── tasks/
│   │   └── main.py
│   └── Dockerfile
│
├── notification_service/
│   ├── bot/
│   ├── consumer/
│   ├── services/
│   ├── db/
│   └── Dockerfile
│
└── docker-compose.yml
```

---

## ⚙️ Technologies Used

### **Backend Core**

* Python 3.12+
* FastAPI
* PostgreSQL
* SQLAlchemy
* Alembic
* Redis
* Celery
* RabbitMQ

### **Microservice & Integrations**

* aiogram (Telegram Bot API)
* aio-pika (RabbitMQ consumer)
* Pydantic
* Docker & docker-compose

### **Architecture**

* Domain‑Driven Structure (DAO + Services)
* Event‑Driven Communication
* Microservice + Monolith Hybrid

---

## 🔐 Authentication

* Access Token (15 min lifetime)
* Refresh Token (stored in Redis)
* Token rotation logic
* Secure password hashing (bcrypt)

---

## 📦 Running the Project

### 1️⃣ Clone the repo:

```bash
git clone https://github.com/your-username/habit-tracker.git
cd habit-tracker
```

### 2️⃣ Start all services:

```bash
docker compose up --build
```

Services included:

* monolith (FastAPI)
* celery worker
* celery beat
* notification-service
* rabbitmq
* redis
* postgres

---

## 🧪 API Documentation

Once running:

* Swagger UI → `http://localhost:8000/docs`
* ReDoc → `http://localhost:8000/redoc`

---

## 🧠 Core Features in Detail

### ⭐ Habit Logic

* Daily/weekly/monthly repetition
* Custom reminder times
* Check-in validation
* Progress percentages
* Streak auto-calculation

### ⭐ Analytics Engine

Celery calculates:

* streak updates
* weekly reports
* actionable habit recommendations

### ⭐ Notification Flow

1. Monolith publishes habit/analytics event → RabbitMQ
2. Notification Microservice consumes it
3. Sends Telegram message instantly

---

## 📬 Telegram Bot Example

Screenshot examples:

```
🔥 Habit reminder: "Drink water"
You haven't completed it today — let's go!
```

```
💡 Daily Report Ready!
• 3 habits completed
• Streak: 4 days
• Recommendation: Try increasing your daily target!
```

---
