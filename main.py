import platform
import sys

#Varibles
a = 0
b = 1

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
    'archive_age': 'Older Than 0 Days Old',
    'archive_creator': 'Logan Kaval',
    'archive_purpose': 'To Help People Remember Stuff',
    'archive_hardware': cpuinfo,
    'archive_contributors': 'Logan Kaval,',
    'help_syntax': ' '



}

question = input('What Do You Want To Know? Enter in the Syntax Here (Do "help_syntax" for the Syntax) -->')
print(data_lib[question])

while True:
    question = input('What Do You Want To Know? Enter in the Syntax Here (Do "help_syntax" for the Syntax) -->')
    print(data_lib[question])
