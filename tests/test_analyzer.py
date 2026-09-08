from app.analyzer import analyze

def test_matching():
    resume="Python developer with FastAPI, SQL, Docker and AWS experience."
    job="Python engineer with FastAPI, Docker, AWS, Kubernetes and SQL."
    result=analyze(resume,job)
    assert "Python" in result["matched"]
    assert "Kubernetes" in result["missing"]
    assert 0 <= result["score"]["overall"] <= 100
