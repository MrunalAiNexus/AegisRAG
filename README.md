# AegisRAG — AI Security Research Laboratory

AegisRAG is a local Flask research application for exploring the question: **Can security-aware RAG reduce prompt injection while preserving answer quality?** It preserves the existing dark research-lab UI while adding a Python demonstration backend.

https://aegis-56c9ictdk-mrunalainexus-projects.vercel.app/

## Research scope

The project compares Baseline RAG, Guarded RAG, and the proposed AegisRAG security-aware pipeline. It evaluates attack success, prompt-injection detection, data leakage, response quality, and a transparent composite score.

## Architecture

`User Query → Query Analysis → Retriever → Retrieved Documents → AegisRAG Security Layer → Context Validation → Answer Generator → Response Validation → Secure Response`

The current answer generator and security detector are deliberately lightweight and local. The security engine is a **rule-based security demonstration**, not an advanced ML security model.

## Threats and metrics

The detector covers direct and indirect prompt injection, data leakage, jailbreak attempts, malicious retrieved content, and context manipulation. Metrics and evaluation comparisons are returned by Python APIs.

## Technology stack

- Python 3.10+
- Flask and Flask-CORS
- Local `.txt` / `.md` document retrieval using explainable keyword matching
- Existing HTML/CSS/JavaScript frontend

## Project structure

```text
backend/       Flask app, RAG pipeline, security engine, evaluator, data models
data/documents Local demonstration documents
index.html     Existing AegisRAG UI
requirements.txt
run.py
```

## How to run

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:5000`.

## API

`GET /api/dashboard`, `/api/research`, `/api/evaluation`, `/api/architecture`, `/api/findings`, `/api/reports`

`POST /api/query`, `/api/attack-test`, `/api/run-evaluation`

## Demo-data disclaimer

This prototype currently uses illustrative evaluation data centralized in `backend/config.py` and `backend/research_data.py`. Replace it with measured experimental results before academic publication. No scientific significance or benchmark improvement is claimed.

## Future work

Add a measured evaluation corpus, stronger retrieval, automated ground-truth scoring, real experiment history, and an optional external LLM adapter.

## Author

Created by Mrunal Urankar
