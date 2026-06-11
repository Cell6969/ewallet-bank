from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import enum
from decimal import Decimal
from app import model

class DataPlan(BaseModel):
    __tablename__ = "data_plan"

    id: Mapped[int] = mapped_column(index=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    price: Mapped[Decimal] = mapped_column(Numeric(precision=15, scale=2),default=0.00)
    operator_card_id: Mapped[int] = mapped_column(
        ForeignKey('operator_card.id', ondelete='cascade'),
    )
    operator_card: Mapped["model.OperatorCard"] = relationship(
        "OperatorCard"
    )

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)

