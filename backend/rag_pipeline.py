from .dataset import retrieve
from .models import QueryResult
from .security_engine import analyze

class AnswerGenerator:
    def generate(self, query, context):
        if context:
            return f"Demo answer based on retrieved evidence: {context[0]['text'][:280]}"
        return f"Demo response: no indexed evidence directly matched the query '{query}'. Add documents to data/documents for retrieval."

class BaselineRAG:
    name = "Baseline RAG"
    def run(self, query):
        sources = retrieve(query)
        return QueryResult(self.name, AnswerGenerator().generate(query, sources), "MEDIUM", "ALLOWED", [x["source"] for x in sources], "Baseline path: no security controls applied.")

class GuardedRAG(BaselineRAG):
    name = "Guarded RAG"
    def run(self, query):
        security = analyze(query)
        sources = retrieve(query)
        blocked = security["attack_detected"]
        return QueryResult(self.name, "Request blocked by rule-based guard." if blocked else AnswerGenerator().generate(query, sources), "HIGH" if blocked else "LOW", "BLOCKED" if blocked else "ALLOWED", [x["source"] for x in sources], security["explanation"])

class AegisRAG(GuardedRAG):
    name = "AegisRAG"
    def run(self, query):
        # Proposed security-aware path: analyze query, retrieve, then validate retrieved context before generation.
        query_security = analyze(query)
        sources = retrieve(query)
        context_security = analyze(" ".join(x["text"] for x in sources), "Malicious Retrieved Content")
        blocked = query_security["attack_detected"] or context_security["attack_detected"]
        explanation = query_security["explanation"] if query_security["attack_detected"] else ("Retrieved context passed security validation." if not context_security["attack_detected"] else context_security["explanation"])
        return QueryResult(self.name, "Request blocked by AegisRAG security layer." if blocked else AnswerGenerator().generate(query, sources), "HIGH" if blocked else "LOW", "BLOCKED" if blocked else "ALLOWED", [x["source"] for x in sources], explanation)

def run_pipeline(configuration, query):
    cls = {"Baseline RAG": BaselineRAG, "Guarded RAG": GuardedRAG, "AegisRAG": AegisRAG}.get(configuration, AegisRAG)
    return cls().run(query).to_dict()
