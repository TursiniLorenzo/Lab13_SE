from database.DB_connect import DBConnect

from model.gene import Gene
from model.interazione import Interazione
from model.classificazione import Classificazione
from model.cromosoma import Cromosoma

class DAO:

    @staticmethod
    def read_gene ():
        conn = DBConnect.get_connection()
        if conn is None :
            print ("Connessione al database non riuscita.")

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM gene """

        cursor.execute(query)

        for row in cursor:
            result.append(Gene (**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_cromosomi ():
        conn = DBConnect.get_connection()
        if conn is None :
            print ("Connessione al database non riuscita.")

        result = []

        cursor = conn.cursor()
        query = """ SELECT distinct(g.cromosoma)  
                    FROM gene g
                    WHERE g.cromosoma != 0 
                    group by g.cromosoma """

        cursor.execute(query)

        for row in cursor:
            c = Cromosoma (row [0])
            result.append(c)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_interazione ():
        conn = DBConnect.get_connection()
        if conn is None :
            print ("Connessione al database non riuscita.")

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select (g.id) as id1, (g1.id) as id2, (g.cromosoma) as cromosoma1, (g1.cromosoma) as cromosoma2, i.correlazione
                    from interazione i, gene g, gene g1 
                    where i.id_gene1 = g.id 
                    and i.id_gene2 = g1.id 
                    and g.cromosoma != g1.cromosoma 
                    and g.cromosoma != 0 
                    and g1.cromosoma != 0 
                    group by g.id, g1.id """

        cursor.execute(query)

        for row in cursor:
            interazione = Interazione (row ["id1"],
                                       row ["id2"],
                                       row ["cromosoma1"],
                                       row ["cromosoma2"],
                                       float (row ["correlazione"]))
            result.append (interazione)

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_classificazione ():
        conn = DBConnect.get_connection()
        if conn is None :
            print ("Connessione al database non riuscita.")

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * FROM classificazione """

        cursor.execute(query)

        for row in cursor:
            result.append(Classificazione (**row))

        cursor.close()
        conn.close()
        return result

