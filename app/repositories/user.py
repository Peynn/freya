import typing

from sqlalchemy.orm import Session

from app.db import models
from app.services import authentication as AuthenticationService


def get_user(db: Session, email: int) -> typing.Optional[models.User]:
    return db.query(models.User).filter(models.User.email == email).first()


def authenticate(
    db: Session, email: str, plain_password: str
) -> typing.Optional[models.User]:
    user: typing.Optional[models.User] = (
        db.query(models.User).filter(models.User.email == email).first()
    )

    if user is None:
        return None

    if (
        AuthenticationService.verify_password(
            plain_password=plain_password, password_hash=user.password_hash
        )
        is False
    ):
        return None

    return user


def create(
    db: Session, email: str, plain_password: str
) -> typing.Optional[models.User]:
    user = db.query(models.User).filter(models.User.email == email).first()

    if user:
        return None

    password_hash = AuthenticationService.hash_password(plain_password=plain_password)
    user = models.User(email=email, password_hash=password_hash)

    db.add(user)
    db.commit()

    return user
