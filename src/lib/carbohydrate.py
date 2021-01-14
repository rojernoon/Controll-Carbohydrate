import psycopg2

class database:
    def __init__(self):
        pass

    def show_all_foods(self):
        with psycopg2.connect(
            "dbname = carbohydrate host = '127.0.0.1' user = guest password = password"
            ) as conn:
            print("access by guest")
            with conn.cursor() as cur:
                cur.execute('select * from food')
                res = cur.fetchall()
        return res
    
    def search_foods(self, carbohydrate_limit):
        with psycopg2.connect(
            "dbname = carbohydrate host = '127.0.0.1' user = guest password = password"
            ) as conn:
            print("access by guest")
            with conn.cursor() as cur:
                cur.execute('select * from food where AmountOfCarbohydrate < 20')
                res = cur.fetchall()
        return res
            

class carbohydrate:
    def __init__(self, name, amount):
        self.name = name

    def search_carbo_amount(self):
        pass
