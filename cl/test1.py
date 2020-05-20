import sys
from antlr4 import *
from SkyLexer import SkyLexer
from SkyParser import SkyParser
from TreeVisitor import TreeVisitor

input_stream = InputStream(input('? '))
lexer = SkyLexer(input_stream)
token_stream = CommonTokenStream(lexer)

parser = SkyParser(token_stream)
tree = parser.root() 

visitor = TreeVisitor()
visitor.visit(tree)
