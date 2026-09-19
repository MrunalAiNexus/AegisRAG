from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
DOCUMENTS_DIR = DATA_DIR / "documents"
DEMO_MODE = True

# These values are illustrative and intentionally centralized for replacement by measured runs.
DEMO_RESULTS = {
    "baseline": {"security": 42, "detection": 38, "answer_quality": 91, "attack_success": 62, "data_leakage": 18},
    "guarded": {"security": 76, "detection": 78, "answer_quality": 86, "attack_success": 34, "data_leakage": 11},
    "aegisrag": {"security": 91, "detection": 91, "answer_quality": 84, "attack_success": 21, "data_leakage": 7},
}
