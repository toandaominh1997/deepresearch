import argparse
import os
from typing import *
from common.logger import logger

class Flag:
    name = ""
    description = ""
    value = ""

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Flag, cls).__new__(cls)
    #     return cls.instance
    def __init__(self, name: str, description: str, value: str, arg_type: Type):
        self.name = name
        self.description = description
        self.value = value
        self.arg_type = arg_type

    def __str__(self):
        return f"{self.name}: {self.value}: {self.description}"

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

    def set_value(self, value: str):
        self.value = value
        return self

    def set_name(self, name: str):
        self.name = name
        return self

    def set_description(self, description: str):
        self.description = description
        return self
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
class FlagStore(metaclass=SingletonMeta):
    parser = argparse.ArgumentParser(
        prog="ProgramName",
        description="What the program does",
        epilog="Text at the bottom of help",
        conflict_handler='resolve'
    )
    flags: Dict[str, Flag] = {}
    def __init__(self):
        pass
    
class Flags:
    share_store: FlagStore = FlagStore()
    @classmethod
    @property
    def parser(cls):
        return cls.share_store.parser
    
    @classmethod
    @property
    def flags(cls):
        return cls.share_store.flags

    @classmethod
    def create(cls, name: str, default: Any, description: str = "Help ...") -> Flag:
        flag_type = type(default)
        try:
            if name not in cls.flags.keys():
                cls.parser.add_argument(
                    f"--{name}", default=default, help=description, type=flag_type, required=False
                )
            else:
                logger.info(f"There are an exist argument: {name}")
        except Exception as e:
            logger.error(f"Error when add_argument: {e}")
        flag = Flag(name, description, default, flag_type)
        cls.flags[name] = flag
        return flag

    @classmethod
    def parse(cls):
        
        # cls.parser.add_argument("-f", required=False)
        # args = cls.parser.parse_args()
        args, unknown = cls.parser.parse_known_args()
        logger.debug("Parsing flags", args.__dict__)
        for flag_name, flag in cls.flags.items():
            setattr(flag, "value", getattr(args, flag_name))
        return cls
    
    @classmethod
    def get_flag_value(cls, name) -> Any:
        return cls.flags[name].value if name in cls.flags else None

    @classmethod
    def __getitem__(cls, item):
        return cls.get_flag_value(item)
    @classmethod
    def get(cls, key: str, default: Optional[Any] = None):
        value = cls.get_flag_value(key)
        return default if value is None else value
    
    @classmethod
    def set(cls, key: str, value: Any):
        Flags.create(key, value)
        return cls
    @classmethod
    def getParse(cls):
        
        return cls.parser.parse_args()
    @classmethod
    def to_dict(cls):
        return  {k: cls.__getitem__(k) for k, v in cls.flags.items()}


if __name__ == "__main__":
    debug = Flags.create("debug", "Enable debug mode", False)
    Flags.create("verbose", "Enable verbose mode", True)

    args = Flags.parse()
    print("args: ", args)

    print(f"debug: {debug.value}, {Flags.get_flag_value('debug')}")
