# AMBIGUIDADE

import sys
from lark import Lark, tree

grammar = """
    sentence: "The" noun verb adj "to" verb    -> simples
            | "The" noun verb adj "to" noun    -> comparative

    noun: adj? NOUN
    verb: VERB
    adj: ADJ

    NOUN: "chicken" | "eat"
    VERB: "is" | "eat"
    ADJ: "ready"

    %import common.WS
    %ignore WS
"""

parser = Lark(grammar, start='sentence', ambiguity='explicit')

sentence = 'The chicken is ready to eat'

if __name__ == '__main__':
    print(parser.parse(sentence).pretty())