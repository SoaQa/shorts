import datetime
import time

custom_list = [
    {"a": 2},
    {"a": 1},
    {"a": 4},
    {"a": 3},
]

sorted_list = sorted(
    custom_list,
    key=lambda x: x["a"]
)
print(sorted_list)


class User:
    def __init__(
            self,
            username: str,
            email: str,
    ):
        self.username = username
        self.email = email
        self.created = datetime.datetime.now()

    def __eq__(self, other):
        assert type(self) is type(other)

        return self.username == other.username

    def __lt__(self, other):
        assert type(self) is type(other)

        return self.created < other.created

    def __repr__(self):
        return self.username


user_max = User(username="Max", email="max@m.su")
time.sleep(0.01)
user_lex = User(username="Lex", email="lex@m.su")

print(user_max == user_lex)


print(sorted([user_lex, user_max, ]))
