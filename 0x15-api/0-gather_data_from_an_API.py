# !/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    try:
        employee_Id = sys.argv[1]
        User_Data_Info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_Id))
        TOdos_response = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_Id))
        ListOfTodos = TOdos_response.json()
        UserInfo = User_Data_Info.json()
        Current_Employee_name = UserInfo['name']
        totalNumberOfTasks = len(ListOfTodos)
        numberOfCompletedTask = 0
        List_of_completed_tasks = []
        for i in ListOfTodos:
            if i['completed'] == True:
                List_of_completed_tasks.append(i['title'])
                numberOfCompletedTask = numberOfCompletedTask + 1
        print('Employee {} is done with tasks({}/{}):'.format(Current_Employee_name, numberOfCompletedTask, totalNumberOfTasks ))
        for completedTask in List_of_completed_tasks:
            print('\t{}'.format(completedTask))
    except:
        print("Please enter an Integer")

