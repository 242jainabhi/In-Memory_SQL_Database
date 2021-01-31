from abc import ABCMeta, abstractmethod

from entity.table.table import Table

class BaseDatabase(metaclass=ABCMeta):
    @abstractmethod
    def createTable(self, table: Table) -> str:
        raise NotImplementedError

    @abstractmethod
    def deleteTable(self, table: Table) -> str:
        raise NotImplementedError

    @abstractmethod
    def getTable(self, table: Table) -> Table:
        raise NotImplementedError


class Database(BaseDatabase):
    def __init__(self, name):
        self.name = name
        self.tables = {}

    def createTable(self, table: Table) -> str:
        if not table.getName() in self.tables:
            self.tables[table.getName()] = table
            return "Table created successfully"
        else:
            raise Exception('Duplicate table')

    def deleteTable(self, table_name: str) -> str:
        if table_name in self.tables:
            del self.tables[table_name]
            return "Table deleted successfully"
        else:
            raise Exception("Table not found")

    def getTable(self, table_name: str) -> Table:
        if table_name in self.tables:
            return self.tables[table_name]
        else:
            raise Exception("Table not found")
