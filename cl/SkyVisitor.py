# Generated from Sky.g by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkyParser import SkyParser
else:
    from SkyParser import SkyParser

# This class defines a complete generic visitor for a parse tree produced by SkyParser.

class SkyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkyParser#root.
    def visitRoot(self, ctx:SkyParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#skyline.
    def visitSkyline(self, ctx:SkyParser.SkylineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#simple.
    def visitSimple(self, ctx:SkyParser.SimpleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#compost.
    def visitCompost(self, ctx:SkyParser.CompostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#aleatori.
    def visitAleatori(self, ctx:SkyParser.AleatoriContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#edifici.
    def visitEdifici(self, ctx:SkyParser.EdificiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkyParser#edaleatori.
    def visitEdaleatori(self, ctx:SkyParser.EdaleatoriContext):
        return self.visitChildren(ctx)



del SkyParser