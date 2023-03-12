# Imports.
import csv

# Script settings
# ------------------------------------------------------------------
# The data of the .csv file will be inserted to that table.
TABLE_TO_INSERT = "employees"
# The data will be extracted from that .csv file.
CSV_FILENAME = "values.csv"
# The output .sql file go that filepath.
OUTPUT_SQL_FILE = "script.sql"
# The script output to tell the user that everything went ok.
SUCCESS_MESSAGE = "The sql script has been generated succesfully."
# ------------------------------------------------------------------

def decorate_with_box(number_of_lines=0,width=40):
    '''
    The return (converted to str) of the function that this decorator decorates will
    be printed inside a box. This decorator takes into consideration the '\\n' character.\n
    '''
    def wrapper(func):
        def wrapper2():
            messages = str(func()).split("\n")
            n = len(messages)
            print("+"+"-"*(width-2)+"+")
            for i in range(number_of_lines):
                print("|"+" "*(width-2)+"|")
            for i in range(n):
                    print("| ",end="")
                    print(f"{str(messages[i]).center(width-3)}",end="")
                    print("|")
            for i in range(number_of_lines):
                print("|"+" "*(width-2)+"|")
            print("+"+"-"*(width-2)+"+")
        return wrapper2
    return wrapper

@decorate_with_box(1,len(SUCCESS_MESSAGE)+5)
def print_success_message():
    return SUCCESS_MESSAGE

def get_data_from_csv(csv_file_name):
    # Open the .csv file and get the data.
    with open(csv_file_name, newline='') as file:
        # Read the data
        data = csv.reader(file)
        # Convert the data to a list.
        data = list(data)

        return data
    
def create_output_csv_file(data):
    # Create the script.sql output file.
    with open(OUTPUT_SQL_FILE, "w") as file:
        # For every value
        for values in data:
            # Get the insert sql command.
            sql_command = get_insert_command(TABLE_TO_INSERT, values)
            # Write the insert sql command to the output csv file and go to the next line.
            file.write(sql_command+"\n")

def get_insert_command(table, values: list):
    formatted_values = ""

    num_of_values = len(values)

    for i in range(0, num_of_values - 1):
        formatted_values += f"{values[i]}, "
    
    if num_of_values != 0:
        formatted_values += f"{values[num_of_values-1]}"

    return f"INSERT INTO {table} VALUES ({formatted_values});"

def main():
    
    data = get_data_from_csv(CSV_FILENAME)
    create_output_csv_file(data)

    print_success_message()

if __name__ == "__main__":
    main()