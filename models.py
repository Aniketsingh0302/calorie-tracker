import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base
from enums import ActivityType, Goal, Sex


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(100))
    nickname: Mapped[str | None] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    health_records: Mapped[list["HealthRecord"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class HealthRecord(Base):
    __tablename__ = "health_records"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True
    )

    # inputs
    weight_kg: Mapped[float] = mapped_column(Float)
    height_m: Mapped[float] = mapped_column(Float)
    age: Mapped[int] = mapped_column(Integer)
    sex: Mapped[Sex] = mapped_column(Enum(Sex, native_enum=False, length=10))
    goal: Mapped[Goal] = mapped_column(Enum(Goal, native_enum=False, length=10))
    activity: Mapped[ActivityType] = mapped_column(
        Enum(ActivityType, native_enum=False, length=32)
    )

    # results
    bmi: Mapped[float] = mapped_column(Float)
    bmr: Mapped[int] = mapped_column(Integer)
    calories: Mapped[int] = mapped_column(Integer)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    user: Mapped["User"] = relationship(back_populates="health_records")