from pydantic import BaseModel, validator
from typing import Optional


# Model Pydantic reprezentujący strukturę CloudEvent
class CloudEventModel(BaseModel):
    id: str
    type: str
    source: str
    subject: Optional[str] = None
    specversion: Optional[str] = "1.0"
    time: Optional[str] = None
    datacontenttype: Optional[str] = "application/json"
    data: dict

    @validator("type")
    def type_must_be_set(cls, v):
        if not v:
            raise ValueError("type must be set")
        if not v.startswith("document."):
            raise ValueError("type must start with 'document.<operation'")
        return v
