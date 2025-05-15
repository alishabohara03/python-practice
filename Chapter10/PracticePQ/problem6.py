#6. Can you change the self parameter inside a class to something else (say "harry")? Try changing self to "slit" or "harry" and see the effect


class Example:
    def __init__(harry, name):
        harry.name = name

    def greet(harry):
        print(f"Hello {harry.name}")


# Example usage
e = Example("Ramesh")
e.greet()

