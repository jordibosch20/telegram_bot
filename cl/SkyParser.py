# Generated from Sky.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\31\n\3\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\7\5!\n\5\f\5\16\5$\13\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16")
        buf.write("\2\2\29\2\20\3\2\2\2\4\23\3\2\2\2\6\32\3\2\2\2\b\34\3")
        buf.write("\2\2\2\n\'\3\2\2\2\f+\3\2\2\2\16\63\3\2\2\2\20\21\5\4")
        buf.write("\3\2\21\22\7\2\2\3\22\3\3\2\2\2\23\24\7\3\2\2\24\30\7")
        buf.write("\b\2\2\25\31\5\6\4\2\26\31\5\b\5\2\27\31\5\n\6\2\30\25")
        buf.write("\3\2\2\2\30\26\3\2\2\2\30\27\3\2\2\2\31\5\3\2\2\2\32\33")
        buf.write("\5\f\7\2\33\7\3\2\2\2\34\35\7\4\2\2\35\"\5\f\7\2\36\37")
        buf.write("\7\13\2\2\37!\5\f\7\2 \36\3\2\2\2!$\3\2\2\2\" \3\2\2\2")
        buf.write("\"#\3\2\2\2#%\3\2\2\2$\"\3\2\2\2%&\7\5\2\2&\t\3\2\2\2")
        buf.write("\'(\7\6\2\2()\5\16\b\2)*\7\7\2\2*\13\3\2\2\2+,\7\t\2\2")
        buf.write(",-\7\f\2\2-.\7\13\2\2./\7\f\2\2/\60\7\13\2\2\60\61\7\f")
        buf.write("\2\2\61\62\7\n\2\2\62\r\3\2\2\2\63\64\7\f\2\2\64\65\7")
        buf.write("\13\2\2\65\66\7\f\2\2\66\67\7\13\2\2\678\7\f\2\289\7\13")
        buf.write("\2\29:\7\f\2\2:;\7\13\2\2;<\7\f\2\2<\17\3\2\2\2\4\30\"")
        return buf.getvalue()


