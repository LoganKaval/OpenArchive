import platform
import sys
from datetime import date
import random

#Varibles
a = 0
b = 1
random = random.randint

print('Welcome')
name = input('What is Your Name?')
print('Hello, ' + name)
print('I am OpenArchive, a Free and Opensource Archive')

#DATA HERE

def get_hardware_info():
    system_info = platform.uname()

cpuinfo = platform.uname()

#All of the syntax for OpenArchive are right here!!!
data_lib = {
    'archive_age': 'Older Than 1 Days Old',
    'archive_creator': 'Logan Kaval',
    'archive_purpose': 'To Help People Remember Stuff',
    'archive_hardware': cpuinfo,
    'archive_contributors': 'Logan Kaval,',
    'archive_usr': name,
    'pla_print_temp': '190C to 220C',
    'tpu_print_temp': '210C to 230C',
    'water_comp': '2 Hydrogen and 1 Oxygen',
    "archive_ver": 'Version: v1.7.6 Flying Lion',
    'help_syntax': ' '



}

question = input('What Do You Want To Know? Enter in the Syntax Here (Do "help_syntax" for the Syntax) -->')
print(data_lib[question])

while True:
    question = input('What Do You Want To Know? Enter in the Syntax Here (Do "help_syntax" for the Syntax) -->')
    print(data_lib[question])

