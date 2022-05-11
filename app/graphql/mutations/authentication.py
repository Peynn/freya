import strawberry
from strawberry.types import Info

from app.graphql.types import UserType
from app.repositories import user as UserRepository


@strawberry.type
class AuthenticationSuccess:
    user: UserType


@strawberry.type
class AuthenticationError:
    message: str


AuthenticationResult = strawberry.union(
    "AuthenticationResult", (AuthenticationSuccess, AuthenticationError)
)


@strawberry.field
def authenticate(
    self, username: str, password: str, info: Info
) -> AuthenticationResult:
    user = UserRepository.get_user(db=info.context["db"], user_id=username)

    if user is None:
        return AuthenticationError("Something went wrong")

    return AuthenticationSuccess(user=UserType(id=user.id, email=user.email))
