
try:

        import json
        from pathlib import Path
        tasks= []
        task_to_delete = None
        file_path = Path("/mnt/c/Users/zazozo/desktop/practice/todo.json")
        file_path.touch(exist_ok=True)       #creates the file is it does't exist

        if file_path.exists():
            try:
                with open(file_path, 'r') as todo:
                 tasks = json.load(todo)
                 print(tasks)
            except json.JSONDecodeError:
                print("Warning: tasks.json was corrupted. Starting with an empty list.")

        while True:
 
              print("\n--- To-Do List ---")
              print("1. Add Task")
              print("2. List Tasks")
              print("3. Complete a Task")
              print("4. Delete a Task")
              print("5. Quit")


              option_chosen = input("Enter your option")

              if option_chosen == '1':
                    task_name  = input('input a task you want to add')
                    if task_name:
                         tasks.append({"task": task_name, "done": False})
                         with open(file_path, 'w') as f:
                           json.dump(tasks, f , indent=2)
                           print('task added successfully')
                           

              elif option_chosen =='2':
                   if tasks:
                         print(tasks)
                   else:
                        print("No task found")
                    
              elif option_chosen == '3':
                   if tasks:
                        print(tasks)
                        set_complete = input("Enter a task you want to set complete")
                        for i in tasks:
                            
                             if i['task'] == set_complete:
                                  i["done"] = True
                                  print("task updated")
                                  with open(file_path, 'w') as f:
                                   json.dump(tasks, f, indent=2)
                                   
                                  break
                        else:
                            print("there is no such task")

              elif option_chosen == "4":
                    if tasks:
                        print(tasks)
                        remove_task = input("Enter task you want to delete")
                        for i in tasks:
                            if i["task"] == remove_task:
                                task_to_delete = i
                                break
                        else:
                            print("There is no such task")

                        if task_to_delete:
                            tasks.remove(task_to_delete)
                            with open(file_path, 'w') as f:
                                json.dump(tasks, f, indent=2)
                            print('task deleted successfully')
                            task_to_delete = None
                    else:
                        print("No task found")

              elif option_chosen == "5":
                    print('Goodbye')
                    break
               
                     
except Exception as e:
        print(e)