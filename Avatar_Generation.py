import random
import requests
from pathlib import Path

def RAn_save():   # Random Avatar and save in the main folder
    response = requests.get(f'https://avatars.dicebear.com/api/male/{random.random()}.svg') 
    with open('avatar.svg', 'wb') as file:
        file.write(response.content)
        

def CAn_save():   # Choose Avatar and save in the main folder
    print("Choose avatar with https://www.dicebear.com/styles")
    avatar_number = input("Enter avatar number: ")
    response = requests.get(f'https://avatars.dicebear.com/api/male/{avatar_number}.svg') 
    with open('avatar.svg', 'wb') as file:
        file.write(response.content)


def RACn_save():   # Random Avatar + Create new folder and save
    response = requests.get(f'https://avatars.dicebear.com/api/male/{random.random()}.svg') 
    name_decision = input("Do you want to select a folder name? YES/NO: ")
    
    if name_decision.upper() == "YES":
        name_folder = input("Enter the folder name: ")
    elif name_decision.upper() == "NO":
        name_folder = "avatars"
    else:
        print("Invalid choice. Using default folder name 'avatars'.")
        name_folder = "avatars"
        
    Path(name_folder).mkdir(exist_ok=True)
    with open(f'./{name_folder}/avatar.svg', 'wb') as file:
        file.write(response.content)
        
        

def CACn_save():    # Choose Avatar + Create new folder and save
    print("Choose avatar with https://www.dicebear.com/styles")
    avatar_number = input("Enter avatar number: ")
    response = requests.get(f'https://avatars.dicebear.com/api/male/{avatar_number}.svg') 
    Path('./avatars').mkdir(exist_ok=True)
    with open('./avatars/avatar.svg', 'wb') as file:
        file.write(response.content)


print("-------- A V A T A R     G E N E R A T I O N ----------")
print(" 1 - Random Avatar and save in the main folder")
print(" 2 - Choose Avatar and save in the main folder")
print(" 3 - Random Avatar + Create new folder and save")
print(" 4 - Choose Avatar + Create new folder and save")


choose_option = input("Choose option: ")

if choose_option == "1":
    RAn_save()

elif choose_option == "2":
    CAn_save()
   
elif choose_option == "3":
    RACn_save()

elif choose_option == "4":
    CACn_save()

else:
    print("Invalid choice.Please repeat")
    