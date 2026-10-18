from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .data import ENCOUNTERS, make, summary_for

app = FastAPI(title="SPACEGUARD API", version="1.0.0", description="Synthetic demo API; not for operational collision avoidance.")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173","http://127.0.0.1:5173"], allow_credentials=False, allow_methods=["GET","POST"], allow_headers=["*"])
_current = [dict(e) for e in ENCOUNTERS]

@app.get("/")
def root(): return {"name":"SPACEGUARD API","status":"ready","data_mode":"synthetic","docs":"/docs"}
@app.get("/health")
def health(): return {"status":"ok","service":"spaceguard-api","data_mode":"synthetic"}
@app.get("/api/summary")
def summary(): return summary_for(_current)
@app.get("/api/encounters")
def encounters(): return _current
@app.get("/api/alerts")
def alerts(threshold: int = 65):
    if not 0 <= threshold <= 100: raise HTTPException(status_code=400, detail="threshold must be between 0 and 100")
    return [e for e in _current if e["score"] >= threshold]
@app.post("/api/scenarios/{scenario}")
def scenarios(scenario: str):
    global _current
    if scenario == "low": lead = make("SG-DEMO-L01","SAT-DEMO-11","DEB-DEMO-21","00:44:00 UTC",24.8,2.1)
    elif scenario == "elevated": lead = make("SG-DEMO-E01","SAT-DEMO-12","DEB-DEMO-22","00:27:00 UTC",3.8,8.2)
    elif scenario == "critical": lead = make("SG-DEMO-C01","SAT-DEMO-13","DEB-DEMO-23","00:09:00 UTC",.28,14.9)
    else: raise HTTPException(status_code=404, detail="Use low, elevated, or critical.")
    _current = [lead] + [dict(e) for e in ENCOUNTERS if e["id"] != "SG-2048"]
    return {"scenario":scenario,"encounters":_current,"summary":summary_for(_current)}
