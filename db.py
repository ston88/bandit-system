import argparse
import pymssql
from timeit import default_timer as timer
from abc import ABC, abstractmethod

class Database(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def connect(self, **kwargs):
        pass

    @abstractmethod
    def create_index(self, tbl_name, col_names, idx_name):
        pass

    @abstractmethod
    def drop_index(self, tbl_name, idx_name):
        pass

    @abstractmethod
    def time_query(self, query):
        pass

class MssqlDatabase(Database):
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self, **kwargs):
        self.conn = pymssql.connect(server=kwargs.get('server'),
                                    user=kwargs.get('username'),
                                    password=kwargs.get('password'),
                                    database=kwargs.get('database'))
        self.cursor = self.conn.cursor()

    def create_index(self, tbl_name, col_names, idx_name):
        query = f'''CREATE INDEX {idx_name}
                    ON {tbl_name} ({', '.join(col_names)})
                '''
        self.cursor.execute(query)
        self.conn.commit()

    def drop_index(self, tbl_name, idx_name):
        query = f"DROP INDEX {tbl_name}.{idx_name}"
        self.cursor.execute(query)
        self.conn.commit()

    def time_query(self, query):
        start = timer()
        self.cursor.execute(query)
        self.conn.commit()
        end = timer()
        return end - start

def main(*args, **kwargs):
    parser = argparse.ArgumentParser(description="Connect to MSSQL DB.")
    parser.add_argument("--server", type=str,
                        help="the address of the MSSQL server")
    parser.add_argument("--database", type=str,
                        help="the name of the database")
    parser.add_argument("--username", type=str,
                        help="username for the database")
    parser.add_argument("--password", type=str,
                        help="password for the database")

    kwargs = vars(parser.parse_args())
    db = MssqlDatabase()
    db.connect(**kwargs)

if __name__ == '__main__':
    main()
