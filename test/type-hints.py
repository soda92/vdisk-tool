import re


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def process_items(item_t: tuple[int, int, str], item_s: set[bytes]):
    return item_t, item_s


def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item(item: int | str):
    print(item)


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


class Person:
    def __init__(self, name: str) -> None:
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}

user = User(**external_data)

print(user)
print(user.id)
