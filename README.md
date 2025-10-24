# AI Resume Analyzer

**AI Resume Analyzer** is a web application that evaluates and scores resumes against a target job role using Google's Gemini AI. It provides detailed suggestions for improvement, ATS optimization tips, and highlights key strengths and missing skills. The project is deployed on **AWS EC2**, aligning with cloud computing principles and practical cloud deployment experience.

---

## **Features**

- Upload resumes in **PDF or DOCX** formats.
- Enter a **target job role** for analysis.
- Extracts resume text and evaluates it using **Google Gemini AI**.
- Provides:
  - Resume Score (0-100)
  - ATS Optimization suggestions
  - Key strengths & weaknesses
  - Role alignment recommendations
  - Missing skills & keywords
  - Suggested certifications or courses
- Hosted on **AWS EC2**, accessible via public URL.
- Secure handling of **API keys** via `.env`.

---

## **Tech Stack**

- **Frontend:** Streamlit (Python)
- **AI Integration:** Google Gemini AI (Generative AI API)
- **Backend:** Python, requests, PyPDF2, python-docx
- **Cloud Deployment:** AWS EC2
- **Environment Management:** `venv`, `.env` for API keys
- **Version Control:** Git & GitHub

---

## **Getting Started**

### **1. Clone the repository**
```bash
git clone https://github.com/tas-neem/resume-analyzer.git
cd resume-analyzer
```

### **2. Create a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add your Gemini API key**
Create a .env file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```

### **5. Run the app locally**
```bash
streamlit run main.py 
```

### **6. Access the app**
Open in browser:
```bash
http://localhost:8501
```

