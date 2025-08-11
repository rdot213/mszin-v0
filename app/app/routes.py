from flask import Blueprint, render_template, request, jsonify
from .core.config import load_memory, save_memory
from .services.gpt import generate_briefing

bp = Blueprint("main", __name__)

@bp.get("/health")
def health():
    return jsonify(status="ok")

@bp.get("/")
def home():
    mem = load_memory()
    return render_template("index.html",
        user_name=mem.get("user_name", "Rob"),
        tone=mem.get("tone", "professional"),
    )

@bp.get("/briefing")
def briefing():
    mem = load_memory()
    b = generate_briefing(mem)
    html = f"""
    <div class='card'><strong>Schedule</strong><br>{b['schedule']}</div>
    <div class='card'><strong>Priorities</strong><ul>{"".join(f"<li>{p}</li>" for p in b['priorities'])}</ul></div>
    <div class='card'><strong>Relationship</strong><br>{b['relationship']}</div>
    <div class='card'><strong>Insight</strong><br>{b['insight']}</div>
    """
    return html

@bp.post("/settings")
def settings():
    mem = load_memory()
    mem["user_name"] = request.form.get("user_name", mem.get("user_name","Rob"))
    mem["tone"] = request.form.get("tone", mem.get("tone","professional"))
    save_memory(mem)
    return "<span>Saved.</span>"

@bp.post("/touchpoint")
def touchpoint():
    mem = load_memory()
    mem.setdefault("touchpoints", []).append({
        "contact": request.form.get("contact",""),
        "note": request.form.get("note","")
    })
    save_memory(mem)
    return "<span>Added.</span>"
