from pathlib import Path
from .config import DOCUMENTS_DIR
from .research_data import DATASET

def load_documents() -> list[dict]:
    DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
    docs = []
    for path in sorted(DOCUMENTS_DIR.glob("*")):
        if path.suffix.lower() in {".txt", ".md"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            docs.append({"name": path.name, "text": text})
    return docs

def chunks(documents=None, size=700):
    documents = load_documents() if documents is None else documents
    output = []
    for doc in documents:
        words = doc["text"].split()
        for i in range(0, len(words), size):
            output.append({"source": doc["name"], "text": " ".join(words[i:i+size])})
    return output

def retrieve(query: str, limit=3):
    terms = {x.lower() for x in query.split() if len(x) > 2}
    scored = []
    for chunk in chunks():
        score = sum(chunk["text"].lower().count(term) for term in terms)
        if score:
            scored.append((score, chunk))
    return [item for _, item in sorted(scored, key=lambda x: x[0], reverse=True)[:limit]]

def metadata():
    return DATASET.copy()
