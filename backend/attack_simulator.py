from .security_engine import analyze

def run_attack(attack_type, payload, target):
    result = analyze(payload, attack_type)
    protected = target in {"Guarded RAG", "AegisRAG"}
    blocked = result["attack_detected"] and protected
    return {**result, "attack_type": attack_type, "target": target, "blocked": blocked, "risk_level": "HIGH" if result["attack_detected"] else "LOW", "security_action": "BLOCKED" if blocked else "ALLOWED", "mode": "DEMO / RULE-BASED"}
