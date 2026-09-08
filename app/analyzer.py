import re
from collections import Counter
from .skills import extract_skills, normalize_skills

STOPWORDS={"the","and","for","with","from","this","that","your","you","are","our","their",
"have","will","work","working","experience","years","year","job","role","team","required",
"looking","using","into","more","than","they","them","when","where","what","while"}

def keywords(text):
    words=re.findall(r"[A-Za-z][A-Za-z+#./-]{2,}", text.lower())
    counts=Counter(w for w in words if w not in STOPWORDS)
    return set(counts)

def score(resume_skills, job_skills, resume_text, job_text):
    rs=normalize_skills(resume_skills); js=normalize_skills(job_skills)
    skill=100 if not js else len(rs & js)/len(js)*100
    jk=keywords(job_text); rt=resume_text.lower()
    keyword=100 if not jk else min(100, sum(w in rt for w in jk)/len(jk)*100)
    words=len(resume_text.split())
    resume_signal=100 if 250<=words<=1500 else 80 if 150<=words<=2000 else 60
    total=round(skill*.60+keyword*.25+resume_signal*.15)
    return {"overall":max(0,min(100,total)),"skill_score":round(skill),
            "keyword_score":round(keyword),"readability_score":round(resume_signal)}

def suggestions(missing, result, text):
    out=[]
    if missing:
        out.append("If you genuinely have experience with these missing skills, surface them clearly: "+", ".join(missing[:8])+".")
    if result["skill_score"]<70:
        out.append("Prioritize the job's core requirements and make relevant projects or experience easy to find.")
    if result["keyword_score"]<70:
        out.append("Use the employer's terminology naturally where it accurately describes your existing experience.")
    if len(text.split())<250:
        out.append("Add concise, measurable project or achievement details if they are currently missing.")
    elif len(text.split())>1500:
        out.append("Remove repetitive or low-value wording and keep the strongest evidence prominent.")
    if not out:
        out.append("Your resume has strong coverage. Focus on measurable achievements and role-specific evidence.")
    return out

def analyze(resume_text, job_description):
    r=extract_skills(resume_text); j=extract_skills(job_description)
    rs=normalize_skills(r); js=normalize_skills(j)
    matched=sorted(rs&js,key=str.lower); missing=sorted(js-rs,key=str.lower)
    additional=sorted(rs-js,key=str.lower)
    sc=score(r,j,resume_text,job_description)
    return {"score":sc,"matched":matched,"missing":missing,"additional":additional,
            "resume_words":len(resume_text.split()),"job_words":len(job_description.split()),
            "suggestions":suggestions(missing,sc,resume_text)}
