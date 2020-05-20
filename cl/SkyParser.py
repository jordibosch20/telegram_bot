# Generated from Sky.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("M\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\35\n\3\3\3\5\3 \n\3\3\4\3\4\3\4\3\4\5\4&\n\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7\60\n\7\f\7\16\7\63\13\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\2\2\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\3\3\2\3\5\2H\2\24\3\2\2\2\4\27")
        buf.write("\3\2\2\2\6!\3\2\2\2\b\'\3\2\2\2\n)\3\2\2\2\f+\3\2\2\2")
        buf.write("\16\66\3\2\2\2\20:\3\2\2\2\22B\3\2\2\2\24\25\5\4\3\2\25")
        buf.write("\26\7\2\2\3\26\3\3\2\2\2\27\30\7\6\2\2\30\37\7\13\2\2")
        buf.write("\31\35\5\n\6\2\32\35\5\f\7\2\33\35\5\16\b\2\34\31\3\2")
        buf.write("\2\2\34\32\3\2\2\2\34\33\3\2\2\2\35 \3\2\2\2\36 \5\6\4")
        buf.write("\2\37\34\3\2\2\2\37\36\3\2\2\2 \5\3\2\2\2!\"\7\6\2\2\"")
        buf.write("%\t\2\2\2#&\5\b\5\2$&\7\17\2\2%#\3\2\2\2%$\3\2\2\2&\7")
        buf.write("\3\2\2\2\'(\7\6\2\2(\t\3\2\2\2)*\5\20\t\2*\13\3\2\2\2")
        buf.write("+,\7\7\2\2,\61\5\20\t\2-.\7\16\2\2.\60\5\20\t\2/-\3\2")
        buf.write("\2\2\60\63\3\2\2\2\61/\3\2\2\2\61\62\3\2\2\2\62\64\3\2")
        buf.write("\2\2\63\61\3\2\2\2\64\65\7\b\2\2\65\r\3\2\2\2\66\67\7")
        buf.write("\t\2\2\678\5\22\n\289\7\n\2\29\17\3\2\2\2:;\7\f\2\2;<")
        buf.write("\7\17\2\2<=\7\16\2\2=>\7\17\2\2>?\7\16\2\2?@\7\17\2\2")
        buf.write("@A\7\r\2\2A\21\3\2\2\2BC\7\17\2\2CD\7\16\2\2DE\7\17\2")
        buf.write("\2EF\7\16\2\2FG\7\17\2\2GH\7\16\2\2HI\7\17\2\2IJ\7\16")
        buf.write("\2\2JK\7\17\2\2K\23\3\2\2\2\6\34\37%\61")
        return buf.getvalue()


class SkyParser ( Parser ):

    grammarFileName = "Sky.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "<INVALID>", "'['", 
                     "']'", "'{'", "'}'", "':='", "'('", "')'", "','" ]

    symbolicNames = [ "<INVALID>", "MES", "MENYS", "MULT", "VAR", "OC", 
                      "TC", "OB", "CB", "ASSIG", "PO", "PT", "COMA", "NUM", 
                      "WS" ]

    RULE_root = 0
    RULE_skyline = 1
    RULE_operacio = 2
    RULE_var = 3
    RULE_simple = 4
    RULE_compost = 5
    RULE_aleatori = 6
    RULE_edifici = 7
    RULE_edaleatori = 8

    ruleNames =  [ "root", "skyline", "operacio", "var", "simple", "compost", 
                   "aleatori", "edifici", "edaleatori" ]

    EOF = Token.EOF
    MES=1
    MENYS=2
    MULT=3
    VAR=4
    OC=5
    TC=6
    OB=7
    CB=8
    ASSIG=9
    PO=10
    PT=11
    COMA=12
    NUM=13
    WS=14

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
            self.state = 18
            self.skyline()
            self.state = 19
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

        def operacio(self):
            return self.getTypedRuleContext(SkyParser.OperacioContext,0)


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
            self.state = 21
            self.match(SkyParser.VAR)
            self.state = 22
            self.match(SkyParser.ASSIG)
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkyParser.OC, SkyParser.OB, SkyParser.PO]:
                self.state = 26
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SkyParser.PO]:
                    self.state = 23
                    self.simple()
                    pass
                elif token in [SkyParser.OC]:
                    self.state = 24
                    self.compost()
                    pass
                elif token in [SkyParser.OB]:
                    self.state = 25
                    self.aleatori()
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            elif token in [SkyParser.VAR]:
                self.state = 28
                self.operacio()
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

    class OperacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SkyParser.VAR, 0)

        def MES(self):
            return self.getToken(SkyParser.MES, 0)

        def MENYS(self):
            return self.getToken(SkyParser.MENYS, 0)

        def MULT(self):
            return self.getToken(SkyParser.MULT, 0)

        def var(self):
            return self.getTypedRuleContext(SkyParser.VarContext,0)


        def NUM(self):
            return self.getToken(SkyParser.NUM, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_operacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacio" ):
                return visitor.visitOperacio(self)
            else:
                return visitor.visitChildren(self)




    def operacio(self):

        localctx = SkyParser.OperacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operacio)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(SkyParser.VAR)
            self.state = 32
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SkyParser.MES) | (1 << SkyParser.MENYS) | (1 << SkyParser.MULT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkyParser.VAR]:
                self.state = 33
                self.var()
                pass
            elif token in [SkyParser.NUM]:
                self.state = 34
                self.match(SkyParser.NUM)
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

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(SkyParser.VAR, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_var

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = SkyParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(SkyParser.VAR)
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
        self.enterRule(localctx, 8, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
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
        self.enterRule(localctx, 10, self.RULE_compost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(SkyParser.OC)
            self.state = 42
            self.edifici()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkyParser.COMA:
                self.state = 43
                self.match(SkyParser.COMA)
                self.state = 44
                self.edifici()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
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
        self.enterRule(localctx, 12, self.RULE_aleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(SkyParser.OB)
            self.state = 53
            self.edaleatori()
            self.state = 54
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
        self.enterRule(localctx, 14, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(SkyParser.PO)
            self.state = 57
            self.match(SkyParser.NUM)
            self.state = 58
            self.match(SkyParser.COMA)
            self.state = 59
            self.match(SkyParser.NUM)
            self.state = 60
            self.match(SkyParser.COMA)
            self.state = 61
            self.match(SkyParser.NUM)
            self.state = 62
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
        self.enterRule(localctx, 16, self.RULE_edaleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(SkyParser.NUM)
            self.state = 65
            self.match(SkyParser.COMA)
            self.state = 66
            self.match(SkyParser.NUM)
            self.state = 67
            self.match(SkyParser.COMA)
            self.state = 68
            self.match(SkyParser.NUM)
            self.state = 69
            self.match(SkyParser.COMA)
            self.state = 70
            self.match(SkyParser.NUM)
            self.state = 71
            self.match(SkyParser.COMA)
            self.state = 72
            self.match(SkyParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





