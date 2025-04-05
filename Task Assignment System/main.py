from Service.task_service import Task_Service
from Service.user_service import User_Service

def main():
    task_service = Task_Service()
    user_service = User_Service()

    user_service.add_user(123, "anshuman", "singhsisodianshuman@gmail.com")

    task_service.create_task(1, "Learn data structure", "Scratch")
    task_service.create_task(2, "Practice data structure", "Scratch")

    print(task_service.complete_task())
    print(task_service.complete_task())
    print(task_service.complete_task())

    history = task_service.get_task_history()

    print("History")
    print((history.pop().title))
    print((history.pop().title))
    
    

if __name__ == "__main__":
    main()