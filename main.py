from fastapi import FastAPI
from models import AlertmanagerPayload
import uuid

app = FastAPI()
incidents = {}

@app.get("/healthz")
def healthz():
    return {"status": "healthy"}


@app.post("/alerts")
def receive_webhook(payload: AlertmanagerPayload):
    for alert in payload.alerts:
        print(alert.labels.get("alertname"), alert.status, alert.fingerprint)
    key = payload.groupKey
    if key not in incidents:
        incidents[key] = {"incident_id": "inc-" + str(uuid.uuid4()), "status": payload.status, "alert_count": len(payload.alerts), "sent_to_recovery": False}
    else:
        incidents[key]["status"] = payload.status
        incidents[key]["alert_count"] += len(payload.alerts)
    return {"received": len(payload.alerts)}


@app.get("/incidents")
def get_incidents():
    return incidents