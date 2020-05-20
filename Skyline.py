class Skyline():
    def __init__(self, edificis = []):
        #Per defecte si no passem el parametre edificis s'inicialitzara a []
       self.edificis = edificis
       print(self.edificis)
    
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


    def escriu(self):
        for i in self.edificis:
            print(i)
    #en aquesta variable hi tindrem cadascun dels edificis que diguem

s1 = Skyline([(1,2,12),(3,4,10)])
s1.multiplicar_numero(3)
s1.escriu()