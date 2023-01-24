from pydantic import BaseModel

class DoubleProductRequest(BaseModel):
    hr: int
    sbp: float