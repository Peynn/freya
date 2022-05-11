import strawberry


@strawberry.type
class UserType:
    id: strawberry.ID
    email: str
