import enum
from typing import TYPE_CHECKING

from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


if TYPE_CHECKING:
    from .order import Order


class UserRole(enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.user)

    orders: Mapped[list["Order"]] = relationship("Order", back_populates="user")
