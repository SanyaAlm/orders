from sqlalchemy.orm import Mapped

from app.models.base import Base


class Product(Base):
    name: Mapped[str]
    price: Mapped[int]
    quantity: Mapped[int]
