#!/usr/bin/env python


class mpretty:
    """turn numbers into easy to read abbreviations"""

    def __init__(self, number):
        """Return a mprettifier object and set number to number"""
        self.number = number
        self.mod_table = [
            { "length":6, 'modifier':'M'},
            { "length":9, 'modifier':'B'},
            { "length":12, 'modifier':'T'},
          ]
        self.prettier_number = self._prettify()

    def __repr__(self):
        return self.prettier_number

    def number(self):
        return self.number

    def pretty_number(self):
        return self.prettier_number 

    def truncate(self, f, n):
        '''Truncates/pads a float f to n decimal places without rounding'''
        #s = '{}'.format(f)
        if 'e' in s or 'E' in s:
            return '{0:.{1}f}'.format(f, n)
        i, p, d = s.partition('.')
        return '.'.join([i, (d+'0'*n)[:n]])

    def _find_bucket(self, s):
        max_length = 0
        modifier=''
        lens = len(s)
        for i in self.mod_table:
            if lens >= i['length'] and i['length'] > max_length:
                modifier = i['modifier']
                max_length = i['length']
        return modifier, max_length

    def _trim(self, num):
        """cut num to 1 sig digit,
           and if that digit is 0,
           cut that and the decimal too"""
        s = self.truncate(num,1)
        if s[-1:] == '0':
            s = s[:-2]
        return(s)
        
    def _split_num(self):
        s = '{}'.format(self.number)
        return s.partition('.')

    def _shift_decimal(self, num, lens):
        num2 = num[:-lens]
        decimal = num[-lens:-(lens-1)]
        return (num2, decimal)

    def _prettify(self):
        """convert number to pretty form"""
        (s,_,d) = self._split_num()
        (mod,lens) = self._find_bucket(s)
        if lens != 0:
            (num,decimal) = self._shift_decimal(s,lens)
        else:
            num = s
            decimal = d[:1]

        if decimal != "0" and decimal != '':
            number = num+'.'+decimal
        else:
            number = num

        return number+mod


if __name__ == '__main__':
    import argparse
    
    def parse_command_line():
        parser = argparse.ArgumentParser(
            description='Prettifier for numbers')
        parser.add_argument(
            'number', help='number to parse')
        args = parser.parse_args()
        return args

    args = parse_command_line()

    print(mpretty(args.number))
