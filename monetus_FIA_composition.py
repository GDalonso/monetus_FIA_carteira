from enum import Enum

from get_quotations import get_current_quotations

"""
Enum with all the papers in the fund, used to get values
"""


class MonetusFiaComposition(Enum):
    # Values are the pct in the fund
    BIDI11 = 16.72
    NTCO3 = 16.44
    EZTC3 = 13.14
    HAPV3 = 10.57
    CVCB3 = 8.52
    UGPA3 = 7.85
    MDIA3 = 6.85
    HGTX3 = 5.08
    RAPT4 = 4.63
    GUAR3 = 3.80
    GRND3 = 2.75
    ABCB4 = 1.86
    POMO4 = 1.15
    POMO3 = 0.55
    CGRA3 = 0.09

    @classmethod
    def get_current_quotations(self):
        return get_current_quotations(enum=self)
