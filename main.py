from fastapi import Depends, FastAPI
from strawberry.fastapi import GraphQLRouter

from app.db.base import SessionLocal
from app.graphql.schema import schema


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


async def get_context(db=Depends(get_db)):
    return {"db": db}


# TODO: graphiql=False for production and Instropection
# TODO: only add this router when user is logged
# DOC: https://strawberry.rocks/docs/integrations/fastapi
graphql_app = GraphQLRouter(schema, graphiql=True, context_getter=get_context)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
