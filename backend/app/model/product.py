from sqlalchemy import String, Numeric, ForeignKey,Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.database.sql import BaseModel
import enum
from decimal import Decimal

class ProductStatus(str, enum.Enum):
    ACTIVE = "active"
    NONACTIVE = "nonactive"

class Product(BaseModel):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    thumbnail: Mapped[str|None] = mapped_column(String(555), nullable=True)
    price: Mapped[Decimal] = mapped_column(Numeric(precision=15, scale=2), default=0.00)
    status: Mapped[ProductStatus] = mapped_column(Enum(ProductStatus, native_enum=False))
    description: Mapped[str | None] = mapped_column(String(555), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(nullable=True)