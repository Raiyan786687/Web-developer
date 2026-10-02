import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI
import uvicorn

app = FastAPI(title="RAYYAN.AI - Decoupled Agent Backend Engine")

# Initialize OpenRouter Client
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY", "")
)

class ChatRequest(BaseModel):
    message: str

class AnalysisRequest(BaseModel):
    target_role: str
    skills_and_bio: str

# -------------------------------------------------------------------
# STRICT GUARDRAILED SYSTEM PROMPT FOR RAYYAN'S PERSONAL ASSISTANT
# -------------------------------------------------------------------
RAYYAN_KNOWLEDGE_BASE = """
You are the official Portfolio AI Assistant for Rayyan!

ABOUT RAYYAN:
- Name: Rayyan
- Class/Grade: 9th Grade Student
- Field of Expertise: Full-Stack AI Engineer, Software & AI Agent Developer
- Course Enrolled: Web Development with Advanced AI
- Core Stack: Python 3.12, FastAPI, Streamlit, OpenAI Agents SDK, OpenRouter API, Pydantic, Git/GitHub,uv, Uvicorn, AsyncOpenAI
- Hardware Setup: Windows Workstation (Lenovo)

KEY PROJECTS & PORTFOLIO HIGHLIGHTS:
1. Decoupled Dual-Server SaaS Portfolio & Resume Evaluator App (FastAPI + Streamlit Architecture)
2. Mini-Devin AI Engineer Agent (Autonomous coding & workflow agent)
3. Voice-Activated Desktop & Web Calculators (Python, Tkinter, Speech Recognition, sounddevice)
4. Streamlit Guardrails Application (Input/Output Guardrails for OpenRouter models)
5. Security-themed conditional logic web apps

ABOUT THIS WEBSITE / PLATFORM:
- Name: RAYYAN.AI
- Architecture: Decoupled Dual-Server Architecture (Terminal 1: FastAPI Backend Port 8000 | Terminal 2: Streamlit Frontend Port 8501)
- Key Features: High-Contrast Luxury Glassmorphism UI, Live AI Resume Evaluator SaaS Portal, Real-time Engine Health Check, Bottom-Right AI Assistant Chat Widget.

STRICT GUARDRAIL RULES:
1. You MUST ONLY answer questions related to Rayyan, his background, skills, education, projects, technical stack, or this website's features and architecture.
2. If the user asks ANY question NOT related to Rayyan or this portfolio (e.g., general math, world news, cooking, weather, story writing, coding help for unrelated topics, general AI queries), politely decline with a message like:
   "I am Rayyan's dedicated Portfolio AI Assistant. I can only answer questions related to Rayyan's profile, skills, projects, or this website!"
3. Always respond in a polite, highly professional, and encouraging tone. Speak proudly of Rayyan's achievements as a 9th-grade Full-Stack AI Developer.
"""

@app.get("/")
async def root():
    return {"status": "ONLINE", "message": "Rayyan AI Engine Backend operational!"}

@app.post("/chat")
async def chat_with_agent(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
        
    try:
        response = await client.chat.completions.create(
            model="poolside/laguna-s-2.1:free",
            messages=[
                {"role": "system", "content": RAYYAN_KNOWLEDGE_BASE},
                {"role": "user", "content": req.message}
            ],
            temperature=0.3
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        return {"response": f"Backend Error: {str(e)}"}

@app.post("/analyze")
async def analyze_portfolio(req: AnalysisRequest):
    try:
        prompt = f"""
        Analyze the candidate's bio against the target role: '{req.target_role}'.
        Candidate Bio/Skills:
        {req.skills_and_bio}

        Return a structured JSON evaluation with:
        - overall_score (integer 0-100)
        - summary (string)
        - strengths (list of strings)
        - weaknesses (list of strings)
        - improvement_tips (list of strings)
        """
        response = await client.chat.completions.create(
            model="poolside/laguna-s-2.1:free",
            messages=[
                {"role": "system", "content": "You are an expert technical AI recruiter. Respond in valid JSON format only."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        import json
        result = json.loads(response.choices[0].message.content)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)