from abc import ABCMeta, abstractmethod
from enum import Enum


class BaseData(metaclass=ABCMeta):
    @abstractmethod
    def getDataType(self):
        raise NotImplementedError

    @abstractmethod
    def printValue(self):
        raise NotImplementedError

    @abstractmethod
    def storeValue(self, value):
        raise NotImplementedError

    @abstractmethod
    def matchValue(self, value):
        raise NotImplementedError

    @abstractmethod
    def getValue(self):
        raise NotImplementedError


class Datatype(Enum):
    INT = 1
    STRING = 2


class IntData(BaseData):

    def __init__(self, value):
        self.value = value

    def storeValue(self, value):
        self.value = int(value)

    def printValue(self):
        print(self.value)

    def getDataType(self):
        return Datatype.INT

    def matchValue(self, value):
        return self.value == int(value)

    def getValue(self):
        return self.value


class StringData(BaseData):

    def __init__(self, value):
        self.value = value

    def storeValue(self, value):
        self.value = str(value)

    def printValue(self):
        print(self.value)

    def getDataType(self):
        return Datatype.STRING

    def matchValue(self, value):
        return self.value == str(value)

    def getValue(self):
        return self.value
