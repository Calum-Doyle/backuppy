 ########     ###     ######  ##    ## ##     ## ########  ########  ##    ## 
 ##     ##   ## ##   ##    ## ##   ##  ##     ## ##     ## ##     ##  ##  ##  
 ##     ##  ##   ##  ##       ##  ##   ##     ## ##     ## ##     ##   ####   
 ########  ##     ## ##       #####    ##     ## ########  ########     ##    
 ##     ## ######### ##       ##  ##   ##     ## ##        ##           ##    
 ##     ## ##     ## ##    ## ##   ##  ##     ## ##        ##           ##    
 ########  ##     ##  ######  ##    ##  #######  ##        ##           ##    

# Backuppy
# a backup management system
# by Calum Doyle
# v0.1
# 21.05.25

'''
TODO
    - Implement file handling  X
    - Implement group and item addition  X
    - Implement group and item deletion  X
    - Add backup functionality
    - Add backup verification
    - Add logging
    - Add backup restoration
'''

### INCLUDE LIBRARIES ###
import argparse
import json

### FILE LOCATIONS ###
DATA_LOCATION = 'data.json'
LOGFILE_LOCATION = 'backup.log'

### lOAD DATA ###
with open(DATA_LOCATION, 'r') as file:
    DATA = json.load(file)

### SAVE DATA ###
def save():
    json_data = json.dumps(DATA)
    with open(DATA_LOCATION, 'w') as file:
        file.write(json_data)

### PRINT CONFIG ###
def print_group(current_group):
    print(f"{current_group['name']}:")
    x = 0
    for item in current_group['items']:
        print(f"{x}. {item['origin']} -> {item['destination']}")
        x += 1

def print_config(selected_group = None):
    if selected_group:
       print_group(selected_group) 
    else:
        for g in DATA['groups']:
            print_group(g)
                
### ADD BACKUP LOCATIONS ###
def add_item(group, origin, destination):
    new_item = { "origin": origin, "destination": destination}
    for g in DATA['groups']:
        if g["name"] == group:
            g["items"].append(new_item)
            return True
    return False

def add_group(group):
    new_group = {"name": group, "items": []} 
    DATA["groups"].append(onew_group)
    
### REMOVE BACKUP LOCATIONS ###
def remove_item(group, number):
    x = 0
    for g in DATA['groups']:
        if g['name'] == group:
            for i in g['items']:
                if x == number:
                    g['items'].pop(x)
                x += 1

def remove_group(group):
    x = 0
    for g in DATA['groups']:
        if g['name'] == group:
            DATA['groups'].pop(x)
            return
        x += 1

### RUNTIME ###
if __name__ == "__main__":
    remove_group("Group2")
    print_config()

