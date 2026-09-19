from .research_data import security_score

def evaluate_result(result: dict) -> dict:
    return {**result, "security_score": security_score(result)}
