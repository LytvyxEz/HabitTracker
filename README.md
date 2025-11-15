                   ┌─────────────────────┐
                   │   FastAPI Monolith  │
                   │   (Habits + Auth)   │
                   └───────┬─────────────┘
                           │ publishes events
                           ▼
                   ┌─────────────────────┐
                   │      RabbitMQ       │
                   │  (event bus)        │
                   └───────┬─────────────┘
                           │ consumes events
                           ▼
           ┌─────────────────────────────────────┐
           │      Notification Microservice      │
           │   - RabbitMQ consumer               │
           │   - Telegram Bot (aiogram)          │
           │   - Retry + logs + filters          │
           └─────────────────────────────────────┘


/project
│
├── monolith/                          
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/
│   │   │   ├── habits/
│   │   │   ├── analytics/
│   │   │   └── health/
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── jwt.py
│   │   ├── db/
│   │   │   ├── session.py
│   │   │   ├── models.py
│   │   │   ├── dao/
│   │   │   └── migrations/
│   │   ├── services/
│   │   │   ├── habit_service.py
│   │   │   ├── analytics_service.py
│   │   │   └── notification_publisher.py  # Нове!
│   │   ├── tasks/
│   │   │   ├── reminders.py
│   │   │   ├── daily_stats.py
│   │   │   └── celery_app.py
│   │   └── main.py
│   │
│   └── docker/
│       ├── Dockerfile
│       ├── celery.Dockerfile
│       └── nginx.conf
│
├── notification_service/   
│   ├── bot/
│   │   ├── handlers/
│   │   ├── router.py
│   │   └── bot.py
│   ├── consumer/
│   │   ├── worker.py
│   │   └── rabbit.py
│   ├── services/
│   │   ├── telegram_notifier.py
│   │   ├── templates.py
│   │   └── filters.py
│   ├── db/
│   │   └── redis.py
│   ├── main.py
│   └── Dockerfile
│
└── docker-compose.yml

