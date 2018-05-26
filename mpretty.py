
class mpretty:
    """turn numbers into easy to read abbreviations"""

    def __init__(self, number):
        """Return a mprettifier object and set number to number"""
        self.number = self._num(number)
        self.prettier_number = self._prettify()

    def __repr__(self):
        return self.prettier_number

    def number(self):
        return self.number

    def pretty_number(self):
        return self.prettier_number 

    def _num(self,s):
        try:
            return int(s)
        except ValueError:
            return float(s)

    def _prettify(self):
        """convert number to pretty form"""
        modifier = ""
        divider = 1
        if self.number < 1000000:
            # no changes
            pass
        elif self.number < 1000000000:
            # millions changes
            modifier = "M"
            divider = 1000000
        elif self.number < 1000000000000:
            # billions changes
            modifier = "B"
            divider = 1000000000
        else:
            # trillions changes
            modifier = "T"
            divider = 1000000000000

        return str(self.number/divider)+modifier

