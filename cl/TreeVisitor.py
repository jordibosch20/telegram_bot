import random as rand
from Skyline import *
# Estem executant el main desde dalt per tant estem fent servir absolute path

if __name__ is not None and "." in __name__:
    from .SkyParser import SkyParser
    from .SkyVisitor import SkyVisitor
else:
    from SkyParser import SkyParser
    from SkyVisitor import SkyVisitor


class TreeVisitor(SkyVisitor):
    def __init__(self, dict):
        # Rebem per parametre el diccionari del context.user_data
        self.nivell = 0
        self.dict = dict

    def visitSkyline(self, ctx: SkyParser.SkylineContext):
        # Visita la regla skyline. Afegeix els resultats (en cas d'assignació) al diccionari.

        n = [x for x in ctx.getChildren()]
        if (hasattr(n[0], 'getSymbol') and (hasattr(n[1], 'getSymbol'))):
            # Significa que estem a una assignacio
            variable = n[0].getText()
            self.dict[variable] = self.visitChildren(ctx)
            self.dict[variable].dibuixar()
        else:
            # significa que hem de dibuixar una expressio pero no assignarla a cap variable
            v1 = self.visitChildren(ctx)
            v1.dibuixar()

    def visitSimple(self, ctx: SkyParser.SimpleContext):
        # Visita regle simple.
        n = [x.getText() for x in ctx.getChildren()]
        return (self.visit(next(ctx.getChildren())))

    def visitOperacio(self, ctx: SkyParser.OperacioContext):
        # Visita regla operacio
        n = [x.getText() for x in ctx.getChildren()]
        print(n)
        # EN AQUEST CAS HE DE SABER SI EL SEGUENT DE LA SUMA es una expressio o be una constant

        n = [x for x in ctx.getChildren()]

        if (len(n) == 1):
            # Estem accedint al token VAR o be a la regla crear
            if (hasattr(n[0], 'getSymbol')):
                if ((SkyParser.symbolicNames[n[0].getSymbol().type]) == "VAR"):
                    # print("1atribut")
                    return self.dict[n[0].getText()]
                    # En principi nomes hauria d'entrar en aquest cas
                '''else:
                    print("ERROR")
                    return int(n[0].getText())
                    #Pensar en canviar int per un convertidor a numeric qualsevol'''
            else:
                # en aquest cas es un del tipus "crear"
                return(self.visit(n[0]))

        if (len(n) == 2):
            # Vol dir que estem en el cas del mirall
            if hasattr(n[1], 'getSymbol'):
                # Significa que dsps del - hi ha una variable amb TOKEN=VAR
                # Accedim a Skyline que representa el TOKEN
                sky1 = self.dict[n[1].getText()]
                sky1.ordenar()
                sky_aux = sky1.reflectir()
                return sky_aux
            else:
                # podria ser un edifici o una expressio, #COM LES PUC DISTINGIR
                resultat = self.visit(n[1])
                resultat.ordenar()
                resultat = resultat.reflectir()
                return(resultat)
        if (len(n) == 3):
            # Primer tractarem el cas dels parentesis
            if (n[0].getText() == '(' and n[2].getText() == ')'):
                # print("parentesis")
                return(self.visit(n[1]))

            if(n[1].getText() == '+'):
                if hasattr(n[2], 'getSymbol'):
                    # Estem sumant amb un numero")
                    sky1 = self.dict[n[0].getText()]
                    sky1 = sky1.suma_numero(int(n[2].getText()))
                    return sky1
                else:
                    # En aquest cas, unim dos skylines diferents
                    sky1 = self.dict[n[0].getText()]
                    sky2 = self.visit(n[2])
                    sky1 = sky1.unio_sky(sky2)
                return sky1

            elif(n[1].getText() == '-'):
                # Estarem traslladant un Skyline a l'esquerra
                sky1 = self.dict[n[0].getText()]
                sky1 = sky1.resta_numero(int(n[2].getText()))

            elif(n[1].getText() == '*'):
                if hasattr(n[2], 'getSymbol'):
                    # Estem multiplicant per un numero
                    sky_aux = self.dict[n[0].getText()]
                    sky1 = sky_aux.multiplicar_numero(int(n[2].getText()))
                else:
                    # En aquest cas intersequem dos skylines diferents
                    sky1 = self.dict[n[0].getText()]
                    sky2 = self.visit(n[2])
                    sky1 = sky1.interseccio(sky2)
            return sky1

    def visitAleatori(self, ctx: SkyParser.AleatoriContext):
        # Mirar que passa si el borrem
        n = [x for x in ctx.getChildren()]
        return (self.visit(n[1]))

    def visitCompost(self, ctx: SkyParser.CompostContext):
        # Objectiu es separar els edificis i retornar [(compost1),(compost2),(compost3)]
        n = [x for x in ctx.getChildren()]
        resultat = Skyline([])
        for i in n:
            if (len(i.getText()) > 5):
                # Voldra dir que aquella expressio es un edifici
                resultat = resultat.unio_sky(self.visit(i))
        return resultat

    def visitEdaleatori(self, ctx: SkyParser.EdaleatoriContext):
        # Generar un Skyline amb els edificis aleatoris
        n = [x.getText() for x in ctx.getChildren()]
        # print(n)
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
            # Escolleixo una posicio inicial random que se segur que compleix restriccions
            edifici = (xmin + pos_inicial_1, h_1, pos_inicial_1+xmin+w_1)
            resultats.append(edifici)
        return Skyline(resultats)

    def visitEdifici(self, ctx: SkyParser.EdificiContext):
        # Retorna un edifici
        n = [x.getText() for x in ctx.getChildren()]
        edifici_llista = (int(n[1]), int(n[3]), int(n[5]))
        if (int(n[1]) > int(n[5])):
            # Retornem Skyline buit ja que no es vàlida la combinació
            return Skyline([])
        return Skyline([edifici_llista])

    def escriu_diccionari(self):
        for key in self.dict:
            self.dict[key].dibuixar()
