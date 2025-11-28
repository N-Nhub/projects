import json

with open("lelist.json", "r") as file:
    tasks_to_do = json.load(file)


tasks_to_do={}

task_amount=int(input("how many tasks do you have to do?\n"))
for i in range(task_amount):
    nameoftask=str(input("whats the name of the task?\n"))
    tasks_to_do[nameoftask]={"done": False}
print (tasks_to_do)

with open("lelist.json", "w") as file:
    json.dump(tasks_to_do, file, indent=4)

def knowtask():
    print(tasks_to_do)

def checktask():
    completed=input("have you completed any tasks?\n")
    if completed=="yes":
        howmanytaskscompleted=int(input("how many then\n"))
        netasks=task_amount-howmanytaskscompleted
        print("you have", netasks, "tasks left")
        whichtaskcompleted=str(input("which task have you completed?\n"))
        tasks_to_do[whichtaskcompleted]["done"] = True

        with open("lelist.json", "w") as f:
            json.dump(tasks_to_do, f, indent=4)
        knowtask()



while True:
    user = input("Check tasks? Type yes to continue or quit to exit: ")
    if user == "quit":
        break
    checktask()

