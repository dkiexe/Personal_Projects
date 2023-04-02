import time
import os
import sqlite3
from pathlib import Path
import help_setup as help


# Setup Values
connection = sqlite3.connect(os.path.dirname(__file__)+'\database.db')
cursor = connection.cursor()
welcome_msg = """
                                  ██████  ████  ████                                    
                              ████░░░░░░██░░░░██░░░░██████                              
                            ██░░▓▓░░░░░░▓▓░░░░▓▓░░░░▓▓░░░░██                            
                        ██████░░░░▓▓░░██████████████▓▓░░░░██████                        
                      ██░░░░▓▓░░░░████▓▓░░░░░░░░░░▓▓████░░▓▓░░░░██                      
                    ████░░░░░░▓▓██░░░░░░░░░░░░░░░░░░░░░░██░░░░░░████                    
                  ██░░░░▓▓░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░██░░▓▓░░▓▓██                  
                  ██░░░░░░░░██░░░░░░░░████░░░░░░░░████░░░░░░██░░░░░░██                  
                  ██▓▓░░░░░░██░░░░░░░░█  █░░░░░░░░█  █░░░░░░██░░░░▓▓██                  
                ██▓▓░░░░░░██░░░░░░░░░░████░░░░░░░░████░░░░░░▓▓██▓▓░░░░██                
                ██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓██░░░░▓▓██                
                  ██▓▓░░░░██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓░░▓▓██░░▓▓██                  
                  ██░░░░░░██▓▓░░░░████░░░░░░░░░░░░░░████▓▓▓▓▓▓██░░░░██                  
                  ██▓▓░░▓▓░░██▓▓▓▓░░██████████████████░░▓▓▓▓██▓▓░░▓▓██                  
                    ████░░░░░░██▓▓▓▓░░░░░░░░░░░░░░░░░░▓▓▓▓██░░░░████                    
                      ██░░░░▓▓░░████▓▓▓▓░░░░░░░░░░▓▓▓▓████▓▓░░░░██                      
                        ████▓▓░░░░▓▓██████████████████░░░░██████                        
                            ████▓▓░░░░░░▓▓░░░░▓▓░░░░▓▓░░░░██                            
                                ████░░░░██░░░░██░░░░██████                              
                                    ██████████████████                                  
                              ██████  ██░░████▒▒▒▒████████                              
                              ██░░░░████░░██▒▒░░░░░░░░▒▒████                            
                          ████▒▒▒▒▒▒▒▒██░░██░░░░░░░░░░░░▒▒██                            
                        ██░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░██████░░▒▒██                          
                      ██░░░░░░░░░░░░░░░░░░▒▒░░░░██      ██████                          
                      ██░░░░░░░░░░░░░░░░░░▒▒▒▒██          ██                            
                      ██████████▒▒░░░░▒▒██████          ██                              
                        ██      ██████████                                              
                          ████
                    _                                       _                              _     _    __           _ 
 __      __   ___  | |   ___    ___    _ __ ___     ___    | |__     ___    __ _   _   _  | |_  (_)  / _|  _   _  | |
 \ \ /\ / /  / _ \ | |  / __|  / _ \  | '_ ` _ \   / _ \   | '_ \   / _ \  / _` | | | | | | __| | | | |_  | | | | | |
  \ V  V /  |  __/ | | | (__  | (_) | | | | | | | |  __/   | |_) | |  __/ | (_| | | |_| | | |_  | | |  _| | |_| | | |
   \_/\_/    \___| |_|  \___|  \___/  |_| |_| |_|  \___|   |_.__/   \___|  \__,_|  \__,_|  \__| |_| |_|    \__,_| |_|                                                                                                               
                                       __   _                                    _                                   
                ___   _   _   _ __    / _| | |   ___   __      __   ___   _ __  | |                                  
               / __| | | | | | '_ \  | |_  | |  / _ \  \ \ /\ / /  / _ \ | '__| | |                                  
               \__ \ | |_| | | | | | |  _| | | | (_) |  \ V  V /  |  __/ | |    |_|                                  
               |___/  \__,_| |_| |_| |_|   |_|  \___/    \_/\_/    \___| |_|    (_)                                  
"""
menu_print = """
> Here are your options :
1) I for insert.
2) V for view.
3) U for update.
4) D for delete.
5) Q for quit application.
"""
# Helper functions
def clear():
    """
    This function clears the screen for better readability.
    Parameters: None
    Returns: None
    """
    os.system('cls')
clear()
print(welcome_msg)