class SkyParser ( Parser ):

    grammarFileName = "Sky.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'['", "']'", "'{'", "'}'", 
                     "':='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "VAR", "OC", "TC", "OB", "CB", "ASSIG", 
                      "PO", "PT", "COMA", "NUM", "WS" ]

    RULE_root = 0
    RULE_skyline = 1
    RULE_simple = 2
    RULE_compost = 3
    RULE_aleatori = 4
    RULE_edifici = 5
    RULE_edaleatori = 6

    ruleNames =  [ "root", "skyline", "simple", "compost", "aleatori", "edifici", 
                   "edaleatori" ]

    EOF = Token.EOF
    VAR=1
    OC=2
    TC=3
    OB=4
    CB=5
    ASSIG=6
    PO=7
    PT=8
    COMA=9
    NUM=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skyline(self):
            return self.getTypedRuleContext(SkyParser.SkylineContext,0)


        def EOF(self):
            return self.getToken(SkyParser.EOF, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkyParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.skyline()
            self.state = 15
            self.match(SkyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SkylineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SkyParser.VAR, 0)

        def ASSIG(self):
            return self.getToken(SkyParser.ASSIG, 0)

        def simple(self):
            return self.getTypedRuleContext(SkyParser.SimpleContext,0)


        def compost(self):
            return self.getTypedRuleContext(SkyParser.CompostContext,0)


        def aleatori(self):
            return self.getTypedRuleContext(SkyParser.AleatoriContext,0)


        def getRuleIndex(self):
            return SkyParser.RULE_skyline

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkyline" ):
                return visitor.visitSkyline(self)
            else:
                return visitor.visitChildren(self)




    def skyline(self):

        localctx = SkyParser.SkylineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_skyline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(SkyParser.VAR)
            self.state = 18
            self.match(SkyParser.ASSIG)
            self.state = 22
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkyParser.PO]:
                self.state = 19
                self.simple()
                pass
            elif token in [SkyParser.OC]:
                self.state = 20
                self.compost()
                pass
            elif token in [SkyParser.OB]:
                self.state = 21
                self.aleatori()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SimpleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edifici(self):
            return self.getTypedRuleContext(SkyParser.EdificiContext,0)


        def getRuleIndex(self):
            return SkyParser.RULE_simple

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple" ):
                return visitor.visitSimple(self)
            else:
                return visitor.visitChildren(self)




    def simple(self):

        localctx = SkyParser.SimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.edifici()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompostContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OC(self):
            return self.getToken(SkyParser.OC, 0)

        def edifici(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkyParser.EdificiContext)
            else:
                return self.getTypedRuleContext(SkyParser.EdificiContext,i)


        def TC(self):
            return self.getToken(SkyParser.TC, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkyParser.COMA)
            else:
                return self.getToken(SkyParser.COMA, i)

        def getRuleIndex(self):
            return SkyParser.RULE_compost

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompost" ):
                return visitor.visitCompost(self)
            else:
                return visitor.visitChildren(self)




    def compost(self):

        localctx = SkyParser.CompostContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_compost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(SkyParser.OC)
            self.state = 27
            self.edifici()
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkyParser.COMA:
                self.state = 28
                self.match(SkyParser.COMA)
                self.state = 29
                self.edifici()
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(SkyParser.TC)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AleatoriContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OB(self):
            return self.getToken(SkyParser.OB, 0)

        def edaleatori(self):
            return self.getTypedRuleContext(SkyParser.EdaleatoriContext,0)


        def CB(self):
            return self.getToken(SkyParser.CB, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_aleatori

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAleatori" ):
                return visitor.visitAleatori(self)
            else:
                return visitor.visitChildren(self)




    def aleatori(self):

        localctx = SkyParser.AleatoriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(SkyParser.OB)
            self.state = 38
            self.edaleatori()
            self.state = 39
            self.match(SkyParser.CB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdificiContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PO(self):
            return self.getToken(SkyParser.PO, 0)

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkyParser.NUM)
            else:
                return self.getToken(SkyParser.NUM, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkyParser.COMA)
            else:
                return self.getToken(SkyParser.COMA, i)

        def PT(self):
            return self.getToken(SkyParser.PT, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_edifici

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdifici" ):
                return visitor.visitEdifici(self)
            else:
                return visitor.visitChildren(self)




    def edifici(self):

        localctx = SkyParser.EdificiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SkyParser.PO)
            self.state = 42
            self.match(SkyParser.NUM)
            self.state = 43
            self.match(SkyParser.COMA)
            self.state = 44
            self.match(SkyParser.NUM)
            self.state = 45
            self.match(SkyParser.COMA)
            self.state = 46
            self.match(SkyParser.NUM)
            self.state = 47
            self.match(SkyParser.PT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdaleatoriContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkyParser.NUM)
            else:
                return self.getToken(SkyParser.NUM, i)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(SkyParser.COMA)
            else:
                return self.getToken(SkyParser.COMA, i)

        def getRuleIndex(self):
            return SkyParser.RULE_edaleatori

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEdaleatori" ):
                return visitor.visitEdaleatori(self)
            else:
                return visitor.visitChildren(self)




    def edaleatori(self):

        localctx = SkyParser.EdaleatoriContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_edaleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SkyParser.NUM)
            self.state = 50
            self.match(SkyParser.COMA)
            self.state = 51
            self.match(SkyParser.NUM)
            self.state = 52
            self.match(SkyParser.COMA)
            self.state = 53
            self.match(SkyParser.NUM)
            self.state = 54
            self.match(SkyParser.COMA)
            self.state = 55
            self.match(SkyParser.NUM)
            self.state = 56
            self.match(SkyParser.COMA)
            self.state = 57
            self.match(SkyParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





