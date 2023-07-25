#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
"""
import requests
import json
import sys

if __name__ == "__main__":
    employee_Id = sys.argv[1]
    User_Data_Info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(employee_Id))
    TOdos_response = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'
        .format(employee_Id))
    ListOfTodos = TOdos_response.json()
    UserInfo = User_Data_Info.json()
    Current_Employee_name = UserInfo['name']
    newDict = {employee_Id: ListOfTodos}
    path = '{}.json'.format(employee_Id)
    with open(path, "w") as csv_file:
        json.dump(newDict, csv_file)
