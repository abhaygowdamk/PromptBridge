from datetime import datetime
from sqlalchemy import DateTime, String, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(100))
    email:Mapped[str] = mapped_column(String(255), unique=True)
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    hashed_password:Mapped[str]=mapped_column(String(255))


class ChatMessage(Base):
    __tablename__ = "chat_message"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(ForeignKey("users.id"))
    prompt: Mapped[str]=mapped_column(String)
    llm_response:Mapped[str]=mapped_column(String)
    created_at:Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )




    