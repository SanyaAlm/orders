from typing import TYPE_CHECKING

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base import Base

if TYPE_CHECKING:
    from .product import Product
    from .order import Order


class OrderProduct(Base):
    __tablename__ = "order_products"

    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)

    order: Mapped["Order"] = relationship(back_populates="order_products")
    product: Mapped["Product"] = relationship(back_populates="product_orders")
