from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Set, Self

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Session, mapped_column
from sqlalchemy.orm.base import Mapped
from sqlalchemy.types import Text


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contact"

    id: Mapped[int] = mapped_column(primary_key=True)
    first: Mapped[Optional[str]] = mapped_column(Text)
    last: Mapped[Optional[str]] = mapped_column(Text)
    phone: Mapped[Optional[str]] = mapped_column(Text)
    email: Mapped[Optional[str]] = mapped_column(Text)

    def __repr__(self) -> str:
        return f"Contact(id={self.id!r}, first={self.first!r}, last={self.last!r}, phone={self.phone!r}, email={self.email!r})"

    @staticmethod
    def search(db: SQLAlchemy, query: str) -> Set[Contact]:
        statement = select(Contact).where(Contact.first.contains(query))
        all = set(db.session.scalars(statement))
        return all

    @staticmethod
    def all(db: SQLAlchemy) -> Set[Contact]:
        statement = select(Contact)
        all = set(db.session.scalars(statement))
        return all

    @staticmethod
    def find(db: SQLAlchemy, id: int) -> Contact | None:
        return db.session.execute(select(Contact).where(Contact.id == id)).scalar()
