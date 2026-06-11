from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import enum

class OperatorCardStatus(str, enum.Enum):
    ACTIVE = "active"
    NONACTIVE = "nonactive"


class OperatorCard(BaseModel):
    __tablename__ = "operator_card"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    status: Mapped[OperatorCardStatus] = mapped_column(Enum(OperatorCardStatus,native_enum=False), default=OperatorCardStatus.ACTIVE)
    thumbnail: Mapped[str|None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)
