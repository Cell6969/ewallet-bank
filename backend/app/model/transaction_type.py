from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import enum

class TransactionAction(str, enum.Enum):
    CR = "cr" # credit (+)
    DR = "dr" # debit (-)

class TransactionType(BaseModel):
    __tablename__ = "transaction_type"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    action: Mapped[TransactionAction] = mapped_column(
        Enum(TransactionAction, native_enum=False),
    )
    thumbnail: Mapped[str | None] = mapped_column(String(255), nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime|None] = mapped_column(nullable=True)
    deleted_at: Mapped[datetime|None] = mapped_column(nullable=True)