
from typing import List, Optional
from datetime import datetime


class User():
    id: int
    name = "xiaoming"
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    "id": 123,
    "signup_ts": "2019-06-01 12:22",
    "friends": [1, 2, "3"]
}

user = User(**external_data)
print(user.id)
print(user.signup_ts)
print(user.friends)
print(user.name)