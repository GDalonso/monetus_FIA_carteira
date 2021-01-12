from enum import Enum


class mock_MonetusFiaComposition(Enum):
    """
    Test with only one paper due to the request limit
    """

    BIDI11 = 16.72

    @classmethod
    def get_current_quotations(self):
        from get_quotations import get_current_quotations

        return get_current_quotations(enum=self)
