from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import uuid
from decimal import Decimal
from app import model

class Tip(BaseModel):
    __tablename__ = "tip"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(String(255),nullable=False)
    thumbnail: Mapped[str] = mapped_column(String(255),nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime|None] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime|None] = mapped_column(nullable=True)

