from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict


class ContactBase(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: str = Field(max_length=50)
    phone: str = Field(max_length=50)
    birth_date: datetime
    additional: str = Field(max_length=250)

class ContactResponse(ContactBase):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birth_date: datetime
    additional: str
    created_at: datetime | None
    updated_at: Optional[datetime] | None

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)

class User(BaseModel):
    id: int
    username: str
    email: str
    avatar: str

    model_config = ConfigDict(from_attributes=True, str_strip_whitespace=True)

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str