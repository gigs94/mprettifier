
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

    def truncate(self, f, n):
        '''Truncates/pads a float f to n decimal places without rounding'''
        s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d+'0'*n)[:n]])

    def _trim(self, num):
        """cut num to 1 sig digit,
           and if that digit is 0,
           cut that and the decimal too"""
        s = self.truncate(num,1)
        if s[-1:] == '0':
            s = s[:-2]
        return(s)
        
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

        return self._trim(str(self.number/divider))+modifier

