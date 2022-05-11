import typing

from sqlalchemy.orm import Session

from app.db import models


def get_user(db: Session, user_id: int) -> typing.Optional[models.User]:
    return db.query(models.User).filter(models.User.id == user_id).first()
