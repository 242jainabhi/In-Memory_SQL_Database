from abc import ABCMeta, abstractmethod


class BaseColumn(metaclass=ABCMeta):
    @abstractmethod
    def getColumnName(self):
        raise NotImplementedError


class Column(BaseColumn):
    def __init__(self, meta_data, data_type, constraints):
        self.metaData = meta_data
        self.dataType = data_type
        self.constraints = constraints

    def getColumnName(self):
        return self.metaData.getName()

    def applyConstraints(self, data):
        if data.getDataType() != self.dataType:
            raise TypeError("Type of input does not match the column data type.")

        for constraint in self.constraints:
            if not constraint.validate(data):
                raise Exception("constraint failed")

        return True
