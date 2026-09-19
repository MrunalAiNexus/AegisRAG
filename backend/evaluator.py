from .research_data import ATTACK_CATEGORIES, DEMO_RESULTS, comparison
from .metrics import evaluate_result

def evaluate():
    return {"status": "DEMO DATA", "comparison": [evaluate_result(x) for x in comparison()], "categories": ATTACK_CATEGORIES, "history": [{"experiment": "Demo baseline", "security": 42, "quality": 91}, {"experiment": "Demo guarded", "security": 76, "quality": 86}, {"experiment": "Demo AegisRAG", "security": 91, "quality": 84}]}
