import pickle
import tkinter as tk
import datetime
from git import Repo



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
# starter_list.append(ToDoItem("Item 1 description this is a test to see if the wrapping works", "25/03/2024", datetime.datetime.now(), 1))
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
            if c_states[i].get() == 1:
                todo_list[i].list_name = "archive"
                todo_list[i].date_completed = now
    clear_frame()
    draw_todo_list()

def unarchive_button_press(todo_list, c_states):
    print("pressed unarchive button")
    for i in range(len(todo_list)):
        if todo_list[i].list_name == "archive":
            if c_states[i].get() == 1:
                todo_list[i].list_name = None
                todo_list[i].date_completed = None
    clear_frame()
    draw_todo_list()
def add_button_press(todo_list):
    print("pressed add button")
    for i in range(len(todo_list)):
        print("here")
    clear_frame()
    draw_todo_list()
def delete_button_press(todo_list, c_states):
    print("pressed delete button")
    for i in range(len(todo_list)):
        if c_states[i].get() == 1:
            todo_list.pop(i)
    clear_frame()
    draw_todo_list()

def up_button_press(todo_list, c_states):
    print("pressed up button")
    index_1=0
    index_2=0
    for i in range(len(todo_list)):
        if c_states[i].get() == 1:
            index_2=i
    if index_2 !=0:
        b_above=False
        index_1 = index_2 - 1
        while b_above:
            pass
        else:
            if todo_list[index_1].list_name == "archive":
                index_1-=1
                # if index_1==0:
                #     index_1+=2
                #     b_above = True
            else:
                b_above=True
        print("moving",index_2,index_1)

    todo_list[index_1],todo_list[index_2]=todo_list[index_2],todo_list[index_1]
    clear_frame()
    draw_todo_list()

def down_button_press(todo_list, c_states):
    print("pressed down button")
    index_1=0
    index_2=0
    for i in range(len(todo_list)):
        if c_states[i].get() == 1:
            index_2=i
    if index_2 != len(todo_list):
        #if index_2 + 1 != "archive"
        index_1 = index_2 + 1

    todo_list[index_1],todo_list[index_2]=todo_list[index_2],todo_list[index_1]
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
            c.append(tk.Checkbutton(root, variable=c_states[list_len1], text=text_description, bg='lightyellow',
                                        wraplength=200))
            c[list_len1].grid(row=i + 1, column=0, columnspan=2, sticky="w")
            list_len1 += 1
    archive_button = tk.Button(root, text="Archive checked", command=lambda: archive_button_press(todo_list, c_states))
    archive_button.grid(row=list_len1 + 1, column=0, columnspan=1,sticky="w")

    add_button = tk.Button(root, text="Add", command=lambda: add_button_press(todo_list))
    add_button.grid(row=list_len1 + 1, column=1, columnspan=1, sticky="w")

    delete_button = tk.Button(root, text="Delete", command=lambda: delete_button_press(todo_list, c_states))
    delete_button.grid(row=list_len1 + 1, column=2, columnspan=1,sticky="w")

    up_button = tk.Button(root, text="Up", command=lambda: up_button_press(todo_list, c_states))
    up_button.grid(row=list_len1 + 1, column=3, columnspan=1, sticky="w")

    down_button = tk.Button(root, text="Down", command=lambda: down_button_press(todo_list, c_states))
    down_button.grid(row=list_len1 + 1, column=4, columnspan=1, sticky="w")

    comment_text = tk.Label(master=root, text=" Archive :", font=("Arial", 10, 'bold', 'underline'), bg='lightyellow')
    comment_text.grid(row=list_len1 + 2, column=0, columnspan=2, sticky="w")
    for i in range(len(todo_list)):
        if (todo_list[i].list_name == "archive"):
            text_description = "" + todo_list[i].description + " completed " + str(
                todo_list[i].date_completed.strftime("%d-%m-%Y"))
            c_states.append(tk.IntVar())
            c.append(
                tk.Checkbutton(root, variable=c_states[list_len1 + list_len2], text=text_description, bg='lightyellow',
                               font=("Arial", 9, 'overstrike'),wraplength=200))
            c[list_len1 + list_len2].grid(row=list_len2 + list_len1 + 3, column=0, columnspan=2, sticky="w")
            list_len2 += 1
    unarchive_button = tk.Button(root, text="Unarchive checked",
                                 command=lambda: unarchive_button_press(todo_list, c_states))
    unarchive_button.grid(row=list_len1 + list_len2 + 5, column=0, columnspan=1)
    #print(list_len1, list_len2)

def clear_frame():
    for widgets in root.winfo_children():
        widgets.destroy()

# checkbutton widget
if __name__ == "__main__":

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