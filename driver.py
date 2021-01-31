from entity.column.column import Column
from entity.column.constraint.constraints import RequiredConstraint, LimitConstraint, LengthConstraint
from entity.data.datatype import Datatype, IntData, StringData
from entity.database.database import Database
from entity.meta.metadata import ColumnMetaData, TableMetaData
from entity.table.table import Table, TableRecord


def create_database(name):
    return Database(name)


def create_table(name, columns):
    meta_data = TableMetaData(name)
    column_dict = {}
    for column in columns:
        column_dict[column.getColumnName()] = column
    return Table(meta_data, column_dict)


def create_column(name, data_type, constraints):
    meta_data = ColumnMetaData(name)
    return Column(meta_data, data_type, constraints)


def create_employee_table():
    required_constraint = RequiredConstraint()
    limit_constraint = LimitConstraint(0, 100)
    length_constraint = LengthConstraint(20)

    id_column = create_column('id', Datatype.STRING, [required_constraint])
    name_column = create_column('name', Datatype.STRING, [length_constraint])
    age_column = create_column('age', Datatype.INT, [limit_constraint])

    return create_table('employee', [id_column, name_column, age_column])


def create_table_record(id, name, age):
    row_data = {'id': StringData(id), 'name': StringData(name), 'age': IntData(age)}
    return TableRecord(row_data)


if __name__ == '__main__':
    database = create_database('emp_db')
    emp_table = create_employee_table()
    try:
        database.createTable(emp_table)
    except:
        raise Exception('Duplicate table')

    # try:
    # insert records in the table
    table = database.getTable('employee')
    table.insert_record(create_table_record('1', 'john', 25))
    table.insert_record(create_table_record('2', 'alice', 22))
    table.insert_record(create_table_record('3', 'bob', 28))

    table.print_records()
    # except ResourceNotFoundException as e:
    #     raise Exception('Table not found')
    # except ConstraintException as e:
    #     raise Exception('Constraint exception')