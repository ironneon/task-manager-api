from pydantic import BaseModel, ConfigDict

class TaskCreate(BaseModel):
    title: str
    completed: bool = False

class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

    model_config = ConfigDict(from_attributes=True)
class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None