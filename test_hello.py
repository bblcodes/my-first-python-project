def test_hello_output():
  expected = [
    "Hello, Git!",
    "I am learning Git and GitHub.",
    "Git is starting to make sense.",
    "I am learning how developers use
    Git.",
    "My first GitHub project is coming together.",
    "I am getting better at Git.",
    ]

    with open("hello.py", "r",
    encoding="utf-8") as file:
    code = file.read()

    for message in expected:
    assert f'print("{message}")' in
    code
