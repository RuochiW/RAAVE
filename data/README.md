<!--
AUTHORS: RW
-->


# Requirement

Be consistent with the names in `tables.py`.

# Usage
View the schema of the database in `tables.py`.\
View the functions of the corresponding class in the data controller.\
Such as `account_data_contorller` for `accounts` class.\
Call `reset_tables()` before call other function. Or, use `clear_tables()` and `create_tables()` as need.
Call `clear_error_log()` to clear error logs.


def clear_tables():
    clear_file(db_path)


def create_tables():

# Function
`write` only take class obj

TODO

