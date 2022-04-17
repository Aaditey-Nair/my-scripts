import sys
PATH_TO_TODO_FILE = "/home/user/todo_file.txt"

try:
    with open(PATH_TO_TODO_FILE) as todo_file:
        lines = todo_file.readlines()
        todo_items = [line for line in lines if not line.startswith("[DONE]")]
        done_items = [line for line in lines if line not in todo_items]
except FileNotFoundError:
    with open(PATH_TO_TODO_FILE, "w") as todo_file:
        todo_items = []
        done_items = []


def add_item():
    new_todo = input("Enter the new todo item: ")
    todo_items.append(new_todo)
    print(f"Added new todo '{new_todo}' successfully")


def finish_item():
    done_item_index = int(input("Enter the index of the todo you completed: "))
    done_todo = todo_items[done_item_index - 1]
    done_items.append(f"[DONE] {done_todo}")
    todo_items.remove(done_todo)
    done_todo = done_todo.strip("\n")
    print(f"Marked '{done_todo}' as done")


def delete_item():
    deleted_item_index = int(input("Enter the index of the todo to be deleted: "))
    deleted_item = todo_items[deleted_item_index - 1]
    todo_items.remove(deleted_item)
    print(f"Successfully deleted item")


def print_stats():
    print("TODO:")
    for todo in todo_items:
        todo = todo.strip("\n")
        print(f"  {todo}")
    print("\nDONE:")
    for done_item in done_items:
        done_item = done_item.strip("\n").strip("[DONE] ")
        print(f"  {done_item}")


args = sys.argv
if args[-1] == "new":
    add_item()
elif args[-1] == "done":
    try:
        finish_item()
    except IndexError:
        print("Item does not exist. Please enter a valid index")
elif args[-1] == "del":
    try:
        delete_item()
    except IndexError:
        print("Item does not exist. Please enter a valid index")
elif args[-1] == "stats":
    print_stats()
elif args[-1] == "clear":
    done_items = []
elif args[-1] == "destroy":
    todo_items = []
    done_items = []
elif args[-1] == "help":
    print("""
    Welcome to the CLI ToDo App. Manage all you todos right from the command line.
    Why? 'Cause that's what a programmer does!
    
    All possible command arguments. Eg. ./todo.py, ./todo.py new, ./todo.py stats
    no args   -   View all you todos and their index number
    new       -   Add a new todo to the list
    done      -   Mark a todo as finished
    del       -   Delete a todo by its index number
    stats     -   View all your todos and your finished tasks
    clear     -   Delete you task history
    destroy   -   Delete your todos and your finished tasks 
    """)
else:
    if todo_items:
        for i, item in enumerate(todo_items):
            item_text = item.strip("\n")
            print(f"[{i + 1}] {item_text}")
    else:
        print("No todo items")

with open(PATH_TO_TODO_FILE, "w") as todo_file:
    sections = [todo_items, done_items]
    for section in sections:
        for item in section:
            item = item.strip("\n")
            todo_file.write(f"{item}\n")
