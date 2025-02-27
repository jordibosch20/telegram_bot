# Generated from Sky.g by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("J\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\7")
        buf.write("\5)\n\5\f\5\16\5,\13\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t")
        buf.write("\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6\16@\n\16")
        buf.write("\r\16\16\16A\3\17\6\17E\n\17\r\17\16\17F\3\17\3\17\2\2")
        buf.write("\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\3\2\5\4\2C\\c|\3\2\62;\4\2\f\f\"\"")
        buf.write("\2M\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7#\3\2\2\2")
        buf.write("\t%\3\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63")
        buf.write("\3\2\2\2\23\65\3\2\2\2\258\3\2\2\2\27:\3\2\2\2\31<\3\2")
        buf.write("\2\2\33?\3\2\2\2\35D\3\2\2\2\37 \7-\2\2 \4\3\2\2\2!\"")
        buf.write("\7/\2\2\"\6\3\2\2\2#$\7,\2\2$\b\3\2\2\2%*\t\2\2\2&)\t")
        buf.write("\2\2\2\')\5\33\16\2(&\3\2\2\2(\'\3\2\2\2),\3\2\2\2*(\3")
        buf.write("\2\2\2*+\3\2\2\2+\n\3\2\2\2,*\3\2\2\2-.\7]\2\2.\f\3\2")
        buf.write("\2\2/\60\7_\2\2\60\16\3\2\2\2\61\62\7}\2\2\62\20\3\2\2")
        buf.write("\2\63\64\7\177\2\2\64\22\3\2\2\2\65\66\7<\2\2\66\67\7")
        buf.write("?\2\2\67\24\3\2\2\289\7*\2\29\26\3\2\2\2:;\7+\2\2;\30")
        buf.write("\3\2\2\2<=\7.\2\2=\32\3\2\2\2>@\t\3\2\2?>\3\2\2\2@A\3")
        buf.write("\2\2\2A?\3\2\2\2AB\3\2\2\2B\34\3\2\2\2CE\t\4\2\2DC\3\2")
        buf.write("\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2GH\3\2\2\2HI\b\17\2")
        buf.write("\2I\36\3\2\2\2\7\2(*AF\3\b\2\2")
        return buf.getvalue()


class SkyLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MES = 1
    MENYS = 2
    MULT = 3
    VAR = 4
    OC = 5
    TC = 6
    OB = 7
    CB = 8
    ASSIG = 9
    PO = 10
    PT = 11
    COMA = 12
    NUM = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'['", "']'", "'{'", "'}'", "':='", "'('", 
            "')'", "','" ]

    symbolicNames = [ "<INVALID>",
            "MES", "MENYS", "MULT", "VAR", "OC", "TC", "OB", "CB", "ASSIG", 
            "PO", "PT", "COMA", "NUM", "WS" ]

    ruleNames = [ "MES", "MENYS", "MULT", "VAR", "OC", "TC", "OB", "CB", 
                  "ASSIG", "PO", "PT", "COMA", "NUM", "WS" ]

    grammarFileName = "Sky.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


