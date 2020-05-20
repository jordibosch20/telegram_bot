import random as rand
if __name__ is not None and "." in __name__:
    from .SkyParser import SkyParser
    from .SkyVisitor import SkyVisitor
else:
    from SkyParser import SkyParser
    from SkyVisitor import SkyVisitor


class TreeVisitor(SkyVisitor):
    def __init__(self):
        self.nivell = 0
        self.dict = {}

    def visitSkyline(self, ctx:SkyParser.SkylineContext):
        #la idea es que la funcio visit et retorni els edificis i els 
        #afegeixi al diccionari de la classe amb el nom de la variable parsejada

        n = [x for x in ctx.getChildren()]
        a = n[0].getText()
        print("La variables es",a)
       	#Nom de la variable
        #Check how many buildings are entered

       	self.dict[a] = self.visitChildren(ctx)
        #En cas que sigui entrada composta tindrem una llista de llistes amb els edificis
       	for i in self.dict:
       	    print(i,"->",self.dict[i])


        #Si aqui fes un return -> tornaria el resultat a test1.py no?

    def visitSimple(self,ctx:SkyParser.SimpleContext):
        n = [x for x in ctx.getChildren()]
        print(n)
        return (self.visit(next(ctx.getChildren())))

    def visitOperacio(self,ctx:SkyParser.OperacioContext):
        print("holaaa")
        n = [x.getText() for x in ctx.getChildren()]
        print(n)
        n = [x for x in ctx.getChildren()]
        '''if hasattr(n[2],'getSymbol'):
            #Significa que estem sumant numero
            self.dict[n[0].getText()]
            #suposem que ja esta guardat al dict com a objecte de la classe Sky
            #llavors jo el que faria, seria que aquesta classe tingues un metode sumardistancia,
            #restar distancia, multiplicardistancia, sumarsky, multiplicarsky i aixi dons calculem
            #la suma aqui i guardem l'objecte resultant en el diccionari
        else:'''


    def visitAleatori(self,ctx:SkyParser.AleatoriContext):
        n = [x for x in ctx.getChildren()]
        return (self.visit(n[1]))
        #Ja que el fill estara al mig dels claus d'ator

    def visitCompost(self,ctx:SkyParser.CompostContext):
        #he de tornar [[compost1],[compost2],[compost3]]
        n = [x for x in ctx.getChildren()]
        resultat = []
        for i in n:
            if (len(i.getText()) > 5):
                #Voldra dir que aquella expressio es un edifici
                resultat += self.visit(i)
        return resultat

    def visitEdaleatori(self, ctx:SkyParser.EdaleatoriContext):
        #Aqui he de generar totes les figures aleatories
        n = [x.getText() for x in ctx.getChildren()]
        print(n)
        num_ed = int(n[0])
        h = int(n[2])
        w = int(n[4])
        xmin = int(n[6])
        xmax = int(n[8])
        resultats = []
        for i in range(num_ed):
            h_1 = h*rand.random()
            w_1 = w*rand.random()
            pos_inicial_1 = (xmax-xmin-w)*(rand.random())
            #Escolleixo una posicio inicial random que se segur que compleix restriccions
            edifici = (xmin + pos_inicial_1,h_1,pos_inicial_1+xmin+w_1)
            resultats.append(edifici)
        return resultats

    def visitEdifici(self,ctx:SkyParser.EdificiContext):
        n = [x.getText() for x in ctx.getChildren()] 
        edifici_llista = (int(n[1]),int(n[3]),int(n[5]))
        return [edifici_llista]