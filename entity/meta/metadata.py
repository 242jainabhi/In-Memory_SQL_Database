from abc import ABCMeta, abstractmethod


class BaseMetaData(metaclass=ABCMeta):
    @abstractmethod
    def getName(self) -> object:
        raise NotImplementedError


class ColumnMetaData(BaseMetaData):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class TableMetaData(BaseMetaData):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name
