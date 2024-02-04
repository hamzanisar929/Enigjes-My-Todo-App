def get_todos(filepath = "todos.txt"):
    with open(filepath,'r') as file:
        todos = file.readlines()
    return todos


def write(todos_local, filepath = "todos.txt"):
    """ Write the items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

