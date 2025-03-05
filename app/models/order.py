import enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from .user import User
    from .product import Product


class OrderStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"


class Order(Base):
    status: Mapped[OrderStatus] = mapped_column(
        Enum(OrderStatus), default=OrderStatus.pending
    )
    total_price: Mapped[int]
    is_deleted: Mapped[bool] = mapped_column(default=True, nullable=False)
    customer_name: Mapped[str] = mapped_column(String, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship("User", back_populates="orders")
    products: Mapped[list["Product"]] = relationship(
        secondary="order_products", back_populates="orders"
    )
