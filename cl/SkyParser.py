# Generated from Sky.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\34")
        buf.write("\n\3\3\3\5\3\37\n\3\3\4\3\4\3\4\5\4$\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\5/\n\5\3\5\3\5\5\5\63\n\5\5\5")
        buf.write("\65\n\5\3\5\3\5\3\5\3\5\5\5;\n\5\7\5=\n\5\f\5\16\5@\13")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\3\7\7\7H\n\7\f\7\16\7K\13\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\2\3\b\13\2")
        buf.write("\4\6\b\n\f\16\20\22\2\3\3\2\3\5\2g\2\24\3\2\2\2\4\36\3")
        buf.write("\2\2\2\6#\3\2\2\2\b\64\3\2\2\2\nA\3\2\2\2\fC\3\2\2\2\16")
        buf.write("N\3\2\2\2\20R\3\2\2\2\22Z\3\2\2\2\24\25\5\4\3\2\25\26")
        buf.write("\7\2\2\3\26\3\3\2\2\2\27\30\7\6\2\2\30\33\7\13\2\2\31")
        buf.write("\34\5\6\4\2\32\34\5\b\5\2\33\31\3\2\2\2\33\32\3\2\2\2")
        buf.write("\34\37\3\2\2\2\35\37\5\b\5\2\36\27\3\2\2\2\36\35\3\2\2")
        buf.write("\2\37\5\3\2\2\2 $\5\n\6\2!$\5\f\7\2\"$\5\16\b\2# \3\2")
        buf.write("\2\2#!\3\2\2\2#\"\3\2\2\2$\7\3\2\2\2%&\b\5\1\2&\'\7\f")
        buf.write("\2\2\'(\5\b\5\2()\7\r\2\2)\65\3\2\2\2*.\7\4\2\2+/\7\6")
        buf.write("\2\2,/\5\6\4\2-/\5\b\5\2.+\3\2\2\2.,\3\2\2\2.-\3\2\2\2")
        buf.write("/\65\3\2\2\2\60\63\5\6\4\2\61\63\7\6\2\2\62\60\3\2\2\2")
        buf.write("\62\61\3\2\2\2\63\65\3\2\2\2\64%\3\2\2\2\64*\3\2\2\2\64")
        buf.write("\62\3\2\2\2\65>\3\2\2\2\66\67\f\4\2\2\67:\t\2\2\28;\7")
        buf.write("\17\2\29;\5\b\5\2:8\3\2\2\2:9\3\2\2\2;=\3\2\2\2<\66\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\t\3\2\2\2@>\3\2")
        buf.write("\2\2AB\5\20\t\2B\13\3\2\2\2CD\7\7\2\2DI\5\20\t\2EF\7\16")
        buf.write("\2\2FH\5\20\t\2GE\3\2\2\2HK\3\2\2\2IG\3\2\2\2IJ\3\2\2")
        buf.write("\2JL\3\2\2\2KI\3\2\2\2LM\7\b\2\2M\r\3\2\2\2NO\7\t\2\2")
        buf.write("OP\5\22\n\2PQ\7\n\2\2Q\17\3\2\2\2RS\7\f\2\2ST\7\17\2\2")
        buf.write("TU\7\16\2\2UV\7\17\2\2VW\7\16\2\2WX\7\17\2\2XY\7\r\2\2")
        buf.write("Y\21\3\2\2\2Z[\7\17\2\2[\\\7\16\2\2\\]\7\17\2\2]^\7\16")
        buf.write("\2\2^_\7\17\2\2_`\7\16\2\2`a\7\17\2\2ab\7\16\2\2bc\7\17")
        buf.write("\2\2c\23\3\2\2\2\13\33\36#.\62\64:>I")
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
    RULE_crear = 2
    RULE_operacio = 3
    RULE_simple = 4
    RULE_compost = 5
    RULE_aleatori = 6
    RULE_edifici = 7
    RULE_edaleatori = 8

    ruleNames =  [ "root", "skyline", "crear", "operacio", "simple", "compost", 
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

        def crear(self):
            return self.getTypedRuleContext(SkyParser.CrearContext,0)


        def operacio(self):
            return self.getTypedRuleContext(SkyParser.OperacioContext,0)


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
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(SkyParser.VAR)
                self.state = 22
                self.match(SkyParser.ASSIG)
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.crear()
                    pass

                elif la_ == 2:
                    self.state = 24
                    self.operacio(0)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 27
                self.operacio(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CrearContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple(self):
            return self.getTypedRuleContext(SkyParser.SimpleContext,0)


        def compost(self):
            return self.getTypedRuleContext(SkyParser.CompostContext,0)


        def aleatori(self):
            return self.getTypedRuleContext(SkyParser.AleatoriContext,0)


        def getRuleIndex(self):
            return SkyParser.RULE_crear

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrear" ):
                return visitor.visitCrear(self)
            else:
                return visitor.visitChildren(self)




    def crear(self):

        localctx = SkyParser.CrearContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_crear)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkyParser.PO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.simple()
                pass
            elif token in [SkyParser.OC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.compost()
                pass
            elif token in [SkyParser.OB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
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

    class OperacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkyParser.OperacioContext)
            else:
                return self.getTypedRuleContext(SkyParser.OperacioContext,i)


        def VAR(self):
            return self.getToken(SkyParser.VAR, 0)

        def crear(self):
            return self.getTypedRuleContext(SkyParser.CrearContext,0)


        def NUM(self):
            return self.getToken(SkyParser.NUM, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_operacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacio" ):
                return visitor.visitOperacio(self)
            else:
                return visitor.visitChildren(self)



    def operacio(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkyParser.OperacioContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_operacio, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 36
                self.match(SkyParser.PO)
                self.state = 37
                self.operacio(0)
                self.state = 38
                self.match(SkyParser.PT)
                pass

            elif la_ == 2:
                self.state = 40
                self.match(SkyParser.MENYS)
                self.state = 44
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 41
                    self.match(SkyParser.VAR)
                    pass

                elif la_ == 2:
                    self.state = 42
                    self.crear()
                    pass

                elif la_ == 3:
                    self.state = 43
                    self.operacio(0)
                    pass


                pass

            elif la_ == 3:
                self.state = 48
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SkyParser.OC, SkyParser.OB, SkyParser.PO]:
                    self.state = 46
                    self.crear()
                    pass
                elif token in [SkyParser.VAR]:
                    self.state = 47
                    self.match(SkyParser.VAR)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SkyParser.OperacioContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operacio)
                    self.state = 52
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 53
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SkyParser.MES) | (1 << SkyParser.MENYS) | (1 << SkyParser.MULT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 56
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SkyParser.NUM]:
                        self.state = 54
                        self.match(SkyParser.NUM)
                        pass
                    elif token in [SkyParser.MENYS, SkyParser.VAR, SkyParser.OC, SkyParser.OB, SkyParser.PO]:
                        self.state = 55
                        self.operacio(0)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
            self.state = 63
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
            self.state = 65
            self.match(SkyParser.OC)
            self.state = 66
            self.edifici()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkyParser.COMA:
                self.state = 67
                self.match(SkyParser.COMA)
                self.state = 68
                self.edifici()
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 74
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
            self.state = 76
            self.match(SkyParser.OB)
            self.state = 77
            self.edaleatori()
            self.state = 78
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
            self.state = 80
            self.match(SkyParser.PO)
            self.state = 81
            self.match(SkyParser.NUM)
            self.state = 82
            self.match(SkyParser.COMA)
            self.state = 83
            self.match(SkyParser.NUM)
            self.state = 84
            self.match(SkyParser.COMA)
            self.state = 85
            self.match(SkyParser.NUM)
            self.state = 86
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
            self.state = 88
            self.match(SkyParser.NUM)
            self.state = 89
            self.match(SkyParser.COMA)
            self.state = 90
            self.match(SkyParser.NUM)
            self.state = 91
            self.match(SkyParser.COMA)
            self.state = 92
            self.match(SkyParser.NUM)
            self.state = 93
            self.match(SkyParser.COMA)
            self.state = 94
            self.match(SkyParser.NUM)
            self.state = 95
            self.match(SkyParser.COMA)
            self.state = 96
            self.match(SkyParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.operacio_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operacio_sempred(self, localctx:OperacioContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




