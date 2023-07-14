import random
import string
import datetime

API_FILE = "api.txt"

def GenerateAPI():
    """Generate a random API string."""
    api_string = "tech-" + ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=45))
    print(api_string)
    return api_string

def SaveAPIString(api_string):
    """Save the generated API string to a file."""
    with open(API_FILE, "a") as file:
        file.write(api_string + "\n")
        print(api_string)

def CheckAPI(api_string):
    """Check if a given string is an API by reading the file."""
    with open(API_FILE, "r") as file:
        api_strings = file.read().splitlines()
    if api_string in api_strings:
        return True
    else:
        return False
