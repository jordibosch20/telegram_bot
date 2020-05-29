import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import time


class Skyline():
    def __init__(self, edificis=[]):
        # Per defecte si no passem el parametre edificis s'inicialitzara a []
        self.edificis = edificis

    # Dues funcions estatiques que ens ajudaran a ordenar segons necessitem
    @staticmethod
    def order_minim(x):
        return x[0]

    @staticmethod
    def order_maxim(x):
        return x[2]

    def ordenar(self):
        # Deixa objecte ordenat petit a gran. També calcula punt_maxim i punt_minim
        self.edificis.sort(key=self.order_maxim, reverse=True)
        self.punt_maxim = self.edificis[0][2]
        self.edificis.sort(key=self.order_minim)
        self.punt_minim = self.edificis[0][0]

    def suma_numero(self, num):
        # Retorna un nou Skyline traslladat num unitats
        edificis1 = self.edificis.copy()
        for counter, valor in enumerate(self.edificis):
            xmin = valor[0] + num
            h = valor[1]
            xmax = valor[2] + num
            edificis1[counter] = (xmin, h, xmax)
        return Skyline(edificis1)

    def resta_numero(self, num):
        # Retorna un nou Skyline traslladat -num unitats
        edificis1 = self.edificis.copy()
        for counter, valor in enumerate(self.edificis):
            xmin = valor[0] - num
            h = valor[1]
            xmax = valor[2] - num
            edificis1[counter] = (xmin, h, xmax)
        return Skyline(edificis1)

    def multiplicar_numero(self, num):
        # Retorna Skyline replicat num vegades
        self.ordenar()
        desplacament = self.punt_maxim - self.punt_minim
        edificis1 = self.edificis.copy()
        # Important fer el .copy() per evitar que cada cop que afegim a edificis1, safegeixi
        # tambe a edificis ja que apuntarien al mateix "objecte" sino
        for counter, valor in enumerate(self.edificis):
            for j in range(1, num):
                xmin = valor[0] + j*(desplacament)
                h = valor[1]
                xmax = valor[2] + j*(desplacament)
                edificis1.append((xmin, h, xmax))

        return Skyline(edificis1)

    def reflectir(self):
        # Retorna Skyline resultat de reflectir respecte un mirall el centre l'Skyline actual

        self.ordenar()
        # Ho ordenem per tenir definit desplacament
        edificis1 = self.edificis.copy()
        desplacament = self.punt_maxim - self.punt_minim
        print(desplacament)
        for counter, valor in enumerate(self.edificis):
            xminfinal = valor[2] + desplacament - 2*(valor[2]-self.punt_minim)
            h = valor[1]
            xmaxfinal = valor[0] + desplacament - 2*(valor[0]-self.punt_minim)
            edificis1[counter] = (xminfinal, h, xmaxfinal)
        return Skyline(edificis1)

    def unio_sky(self, sky_aux):
        # Retorna Skyline unio afegint els edificis del parametre objecte al nostre objecte. No treu els solapats
        ed1 = self.edificis
        ed2 = sky_aux.edificis
        edtotal = ed1 + ed2
        return Skyline(edtotal)

    def unio(self, edtotal):
        # Retorna al parametre self.linia el conjunt d'edificis SENSE solapament
        # Ho fem utilitzant un algoritme divide and conquer
        if not edtotal:
            self.linia = []
            return self.linia
        if len(edtotal) == 1:
            self.linia = [[edtotal[0][0], edtotal[0][1]], [edtotal[0][2], 0]]
            return self.linia

        mig = len(edtotal) // 2
        esquerra = self.unio(edtotal[:mig])
        dreta = self.unio(edtotal[mig:])
        self.linia = self.merge(esquerra, dreta)
        return self.linia

    def merge(self, esquerra, dreta):
        # Ajunta dos Skylines ordenats, traient edificis solapats.

        a1, a2 = 0, 0  # alcada1 i alcada2
        i, j = 0, 0  # iteradors per a cada llista
        res = [[0, 0]]  # resultat de les parelles

        while i < len(esquerra) and j < len(dreta):
            x0 = esquerra[i][0]
            x1 = dreta[j][0]
            if x0 <= x1:
                a1 = esquerra[i][1]
                i += 1
            if x1 <= x0:
                a2 = dreta[j][1]
                j += 1
            if max(a1, a2) != res[-1][1]:
                # comprovem que el nou maxim sigui diferent de l'alcada anterior,
                # ja que sino no introduiriem cap nou "punt"
                res.append([min(x0, x1), max(a1, a2)])

        res.extend(dreta[j:])
        res.extend(esquerra[i:])
        # ja que un cop acabada la i o la j, nomes falta afegir els altres de laltre
        return res[1:]

    def intersec_rectangles(self, a1, a2):
        # Rep dos rectangles i ens diu si es solapen. En cas que es solapin ens diu quin es mes llarg
        a, b = a1[0], a1[2]
        c, d = a2[0], a2[2]
        p1 = not ((b <= c) or (d <= a))
        if (max(b, d) == b):
            # El primer es el mes llarg
            p2 = 1
        else:
            # El segon es el mes llarg
            p2 = 2
        # retorna quin acaba mes lluny tambe
        return p1, p2

    def interseccio(self, sky1):
        # Retorna un nou Skyline obtingut fent la interseccio de dos skylines
        self.ordenar()
        sky1.ordenar()
        i = 0
        j = 0
        ed0 = self.edificis
        ed1 = sky1.edificis
        print("ed0", ed0)
        print("ed1", ed1)
        # Suposem els dos ordenats
        res = []
        while (i < len(ed0) and j < len(ed1)):
            x0 = ed0[i][0]
            x1 = ed1[j][0]
            if x0 <= x1:
                p1, p2 = self.intersec_rectangles(ed0[i], ed1[j])
                if (p1):
                    res.append((max(ed0[i][0], ed1[j][0]), min(ed0[i][1], ed1[j][1]),
                                min(ed0[i][2], ed1[j][2])))
                    if (p2 == 1):
                        j += 1
                    else:
                        i += 1
                else:
                    i += 1
            else:
                p1, p2 = self.intersec_rectangles(ed0[i], ed1[j])
                if (p1):
                    res.append((max(ed0[i][0], ed1[j][0]), min(ed0[i][1], ed1[j][1]),
                                min(ed0[i][2], ed1[j][2])))
                    if (p2 == 1):
                        j += 1
                    else:
                        i += 1
                else:
                    j += 1
        return Skyline(res)

    def area_alcada(self):
        # Retorna l'area i l'alçada d'un skyline
        area = 0
        alcada = 0
        for i in self.edificis:
            area += (i[2]-i[0]) * i[1]
            alcada = max(alcada, i[1])
        return area, alcada

    def dibuixar(self):
        # Fa el plot de l'Skyline
        self.ordenar()
        self.unio(self.edificis)
        # self.linies conte l'skyline sense solapaments
        fig, ax = plt.subplots()
        area = 0
        alcada = 0
        for counter, value in enumerate(self.linia):
            if(counter < (len(self.linia)-1)):
                index = counter + 1
                ax.add_patch(
                     patches.Rectangle(
                        (value[0], 0),
                        (self.linia[index][0] - value[0]),
                        value[1],
                        edgecolor='red',
                        facecolor='red',
                        fill=True
                     ))
                area += (self.linia[index][0] - value[0])*(value[1])
                alcada = max(alcada, value[1])
        f = open('area_alcada.txt', 'w')
        f.write("area: "+str(area)+"\n"+"alçada: "+str(alcada))
        # f.write("alçada: " + str(alcada))
        f.close()
        ax.plot()
        plt.savefig('skyline.png', bbox_inches="tight")
