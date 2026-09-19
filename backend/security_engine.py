import re

PATTERNS = {
    "Prompt Injection": [r"ignore\s+(all\s+)?previous\s+instructions", r"forget\s+your\s+rules", r"bypass\s+security", r"override\s+instructions"],
    "Indirect Prompt Injection": [r"retrieved\s+(document|content).{0,40}(ignore|follow|execute)", r"document\s+instructs?\s+you"],
    "Data Leakage": [r"reveal\s+(your|the)\s+(system\s+)?prompt", r"show\s+hidden\s+instructions", r"reveal\s+confidential", r"secret\s+data"],
    "Jailbreak Attempts": [r"developer\s+message", r"do\s+anything\s+now", r"bypass\s+(your\s+)?safety", r"without\s+restrictions"],
    "Malicious Retrieved Content": [r"malicious\s+(retrieved|document)\s+content", r"execute\s+this\s+document"],
    "Context Manipulation": [r"change\s+the\s+context", r"treat\s+the\s+following\s+as\s+system", r"new\s+system\s+message"],
}

def analyze(text: str, attack_type: str | None = None) -> dict:
    text = text or ""
    matches = []
    for category, patterns in PATTERNS.items():
        if attack_type and attack_type.lower() not in category.lower() and category.lower() not in attack_type.lower():
            continue
        for pattern in patterns:
            if re.search(pattern, text, flags=re.I | re.S):
                matches.append((category, pattern))
    detected = bool(matches)
    category = matches[0][0] if matches else (attack_type or "None")
    return {"attack_detected": detected, "category": category, "confidence": 0.91 if detected else 0.12, "explanation": "Suspicious instruction override pattern detected." if detected else "No suspicious instruction detected."}
