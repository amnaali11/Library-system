from tkinter import *
from tkinter import messagebox


def save_book():
    if input_name.get() != "" and input_discription.get() != "" and input_title.get() != "" and input_id.get() != "":
        new_line = f"{input_id.get()}"+f"-{input_title.get()}" + \
            f"-{input_name.get()}"+f"-{input_discription.get()}"+"\n"
        addline = open("data.txt", "a+")
        # addline.write("\n")
        addline.write(new_line)
        addline.close()
        add.destroy()
        root.destroy()
        window()


def add_book():
    global add

    add = Tk()
    add.title("Adding new book")
    add.geometry("600x600+80+80")
    j = Label(add, text="add  a new book ", font=(
        'Arail', 20, 'bold'), fg='lightblue')
    j.pack(padx=10, pady=20)
    #

    global input_name
    global input_title
    global input_discription
    global input_id

    id = Label(add, text="ID:", font=('Arail', 16, 'bold'), fg='lightblue')
    id.pack(padx=10, pady=7)
    input_id = Entry(add, textvariable=id, font=('Arail', 15))
    input_id.pack(padx=10, pady=7)
    #
    title = Label(add, text="Title:", font=(
        'Arail', 16, 'bold'), fg='lightblue')
    title.pack(padx=10, pady=7)
    input_title = Entry(add, width=18, textvariable=title, font=('Arail', 16))
    input_title.pack(padx=10, pady=7)
    #
    name = Label(add, text="Author Name:", font=(
        'Arail', 15, 'bold'), fg='lightblue')
    name.pack(padx=10, pady=7)
    input_name = Entry(add, textvariable=name, font=('Arail', 15))
    input_name.pack(padx=10, pady=7)
    #
    discription = Label(add, text="Discription:", font=(
        'Arail', 16, 'bold'), fg='lightblue')
    discription.pack(padx=10, pady=7)
    input_discription = Entry(
        add, textvariable=discription, font=('Arail', 15))
    # print(input_discription)
    input_discription.pack(padx=10, pady=10)
    # add here save function

    save_button = Button(add, width=16, text="Save", bg='lightblue', font=(
        'Arail', 16, 'bold'), command=save_book)
    save_button.pack(padx=10, pady=10)
    add.mainloop()


class Table():

    def __init__(self, frame):

        book_file = open("data.txt", "r+")
        book_list = []
        line = []
        lines = book_file.readlines()

        for key in lines:
            line = key.split("-")
            book_list.append(line)
        book_file.close()
        rows = len(book_list)
        columns = len(book_list[0])

        for i in range(rows):
            for j in range(columns):
                if i == 0:
                    self.entry = Entry(
                        frame, width=20, bg='lightblue', fg='black', font=('Arail', 16, 'bold'))
                else:
                    self.entry = Entry(
                        frame, width=20, fg='black', font=('Arail', 16, 'bold'))
                self.entry.grid(row=i, column=j)
                self.entry.insert(END, book_list[i][j])


# create root window
def window():
    global root
    root = Tk()
    root.title("the library")
    root.geometry('1000x800+10+10')

    def about():
        messagebox.showinfo(
            'our library', 'the library Guides aims at providing best practical tutorials')

    menubar = Menu(root, background='lightblue', foreground='black',
                   activebackground='white', activeforeground='black')
    Books = Menu(menubar, tearoff=0,
                 background='lightblue', foreground='black')
    Books.add_command(label="New Books")
    Books.add_command(label="Arabic Books")
    Books.add_command(label="English Books")
    Books.add_command(label="Show")
    Books.add_separator()
    Books.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="Books", menu=Books)

    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="Undo")
    edit.add_separator()
    edit.add_command(label="Cut")
    edit.add_command(label="Copy")
    edit.add_command(label="Paste")
    menubar.add_cascade(label="Edit", background='lightblue', menu=edit)

    help = Menu(menubar, tearoff=0)
    help.add_command(label="About", background='lightblue', command=about)
    menubar.add_cascade(label="Help", background='lightblue', menu=help)
    root.config(menu=menubar)
    l = Label(root, text="___welcome to our python library___",
              font=('Arail', 24 , 'bold'), pady=20)
    l.pack()
    frame = Frame(root)
    frame.pack(padx=10, pady=50)
    table = Table(frame)
    button = Button(root, text="Add new book", bg='lightblue',
                    font=('Arail', 16, 'bold'), command=add_book)
    button.pack()
    root.mainloop()


window()
