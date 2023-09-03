foo = {"a": 1, "b": "Hi"}

bar = str.upper(b) if (b := foo.get("b")) else "empty"

print(bar)
