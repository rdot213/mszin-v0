# MsZin – Flask + Jinja + HTMX (Prompt-First Spec)

## Stack
Flask (Python), Jinja templates, HTMX via CDN. Local JSON for memory (no DB).

## Files
requirements.txt
wsgi.py
app/__init__.py
app/routes.py
app/services/gpt.py
app/core/config.py
templates/index.html
static/css/style.css
data/  (created at runtime; seeds memory.json if missing)

## requirements.txt
flask
jinja2
python-dotenv
httpx
gunicorn

## Run
gunicorn wsgi:app  (host 0.0.0.0, port 8000). For dev: python wsgi.py.

## Endpoints
GET /            -> render index.html (greeting, “Aware Mode” bar, HTMX div that loads /briefing)
GET /briefing    -> HTML snippet with four cards: Schedule, Priorities(list), Relationship, Insight
POST /settings   -> save user_name + tone (professional|warm|direct) to data/memory.json; return “Saved”
POST /touchpoint -> append {contact, note}; return “Added”
GET /health      -> {"status":"ok"}

## Services
app/services/gpt.py -> generate_briefing(mem) returns mock dict: schedule, priorities[3], relationship (last touchpoint if any), insight.

## Memory
app/core/config.py -> load_memory(), save_memory(), ensure_memory()  
Seed: {"user_name":"Rob","tone":"professional","touchpoints":[]}

## UI
Dark “living canvas” gradient, soft cards, small animated “Aware Mode” bar.

## Acceptance
- Structure above exists
- /health works
- Home renders and HTMX loads /briefing
- Settings/Touchpoint persist to JSON
- Requirements installed; app runs with one click

## Agent
Scaffold all files, install deps, run server so preview opens.  
Then show folder tree and open app/routes.py. Stick to this spec exactly.
