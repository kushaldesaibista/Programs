import operator


class ComputeDigitClass:
    def compute_digits(self, opt, val1=10, val2=20):
        ops = {'>': operator.gt,
               '<': operator.lt,
               '>=': operator.ge,
               '<=': operator.le,
               '==': operator.eq,
               '+': operator.add,
               '-': operator.sub,
               '*': operator.mul,
               '/': operator.floordiv,
               }
        return ops[opt](val1, val2)


v = input('var:')
if v == '+':
    print(ComputeDigitClass().compute_digits('+'))
if v == '-':
    print(ComputeDigitClass().compute_digits('-'))

