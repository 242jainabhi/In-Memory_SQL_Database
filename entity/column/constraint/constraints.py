from abc import ABCMeta, abstractmethod
from enum import Enum

from entity.data.datatype import Datatype


class BaseConstraint(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, data):
        raise NotImplementedError

    @abstractmethod
    def getType(self):
        raise NotImplementedError


class ConstraintType(Enum):
    REQUIRED = 1
    LENGTH = 2
    LIMIT = 3


class LengthConstraint(BaseConstraint):
    def __init__(self, length):
        self.length = length

    def getType(self):
        return ConstraintType.LENGTH

    def validate(self, data):
        data_type = data.getDataType()
        if data_type == Datatype.STRING:
            value = str(data.getValue())
            return value is not None and len(value) <= self.length
        else:
            raise Exception("Length constraint can only be applied to String dataType.")


class LimitConstraint(BaseConstraint):
    def __init__(self, lower_limit, upper_limit):
        self.lowerLimit = lower_limit
        self.upperLimit = upper_limit

    def getType(self):
        return ConstraintType.LIMIT

    def validate(self, data):
        data_type = data.getDataType()
        if data_type == Datatype.INT:
            value = int(data.getValue())
            return self.lowerLimit <= value <= self.upperLimit
        else:
            raise Exception("Limit constraint can be applied only to Integer DateType.")


class RequiredConstraint(BaseConstraint):
    def __init__(self):
        pass

    def getType(self):
        return ConstraintType.REQUIRED

    def validate(self, data):
        value = data.getValue()
        return value is not None
