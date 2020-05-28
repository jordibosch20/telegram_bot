import random as rand
from Skyline import *
#Estem executant el main desde dalt per tant estem fent servir absolute path

if __name__ is not None and "." in __name__:
    from .SkyParser import SkyParser
    from .SkyVisitor import SkyVisitor
else:
    from SkyParser import SkyParser
    from SkyVisitor import SkyVisitor


class TreeVisitor(SkyVisitor):
    dict = {}
    def __init__(self):
        self.nivell = 0
        #BONA IDEA que ordenar sigui treure els edificis no necessaris!!!!

    def visitSkyline(self, ctx:SkyParser.SkylineContext):
        #la idea es que la funcio visit et retorni els edificis i els 
        #afegeixi al diccionari de la classe amb el nom de la variable parsejada

        n1 = [x.getText() for x in ctx.getChildren()]
        print(n1)
        n = [x for x in ctx.getChildren()]
        variable = n[0].getText()

       	TreeVisitor.dict[variable] = self.visitChildren(ctx)
        #En cas que sigui entrada composta tindrem una llista de llistes amb els edificis
       	#print("Escriure el meu objecte")
        #for i in TreeVisitor.dict:
        #  print(i,"->",TreeVisitor.dict[i])
        TreeVisitor.dict[variable].dibuixar()

    def visitSimple(self,ctx:SkyParser.SimpleContext):
        n = [x.getText() for x in ctx.getChildren()]
        #Mirar els fills
        return (self.visit(next(ctx.getChildren())))


    def visitOperacio(self,ctx:SkyParser.OperacioContext):
        n = [x.getText() for x in ctx.getChildren()]
        print(n)
        #EN AQUEST CAS HE DE SABER SI EL SEGUENT DE LA SUMA es una expressio o be una constant

        n = [x for x in ctx.getChildren()]
        if (len(n) == 2):
            #Vol dir que estem en el cas del mirall
            resultat = self.visit(n[1])
            resultat.ordenar()
            resultat.reflectir()
            return(resultat)

        if (len(n) == 1):
            if (hasattr(n[0],'getSymbol')):
                if ((SkyParser.symbolicNames[n[0].getSymbol().type]) == "VAR"):
                    return TreeVisitor.dict[n[0].getText()]
                    #En principi nomes hauria d'entrar en aquest cas
                else:
                    print("ERROR")
                    return int(n[0].getText())
                    #Pensar en canviar int per un convertidor a numeric qualsevol
            else:
                #en aquest cas es un del tipus "crear"
                return(self.visit(n[0]))
        else:

            if(n[1].getText() == '+'):
                if hasattr(n[2],'getSymbol'):
                    sky1 = TreeVisitor.dict[n[0].getText()]
                    #En principi ara tenim un objecte Sky
                    sky1.suma_numero(int(n[2].getText()))
                else:
                    #L'expressio de la dreta es tambe una variable->objecte Skyline
                    sky1 = TreeVisitor.dict[n[0].getText()]
                    sky2 = self.visit(n[2])
                    sky1.unio(sky2)
                return sky1

            elif(n[1].getText() == '-'):
                sky1 = TreeVisitor.dict[n[0].getText()]
                    #En principi ara tenim un objecte Sky
                sky1.resta_numero(int(n[2].getText()))

            elif(n[1].getText() == '*'):
                if hasattr(n[2],'getSymbol'):
                    sky1 = TreeVisitor.dict[n[0].getText()]
                    #En principi ara tenim un objecte Sky
                    sky1.multiplicar_numero(int(n[2].getText()))
                else:
                    #L'expressio de la dreta es tambe una variable->objecte Skyline
                    sky1 = TreeVisitor.dict[n[0].getText()]
                    sky2 = self.visit(n[2])
                    sky1.interseccio(sky2)
            return sky1

    def visitAleatori(self,ctx:SkyParser.AleatoriContext):
        n = [x for x in ctx.getChildren()]
        return  (self.visit(n[1]))
        #Ja que el fill estara al mig dels claus d'ator

    def visitCompost(self,ctx:SkyParser.CompostContext):
        #he de tornar [[compost1],[compost2],[compost3]]
        n = [x for x in ctx.getChildren()]
        n1 = [x.getText() for x in ctx.getChildren()]
        print(n1)
        resultat = Skyline([])

#Seria interessant veure que esta fallant pq necessiti la [] dins skyline

        for i in n:
            if (len(i.getText()) > 5):
                #Voldra dir que aquella expressio es un edifici
                resultat.unio(self.visit(i))
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
        return Skyline(resultats)

    def visitEdifici(self,ctx:SkyParser.EdificiContext):
        n = [x.getText() for x in ctx.getChildren()] 
        edifici_llista = (int(n[1]),int(n[3]),int(n[5]))
        return Skyline([edifici_llista])

    def escriu_diccionari(self):
        for key in TreeVisitor.dict:
            TreeVisitor.dict[key].dibuixar()