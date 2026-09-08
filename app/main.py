from pathlib import Path
from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .analyzer import analyze
from .pdf_utils import extract_pdf_text

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="AI Resume Analyzer & Job Matcher", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None, "error": None})

@app.post("/analyze", response_class=HTMLResponse)
async def analyze_resume(request: Request, resume: UploadFile = File(...), job_description: str = Form(...)):
    try:
        if not resume.filename or not resume.filename.lower().endswith(".pdf"):
            raise ValueError("Please upload a PDF resume.")
        if not job_description.strip():
            raise ValueError("Please paste a job description.")
        data = await resume.read()
        if len(data) > 10 * 1024 * 1024:
            raise ValueError("Resume is too large. Maximum size is 10 MB.")
        text = extract_pdf_text(data)
        if not text.strip():
            raise ValueError("Could not extract readable text from the PDF.")
        result = analyze(text, job_description)
        return templates.TemplateResponse("index.html", {"request": request, "result": result, "error": None})
    except Exception as exc:
        return templates.TemplateResponse("index.html", {"request": request, "result": None, "error": str(exc)}, status_code=400)
