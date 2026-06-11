from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import enum

class PaymentMethodStatus(str,enum.Enum):
    ACTIVE = "active"
    NONACTIVE = "nonactive"

class PaymentMethod(BaseModel):
    __tablename__ = "payment_method"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    code: Mapped[str] = mapped_column(String(50),index=True, nullable=False)
    thumbnail:Mapped[str|None] = mapped_column(String(50),nullable=True)
    status: Mapped[PaymentMethodStatus] = mapped_column(
        Enum(PaymentMethodStatus, native_enum=False)
    )
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime | None] = mapped_column(nullable=True)
