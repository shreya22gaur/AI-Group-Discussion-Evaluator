
# 🎤 AI Group Discussion Evaluator

An AI-powered application that evaluates Group Discussion (GD) responses and provides detailed feedback on communication, clarity, relevance, confidence, and grammar using Large Language Models (LLMs).

## 🚀 Live Demo

Add your Render deployment link here:

https://ai-group-discussion-evaluator.onrender.com/

---

## 📌 Features

* Enter any Group Discussion topic
* Submit your GD response
* AI-powered evaluation and scoring
* Communication Skills Assessment
* Clarity & Relevance Analysis
* Confidence Evaluation
* Grammar Review
* Strengths & Weaknesses Identification
* Personalized Improvement Suggestions

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Groq API
* Llama 3.3 70B Versatile
* Render (Deployment)

---

## 📂 Project Structure

ai-gd-evaluator/

├── app.py

├── requirements.txt

├── render.yaml

├── .gitignore

├── README.md

└── .env (local only)

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/ai-gd-evaluator.git
cd ai-gd-evaluator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 🧠 How It Works

1. Enter a Group Discussion topic.
2. Type your GD response.
3. Click **Evaluate Response**.
4. The AI analyzes your response.
5. Receive:

   * Communication Score
   * Clarity Score
   * Relevance Score
   * Confidence Score
   * Grammar Score
   * Strengths
   * Weaknesses
   * Suggestions for Improvement

---

## 🎯 Use Cases

* Placement Preparation
* Campus Recruitment Training
* Communication Skill Development
* Interview Readiness
* Public Speaking Practice
* Self-Evaluation and Learning

---

## 💡 Future Enhancements

* Voice-based GD Evaluation
* Speech-to-Text Integration
* Multi-participant GD Analysis
* Downloadable Evaluation Reports
* Historical Performance Tracking
* Interview Follow-up Question Generator

---

## 📈 Resume Description

Developed an AI-powered Group Discussion Evaluator using Streamlit and Groq LLMs that assesses communication skills, clarity, confidence, grammar, and topic relevance while providing actionable feedback and personalized improvement suggestions.

---

## 🤝 Contributing

Contributions and suggestions are welcome. Feel free to fork the repository and submit pull requests.

---

## 📜 License

This project is licensed under the MIT License.
