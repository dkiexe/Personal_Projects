from datetime import date
from calendar import day_name

# Setup variables
current_day_list = str(date.today()).split('-')
current_year= int(current_day_list[0]) # Automaticaly checks the current year for later use....
Table_name = "elushims_goal_table"
formats = {
    "date_format" : "dd/mm/yyyy",
    "time_format" : "hh:mm",
    "database_data" : "(Rowid ,Date, Day, Time, Goals_Achived, Time_each_goal_took, Total_Break_time, Amount_of_breaks)"
}
all_avaliable_operations = ['insert', 'view', 'update', 'delete', 'quit']
time_of_achivement_list = []

# Helper functions
def print_intro(input):
    selected_input = ''
    for elem in all_avaliable_operations:
        if elem.startswith(input):
            selected_input = elem
    print(f'> {selected_input} operation selected!')

def day_calcu(date_list):
    """
    This function takes a list of dates(splitted list from string sperator=> '\') and returns the name of the week day based on the values inside the list
    this is done by converting the list elements into ints with a list comprihension(int_vals_date_list) after that using the reversed to return a iterable
    of the list but in reverse(original format=> dd/mm/yyyy modified format=> yyyy/mm/dd because date takes=>(yyyy/mm/dd)),
    then calling the next() method 3 times to retrive values from the iterator so the date function could return a int value based on the day.
    taking this int value we got from the datetime module's date function we can use this number to acsses a value from the day_name dict that is located in the
    calendar module giving us the final day of the week name based on the date.
    """
    int_vals_date_list= [int(num) for num in date_list]
    int_vals_date_reversed= reversed(int_vals_date_list)
    return day_name[date(next(int_vals_date_reversed),next(int_vals_date_reversed),next(int_vals_date_reversed)).weekday()]

def date_check(user_date_input):
    if user_date_input.count('/') != 2 or len(user_date_input) != len(formats['date_format']):
        return False, "ERR > Non valid format"
    list_from_user_date_input = user_date_input.split('/')
    # Checking for numbers.
    try:
        day_part = int(list_from_user_date_input[0])
        month_part = int(list_from_user_date_input[1])
        year_part = int(list_from_user_date_input[2])
    except:
        return False, "ERR> Non number value detected"
    # Day checking.
    if day_part > 31:
        return False, "ERR> Day value cant be more than 31."
    elif month_part > 12:
        return False, "ERR> Month value cant be more than 12."
    elif year_part > current_year:
        return False, "ERR> Year value cant be more than curren year."
    else:
        return True, ""

def time_check(user_time_input):
    if user_time_input.count(':') != 1 or len(user_time_input) != len(formats['time_format']):
        return False, "ERR > Non valid format"
    list_from_user_time_input = user_time_input.split(':')
    # Checking for numbers.
    try:
        hours_part = int(list_from_user_time_input[0])
        minutes_part = int(list_from_user_time_input[1])
    except:
        return False, "ERR> Non number value detected"
    # Day checking.
    if minutes_part > 60:
        return False, "ERR> Minutes value cant be bigger than 60"
    elif hours_part > 24:
        return False, "ERR> Hours value cant be bigger than 24"
    else:
        return True, ""

# COLLECTOR FUNCTIONS!
def date_collector():
    while True:
        date_input = input(f'\n> Please insert a date here(format = {formats["date_format"]}) : ')
        (check_date_result, err_msg) = date_check(date_input)
        if check_date_result:
            break
        print(f'{err_msg}')
    day_from_date = day_calcu(date_input.split('/')) # calculating day from date using the day_calcu() function
    return date_input, day_from_date

def time_collector():
    while True:
        time_input = input(f'> Please insert a time here(format = {formats["time_format"]}) : ')
        (check_time_result, err_msg) = time_check(time_input)
        if check_time_result:
                break
        print(f'{err_msg}')
    return time_input

def goal_collector():
    goals_achived_list = []
    while True:
        user_goal_input = input('\n> Type your goals here please(!to stop type stop!): ')
        if user_goal_input == 'stop':
            if len(goals_achived_list) == 0:
                print('ERR> list must have at least one goal!')
                continue
            break
        goals_achived_list.append(user_goal_input)
        print('> added!')
    return goals_achived_list

def time_of_achivement_collector(goals_list = None):
    goals_list_to_display = goals_list if goals_list != None else '> Note! Display Not Avaliable for update operation'
    while len(goals_list_to_display) > 0:
        print(goals_list_to_display)
        while True:
            user_time_input = input(f'\n> Please type The time it took to complete each goal in order.(format = {formats["time_format"]}): ')
            (check_time_result, err_msg) = time_check(user_time_input)
            if check_time_result:
                break
            print(f'{err_msg}')
        time_of_achivement_list.append(user_time_input)
        try:
            goals_list_to_display.pop(0)
        except:
            continue
    return time_of_achivement_list

def total_break_time_collector():
    while True:
        user_total_break_time = input(f'\n> Please type the total break time for the day (format = {formats["time_format"]}): ')
        (check_time_result, err_msg) = time_check(user_total_break_time)
        if check_time_result:
            break
        print(f'{err_msg}')
    return user_total_break_time

def break_count_collector():
    while True:
        user_break_count_input = input(f'\n> Please type the amout of breakes you took that day(numbers only!): ')
        try:
            final_value = int(user_break_count_input)
            break
        except:
            print(f'ERR> Non number detected!')
    return final_value