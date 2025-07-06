from datetime import datetime
import os
import json
from tabulate import tabulate


print("TO DO APP")
base_path = os.path.dirname(os.path.abspath(__file__))
file_path_json = os.path.join(base_path,"task.json")


def create_task():
    all_tasks = []
    task = input("WRITE YOUR TASK ")
    current_time = datetime.now()
    date = current_time.strftime("%d/ %m/ %Y")
    
    new_task = [task,date]

    if os.path.exists(file_path_json):
        with open(file_path_json,'r') as file:
            try:
                all_tasks = json.load(file)
            except:
                all_tasks = []

    all_tasks.append(new_task)

    with open(file_path_json,'w') as file:
        json.dump(all_tasks,file)
    print("saved successfully")
    


def view_tasks():
    data =[]
    #view tasks by fetching from json file
    with open(file_path_json,'r') as file:
        all_tasks = json.load(file)
    print(all_tasks)

    headers =["task","date"]
    print(tabulate(all_tasks,headers = headers,tablefmt = "grid"))
    #what is the error in this?


while True:
    print("1. CREATE TASK\n2. VIEW TASKS\n 3.EXIT")
    user_response = int(input("Enter your choice"))

    if user_response == 1:
        create_task()
    if user_response == 2:
        view_tasks()
    if user_response == 3:
        break