from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.schema.Base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    password: Mapped[str] = mapped_column(String)

    blogs = relationship("Blog", back_populates="creator")
