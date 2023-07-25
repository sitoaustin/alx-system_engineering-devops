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
        employee_Id = int(sys.argv[1])
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
        task_n_status = list(
            filter(lambda x: x.get('userId') == employee_Id, ListOfTodos))
        path = '{}.csv'.format(employee_Id)
        with open(path, "w", newline="\n") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for i in task_n_status:
                writer.writerow(i)
        with open('{}.csv'.format(employee_Id), 'w') as file:
            for todo in task_n_status:
                file.write(
                    '"{}","{}","{}","{}"\n'.format(
                        employee_Id,
                        Current_Employee_name,
                        todo.get('completed'),
                        todo.get('title')
                    )
                )
    except TypeError as e:
        print("Please enter an Integer")
