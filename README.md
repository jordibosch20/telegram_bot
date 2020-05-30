# SkyLine Telegram bot
## Introducció
---
Utilitzant la API de Telegram per Python hem programat un bot de Telegram capaç de representar Skylines i realitzar operacions amb aquests.

## Funcionament
---
La idea és que som capaços de definir un llenguatge que actuarà sobre diferents Skylines.
Per exemple, __a := (1,2,3)__ representa l'edifici que comença a __x = 1__, acaba a __x = 3__ i té alçada 2. 
Tenim altres maneres de definir Skylines. Si volem definir un Skyline amb molts edificis a dins adoptarem la seguent sintaxi:
__a := [edifici1,edifici2,...]__
Si volem inicialitzar aleatòriament un Skyline amb n edificis on cadascun pot tenir una alçada entre 0 i h, i una amplada entre 0 i w, entre xmin i xmax ho podem fer amb la comanda {n, h, w, xmin, xmax}
A aquest edifici li podem aplicar certes operacions que poden ser:
- __skyline + skyline__ : Aquest operador rep dos Skylines, els superposa i retorna el nou Skyline
-  __skyline + NUM__ : Traslladem un Skyline NUM unitats a la dreta
-  __skyline - NUM__ : Traslladem un Skyline NUM unitats a l'esquerra
-  __skyline * NUM__ : Repliquem l'Skyline NUM vegades
-  __skyline * skyline__ :
-  __-skyline__:  Reflectim l'Skyline amb un mirall respecte el seu centre
L'objectiu és que l'usuari sigui capaç d'anar realitzant les operacions que vulgui i el nostre bot ha de retornar per cada operació el plot del nou Skyline per la pantalla juntament amb un missatge que indiqui l'àrea i l'alçada màxima

L'usuari també pot fer servir diferents comandes

__/start__: Inicia la conversa.
__/help__: Llista de totes les possibles comandes i una breu documentació sobre el seu propòsit i ús.
__/author__: Bot escriu el nom complet de l’autor del projecte i seu correu electrònic oficial de la facultat.
__/lst__: mostra els identificadors definits i la seva corresponent àrea.
__/clean__: esborra tots els identificadors definits.
__/save id__: El bot guarda un skyline definit amb el nom id.sky.
__/load id__: El bot carrega l'identificador id a la sessió

## Instal·lació
---
Recomanable definir un entorn virtual per no tenir problemes amb els packages a instal·lar. Un cop creat, mou el fitxer allà i desde la comanda de terminals fes un:
```console
pip3 install -r requierements.txt
```
```console
python3 bot.py
```
## Implementació
---
El codi està estructurat en diferents mòduls: Skyline.py, bot.py i certs fixers dins la carpeta cl com ara TreeVisitor.py, juntament amb la gramàtica Sky.g. Aquesta gramàtica definida amb ANTLR4 i ens permet reconeixer diferents estructures sintàctiques i ens proporciona un arbre que podem recòrrer i evaluar.
1. __TreeVisitor.py__ rep l'arbre generat per la gramàtica (AST) i el recorre. Recorrem l'arbre en funció de les regles de la gramàtica que hem definit. A TreeVisitor.py tenim una funció definida per cada regla de la nostra gramàtica. A cada funció indicarem com hem de procedir amb l'avaluació. La implementació de cada funció i els seus comentaris es troben en el codi, però el que utilizem en cada regla per saber que hem de fer és mirar quants fills té cada node i si els fills són TOKEN's o no (utilitzant la funció __hasattr(node, 'getSymbol'))__. Amb aquestes dues propietats som capaços de disernir bé cada cas.
Cada instància de TreeVisitor rep un diccionari com a paràmetre d'inici quan el criden. Aquest diccionari és un registre de les variables definides durant la sessió amb l'usuari. Ens mapeja doncs identificadors amb instàncies de Skylines. Això ens és molt útil ja que necessitem recordar la conversa que hem tingut amb l'usuari, les variables que ja s'han definit i guardar les que s'han creat de noves.
2. __Skyline.py__: Aquesta classe ens proporciona la representació d'un objecte skyline i les funcions que hi podem aplicar. Un Skyline serà representat simplement com una llista de tuples on cada tupla és un dels edificis. Hi tenim definides tots les funcions que representen les operacions que podem fer. La majoria de funcions són molt senzilles. Una menció especial, mereix però, la funció unió() i dibuixar() ja que de la seva implementació depén la velocitat del nostre Bot.
Volem intentar que si tenim un Skyline, a l'hora de fer-ne el plot, no cridem a edificis que es solapen ja que, si ens hi fixem estem dibuixant molts edificis que no s'acaben representant en la figura final i això fa que el nostre Bot sigui lent per entrades molt grans. Per això abans de cridar la funció dibuixar(), ens assegurarem que la nostra representació amb una llista d'edificis sigui aquella representació tal que tots els edificis no es solapen. D'aquesta manera estarem dibuixant el nombre mínim de rectangles necessaris per representar correctament el nostre Skyline.
D'això se'n carrega la funció unio(). La idea és utilitzar la tècnica de Divide and Conquer per aconseguir simplificar la representació dels edificis de manera que no es solapin en O(nlogn). Procedirem de manera molt similar al merge sort. 
Nosaltres podem donades dues llistes d'edificis que no es solapen, aconseguir la llista total d'edificis que no es solapen. Això es pot realitzar amb un parell d'iteradors a les dues llistes i anar movent convenienment un o l'altre en funció de la posició en què estem(veure detalls a la implementació del codi).
La idea doncs es anar dividint el nostre Skyline per la meitat, fins arribar al cas base, construir la solució de manera trivial en el cas que només tenim un edifici i reconstruir les solucions.
Si ens hi fixem la recurrència compleix T(n) = 2T(n/2) + O(n), que pel Teorema Mestre sabem que és O(nlogn).
3. __bot.py__: És un fitxer que s'encarrega de sincronitzar-se amb Telegram i dir quines funcions s'han d'executar en cada cas. Els codis són senzills. Cal destacar que les funcions /save id i /load id treballen amb la llibreria pickle. Pickle s'utilitza perquè ens permet serialitzar objectes. En el nostre cas /save id guarda l'instància de la classel Skyline amb identificador id en un fitxer. Ens hem d'assegurar que diferents usuaris puguin guardar els mateixos id's en diferents sessions. Per això és important definir un hash entre usuaris i fitxers que en el nostre codi es fa de la seguent forma. /save id -> guarda el fitxer chat_id + id.sky. Com que el __chat_id__ és únic per cada usuari, som capaços de guardar mateixos identificadors en diferents sessions de manera simultània.
__/load id__ simplement deserialitza l'objecte amb l'identificador id i el porta al 'workspace'.
4. Sky.g ens defineix la gramàtica. La majoria de regles són senzilles. Operació és la única regla més complicada ja que hem de disernir entre bastantes opcions. Fixem-nos que hem afegit '(' operacio ')' per tenir en compte que l'usuari pugui definir la prioritat a través de parèntesis. També hem fet respectar la prioritats'-'/'*'/'+-' colocant les opcions per la regla operació convenientment començant per l'esquerra.
 
