import typing

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from strawberry.fastapi import GraphQLRouter

from app.db import models
from app.db.base import SessionLocal
from app.graphql.schema import schema
from app.services import authentication as AuthenticationService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)


def get_db() -> Session:
    db: Session = SessionLocal()

    try:
        yield db
    finally:
        db.close()


def get_current_user(
    db=Depends(get_db), token: str = Depends(oauth2_scheme)
) -> typing.Optional[models.User]:
    if token is None:
        return None

    user = AuthenticationService.get_current_user(db=db, token=token)

    return user


async def get_context(
    db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)
) -> dict:
    return {"db": db, "user": current_user}


# TODO: graphiql=False for production and Instropection
# TODO: only add this router when user is logged
# DOC: https://strawberry.rocks/docs/integrations/fastapi
graphql_app = GraphQLRouter(schema, graphiql=True, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
