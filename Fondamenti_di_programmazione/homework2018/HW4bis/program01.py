

''' 
    Alice e Bob si affrontano nel seguente gioco: 
    hanno  una sequenza iniziale di  N interi, 
    una mossa del gioco consiste nel selezionare dalla sequenza  due numeri  consecutivi 
    a e b, con a>b, i due numeri vengono eliminati dalla sequenza e 
    sostituiti dalla loro  differenza (a-b). Alice e Bob si alternano nelle mosse 
    con Alice che effettua la prima mossa, il gioco e' vinto se all'avversario viene 
    lasciata una sequenza per cui non e' possibile muovere (vale a dire: nella sequenza 
    non sono presenti due numeri consecutivi a e b con a>b).
    Data la sequenza  iniziale siamo interessati a trovare il numero 
    di possibili partite che portano alla vittoria di  Alice ed il numero di 
    possibili partite che portano alla vittoria di Bob. 
    
    Si consideri ad esempio l'albero di gioco che si ottiene a partire dalla 
    sequenza-configurazione '19 -3 2 -10 -20'  e che e' riportato  nel file 
    albero_di_gioco1.pdf:
    le possibili partite vittoriose per Alice sono tre (tutte portano alla 
    sequenza-configurazione '22 32') mentre le possibili partite vittoriose  per Bob sono 
    sei (tre partite con configurazione finale '10', due partite con configurazione 
    finale '30' e una partita con configurazione finale '50'). 
    
    Definire una funzione es(s) ricorsiva (o che fa uso di funzioni o 
    metodi ricorsive/i) che, data una  stringa  che codifica  una  configurazione iniziale 
    del gioco (i numeri della sequenza son separati da uno spazio), restituisce  
    una tupla di 6 elementi.
    - la prima   componente della tupla e' il numero di possibili vittorie di Alice
    - la seconda componente della tupla e' il numero di possibili vittorie di Bob
    - la terza   componente della tupla e' il numero di nodi-configurazioni presenti 
      nell'albero di gioco.
    - la quarta  componente della tupla e' il nome del vincitore della partita più corta
    - la quinta  componente della tupla e' il nome del vincitore della partita più lunga
    - la sesta   componente e' una lista con tutte le DIVERSE configurazioni di gioco presenti
    nell'albero di gioco. Ciascuna configurazione deve apparire nella lista
    come tupla di interi e le tuple devono comparire nella lista ordinate per lunghezza 
    crescente e, a parita' di lunghezza, in ordine crescente.
    
    Ad esempio es('19, -3, 2, -10, -20') deve restituire la sestupla 
    (3, 6, 25, 'Bob', 'Alice', 
        [(10,), (30,), (50,), 
        (10, -20), (20, 10), (22, 32), (30, -20), 
        (19, -3, 32), (20, -10, -20), (22, 2, 10), (22, 12, -20), 
        (19, -3, 2, 10), (19, -3, 12, -20), (22, 2, -10, -20), 
        (19, -3, 2, -10, -20)])

ATTENZIONE: non sono permesse altre librerie altre a quelle già importate.

TIMEOUT: il timeout per ciascun test è di 1 secondo.

ATTENZIONE: quando consegnate il programma assicuratevi che sia nella codifica UTF8
(ad esempio editatelo dentro Spyder o usate Notepad++)

'''
def getkey(x):
    return len(x), x

def es1(s):
    sequence = list(map(lambda x: int(x),s.split(" ")))

    albero = Albero(sequence)
    tree_builder(sequence, albero)
    nodes = albero.count_nodes(albero.children) + 1
    depth_dic = {}
    nodes_list = list()
    min_max(albero, 0, depth_dic, nodes_list)
    player_min_height = min(depth_dic.items(), key= lambda x: x[1])[0].player
    player_max_height = max(depth_dic.items(), key= lambda x: x[1])[0].player

    nodes_list = sorted(nodes_list, key=getkey )





    return albero.players["Alice"], albero.players["Bob"], nodes, player_max_height, player_min_height, nodes_list






def min_max(node, depth, depth_dict, nodes_list):
    if node.children is None:
        return 0

    t = tuple(node.radice)
    if t not in nodes_list:
        nodes_list.append(t)

    for child in node.children:
        tuple_child = tuple(child.radice)
        if tuple_child not in nodes_list:
            nodes_list.append(tuple_child)
        min_max(child, depth + 1, depth_dict, nodes_list)
        if child.children is None:
            depth_dict[child] = depth +1
    return 0

    
    
    
    
    
def tree_builder(sequence, albero, player = "Bob"):
    ##ora, se funziona, se la sequence non ha childre hai trovato il vincitore!
    if player == "Alice":
        player = "Bob"
    else:
        player = "Alice"


    if len(sequence) == 1:
        return sequence
    for i, el_a in enumerate(sequence):
        
        if i + 1 < len(sequence):
            el_b = sequence[i+1] #numbers must be consecutive
            if el_b < el_a:
                sequenza_appoggio = sequence.copy()
                sequenza_appoggio[i] = (el_a-el_b)
                sequenza_appoggio.remove(el_b)
                albero_ = Albero(sequenza_appoggio)
                albero.append_child(albero_)
                albero_.player = player

                tree_builder(sequenza_appoggio, albero_, player)
    return albero
    

class Albero:

    def __init__(self, radice):
        self.radice = radice
        self.children = None
        self.nodi = 0
        self.player_min="";
        self.player_max="";
        self.player = ""
        self.players = {"Alice":0,"Bob":0}
    def append_child(self, child):
        if not self.children:
            self.children = list()

        self.children.append(child)

    def __str__(self):
        return self.player + ''.join(str(self.radice)) + " children:" + ''.join(str(self.children))
    def __repr__(self):
        return"player: "+ self.player +"  " + ''.join(str(self.radice)) + " children:" + ''.join(str(self.children))

    def count_nodes(self, children):
        if not children:
            return 0

        branch_depth_sum = 0
        for child in children:

            branch_depth = self.branch_depth(child.children)
            branch_depth_sum += branch_depth + 1
        return branch_depth_sum
    

    def branch_depth(self, branch):
        if not branch:
            return 0
        count = 0
        for child in branch:
            if child.children == None:
                self.players[child.player]+=1
            count += 1 + self.branch_depth(child.children)

        return count

if __name__ == "__main__":
    print(es1("5 4 3 2 1"))
