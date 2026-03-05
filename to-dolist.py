# add tasks, setdeadlines, assign priorities, and filter by projects or tags 
class Task:
    def __init__(self,title,deadline):

        self.title = title
        self.deadline = deadline
    def show_Task(self):
        print("Task:", self.title)
        print("Deadline:", self.deadline)
class PriorityTask(Task):
    def __init__(self, title, deadline, priority, project, tag):
        super().__init__(title, deadline)
        self.priority = priority
        self.project = project
        self.tag = tag
    def show_Task(self):
        print("\nTitle:", self.title)  
        print("Priority:", self.priority)
        print("Project:", self.project)
        print("Tag:", self.tag)
        print("Deadline:", self.deadline)
class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")
    def show_tasks(self):
        for task in self.tasks:
            print("\n Your Tasks:")
            task.show_Task()
    def filter_by_project(self, project):
        print("\nTasks in Project:", project)
        for task in self.tasks:
            if task.project == project:
                task.show_Task()
    def filter_by_tag(self, tag):
        print("\nTasks with Tag:", tag)
        for task in self.tasks:
            if task.tag == tag:
                task.show_Task()
td = ToDoList()
while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Filter by Project")
        print("4. Filter by Tag")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            deadline = input("Enter deadline (DD-MM-YYYY): ")
            priority = input("Enter priority (High/Medium/Low): ") 
            project = input("Enter project name: ")
            tag = input("Enter tag: ")
            task = PriorityTask(title, deadline, priority, project, tag)
            td.add_task(task)
        elif choice == "2":
            td.show_tasks()
        elif choice == "3":
            project = input("Enter project name to filter: ")
            td.filter_by_project(project)
        elif choice == "4":
            tag = input("Enter tag to filter: ")
            td.filter_by_tag(tag)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")
        
            