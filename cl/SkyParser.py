# Generated from Sky.g by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\5\3\36\n\3\3\3\5\3!\n\3\3\4\3\4\3\4\5\4&\n\4\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\60\n\6\5\6\62\n\6\3\6")
        buf.write("\3\6\3\6\3\6\5\68\n\6\7\6:\n\6\f\6\16\6=\13\6\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\7\bE\n\b\f\b\16\bH\13\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\2\3\n\f\2")
        buf.write("\4\6\b\n\f\16\20\22\24\2\3\3\2\3\5\2`\2\26\3\2\2\2\4 ")
        buf.write("\3\2\2\2\6%\3\2\2\2\b\'\3\2\2\2\n\61\3\2\2\2\f>\3\2\2")
        buf.write("\2\16@\3\2\2\2\20K\3\2\2\2\22O\3\2\2\2\24W\3\2\2\2\26")
        buf.write("\27\5\4\3\2\27\30\7\2\2\3\30\3\3\2\2\2\31\32\7\6\2\2\32")
        buf.write("\35\7\13\2\2\33\36\5\6\4\2\34\36\5\n\6\2\35\33\3\2\2\2")
        buf.write("\35\34\3\2\2\2\36!\3\2\2\2\37!\5\n\6\2 \31\3\2\2\2 \37")
        buf.write("\3\2\2\2!\5\3\2\2\2\"&\5\f\7\2#&\5\16\b\2$&\5\20\t\2%")
        buf.write("\"\3\2\2\2%#\3\2\2\2%$\3\2\2\2&\7\3\2\2\2\'(\7\4\2\2(")
        buf.write(")\7\6\2\2)\t\3\2\2\2*+\b\6\1\2+,\7\4\2\2,\62\5\n\6\5-")
        buf.write("\60\5\6\4\2.\60\7\6\2\2/-\3\2\2\2/.\3\2\2\2\60\62\3\2")
        buf.write("\2\2\61*\3\2\2\2\61/\3\2\2\2\62;\3\2\2\2\63\64\f\4\2\2")
        buf.write("\64\67\t\2\2\2\658\7\17\2\2\668\5\n\6\2\67\65\3\2\2\2")
        buf.write("\67\66\3\2\2\28:\3\2\2\29\63\3\2\2\2:=\3\2\2\2;9\3\2\2")
        buf.write("\2;<\3\2\2\2<\13\3\2\2\2=;\3\2\2\2>?\5\22\n\2?\r\3\2\2")
        buf.write("\2@A\7\7\2\2AF\5\22\n\2BC\7\16\2\2CE\5\22\n\2DB\3\2\2")
        buf.write("\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2GI\3\2\2\2HF\3\2\2\2I")
        buf.write("J\7\b\2\2J\17\3\2\2\2KL\7\t\2\2LM\5\24\13\2MN\7\n\2\2")
        buf.write("N\21\3\2\2\2OP\7\f\2\2PQ\7\17\2\2QR\7\16\2\2RS\7\17\2")
        buf.write("\2ST\7\16\2\2TU\7\17\2\2UV\7\r\2\2V\23\3\2\2\2WX\7\17")
        buf.write("\2\2XY\7\16\2\2YZ\7\17\2\2Z[\7\16\2\2[\\\7\17\2\2\\]\7")
        buf.write("\16\2\2]^\7\17\2\2^_\7\16\2\2_`\7\17\2\2`\25\3\2\2\2\n")
        buf.write("\35 %/\61\67;F")
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
    RULE_mirall = 3
    RULE_operacio = 4
    RULE_simple = 5
    RULE_compost = 6
    RULE_aleatori = 7
    RULE_edifici = 8
    RULE_edaleatori = 9

    ruleNames =  [ "root", "skyline", "crear", "mirall", "operacio", "simple", 
                   "compost", "aleatori", "edifici", "edaleatori" ]

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
            self.state = 20
            self.skyline()
            self.state = 21
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
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(SkyParser.VAR)
                self.state = 24
                self.match(SkyParser.ASSIG)
                self.state = 27
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 25
                    self.crear()
                    pass

                elif la_ == 2:
                    self.state = 26
                    self.operacio(0)
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
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
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkyParser.PO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.simple()
                pass
            elif token in [SkyParser.OC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.compost()
                pass
            elif token in [SkyParser.OB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
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

    class MirallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MENYS(self):
            return self.getToken(SkyParser.MENYS, 0)

        def VAR(self):
            return self.getToken(SkyParser.VAR, 0)

        def getRuleIndex(self):
            return SkyParser.RULE_mirall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMirall" ):
                return visitor.visitMirall(self)
            else:
                return visitor.visitChildren(self)




    def mirall(self):

        localctx = SkyParser.MirallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mirall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(SkyParser.MENYS)
            self.state = 38
            self.match(SkyParser.VAR)
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


        def crear(self):
            return self.getTypedRuleContext(SkyParser.CrearContext,0)


        def VAR(self):
            return self.getToken(SkyParser.VAR, 0)

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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_operacio, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkyParser.MENYS]:
                self.state = 41
                self.match(SkyParser.MENYS)
                self.state = 42
                self.operacio(3)
                pass
            elif token in [SkyParser.VAR, SkyParser.OC, SkyParser.OB, SkyParser.PO]:
                self.state = 45
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [SkyParser.OC, SkyParser.OB, SkyParser.PO]:
                    self.state = 43
                    self.crear()
                    pass
                elif token in [SkyParser.VAR]:
                    self.state = 44
                    self.match(SkyParser.VAR)
                    pass
                else:
                    raise NoViableAltException(self)

                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SkyParser.OperacioContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_operacio)
                    self.state = 49
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 50
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SkyParser.MES) | (1 << SkyParser.MENYS) | (1 << SkyParser.MULT))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 53
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [SkyParser.NUM]:
                        self.state = 51
                        self.match(SkyParser.NUM)
                        pass
                    elif token in [SkyParser.MENYS, SkyParser.VAR, SkyParser.OC, SkyParser.OB, SkyParser.PO]:
                        self.state = 52
                        self.operacio(0)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_simple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
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
        self.enterRule(localctx, 12, self.RULE_compost)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(SkyParser.OC)
            self.state = 63
            self.edifici()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkyParser.COMA:
                self.state = 64
                self.match(SkyParser.COMA)
                self.state = 65
                self.edifici()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
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
        self.enterRule(localctx, 14, self.RULE_aleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SkyParser.OB)
            self.state = 74
            self.edaleatori()
            self.state = 75
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
        self.enterRule(localctx, 16, self.RULE_edifici)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(SkyParser.PO)
            self.state = 78
            self.match(SkyParser.NUM)
            self.state = 79
            self.match(SkyParser.COMA)
            self.state = 80
            self.match(SkyParser.NUM)
            self.state = 81
            self.match(SkyParser.COMA)
            self.state = 82
            self.match(SkyParser.NUM)
            self.state = 83
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
        self.enterRule(localctx, 18, self.RULE_edaleatori)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(SkyParser.NUM)
            self.state = 86
            self.match(SkyParser.COMA)
            self.state = 87
            self.match(SkyParser.NUM)
            self.state = 88
            self.match(SkyParser.COMA)
            self.state = 89
            self.match(SkyParser.NUM)
            self.state = 90
            self.match(SkyParser.COMA)
            self.state = 91
            self.match(SkyParser.NUM)
            self.state = 92
            self.match(SkyParser.COMA)
            self.state = 93
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
        self._predicates[4] = self.operacio_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def operacio_sempred(self, localctx:OperacioContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




