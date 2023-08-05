"""
Database models for Humbug integration.
"""
import uuid

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    MetaData,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from brood.models import utcnow

"""
Naming conventions doc
https://docs.sqlalchemy.org/en/13/core/constraints.html#configuring-constraint-naming-conventions
"""
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)


class HumbugEvent(Base):  # type: ignore
    """
    Integration event of Humbug.
    """

    __tablename__ = "humbug_events"
    __table_args__ = (UniqueConstraint("group_id", "journal_id"),)

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    group_id = Column(UUID(as_uuid=True), nullable=False)
    journal_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(
        DateTime(timezone=True), server_default=utcnow(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        onupdate=utcnow(),
        nullable=False,
    )
    bugout_user = relationship(
        "HumbugBugoutUser", uselist=False, cascade="all, delete, delete-orphan"
    )


class HumbugBugoutUser(Base):  # type: ignore
    """
    access_token_id - NOT restricted token! This token control autogenerated user.
    UniqueConstraint("event_id", "user_id") control HumbugEvent.bugout_user is not List.
    """

    __tablename__ = "humbug_bugout_users"
    __table_args__ = (UniqueConstraint("event_id", "user_id"),)

    user_id = Column(UUID(as_uuid=True), primary_key=True, unique=True, nullable=False)
    access_token_id = Column(UUID(as_uuid=True), nullable=True)

    event_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "humbug_events.id",
            ondelete="CASCADE",
        ),
    )

    created_at = Column(
        DateTime(timezone=True), server_default=utcnow(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=utcnow(),
        onupdate=utcnow(),
        nullable=False,
    )

    restricted_tokens = relationship(
        "HumbugBugoutUserToken",
        cascade="all, delete, delete-orphan",
    )


class HumbugBugoutUserToken(Base):  # type: ignore
    """
    List of restricted tokens belongs to HumbugBugoutUser.
    """

    __tablename__ = "humbug_bugout_user_tokens"

    restricted_token_id = Column(
        UUID(as_uuid=True), primary_key=True, unique=True, nullable=False
    )
    event_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "humbug_events.id",
            ondelete="CASCADE",
        ),
    )
    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey(
            "humbug_bugout_users.user_id",
            ondelete="CASCADE",
        ),
    )
    app_name = Column(String, nullable=False)
    app_version = Column(String, nullable=False)
    store_ip = Column(Boolean, default=False, nullable=False)
