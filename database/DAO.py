from database.DB_connect import DBConnect
from model.album import Album


class DAO():
    def __init__(self):
        pass



    @staticmethod
    def getAllNodes():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select a.AlbumId, a.Title, sum(t.Milliseconds) as durata
            from album a, track t 
            where t.AlbumId = a.AlbumId 
            group by a.AlbumId , a.Title 
        """
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Album(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdge(u, v):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            select distinctrow a1.AlbumId as a1,  a2.AlbumId as a2
            from album a1, album a2, playlisttrack p1, playlisttrack p2, track t1, track t2
            where t1.AlbumId = a1.AlbumId and t2.AlbumId = a2.AlbumId
                and p1.TrackId = t1.TrackId and p2.TrackId = t2.TrackId
                and p1.PlaylistId = p2.PlaylistId
                and a1.AlbumId = %s and a2.AlbumId = %s
                """
        try:
            cursor.execute(query, (u, v, ))

        except Exception as e:
            print(e)
            cursor.close()
            conn.close()
            return []
        result = []
        for row in cursor:
            result.append((row["a1"], row["a2"]))
        cursor.close()
        conn.close()
        return result
