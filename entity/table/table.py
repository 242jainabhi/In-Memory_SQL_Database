from abc import ABCMeta, abstractmethod

from entity.meta.metadata import TableMetaData


class BaseTable(metaclass=ABCMeta):
    @abstractmethod
    def getName(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def insert_record(self, tableRecord):
        raise NotImplementedError

    @abstractmethod
    def print_records(self):
        raise NotImplementedError


class Table(BaseTable):
    def __init__(self, meta_data: TableMetaData, columns: dict):
        self.meta_data = meta_data
        self.columns = columns
        self.records = []

    def getName(self):
        return self.meta_data.getName()

    def insert_record(self, table_record):
        row_data = table_record.get_row()
        for entry in row_data:
            column = self.columns[entry]
            if column is not None:
                column.applyConstraints(row_data[entry])
        self.records.append(table_record)

    def print_records(self):
        for record in self.records:
            row_data = record.get_row()
            current_record = []
            for col_name, data in row_data.items():
                current_record.append(data.getValue())
            for d in current_record:
                print(d, end=' ')
            print()


class TableRecord():
    def __init__(self, row):
        '''
        row = {column_name: data}
        :param row:
        '''
        self.row = row

    def get_row(self):
        return self.row

    def set_row(self, row):
        self.row = row
