import strawberry
from strawberry.types import Info

from app.repositories import user as UserRepository
from app.services import authentication as AuthenticationService


@strawberry.type
class AuthenticationSuccess:
    token: str


@strawberry.type
class AuthenticationError:
    message: str


AuthenticationResult = strawberry.union(
    "AuthenticationResult", (AuthenticationSuccess, AuthenticationError)
)


@strawberry.field
def authenticate(email: str, password: str, info: Info) -> AuthenticationResult:
    user = UserRepository.authenticate(
        db=info.context["db"], email=email, plain_password=password
    )

    if user is None:
        return AuthenticationError("Password or email is wrong")

    access_token = AuthenticationService.create_access_token(data={"sub": user.email})

    if access_token is None:
        return AuthenticationError("Something went wrong")

    return AuthenticationSuccess(token=access_token)
