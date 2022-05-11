import strawberry


@strawberry.field
def say_hello(self) -> str:
    return "Hello World"
