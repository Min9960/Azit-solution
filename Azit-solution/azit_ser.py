import pymysql

DB_CONFIG = dict(
    host="localhost",
    user="root",
    password="0000",
    database="myazit",
    charset="utf8mb4"
)
class DB:
    def __init__(self, **config):
        self.config = config

    def connect(self):
        return pymysql.connect(**self.config)

    # 공통 실행 (INSERT, UPDATE, DELETE)
    def execute(self, sql, params=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
            conn.commit()
        finally:
            conn.close()

    # 공통 조회 (SELECT)
    def execute_all(self, sql, params=None):
        conn = self.connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(sql, params)
                return cursor.fetchall()
        finally:
            conn.close()

    # assets 전체 조회
    def fetch_assets(self):
        sql = """
        SELECT id, product_name, category_large,
               category_small, quantity, price,
               lot_number, created_at
        FROM assets
        """
        return self.execute_all(sql)

    #추가
    def insert_asset(self, name, carl, cars, q, p, lot, log):
        sql = """
        INSERT INTO assets
        (product_name, category_large, category_small,
         quantity, price, lot_number)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        self.execute(sql, (name, carl, cars, q, p, lot))

    #수정
    def update_asset(self, asset_id, name, carl, cars, q, p, lot):
        sql = """
        UPDATE assets
        SET product_name = %s,
            category_large = %s,
            category_small = %s,
            quantity = %s,
            price = %s,
            lot_number = %s
        WHERE id = %s
        """
        self.execute(sql, (name, carl, cars, q, p, lot, asset_id))
    #삭제
    def delete_asset(self, asset_id):
        sql = "DELETE FROM assets WHERE id = %s"
        self.execute(sql, (asset_id,))