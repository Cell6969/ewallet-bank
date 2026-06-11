from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from app.database.sql import BaseModel
from decimal import Decimal
from app import model

class Wallet(BaseModel):
    __tablename__ = "wallet"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    card_number: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    balance: Mapped[Decimal] = mapped_column(Numeric(precision=15, scale=2), default=0.00)
    pin: Mapped[str | None] = mapped_column(String(6))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    user_id: Mapped[int] = mapped_column(ForeignKey('user.id',ondelete='CASCADE'), index=True)

    user: Mapped["model.User"] = relationship("User", back_populates="wallet")

