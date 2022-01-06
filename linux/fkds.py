from colorama import init, Fore, Style
import platform as pf
import os
init()

SYSTEM = pf.system()
GR = Fore.GREEN
RE = Fore.RED
WH = Fore.WHITE
BOL = Style.BRIGHT
RES = Style.RESET_ALL







cwd = os.getcwd()
files = os.listdir()

# Prints debug info
print(f'{BOL}{GR}[DEBUG]{RES} CWD: {cwd}')
print(f'{BOL}{GR}[DEBUG]{RES} OS: {pf.platform()}\n')

# Gets all the .DS_Store files
file_list = []
for directory, folders, files in os.walk(cwd):
    for file in files:
        if file == '.DS_Store':
            file_path = os.path.join(directory, file).replace(cwd, '') 
            file_list.append( os.path.join(directory, file) )
            print(f'{BOL}{RE}[MATCH]{RES} .{file_path}')



# If no files are found, print a message and exit
if not len(file_list):
    print(f'{BOL}{GR}[INFO]{RES}  No .DS_Store files found :)')
    exit()

# Asks if they want to delete the files
count = len(file_list)
chc = input(f'\nI have found {RE}{count}{RES} .DS_Store files. Would you like to execute them? (Y/n)\n')



# Deletes all the files
if chc in ['Y','y','']:
    for file in file_list:    os.remove(file)
    print(f'{BOL}{GR}[INFO]{RES}  Deleted {count} .DS_Store files.')

# Else, tells operation was cancelled
else:    print(f'{BOL}{GR}[INFO]{RES}  Operation cancelled.')



