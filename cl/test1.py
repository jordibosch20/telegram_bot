import sys
from antlr4 import *
from SkyLexer import SkyLexer
from SkyParser import SkyParser
from TreeVisitor import TreeVisitor

while True:
	input_stream = InputStream(input('? '))
	lexer = SkyLexer(input_stream)
	token_stream = CommonTokenStream(lexer)

	parser = SkyParser(token_stream)
	tree = parser.root() 

	visitor = TreeVisitor()
	visitor.visit(tree)
#Aquest test seria on s'executaria el bot, fixem-nos que amb visitor, som capacos d'accedir
#en tot moment al diccionari. Per tant podem anar donant les respostes.
#La classse Sky tambe tindra metodes per dibuixar que es cridaran sobre el resultat des d'aqui
#de l'objecte que retorni el diccionari per cada cas