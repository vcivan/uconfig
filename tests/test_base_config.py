from uconfig.examples.example_configs import (
    ExampleConfig1, ExampleConfig2, ExampleConfig5, ExampleConfig6, UserTypes, AppId
)


def test_init():
    assert ExampleConfig1().__dict__ == ExampleConfig2().__dict__


def test_eq():
    assert ExampleConfig1() == ExampleConfig1()


def test_sub1():
    assert ExampleConfig5() - ExampleConfig6() == {
        "first.int": 5,
        "first.str": "some string",
        "first.bool": True,
        "first.list": [UserTypes.CLIENT, AppId.CLIENT_APP],
        "first.tuple": [1, 2, "b", False],
        "second.int": 3,
        "second.str": "some strings",
        "second.bool": False,
        "second.list": [UserTypes.CLIENT, AppId.VENDOR_APP]
    }


def test_save_load():
    config = ExampleConfig1()
    config_to_save_and_load = ExampleConfig1()

    config_to_save_and_load.save_config("./ExampleConfig1.json")
    config_to_save_and_load.load_config("./ExampleConfig1.json")

    assert config == config_to_save_and_load