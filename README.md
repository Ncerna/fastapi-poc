#  FastAPI + Django ORM + PostgreSQL (Clean Architecture + Vertical Slicing)

##  Descripción

Este proyecto es una arquitectura backend híbrida que combina:

- ⚡ FastAPI (capa de presentación)
- 🐍 Django ORM (capa de infraestructura)
- 🐘 PostgreSQL (base de datos)
- 🧱 Clean Architecture
- 📦 Arquitectura vertical por módulo (User / Product)

El objetivo es construir un sistema escalable, desacoplado y mantenible.

---
##  Arquitectura

```text
fastapi-poc/
│
├── domain/
│   └── entities/
│   │   ├── user.py
│   │   ├── product.py
│   │
│   └── value_objects/
│       ├── price.py
│       ├── stock.py
│
├── application/
│   ├── interfaces/
│   │   ├── user_repository.py
│   │   ├── user_service.py
│   │
│   ├── contracts/
│   │   ├── user_service_interface.py
│   │   ├── product_service_interface.py
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── product_service.py
│   │
│   ├── dto/
│   │   ├── user/
│   │   ├── product/
│   │
│   ├── errors/
│   │
│   ├── mappers/
│   │
│   └── shared/
│
├── infrastructure/
│   └── django_infra/
│       ├── models/
│       │   ├── user_model.py
│       │   ├── product_model.py
│       │
│       ├── repositories/
│       │   ├── user_repository.py
│       │   ├── product_repository.py
│       │
│       └── exceptions/
│
├── presentation/
│   ├── controllers/
│   │   ├── user_controller.py
│   │   ├── product_controller.py
│   │
│   └── module.py
│
└── main.py
```

## 🔁 Flujo de arquitectura


Controller (FastAPI)
↓
Service (Application)
↓
Repository Interface
↓
Repository Implementation (Django ORM)
↓
PostgreSQL


---

## 🧠 Principios aplicados

- ✔ Clean Architecture
- ✔ Dependency Inversion Principle (DIP)
- ✔ Vertical Slicing (por feature)
- ✔ Separation of Concerns

---

## 📦 Domain Layer

Entidades puras sin dependencias externas.

```python
class User:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
