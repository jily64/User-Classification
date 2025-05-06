from pydantic import BaseModel

class QuestionareResults(BaseModel):
    email: str
    ans: str

class PsycoType(BaseModel):
    matched: str

class OnlyUser(BaseModel):
    email: str