def insert_operation():
    # collecting date from user and automatically getting the day name(i.e : sunday) for that date.
    (date_value, day_value) = help.date_collector()
    # collecting time from user.
    time_value = help.time_collector()
    # collecting all goals from the user and creating a ordered string
    goals_list = help.goal_collector()
    goals_value = "||".join(goals_list)
    # collecting the time each goal took
    achivement_time_list = help.time_of_achivement_collector(goals_list)
    achivement_time_value = "||".join(achivement_time_list)
    # collecting the total break time for that day
    break_time_total_value = help.total_break_time_collector()
    # collecting the count of breaks for that day
    break_count_value = help.break_count_collector()
    # Inserting to the database the collected values!
    cursor.execute(f"INSERT INTO {help.Table_name} VALUES (?,?,?,?,?,?,?)",(date_value, day_value, time_value, goals_value, achivement_time_value, break_time_total_value, break_count_value))
    connection.commit()
    print('INSERTED!')
    time.sleep(2)
    clear()

def read_open_file(ask = True):
    """
    This function Creates a text file in the relative path to this file, takes all data from the database and writes it to to the file it created.
    the file gets created if its missing and if the file is present in the relative path it just gets an update. at the end the file created/updated would be
    opened up infront of the user in order for him to see the record.

    Returns: None
    Arguments: None
    """
    if ask:
      view_choice= input('> Do you wish to view all data from the databse? !this creates a readable text file in the directory and opens it! (y/n): ')
      if view_choice == 'y':
        open(str(Path(__file__).parent.resolve())+r'\all_data.txt','w').close() #creates a new file or resets a existing one.
        with open(str(Path(__file__).parent.resolve())+r'\all_data.txt','a+') as path_selection:
            cursor.execute(f'SELECT rowid,* FROM {help.Table_name}')
            path_selection.write(f'Format-> {help.formats["database_data"]}'+'\n')
            all_vals= cursor.fetchall()
            for record in all_vals:
                path_selection.write('\n'+str(record))
            #opens the created text file so user could read it.
            os.startfile(str(Path(__file__).parent.resolve())+r'\all_data.txt')
            connection.commit()
    else:
        open(str(Path(__file__).parent.resolve())+r'\all_data.txt','w').close() #creates a new file or resets a existing one.
        with open(str(Path(__file__).parent.resolve())+r'\all_data.txt','a+') as path_selection:
            cursor.execute(f'SELECT rowid,* FROM {help.Table_name}')
            path_selection.write(f'Format-> {help.formats["database_data"]}'+'\n')
            all_vals= cursor.fetchall()
            for record in all_vals:
                path_selection.write('\n'+str(record))
            #opens the created text file so user could read it.
            os.startfile(str(Path(__file__).parent.resolve())+r'\all_data.txt')
            connection.commit()

def delete_operation():
        user_selected_row = input('> Input a seleccted rowid to Delete(number only): ')
        # Checking user input for a number.
        try:
            user_selected_row = int(user_selected_row)
        except ValueError:
            print('> Non number detected please try again.')
            time.sleep(2)
            delete_operation()
        # Checking if the row is in the database, or the user has inputed a 0
        if len(cursor.execute(f"SELECT * FROM {help.Table_name}").fetchall()) < user_selected_row or user_selected_row == 0:
            print('>! Non existent row selected please select a row that actually exists in the database....')
            time.sleep(1)
            delete_operation()
        assurance= input(f'> ARE YOU SURE? type YES if you want to delete row-number:{user_selected_row} > ').casefold()
        if assurance == 'yes':
            cursor.execute(f"""
            DELETE FROM {help.Table_name} WHERE rowid = {user_selected_row}
            """)
            connection.commit()
            print('> Deleted')
        else:
            print('> Nothing was deleted :)')

