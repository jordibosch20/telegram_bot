import matplotlib.pyplot as plt
import matplotlib.patches as patches

class Skyline():
    def __init__(self, edificis = []):
        #Per defecte si no passem el parametre edificis s'inicialitzara a []
       self.edificis = edificis
       print(self.edificis)
       self.ordenar()
    
    @staticmethod
    def order_minim(x):
        return x[0]

    @staticmethod
    def order_maxim(x):
        return x[2]

    def ordenar(self):
        #Ens ordenara els edificis segons la primera component (es a dir, desquerra a dreta)
        #Guardare tambe el valor mes a la dreta per a futurs calculs
        self.edificis.sort(key = self.order_maxim, reverse = True)
        self.punt_maxim = self.edificis[0][2]
        print("el punt mes a la dreta es",self.punt_maxim)
        self.edificis.sort(key = self.order_minim)       
        self.punt_minim = self.edificis[0][0]
        print("El punt mes a l'esquerra es",self.edificis[0][0])

        #Al final ho deixa amb l'ordre ascendent ordinari

    def suma_numero(self,num):
        #Fem una translació de num
        for counter,valor in enumerate(self.edificis):
            xmin = valor[0] + num
            h = valor[1]
            xmax = valor[2] + num
            self.edificis[counter] = (xmin,h,xmax)
    
    def resta_numero(self,num):
        #Fem una translació de num
        for counter,valor in enumerate(self.edificis):
            xmin = valor[0] - num
            h = valor[1]
            xmax = valor[2] - num
            self.edificis[counter] = (xmin,h,xmax)

    def multiplicar_numero(self,num):
    #Trobar el punt minim i el punt maxim. Un cop sabem aixo, fer una translacio de la resta dels valors  
        self.ordenar()
        desplacament = self.punt_maxim - self.punt_minim

        edificis1 = self.edificis.copy()
        #Important fer el .copy() per evitar que cada cop que afegim a edificis1, safegeixi
        #tambe a edificis degut a les referencies

        for counter,valor in enumerate(self.edificis):
            for j in range(1,num):
                xmin = valor[0] + j*(desplacament)
                h = valor[1]
                xmax = valor[2] + j*(desplacament)
                edificis1.append((xmin,h,xmax))
        
        self.edificis = edificis1
        self.ordenar()

    def reflectir(self):
        #Suposem que ja ho hem ordenat
        desplacament = self.punt_maxim - self.punt_minim
        print(desplacament)
        for counter,valor in enumerate(self.edificis):
            xminfinal = valor[2] + desplacament - 2*(valor[2]-self.punt_minim)
            h = valor[1]
            xmaxfinal = valor[0] + desplacament - 2*(valor[0]-self.punt_minim)
            self.edificis[counter] = (xminfinal,h,xmaxfinal)

    def suma_skyline(self,sky_aux):
        #Rep un sky i l'afegeix al sky que ja tenim
        for i in sky_aux.edificis:
            #estem dins el vector de sky auxiliar
            self.append(i)
            #Hi ha d'haver maneres mes optimes, no?
            self.ordenar()
            #Amb aixo aconseguim O(nlogn), laltre metedo(bisect) serie O(logn)

    def solapament(self,i1,i2):
        #funcio que ens retorna si dos intervals tenen solapament
        #i1 = [a,alcada,b]
        #i2 = [c,alcada,d]
        if (not(i1[2]<=i2[0] or i2[2]<=i2[0])):
            return True
            #retorna cert si es solapen
        return False

    def interseccio_punt_rectangle(self, punt, r):
        if (punt < r[2] and punt > r[0]):
            return True
        return False

    def interseccio_skyline(self,sky_aux):
        #Interesecar es com posar les dues figures i quedarnos amb el nou sky que veuriem
        #Realitzarem una busca binaria, podriem utilitzar el modul bisect, pero l'implementarem nosatlres
        intervals_1 = sky_aux.edificis
        intervals_2 = self.edificis
        #El que fare sera ordenar el nou skyline i mirar quins es solapen
        intervals_final = intervals_2 + intervals_1
        intervals_final.sort(key=self.order_minim)
        intervals_out = []
        intervals_definitiu = []
        for i in intervals_final:
            intervals_out.append(i[0])
            intervals_out.append(i[2])
        
        intervals_out.sort() #Ara estan ordenats pero repetits

        lookup = set()  # a temporary lookup set
        intervals_out = [x for x in intervals_out if x not in lookup and lookup.add(x) is None]
        #Em desfaig de les duplicitats conservant l'ordre.

        print("INTERVAL OUT ES",intervals_out)
        #intervals_out es un set amb tots els llocs on pot canviar lalcada!
        longitud = len(intervals_out)
        for counter, value in enumerate(intervals_out):
            if (counter < longitud - 1):
                a = value
                b = intervals_out[counter+1]
                mig = float(a + b) / float(2)
                print("a i b son", a, "->",b,"i el punt mig es",mig)
        #Volem saber l'alcada del punt mig
        
        #Ho fare a lo bestia pero hi podria haver millors implementacions, utilizant que 
        #la llista esta ordenada i fent binaria
                maxim = 0
                for i in intervals_final:
                    if self.interseccio_punt_rectangle(mig,i):
                        maxim = max(maxim,i[1])
                intervals_definitiu.append((a,maxim,b))

        print("els intervals definitius son",intervals_definitiu)
        self.edificis = intervals_definitiu

    def escriu(self):
        for i in self.edificis:
            print(i)
    #en aquesta variable hi tindrem cadascun dels edificis que diguem
    def dibuixar(self):
        #We have to loop over all rectangles
        fig, ax = plt.subplots()
        for i in self.edificis:
            ax.add_patch(
                 patches.Rectangle(
                    (i[0], 0),
                    (i[2]-i[0]),
                    i[1],
                    edgecolor = 'red',
                    facecolor = 'blue',
                    fill=True
                 ) )
        ax.plot()
        plt.show()

    def area_alcada(self):
        area = 0
        alcada = 0
        for i in self.edificis:
            area += (i[2]-i[0])*(i[1])
            alcada = max(alcada,i[1])
        return area,alcada


s1 = Skyline([(0,3,1),(1,4,2)])
s1.ordenar()
s2 = Skyline([(2,5,3),(0.5,3.5,2.5)])
s1.interseccio_skyline(s2)
s1.dibuixar()
print(s1.area_alcada())