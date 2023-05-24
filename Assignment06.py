# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# BRaupe,2023.05.20,Created started script
# BRaupe,2023.05.21,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        try: # Try to read the file name identified in file_obj
            file_obj = open(file_name, "r")
            for line in file_obj:
                try:
                    task, priority = line.split(",")
                    row = {"Task": task.strip(), "Priority": priority.strip()}
                    list_of_rows.append(row)
                except ValueError:
                    print(f"Skipping line: '{line.strip()}' - it does not contain the expected comma-separated values.")
            file_obj.close()
        except FileNotFoundError: # Error when file in file_obj not found
            print(f"File '{file_name}' not found. No data loaded.")
        except Exception as e:
            print("An error occurred while reading the file:", (e))
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with name of priority:
        :param list_of_rows: (list) you want to add more data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": str(task).strip(), "Priority": str(priority).strip()}
        # TODO: Add Code Here!
        list_of_rows.append(row)  # Add the new row to the list
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from a list of dictionary rows

        :param task: (string) with name of task:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        for row in list_of_rows:
            if row["Task"] == task:
                list_of_rows.remove(row)  # Remove the row from the list if the task matches
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data from a list of dictionary rows to a File

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        # TODO: Add Code Here!
        file_obj = open(file_name, "w")
        for row in list_of_rows:
            file_obj.write(row["Task"] + "," + row["Priority"] + "\n")  # Write each row to the file
        file_obj.close()
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """  Gets task and priority values to be added to the list

        :return: (string, string) with task and priority
        """
        pass  # TODO: Add Code Here!
        task = input("Enter the task: ")
        priority = input("Enter the priority: ")
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """  Gets the task name to be removed from the list

        :return: (string) with task
        """
        #task = input("Enter the task to remove: ")
        pass  # TODO: Add Code Here!
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False  # Use this to verify that the data was found and removed
        for row in table_lst: # For loop to search for the selected task to remove and changed flag to true
            task, priority = dict(row).values()
            if task.lower() == strKeyToRemove.lower():
                table_lst.remove(row)
                blnItemRemoved = True

        # Update user on the status
        if blnItemRemoved == True: # Once found and removed, this if statement prints feedback to user.
            print("The task was removed.")
        else: # Additional feedback to user indicating not able to remove find and remove task
            print("I'm sorry, but I could not find that task.")

        # Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in table_lst:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        #continue  # to show the menu
        return task


# Main Body of Script  ------------------------------------------------------ #


# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name=file_name_str, list_of_rows=table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while True:
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows=table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        table_lst = Processor.add_data_to_list(task=task, priority=priority, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove()
        table_lst = Processor.remove_data_from_list(task=task, list_of_rows=table_lst)
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
        print("Data Saved!")
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program after verifying that the user does not want to save.
        if "y" == str(input("Save this data to file? (y/n) ")).strip().lower():
            Processor.write_data_to_file(file_name=file_name_str, list_of_rows=table_lst)
            input("Data saved to file!  Press the [Enter] key to return to the main menu.")
        else:
            print("Goodbye!")
            break  # by exiting loop
