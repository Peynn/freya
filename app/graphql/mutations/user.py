import strawberry
from strawberry.types import Info

from app.graphql import types
from app.repositories import user as UserRepository


@strawberry.input
class UserCreate:
    email: str
    password: str


@strawberry.type
class UserCreationSuccess(types.User):
    ok: bool


@strawberry.type
class UserCreationError:
    message: str


UserCreationResult = strawberry.union(
    "UserCreationResult", (UserCreationSuccess, UserCreationError)
)


@strawberry.mutation
def create_user(user: UserCreate, info: Info) -> UserCreationResult:
    user = UserRepository.create_user(
        db=info.context["db"], email=user.email, plain_password=user.password
    )

    if user is None:
        return UserCreationError(message="User creation failed")

    return UserCreationSuccess(ok=True, id=user.id, email=user.email)
