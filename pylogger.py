from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, DateTime
from datetime import datetime

class PyLogger():
    def __init__(self, db_uri='sqlite:///db.sqlite', table_name='Logs'):
        self.db_uri = db_uri
        self.table_name = table_name
        self.engine = create_engine(db_uri)
        self.table = self.__create_table()
        self.connection = self.engine.connect()
    
    def __create_table(self):
        metadata = MetaData(self.engine, reflect=True)

        if not self.engine.dialect.has_table(self.engine, self.table_name):
            log_table = Table(self.table_name, metadata,
            Column('Id', Integer, primary_key=True),
            Column('Message', String),
            Column('Stacktrace', String),
            Column('Timestamp', DateTime))
            log_table.create()
            print("%s table created" % self.table_name)
            return log_table
        else:
            print("%s table already exixts." % self.table_name)
            return metadata.tables[self.table_name]
    
    def log(self, message, stacktrace=''):
        insert_statement = self.table.insert().values(
            Message=message,
            Stacktrace=stacktrace,
            Timestamp=datetime.utcnow()
        )
        insert_statement.compile().params
        self.connection.execute(insert_statement)