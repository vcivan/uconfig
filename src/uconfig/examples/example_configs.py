from enum import Enum
from uconfig import BaseConfig


class UserTypes(str, Enum):
    CLIENT = "client"
    VENDOR = "vendor"


class AppId(int, Enum):
    CLIENT_APP = 0
    VENDOR_APP = 1


class ExampleConfig1(BaseConfig):
    def define_config(self) -> None:
        self.dictionary = {
            "a": 1234,
            "b": "some random string",
            "c": [1, 2, 3, 4],
            "d": {
                "a": [1.1, 2.2, 3.3, UserTypes.VENDOR],
                "b": "another random string"
            },
            "e": True,
            "f": None,
            "g": AppId.VENDOR_APP,
            "h": [[1, 2], [3, 4]]
        }
        self.list = ["a", "bc", "def", AppId.CLIENT_APP]
        self.bool = False
        self.int = 6
        self.float = 7.6
        self.str = "a third random strin"
        self.enum = UserTypes.CLIENT


class ExampleConfig2(BaseConfig):
    def define_config(self) -> None:
        self.dictionary = {
            "a": 1234,
            "b": "some random string",
            "c": [1, 2, 3, 4],
            "d": {
                "a": (1.1, 2.2, 3.3, UserTypes.VENDOR),
                "b": "another random string"
            },
            "e": True,
            "f": None,
            "g": AppId.VENDOR_APP,
            "h": [[1, 2], [3, 4]]
        }
        self.list = ("a", "bc", "def", AppId.CLIENT_APP)
        self.bool = False
        self.int = 6
        self.float = 7.6
        self.str = "a third random strin"
        self.enum = UserTypes.CLIENT


class ExampleConfig3(BaseConfig):
    def define_config(self) -> None:
        self.dictionary = {
            "a": 1234,
            "b": "some random string",
            "c": [1, 2, 3, 4],
            "d": {
                "a": [1.1, 2.2, 3.3, UserTypes.VENDOR],
                "b": "another random string"
            },
            "e": True,
            "f": None,
            "g": AppId.VENDOR_APP,
            "h": [[1, 2], [3, 4]],
            "i": [[1, 2], [3, 4]],
            "j": [[1, 2], [3, 4]]
        }
        self.list = ["a", "bc", "def", AppId.CLIENT_APP]
        self.bool = False
        self.int = 6
        self.float = 7.6
        self.str = "a third random strin"
        self.enum = UserTypes.CLIENT


class ExampleConfig4(BaseConfig):
    def define_config(self) -> None:
        self.dictionary = {
            "a": 1234,
            "b": "some random string",
            "c": (1, 2, 3, 4),
            "d": {
                "a": [1.1, 2.2, 3.3, UserTypes.VENDOR],
                "b": "another random string"
            },
            "e": True,
            "f": None,
            "g": AppId.VENDOR_APP,
            "h": [(1, 2), [3, 4]],
            "i": ([1, 2], [3, 4]),
            "j": ([1, 2], (3, 4))
        }
        self.list = ["a", "bc", "def", AppId.CLIENT_APP]
        self.bool = False
        self.int = 6
        self.float = 7.6
        self.str = "a third random strin"
        self.enum = UserTypes.CLIENT


class ExampleConfig5(BaseConfig):
    def define_config(self) -> None:
        self.int = 5
        self.dict = {
            "a": "a",
            "b": "b"
        }
        self.float = 4.7
        self.str = "some string"
        self.bool = True
        self.list = [UserTypes.CLIENT, AppId.CLIENT_APP]
        self.tuple = (1, 2, "b", False)


class ExampleConfig6(BaseConfig):
    def define_config(self) -> None:
        self.int = 3
        self.dict = {
            "a": "a",
            "b": "b"
        }
        self.float = 4.7
        self.str = "some strings"
        self.bool = False
        self.list = [UserTypes.CLIENT, AppId.VENDOR_APP]