import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime


from datetime import datetime

def greet_based_on_time():
    current_time = datetime.now().time()
    
    if current_time.hour < 12:
        greeting = "Good Morning!"
    elif 12 <= current_time.hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"
    
    return greeting

# Call the function to display the greeting
print(greet_based_on_time())
