from enum import Enum


class mock_MonetusFiaComposition(Enum):
    """
    Test with only one paper due to the request limit
    """

    BIDI11 = 16.72

    @classmethod
    def get_current_quotations(self):
        from get_variation_pct import get_current_variations

        return get_current_variations(enum=self)
