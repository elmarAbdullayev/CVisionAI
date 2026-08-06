# CVisionAI - AI-Powered CV Analysis Platform

CVisionAI is a full-stack AI application that analyzes resumes (CVs) based on a given job description. It uses Large Language Models (LLMs) to evaluate candidate compatibility, identify strengths and missing skills, suggest improvements, and generate a personalized cover letter.

The goal of this project is to help job seekers understand how well their experience matches a position and improve their applications.

---

## 🚀 Features

### CV Analysis

* Upload a CV in PDF format
* Extract text automatically from the document
* Analyze the CV against a job description using AI

### AI-Powered Evaluation

The system provides:

* Match score percentage
* Detected skills
* Missing skills
* Improvement suggestions
* Personalized cover letter generation

### Full-Stack Architecture

* Modern React frontend
* FastAPI backend
* LLM integration
* PDF text extraction
* Structured API responses

---

## 🏗️ Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Axios
* CSS

### Backend

* Python
* FastAPI
* Pydantic
* PyPDF2
* Groq LLM API

### AI

* Large Language Model integration
* Prompt-based CV evaluation
* Structured JSON responses

---

## 📂 Project Structure

```
CVisionAI
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── models
│   │   ├── services
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   ├── src
│   │   ├── components
│   │   ├── services
│   │   ├── types
│   │   └── css
│   │
│   ├── package.json
│   └── vite.config.ts
│
└── README.md
```

---

# ⚙️ Installation & Setup

## Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=api_key_here
```

Start the backend:

```bash
uvicorn app.main:app --reload
```

Backend will run on:

```
http://localhost:8000
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start development server:

```bash
npm run dev
```

Frontend will run on:

```
http://localhost:5173
```

---

# 🔄 Application Flow

```
User uploads CV + Job Description
              |
              ↓
React Frontend sends FormData
              |
              ↓
FastAPI receives request
              |
              ↓
PDF text extraction
              |
              ↓
AI analysis with LLM
              |
              ↓
Structured JSON response
              |
              ↓
Frontend displays results
```

---

# 📊 Example AI Response

```json
{
  "match_score": 85,
  "skills": [
    "React",
    "TypeScript",
    "FastAPI"
  ],
  "missing_skills": [
    "Docker",
    "AWS"
  ],
  "improvements": [
    "Add cloud deployment experience"
  ],
  "cover_letter": "Generated cover letter..."
}
```

---

# 🔒 Environment Variables

The project requires:

| Variable     | Description                   |
| ------------ | ----------------------------- |
| GROQ_API_KEY | API key for LLM communication |

Never commit your `.env` file to GitHub.

---

# 🎯 Future Improvements

* User authentication
* Save previous CV analyses
* Export analysis as PDF
* Multi-language support
* Improved AI scoring system
* Job recommendation system
* Cloud deployment

---

# 👨‍💻 Author

**Elmar Abdullayev**

Full-Stack Developer passionate about AI-powered applications and modern web technologies.

---

# 📄 License

This project is for educational and portfolio purposes.
