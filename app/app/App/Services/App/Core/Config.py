import os, json

DATA_PATH = "data/memory.json"

def ensure_memory():
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    if not os.path.exists(DATA_PATH):
        save_memory({"user_name":"Rob","tone":"professional","touchpoints":[]})

def load_memory() -> dict:
    ensure_memory()
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(mem: dict) -> None:
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(mem, f, indent=2)
