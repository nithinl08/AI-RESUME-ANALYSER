import re

SKILLS = [
"Python","Java","JavaScript","TypeScript","C","C++","C#","Go","Rust","SQL",
"HTML","CSS","React","Angular","Vue","Node.js","FastAPI","Flask","Django",
"REST API","GraphQL","Git","GitHub","Docker","Kubernetes","AWS","Azure","GCP",
"Linux","Windows","PostgreSQL","MySQL","MongoDB","Redis","Kafka","Jenkins",
"GitHub Actions","CI/CD","Terraform","Ansible","Selenium","Playwright","PyTest",
"JMeter","Machine Learning","Deep Learning","Artificial Intelligence","AI","NLP",
"LLM","RAG","OpenAI","LangChain","Pandas","NumPy","scikit-learn","TensorFlow",
"PyTorch","Power BI","Tableau","Excel","Data Analysis","Data Science","Agile",
"Scrum","Microservices","System Design","Unit Testing","Test Automation",
"Automation","Debugging","Communication","Leadership"
]

def contains(text, skill):
    t=text.lower(); s=skill.lower()
    if re.fullmatch(r"[a-z0-9+#]+", s):
        return re.search(rf"(?<![a-z0-9]){re.escape(s)}(?![a-z0-9])", t) is not None
    return s in t

def extract_skills(text):
    found=[]
    for skill in SKILLS:
        canonical="PyTest" if skill=="pytest" else skill
        if contains(text, skill) and canonical not in found:
            found.append(canonical)
    return sorted(found, key=str.lower)

def normalize_skills(items):
    aliases={"rest":"REST API","rest api":"REST API","pytest":"PyTest","ci/cd":"CI/CD"}
    return {aliases.get(x.strip().lower(), x.strip()) for x in items if x.strip()}
