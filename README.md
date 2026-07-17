# Customer Support AI 🤖

An AI-powered customer support system built with **FastAPI**, **React (Vite)**, **MongoDB**, **Gemini AI**, and **Retrieval-Augmented Generation (RAG)**.

---

# Features

* AI-powered customer support chatbot
* Multi-Agent Architecture
* Retrieval-Augmented Generation (RAG)
* Gemini AI integration
* FAISS Vector Database
* HuggingFace Embeddings
* MongoDB Database
* FastAPI Backend
* React + Vite Frontend
* PDF Knowledge Base
* Swagger API Documentation
* Chat History Storage
* Complaint Management
* Product Management
* Feedback Management

---

# Tech Stack

## Frontend

* React
* Vite
* Axios
* React Router

## Backend

* FastAPI
* Uvicorn
* Python

## AI & RAG

* Google Gemini
* LangChain
* HuggingFace Embeddings
* FAISS
* Sentence Transformers

## Database

* MongoDB

---

# Project Structure

```text
customer-support-ai/
│
├── backend/
│   ├── agents/
│   ├── api/
│   ├── database/
│   ├── datasets/
│   ├── knowledge_base/
│   ├── llm/
│   ├── rag/
│   ├── vectorstore/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── components/
│   ├── hooks/
│   ├── pages/
│   ├── services/
│   ├── styles/
│   └── package.json
│
└── README.md
```

---

# Backend Setup

## 1. Clone Repository

```bash
git clone https://github.com/sikotariyasanjana-ui/customer-support-ai

cd customer-support-ai
```

---

## 2. Create Virtual Environment

Windows

```bash
cd backend

python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment

Create a file named

```
.env
```

Example

MONGODB_URI=mongodb://localhost:27017

DATABASE_NAME=customer_support_ai
```

---

## 5. Start MongoDB

Ensure MongoDB is running locally.

Default URI

```
mongodb://localhost:27017
```

---

## 6. Build the Vector Database

```bash
python build_vectorstore.py
```

Expected output

```
Loading PDF documents...
Created text chunks...
Embedding documents...
Saving FAISS index...
Vector Store Created Successfully
```

---

## 7. Run Backend

```bash
uvicorn main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

Open another terminal

```bash
cd frontend
```

Install packages

```bash
npm install
```

Run

```bash
npm run dev
```

Frontend URL

```
http://localhost:5173
```

---

# Knowledge Base

Store PDF documents inside

```
backend/knowledge_base/
```

Example

* faq.pdf
* refund_policy.pdf
* shipping_policy.pdf
* warranty.pdf
* user_manual.pdf
* Products.pdf
* Pricing.pdf
* InstallationGuide.pdf

---

# Dataset

CSV files

```
backend/datasets/
```

Example

* products.csv
* users.csv
* orders.csv
* complaints.csv
* faq.csv

---

# RAG Workflow

```
PDF Documents
      │
      ▼
Document Loader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
      │
      ▼
FAISS Vector Store
      │
      ▼
Retriever
      │
      ▼
Gemini AI
      │
      ▼
Generated Answer
```

---

# API Endpoints

| Method | Endpoint           | Description      |
| ------ | ------------------ | ---------------- |
| GET    | /                  | Backend Status   |
| GET    | /docs              | Swagger UI       |
| GET    | /api/health        | Health Check     |
| POST   | /api/chat          | Chat with AI     |
| POST   | /api/auth/register | Register User    |
| POST   | /api/auth/login    | User Login       |
| POST   | /api/products/add  | Add Product      |
| GET    | /api/products      | List Products    |
| POST   | /api/complaints    | Create Complaint |
| GET    | /api/complaints    | List Complaints  |
| POST   | /api/feedback      | Submit Feedback  |

---

# Future Improvements

* JWT Authentication
* Role-Based Access Control
* Admin Dashboard
* Order Tracking Agent
* Voice Assistant
* Image Upload Support
* Docker Deployment
* Kubernetes Deployment
* CI/CD Pipeline

---

# Author

Sanjana Sikotariya

AI/ML Project

Customer Support AI using FastAPI, MongoDB, Gemini AI, and RAG.
