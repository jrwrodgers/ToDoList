import pickle
import tkinter as tk
import datetime


# compare_time = datetime.datetime(2024, 3, 29,0,0,0)
# print(now.strftime("%d-%m-%Y"))
# delta_days=compare_time-now
# print(f"{delta_days.days} days")
class ToDoItem:

    def __init__(self, description, due_date, date_entered, todo_id):
        self.description = description
        self.due_date = datetime.datetime.strptime(due_date, "%d/%m/%Y")
        self.date_entered = date_entered
        self.date_completed = None
        self.id = todo_id
        self.list_name = None

    def __str__(self):
        return f"{self.description} is due on the {self.due_date:%d/%m/%Y} that is in {(self.due_date - now).days} days"

# starter_list=[]
# starter_list.append(ToDoItem("Item 1 description", "25/03/2024", datetime.datetime.now(), 1))
# starter_list.append(ToDoItem("Item 2 description", "26/03/2024", datetime.datetime.now(), 2))
# starter_list.append(ToDoItem("Item 3 description", "27/03/2024", datetime.datetime.now(), 3))
# starter_list.append(ToDoItem("Item 4 description", "28/03/2024", datetime.datetime.now(), 4))
# starter_list.append(ToDoItem("Item 5 description", "29/03/2024", datetime.datetime.now(), 5))
# starter_list[4].list_name="archive"
# starter_list[4].date_completed=datetime.datetime.now()
# starter_list[1].list_name="archive"
# starter_list[1].date_completed=datetime.datetime.now()

# with open("data.mytodo", "wb") as f:
#     pickle.dump(starter_list, f)

# for item in todo_list:
#     print(item)

# Read in ToDo List
# Print ToDo List
# Get list properties
# check list integrity
# save list to pickle
# options

# 1- Mark complete
# 2- Mark incomplete
# 3- create new entry
# 4- edit and entr
# 5- move entry up or down
# 6- archive entries that are complete

def archive_button_press(todo_list, c_states):
    print("pressed archive button")
    for i in range(len(todo_list)):
        if todo_list[i].list_name != "archive":
            # print(f"{c_states[i].get()} > {todo_list[i].description}")
            if c_states[i].get() == 1:
                todo_list[i].list_name = "archive"
                todo_list[i].date_completed = now
    clear_frame()
    draw_todo_list()

def unarchive_button_press(todo_list, c_states):
    print("pressed unarchive button")
    for i in range(len(todo_list)):
        if todo_list[i].list_name == "archive":
            # print(f"{c_states[i].get()} > {todo_list[i].description}")
            if c_states[i].get() == 1:
                todo_list[i].list_name = None
                todo_list[i].date_completed = None
    clear_frame()
    draw_todo_list()


def draw_todo_list():
    comment_text = tk.Label(master=root, text=" To Do List :", font=("Arial", 10, 'bold', 'underline'),
                            bg='lightyellow')
    comment_text.grid(row=0, column=0, columnspan=2, sticky="w")
    # get list lengths

    list_len1 = 0
    list_len2 = 0
    c = []
    c_states = []
    for i in range(len(todo_list)):
        if (todo_list[i].list_name != "archive"):
            text_description = "" + todo_list[i].description + " due in " + str(
                (todo_list[i].due_date - now).days) + " days"
            c_states.append(tk.IntVar())
            c.append(tk.Checkbutton(root, variable=c_states[list_len1], text=text_description, bg='lightyellow'))
            c[list_len1].grid(row=i + 1, column=0, columnspan=2, sticky="w")
            list_len1 += 1
    archive_button = tk.Button(root, text="Archive checked", command=lambda: archive_button_press(todo_list, c_states))
    archive_button.grid(row=list_len1 + 1, column=0, columnspan=1)
    comment_text = tk.Label(master=root, text=" Archive :", font=("Arial", 10, 'bold', 'underline'), bg='lightyellow')
    comment_text.grid(row=list_len1 + 2, column=0, columnspan=2, sticky="w")
    for i in range(len(todo_list)):
        if (todo_list[i].list_name == "archive"):
            text_description = "" + todo_list[i].description + " completed " + str(
                todo_list[i].date_completed) + " days"
            c_states.append(tk.IntVar())
            c.append(
                tk.Checkbutton(root, variable=c_states[list_len1 + list_len2], text=text_description, bg='lightyellow',
                               font=("Arial", 9, 'overstrike')))
            c[list_len1 + list_len2].grid(row=i + list_len2 + 3, column=0, columnspan=2, sticky="w")
            list_len2 += 1
    unarchive_button = tk.Button(root, text="Unarchive checked",
                                 command=lambda: unarchive_button_press(todo_list, c_states))
    unarchive_button.grid(row=list_len1 + list_len2 + 4, column=0, columnspan=1)
    print(list_len1, list_len2)

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()

# checkbutton widget
# if __name__ == "__main__":

datafile = "data.mytodo"
with open(datafile, "rb") as f:
    todo_list = pickle.load(f)
print("Starting ToDoList App")
# print(len(todo_list))
now = datetime.datetime.now()
root = tk.Tk()
root.configure(bg='lightyellow')
root.title('')
root.geometry('270x250')
#root.resizable(0, 0)
draw_todo_list()
root.mainloop()