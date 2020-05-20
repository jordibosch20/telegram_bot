# Generated from Sky.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write(";\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\33")
        buf.write("\n\2\r\2\16\2\34\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\6\13\61\n\13\r\13")
        buf.write("\16\13\62\3\f\6\f\66\n\f\r\f\16\f\67\3\f\3\f\2\2\r\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\3\2\5")
        buf.write("\4\2C\\c|\3\2\62;\4\2\f\f\"\"\2=\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\3\32\3\2\2\2\5\36\3\2\2\2\7 \3\2\2\2\t\"\3\2")
        buf.write("\2\2\13$\3\2\2\2\r&\3\2\2\2\17)\3\2\2\2\21+\3\2\2\2\23")
        buf.write("-\3\2\2\2\25\60\3\2\2\2\27\65\3\2\2\2\31\33\t\2\2\2\32")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2")
        buf.write("\35\4\3\2\2\2\36\37\7]\2\2\37\6\3\2\2\2 !\7_\2\2!\b\3")
        buf.write("\2\2\2\"#\7}\2\2#\n\3\2\2\2$%\7\177\2\2%\f\3\2\2\2&\'")
        buf.write("\7<\2\2\'(\7?\2\2(\16\3\2\2\2)*\7*\2\2*\20\3\2\2\2+,\7")
        buf.write("+\2\2,\22\3\2\2\2-.\7.\2\2.\24\3\2\2\2/\61\t\3\2\2\60")
        buf.write("/\3\2\2\2\61\62\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\26\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\66\67\3\2\2\2")
        buf.write("\67\65\3\2\2\2\678\3\2\2\289\3\2\2\29:\b\f\2\2:\30\3\2")
        buf.write("\2\2\6\2\34\62\67\3\b\2\2")
        return buf.getvalue()


class SkyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    VAR = 1
    OC = 2
    TC = 3
    OB = 4
    CB = 5
    ASSIG = 6
    PO = 7
    PT = 8
    COMA = 9
    NUM = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'{'", "'}'", "':='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "OC", "TC", "OB", "CB", "ASSIG", "PO", "PT", "COMA", 
            "NUM", "WS" ]

    ruleNames = [ "VAR", "OC", "TC", "OB", "CB", "ASSIG", "PO", "PT", "COMA", 
                  "NUM", "WS" ]

    grammarFileName = "Sky.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


