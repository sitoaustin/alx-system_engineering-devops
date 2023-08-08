#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
"""
import json
import requests

if __name__ == "__main__":
    employee_Id = 1
    User_Data_Info = requests.get(
        'https://jsonplaceholder.typicode.com/users/'
        .format(employee_Id))
    TOdos_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(employee_Id))
    ListOfTodos = TOdos_response.json()
    UserInfo = User_Data_Info.json()
    newList = []
    newDic = {}
    for i in ListOfTodos:
        # print(i)
        for key, val in i.items():
            if key == 'title' or key == 'completed':
                newList.append('"{}": "{}"'.format(key, val))
                # newDic[key] = val
    # for key, val in UserInfo[0].items():
    #     if key == 'username':
    #         print(key, val)
    print(newList)
    # print(UserInfo[0])
    # print(ListOfTodos)
    # Current_Employee_name = UserInfo['name']
    # newDict = {employee_Id: ListOfTodos}
    # path = '{}.json'.format(employee_Id)
    # with open(path, "w") as csv_file:
    #     json.dump(newDict, csv_file)
#  "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
