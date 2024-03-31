#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tasks = []

def my_list(tasks):
    if not tasks:
        print("There is no tasks.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"{index}. {tasks}")

def add_task(tasks):
    task = input("Please enter a task:")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")

def delete_task(tasks):
  my_list(tasks)
  try:
    tasktodelete = int(input("Enter the task number to delete:"))
    if 1 <= tasktodelete >= 0 and tasktodelete < len(tasks):
      tasks.pop(tasktodelete)
      print(f"Task {tasktodelete} delete from mylist.")
    else:
      print(f"Task #{tasktodelete} was not found.")
  except:
    print("Invalid input.")

if name == "main":
    print("Welcome to the to-do list")
    while True:
        print("Menu:")
        print("1. my list")
        print("2. add a task")
        print("3. delete a task ")
        print("4. Quit")

        options = input("Enter your options(1-4):")

        if(options == "1"):
            my_list(tasks)
        elif(options == "2"):
            add_task(tasks)
        elif(options == "3"):
            delete_task(tasks)
        elif(options == "4"):
            break
        else:
            print("Invalid input.Please try again.")
            print("Goodbye")

