# list -> powerful massive -> []
# different types of data

# VARIABLES -> define = -> a = 0, list = [1,2,3]

# run method -> return result
# this_minute = datetime.today().minute -> return NOT data structure, return RESULT of running method

from datetime import datetime
time_now = datetime.today() # today -> return object of time with information about current time
rigth_this_minute = time_now.minute # attribute minute -> return current minutes of time



# DECISION to run block of code
# operator IN -> checks that one contains in other -> if one in other -> return true/false

# if - elif - else
today = 0
if today == 'Saturday':
    print('Party!')
elif today == 'Sunday':
    print('Recover')
else:
    print('Work, work, work')