from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def load_text(name: str) -> str:
    path = BASE_DIR / "texts" / f"{name}.txt"
    return path.read_text(encoding="utf-8")
