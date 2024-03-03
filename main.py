
class ToDo():
    def __init__(self, number, item, deadline):
        self.number = number
        self.item = item
        self.date_entered = "01/01/2023"
        self.deadline = deadline
        self.list = list


if __name__ == "__main__":
    todo_list=[]
    for i in range(5):
        todo_list.append(ToDo(i,"20/05/2023"))

    temp=vars(todo_list[0])
    for item in temp:
        print(item, ' : ', temp[item])

