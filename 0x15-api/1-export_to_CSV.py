#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
"""
import csv
import requests
import sys

if __name__ == "__main__":
    try:
        employee_Id = sys.argv[1]
        User_Data_Info = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'
            .format(employee_Id))
        TOdos_response = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'
            .format(employee_Id))
        ListOfTodos = TOdos_response.json()
        UserInfo = User_Data_Info.json()
        Current_Employee_name = UserInfo['username']
        totalNumberOfTasks = len(ListOfTodos)
        numberOfCompletedTask = 0
        task_n_status = []
        for todos in ListOfTodos:
            task_n_status.append("'{}','{}','{}','{}'".format(
                employee_Id, Current_Employee_name, todos['completed'],
                todos['title']).split(","))

        path = '{}.csv'.format(employee_Id)
        with open(path, "w", newline='\n') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerows(task_n_status)
    except TypeError as e:
        print("Please enter an Integer")
