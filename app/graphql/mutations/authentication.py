import strawberry


@strawberry.type
class AuthenticationSuccess:
    user: str


@strawberry.type
class AuthenticationError:
    message: str


AuthenticationResult = strawberry.union(
    "AuthenticationResult", (AuthenticationSuccess, AuthenticationError)
)


@strawberry.field
def authenticate(self, username: str, password: str) -> AuthenticationResult:
    user = "bleh" if password == "yolo" else None

    if user is None:
        return AuthenticationError("Something went wrong")

    return AuthenticationSuccess(user=user)
