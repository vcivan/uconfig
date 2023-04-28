from __future__ import annotations

import json
from os import PathLike
from typing import Union

from .utils import (
    check_values_are_only_allowed_types,
    convert_tuples_in_dict_to_lists,
    convert_enums_in_dict_to_values,
    ALLOWED_BASE_TYPES,
    ALLOWED_CONTAINER_TYPES,
    DEFAULT_JSON_INDENT
)


class BaseConfig:
    """This is the base config class.
    
    Users should extend this class in their own code and override 
    the define_config() method to create their config variables. 
    You can see an example of this in src/uconfig/examples/example_config1.py
    """

    def __init__(self) -> None:
        self.define_config()
        self.normalize_config()
        if not check_values_are_only_allowed_types(self.__dict__.values()):
            raise ValueError(
                "One or more of the config attributes are not one of the allowed types: {}".format(
                ALLOWED_BASE_TYPES + ALLOWED_CONTAINER_TYPES
            )
            )

    def define_config(self) -> None:
        """This method should be overriden by the user to define the attributes of the cfg.
        
        This method is called in the __init__ method in order to intialize the default 
        values of the config as object attributes.
        """
        raise NotImplementedError(
            "This method needs to be implemented in order to define the config"
        )
    
    def normalize_config(self) -> None:
        """This method normalizes the config, i.e. it converts all tuples to lists.
        
        This is a design choice, because when saving and loading from json, both 
        lists and tuples are turned to lists and is impossible to know for sure 
        all of the time if a certain list was intended to be a list or a tuple by the 
        user. Therefore it's the user's job to ensure a list in the config is converted 
        to a tuple, if that is what was intended.
        """
        self.__dict__ = convert_tuples_in_dict_to_lists(self.__dict__)

    def save_config(
        self,
        save_path: Union[str, PathLike],
        indent: Union[int, str] = DEFAULT_JSON_INDENT
    ) -> None:
        """This method saves the config to a json file.
        
        Args:
            save_path: A Union[str, PathLike] object representing the save path
            indent: A Union[int, str] object representing the indent with which the 
                json should be formatted
        """
        with open(save_path, "w+") as f:
            json.dump(convert_enums_in_dict_to_values(self.__dict__), f, indent=indent)

    def load_config(self, load_path: Union[str, PathLike]) -> None:
        """This method loads the config from a json file.
        
        Args:
            save_path: A Union[str, PathLike] object representing the load path
        """
        with open(load_path, "r") as f:
            self.__dict__ = json.load(f)

    def to_simple_dict(self) -> dict:
        """The method returns the config as a dict.
        
        It also converts all Enums to raw values, i.e. an instance of 
        EnumClass(str, Enum) would be converted to its underlying str value. this method 
        can be used in case the underlying dict with base Python types is needed, e.g. 
        for compatibility with 3rd parties.

        Returns:
            A dict with only Python type representing the config.
        """
        return convert_enums_in_dict_to_values(self.__dict__)
        

    def __str__(self) -> str:
        return "{} instance: (\n{}\n)".format(
            self.__class__.__name__, 
            json.dumps(
                self.to_simple_dict(), 
                indent=DEFAULT_JSON_INDENT
            )
        )

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: BaseConfig) -> bool:
        """Overrides the '==' operator.
        
        Args:
            other: An instance of a class inheriting from BaseConfig

        Returns:
            A boolean

        Raises:
            TypeError: Occurs if other is of the wrong type
        """
        if not isinstance(other, BaseConfig):
            raise TypeError(
                "The second term of the equality comparison operation should be a child of the BaseConfig class."
            )

        return self.__dict__ == other.__dict__

    def __sub__(self, other: BaseConfig) -> dict:
        """Overrides the '-' operator.
        
        Performing a subtraction operation between two configs will create a dictionary 
        containing keys and values for which the keys are present in either self or other but not in 
        both, and will contain keys and values present in both but for which the values 
        differ.

        In the output dictionary, keys from self will have 'first.' preprended to them and 
        keys from other will have 'second.' prepended to them.

        Args:
            other: An instance of a class inheriting from BaseConfig

        Returns:
            A dict containing the differences between self and other

        Raises:
            TypeError: Occurs if other is of the wrong type
        """
        if not isinstance(other, BaseConfig):
            raise TypeError(
                "The second term of the subtraction operation should be a child of the BaseConfig class."
            )

        differences_dict = {}
        for k, v in self.__dict__.items():
            if k not in other.__dict__.keys():
                differences_dict["first." + k] = v
            elif v != other.__dict__[k]:
                differences_dict["first." + k] = v
            else:
                continue

        for k, v in other.__dict__.items():
            if k not in self.__dict__.keys():
                differences_dict["second." + k] = v
            elif v != self.__dict__[k]:
                differences_dict["second." + k] = v
            else:
                continue

        return differences_dict