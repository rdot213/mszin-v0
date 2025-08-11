import datetime

def generate_briefing(mem: dict) -> dict:
    today = datetime.datetime.now().strftime("%A, %b %d")
    relationship = "Say hello to someone important today."
    if mem.get("touchpoints"):
        last = mem["touchpoints"][-1]
        relationship = f"Follow up with {last['contact']}: {last.get('note','(no note)')}"
    priorities = [
        "Deep work: 90 minutes on Ms. Zin MVP",
        "Send recap email (auto-drafted soon)",
        "Two calls max in the afternoon window",
    ]
    insight = "Your 10am block is next to a high-drain task. Move admin work to 3pm; keep the morning strategic."
    schedule = f"{today}: 3 meetings (10:00, 1:00, 4:30). Buffer: 15m."
    return {"schedule": schedule, "priorities": priorities,
            "relationship": relationship, "insight": insight}
