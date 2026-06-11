from sqlalchemy import String, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
from app import model


class User(BaseModel):
    __tablename__ = "user"
    
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255),index=True, unique=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50),unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    verified: Mapped[bool | None] = mapped_column(default=False, nullable=True)
    profile_picture: Mapped[str | None] = mapped_column(String(555), nullable=True)
    ktp: Mapped[str] = mapped_column(String(16), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime|None] = mapped_column()

    # Foreign
    wallet: Mapped["model.Wallet"] = relationship("Wallet", back_populates="User", uselist=False)
    transaction:Mapped[list["model.Transaction"]] = relationship("Transaction", back_populates="User")
