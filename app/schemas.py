from pydantic import BaseModel, Field, EmailStr, ConfigDict

class ChatRequest(BaseModel):
        prompt: str = Field(..., min_length=1)

class ChatResponse(BaseModel):
        response: str
        
class UserCreate(BaseModel):
        name: str = Field(min_length=1, max_length=100)
        email: EmailStr
        password:str=Field(min_length=8, max_length=128)

class UserUpdate(BaseModel):
        name: str|None = Field(default=None, min_length=1, max_length=100)
        email:EmailStr|None = None

class UserResponse(BaseModel):
        model_config = ConfigDict(from_attributes=True)

        id: int
        name:str
        email:EmailStr
        created_at: datetime

class LoginRequest(BaseModel):
        email: EmailStr
        password:str

class TokenResponse(BaseModel):
        access_token:str
        token_type:str