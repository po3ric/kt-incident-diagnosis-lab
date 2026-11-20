import json
from models import AlertmanagerPayload

with open("samples/site_firing.json", encoding="utf-8") as f:
    data = json.load(f)

payload = AlertmanagerPayload(**data)
print(len(payload.alerts))
print(payload.alerts[0].labels["category"])
print(payload.alerts[2].labels.get("target_name"))
