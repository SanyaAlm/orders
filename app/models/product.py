from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from app.models.base import Base

if TYPE_CHECKING:
    from .order import Order


class Product(Base):
    name: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]

    orders: Mapped[list["Order"]] = relationship(
        secondary="order_products", back_populates="products"
    )
