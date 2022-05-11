from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from app.graphql.schema import schema

# TODO: graphiql=False for production and Instropection
# TODO: only add this router when user is logged
# DOC: https://strawberry.rocks/docs/integrations/fastapi
graphql_app = GraphQLRouter(schema, graphiql=True)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
