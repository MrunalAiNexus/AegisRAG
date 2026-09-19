from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from .config import ROOT_DIR
from .dataset import metadata
from .evaluator import evaluate
from .rag_pipeline import run_pipeline
from .attack_simulator import run_attack
from .research_data import RESEARCH_QUESTION, DATASET, ATTACK_CATEGORIES, DEMO_MODE, comparison, security_score

app = Flask(__name__, static_folder=str(ROOT_DIR), static_url_path="")
CORS(app)

@app.get("/")
def index():
    return send_from_directory(ROOT_DIR, "index.html")

@app.get("/api/dashboard")
def dashboard():
    aegis = next(x for x in comparison() if x["configuration"] == "AegisRAG")
    return jsonify({"status": "DEMO DATA" if DEMO_MODE else "MEASURED DATA", "experiments": 12, "attack_tests": 48, "detection_rate": aegis["detection"], "answer_quality": aegis["answer_quality"], "security_score": security_score(aegis), "question": RESEARCH_QUESTION, "dataset": metadata()})

@app.get("/api/research")
def research():
    return jsonify({"question": RESEARCH_QUESTION, "status": "DEMO DATA" if DEMO_MODE else "MEASURED DATA", "stages": ["Query", "Retrieval", "Context Analysis", "AegisRAG Security Layer", "LLM", "Response Validation"], "controls": ["Input Analysis", "Retrieval Validation", "Prompt Injection Detection", "Context Sanitization", "Output Validation", "Data Leakage Detection"]})

@app.get("/api/evaluation")
def evaluation():
    return jsonify(evaluate())

@app.get("/api/architecture")
def architecture():
    return jsonify({"status": "IMPLEMENTED DEMONSTRATION PIPELINE", "components": ["User Query", "Query Analysis", "Retriever", "Retrieved Documents", "AegisRAG Security Layer", "Context Validation", "LLM / Answer Generator", "Response Validation", "Secure Response"]})

@app.get("/api/findings")
def findings():
    return jsonify({"status": "ILLUSTRATIVE FINDINGS", "security": "The rule-based demonstration identifies common suspicious instruction patterns and applies blocking only in defended configurations.", "quality": "Response quality is represented as a comparison metric and should be replaced by measured ground-truth evaluation.", "tradeoff": "Security controls can change which requests are answered; both attack resistance and answer quality must be measured together.", "limitations": ["Rule-based detector only", "No external LLM is configured", "Demo dataset values are illustrative"]})

@app.get("/api/reports")
def reports():
    return jsonify({"status": "DEMO DATA", "sections": ["Experiment Summary", "Dataset", "Methodology", "Attack Categories", "Evaluation Metrics", "Results", "Findings", "Limitations", "Future Work"]})

@app.post("/api/query")
def query():
    payload = request.get_json(silent=True) or {}
    question = str(payload.get("query", "")).strip()
    if not question:
        return jsonify({"error": "query is required"}), 400
    return jsonify(run_pipeline(payload.get("configuration", "AegisRAG"), question))

@app.post("/api/attack-test")
def attack_test():
    payload = request.get_json(silent=True) or {}
    if not payload.get("payload"):
        return jsonify({"error": "payload is required"}), 400
    return jsonify(run_attack(payload.get("attack_type", "Prompt Injection"), payload["payload"], payload.get("target", "AegisRAG")))

@app.post("/api/run-evaluation")
def run_evaluation():
    return jsonify({"message": "Evaluation completed in demonstration mode.", **evaluate()})

@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({"error": "API endpoint not found"}), 404
    return send_from_directory(ROOT_DIR, "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
