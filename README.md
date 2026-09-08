# AI Resume Analyzer & Job Matcher

A personal AI portfolio project that compares a PDF resume with a job description, identifies matched and missing skills, calculates an explainable match score, and provides improvement suggestions.

## Features
- PDF resume upload and text extraction
- Job description analysis
- Skill matching and gap detection
- Explainable match score
- Improvement suggestions
- Responsive web UI
- Works without an AI API key
- Optional AI extension point
- Docker support
- Unit test

## Tech Stack
Python, FastAPI, Jinja2, PyMuPDF, HTML/CSS/JavaScript, Docker

## Run locally
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

## Docker
```bash
docker build -t ai-resume-analyzer .
docker run --rm -p 8000:8000 ai-resume-analyzer
```

## GitHub
```bash
git init
git add .
git commit -m "Initial release: AI Resume Analyzer"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
git push -u origin main
```

## Privacy
Resume files are processed in memory and are not intentionally stored by this application. Do not commit resumes, API keys, or other private information.

## Future improvements
- Semantic embeddings
- ATS keyword analysis
- Experience-level matching
- Local LLM support
- Resume version tracking
- Job application tracker
