"""NanamiLan HashMap Data Type"""

# This file is a part of NanamiLang Project
# This project licensed under GNU GPL version 2
# Initially made by @jedi2light (aka Stoian Minaiev)

import functools
from .base import Base
from .nil import Nil


class HashMap(Base):
    """NanamiLang HashMap Data Type Class"""

    name: str = 'HashMap'
    _expected_type = dict
    _python_reference: dict

    def get(self, key: Base) -> Base:
        """NanamiLang HashMap, get() implementation"""

        for k, v in self.reference().items():
            if k.name == key.name:
                if k.reference() == key.reference():
                    return v
        return Nil('nil')

    def __init__(self, reference: dict) -> None:
        """NanamiLang HashMap, initialize new instance"""

        super(HashMap, self).__init__(reference=reference)

    def format(self) -> str:
        """NanamiLang HashMap, format() method implementation"""

        return '{' + f'{" ".join([f"{k.format()} {v.format()}" for k, v in self.reference().items()])}' + '}'

    def reference_as_list(self) -> list:
        """NanamiLang HashMap, reference_as_list() method implementation"""

        return functools.reduce(lambda existing, curr: existing + (curr[0], curr[1]), self.reference().items())
