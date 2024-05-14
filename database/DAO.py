from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllCountryYearNodes(year):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select distinct con.state1ab,con.state1no ,c.StateNme  
                    from contiguity con, country c 
                    where con.`year` <= %s and con.state1no = c.CCode """
        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllContiguityYearEdge(year):
        conn = DBConnect.get_connection()

        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select * from contiguity c 
                    where c.`year` <= %s and c.conttype =1"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append(Contiguity(**row))

        cursor.close()
        conn.close()
        return result

