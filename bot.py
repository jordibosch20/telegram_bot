import sys
from antlr4 import *
from cl.SkyLexer import SkyLexer
from cl.SkyParser import SkyParser
from cl.TreeVisitor import TreeVisitor

while True:
	input_stream = InputStream(input('? '))
	lexer = SkyLexer(input_stream)
	token_stream = CommonTokenStream(lexer)

	parser = SkyParser(token_stream)
	tree = parser.root() 
	print(tree.toStringTree(recog=parser))

	visitor = TreeVisitor()
	visitor.visit(tree)
	#suposem que els retorna un objecte de la classe skyline
	

	#Detallar lo de absolute path -> en el docs