## Complexitat
---
Hem analitzat l'entrada d'edificis aleatòria. __T(Aleatori)__ representa el temps que necessita a generar tots els edificis. Sabem que aquesta funció és O(n) ja que només recorre l'interval i crida a rand.
__T(Merge Sort)__ és el temps que necessitem per obtenir la representació sense solapaments del nostre Skyline utilitzant un algorime similar al Merge Sort (mateixa idea en el fons) i __T(Dibuixar,Guardar, Enviar)__ és el temps que tarda el plot, guardar la imatge en un fitxer i enviar-la. Anem a veure quins han sigut els resultats.

| Entrada | T(Aleatori) | T(Merge sort)| T(Dibuixar,Guardar,Enviar)  |
| ------------ | ---------- |:----------------:| -----:|
|{10,20,3,1,10000} | 4.48E-05    | 7.25E-05 | 0.5622837543 |
|{100,20,3,1,10000} | 0.0001478195     | 0.0010614395      |   0.9347276688 |
| {1000,20,3,1,10000} | 0.0033135414 | 0.0211517811    |    4.9707486629 |
|{10000,20,3,1,10000} |   0.0280365944   |    0.1545734406    | 27.0360732079 |
|{100000,20,3,1,10000} |  0.1801066399  |   1.2534968853    | 34.5079908371 |
|{1000000,20,3,1,10000} |   1.0655961037  |    8.718421936    |   34.1657905579 |
---
 Veiem les dades del factor __T(Merge Sort)__ confirmen quecreix a ritme de __nlog(n)__ (quasilineal) ja que cada cop que multipliquem l'entrada per 10, el T(Merge Sort) també es multiplica amb un factor aprox de __*10__. Això es correponen amb el que hem vist que hauria de complir. El temps de dibuixar no segueix creixent ja que per una certa entrada arriba al límit de rectangles que hi ha pot dibuixar a dins de l'interval. El paràmetre que segueix creixent es el T(merge sort) i el T(Aleatoris). Com que el T(Merge Sort) és dominant, la complexitat del nostre algoritme vindrà donada pel Temps que trigui el merge sort, __O(nlogn)__
 ## Construit 
 ---
 Amb Python3
 ## Autors
 ---
 Jordi Bosch, estudiant de la FIB, jordi.bosch.bosch@est.fib.upc.edu
