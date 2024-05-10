from enum import Enum

class UserData(Enum):
    data = 20
    work = "sandy"

print(UserData.data.value)