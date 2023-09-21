from pydantic import BaseModel


class TagsErrorResponse(BaseModel):
    error: str
    code: str
