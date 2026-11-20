from pydantic import BaseModel

class Alert(BaseModel):
    status: str
    labels: dict[str, str]
    annotations: dict[str, str] = {}
    startsAt: str
    endsAt: str | None = None
    fingerprint: str
    generatorURL: str | None = None

class AlertmanagerPayload(BaseModel):
    status: str
    receiver: str
    alerts: list[Alert]
    groupKey: str | None = None
    externalURL: str | None = None
    