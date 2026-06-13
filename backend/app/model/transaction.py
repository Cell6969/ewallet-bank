from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import uuid
from decimal import Decimal
from app import model

class Transaction(BaseModel):
    __tablename__ = "transaction"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, index=True, default=uuid.uuid4)

    user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    transaction_type_id: Mapped[int] = mapped_column(
        ForeignKey("transaction_type.id", ondelete='CASCADE'),
        index=True
    )
    payment_method_id: Mapped[int] = mapped_column(
        ForeignKey("payment_method.id", ondelete='CASCADE'),
        index=True
    )
    product_id: Mapped[int|None] = mapped_column(
        ForeignKey("product.id", ondelete='CASCADE'),
        index=True,
        nullable=True
    )
    amount: Mapped[Decimal] = mapped_column(Numeric(precision=15,scale=2), nullable=False)
    transaction_code: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    description: Mapped[str|None] = mapped_column(String(555), nullable=True)
    status: Mapped[str] = mapped_column(String(50),nullable=False,index=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)

    user: Mapped["model.User"] = relationship("User", back_populates="transaction")
    transaction_type: Mapped["model.TransactionType"] = relationship("TransactionType")
    payment_method: Mapped["model.PaymentMethod"] = relationship("PaymentMethod")
    product: Mapped["model.Product"] = relationship("Product")