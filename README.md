# 🚀 Enterprise Agentic AI RAG Platform

A production-style **Agentic AI system** combining:
- RAG (Retrieval-Augmented Generation)
- SQL analytics agent
- Conversational memory
- Validation & governance layer
- MLflow observability

This project demonstrates **enterprise-grade GenAI architecture** with modular multi-agent design.

---

## 🧠 Key Capabilities

### 🔹 Agentic AI System
- Planner-based routing (retrieval vs SQL)
- Multi-agent orchestration
- Modular agent architecture

### 🔹 RAG Pipeline
- Document ingestion
- Vector embeddings
- Semantic retrieval for context-aware answers

### 🔹 SQL Analytics Agent
- Natural language query execution
- Data-driven insights from structured datasets

### 🔹 Memory System
- Maintains conversation history
- Enables contextual responses

### 🔹 Validation Layer
- Response validation
- Risk and safety checks

### 🔹 MLflow Tracking
- Logs queries, responses, and routes
- Tracks experiment metadata
- Enables observability for AI workflows

---

## 🏗️ Architecture Flow

```text
User Query
    ↓
Planner Agent
    ↓
-------------------------
| Retrieval Agent (RAG) |
| SQL Agent             |
-------------------------
    ↓
Validation Agent
    ↓
Memory Store
    ↓
MLflow Tracking
    ↓
Final Response