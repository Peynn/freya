import strawberry


@strawberry.field
def say_hello() -> str:
    return "Hello World"
