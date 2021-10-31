def get_greeting(name: str) -> str:
    return "Hello, " + name + "!"


if __name__ == "__main__":
    MESSAGE = get_greeting("World")
    print(MESSAGE)
