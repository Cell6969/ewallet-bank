from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import uuid
from decimal import Decimal
from app import model

class TransferHistory(BaseModel):
    __tablename__ = "transfer_history"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, index=True, default=uuid.uuid4)
    sender_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    receiver_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    transaction_code: Mapped[str] = mapped_column(String(255), nullable=False)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    sender:Mapped["model.User"] = relationship("User", foreign_keys=[sender_id])
    receiver: Mapped["model.User"] = relationship("User", foreign_keys=[receiver_id])
