tasks = []

def createTask(task: object):
    tasks.append(task)

    return task

def deleteTask(id: str):
    return 'task deleted'
    

def viewAllTask():
    return tasks

def viewATask(id: str):
    return 'here is the task'
    

def markAsComplete(id: str):
    return tasks
    

def editTask(id: str):
    return 'edited task'
    