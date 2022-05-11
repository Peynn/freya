import strawberry
from strawberry.tools import create_type

from app.graphql.mutations.authentication import authenticate
from app.graphql.mutations.user import create_user
from app.graphql.queries.hello_world import say_hello

# Code organization: https://github.com/strawberry-graphql/strawberry/discussions/1207
Query = create_type("Query", [say_hello])
Mutation = create_type("Mutation", [authenticate, create_user])

schema = strawberry.Schema(query=Query, mutation=Mutation)
