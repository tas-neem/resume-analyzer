import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

configuration = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8597,
    "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
    model_name="gemini-2.5-flash",
    generation_config=configuration
)

def analyse_resume(resume_text, job_role):
    if not job_role:
        return "Error: Job role is required."

    base_prompt = f"""
You are an expert resume analyst with deep knowledge of industry standards, job requirements, and hiring practices across various fields. Your task is to provide a comprehensive, detailed analysis of the resume provided.

Structure your response in the following format:

## Overall Assessment
[Provide a detailed assessment of the resume's overall quality, effectiveness, and alignment with industry standards. Include specific observations about formatting, content organization, and general impression. Be specific and concise.]

## Professional Profile Analysis
[Analyze the candidate's professional profile, experience trajectory, and career narrative. Discuss how well their story comes across and whether their career progression makes sense for their apparent goals in short.]

## Skills Analysis
- **Skill Proficiency**: [Assess the apparent level of expertise in key skills based on how they're presented in the resume]
- **Missing Skills**: [List important skills that would improve the resume for their target role. Be specific and explain why each skill matters.]

## Experience Analysis
[Provide detailed feedback on how well the candidate has presented their experience. Analyze the use of action verbs, quantifiable achievements, and relevance to their target role. Suggest specific improvements.]

## Education Analysis
[Analyze the education section, including relevance of degrees, certifications, and any missing educational elements that would strengthen their profile.]

## Key Strengths
[List 5 specific strengths of the resume with detailed explanations of why these are effective]

## Areas for Improvement
[List 5 specific areas where the resume could be improved with detailed, actionable recommendations]

## ATS Optimization Assessment
[Analyze how well the resume is optimized for Applicant Tracking Systems. Provide a specific ATS score from 0-100, with 100 being perfectly optimized. Use this format: "ATS Score: XX/100". Then suggest specific keywords and formatting changes to improve ATS performance.]

## Resume Score
[Provide a score from 0-100 based on the overall quality of the resume. Use this format exactly: "Resume Score: XX/100" where XX is the numerical score. Be consistent with your assessment - a resume with significant issues should score below 60, an average resume 60-75, a good resume 75-85, and an excellent resume 85-100.]

Resume:
{resume_text}

Analyze how well the resume aligns with the target role of {job_role}. Provide specific recommendations to better align the resume with this role.
"""
    try:
        response = model.generate_content(base_prompt)
        return response.text
    except Exception as e:
        return f"Error analyzing resume: {str(e)}"