def update_operation():
  while True:
    user_row_input = input('> Please input a row number(rowid) as a number: ')
    records_total_number = len(cursor.execute(f'SELECT rowid FROM {help.Table_name}').fetchall())
    try:
      int(user_row_input)
    except:
      print('ERR> Non number value detected!')
      continue
    if int(user_row_input) > records_total_number or int(user_row_input) < 1:
      print(f'ERR> Row number cant be bigger than {records_total_number} (Total number of rows) and cant be smaller than 0')
      continue
    break
  clear()
  while True:
    user_colum_to_update_input = input(f"""
  UPDATING ROW NUMBER[{user_row_input}]
> Here are your options:
1) Update Date (Note! changing the date causes an automatic change in the day)

2) Update Start time.

3) Update goals achived.

4) Update time each goal took.

5) Update total break time.

6) Update amount of breaks.

7) Change the row number.

8) Quit the update operation. 
    """+ '\n> Type your answer here(use number of option !no english characters!): ')
    try:
      int(user_colum_to_update_input)
    except:
      print('ERR> Non number value detected!')
      continue
    if user_colum_to_update_input not in [str(num) for num in range(9)]:
      print('ERR> Value dosent exist on options menu.')
      continue
    else:
      match user_colum_to_update_input:
        case '1':
          (date_value, day_value) = help.date_collector()
          cursor.execute(f"""
          UPDATE {help.Table_name} SET Date = "{date_value}", Day = "{day_value}" WHERE rowid = "{user_row_input}"
          """)
          connection.commit()
          print(f'\n> SUCSSESS!!! updated Date + Day in {help.Table_name}')
          time.sleep(2)
          clear()
          continue
        case '2':
          time_value = help.time_collector()
          cursor.execute(f"""
          UPDATE {help.Table_name} SET Start_Time = "{time_value}" WHERE rowid = "{user_row_input}"
          """)
          connection.commit()          
          print(f'\n> SUCSSESS!!! updated Start time in {help.Table_name}')
          time.sleep(2)
          clear()
        case '3':
          goals_list = help.goal_collector()
          goals_value = "||".join(goals_list)
          cursor.execute(f"""
          UPDATE {help.Table_name} SET Goals_Achieved = "{goals_value}" WHERE rowid = "{user_row_input}"
          """)
          connection.commit()          
          print(f'\n> SUCSSESS!!! updated Goals Achieved in {help.Table_name}')
          time.sleep(2)
          clear()
        case '4':
          achivement_time_list = help.time_of_achivement_collector()
          achivement_time_value = "||".join(achivement_time_list)
          cursor.execute(f"""
          UPDATE {help.Table_name} SET Time_each_goal_took = "{achivement_time_value}" WHERE rowid = "{user_row_input}"
          """)
          connection.commit()          
          print(f'\n> SUCSSESS!!! updated Time each goal took in {help.Table_name}')
          time.sleep(2)
          clear()
        case '5':
          break_time_total_value = help.total_break_time_collector()
          cursor.execute(f"""
          UPDATE {help.Table_name} SET Total_Break_time = "{break_time_total_value}" WHERE rowid = "{user_row_input}"
          """)
          connection.commit()          
          print(f'\n> SUCSSESS!!! updated Total_Break_time in {help.Table_name}')
          time.sleep(2)
          clear()
        case '6':
          break_count_value = help.break_count_collector()
          cursor.execute(f"""
          UPDATE {help.Table_name} SET Amount_of_breaks = "{break_count_value}" WHERE rowid = "{user_row_input}"
          """)
          connection.commit()          
          print(f'\n> SUCSSESS!!! updated Amount_of_breaks in {help.Table_name}')
          time.sleep(2)
          clear()
        case '7':
          update_operation()
          break
        case '8':
          break

# Main function
def main():
    connection = sqlite3.connect(os.path.dirname(__file__)+'\database.db') # Trying to connect to a db, Makes the database if there is no db file in the directory.
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables_list= []
    for tup in cursor.fetchall():
        tables_list.append(tup[0])
    if len(tables_list) == 0 or help.Table_name not in (tables_list): # Check the database for the right table if not present creates it.
        cursor.execute(f"""CREATE TABLE {help.Table_name}(
            Date TEXT,
            Day TEXT,
            Start_Time TEXT,
            Goals_Achieved TEXT,
            Time_each_goal_took TEXT,
            Total_Break_time TEXT,
            Amount_of_breaks INTEGER
            )""")
        print('> New Table created (was missing)')
    # print(welcome_msg)
    while True:
        user_input = input(menu_print + '> ').casefold()
        if not any(list(map(lambda list_elem: True if list_elem.startswith(user_input) else False, help.all_avaliable_operations))): # check for correct input from user.
            print('>ERR !Non valid input detected!')
            time.sleep(2)
            clear()
            continue
        clear()
        help.print_intro(user_input)
        match user_input:
            case 'i':
                insert_operation()
            case 'd':
                read_open_file()
                delete_operation()
            case 'v':
                read_open_file(False)
            case 'u':
                read_open_file()
                update_operation()
            case 'q':
                break
    print('Goodbye! <3')
    connection.commit()
    connection.close()

# If statement so that only this file can call main
if __name__ == '__main__':
    main()