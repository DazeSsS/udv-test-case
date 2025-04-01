from pydantic import BaseModel, Field


class ErrorResponse(BaseModel):
    detail: str

class NotFoundResponse(ErrorResponse):
    detail: str = Field(..., examples=['Object with ID 1 does not exist'])
