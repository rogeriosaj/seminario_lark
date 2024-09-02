# CALCULADORA BÁSICA

from lark import Lark, Transformer, v_args

calc_grammar = """
    ?start: sum
          | NAME "=" sum    -> definir variável

    ?sum: product
        | sum "+" product   -> soma
        | sum "-" product   -> subtração

    ?product: atom
        | product "*" atom  -> multiplicação
        | product "/" atom  -> divisão

    ?atom: NUMBER           -> número
         | "-" atom         -> negativo
         | NAME             -> variável
         | "(" sum ")"

    %import common.CNAME -> NAME
    %import common.NUMBER
    %import common.WS_INLINE

    %ignore WS_INLINE
"""


@v_args(inline=True)
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)


calc_parser = Lark(calc_grammar, parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse


def main():
    while True:
        try:
            s = input('> ')
        except EOFError:
            break
        print(calc(s))

if __name__ == '__main__':
    # test()
    main()