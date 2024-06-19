from tkinter import *


def create_widjets():
    global label_current_status, b_start, b_pause, b_shutdown, img_button_green, img_button_yellow, img_button_gray, img_button_red
    label_status_work = Label(text="Статус работы:", bg="#EDEDED", font=("Inter", 26, "italic"), fg="black")
    label_status_work.place(x=161, y=15)
    label_current_status = Label(text="Выключен", bg="#EDEDED", font=("Inter", 26, "bold"), fg="black")
    label_current_status.place(x=457, y=15)

    canvas.create_rectangle(99, 78, 299, 276, fill="#B7B7B7")
    canvas.create_rectangle(350, 78, 550, 276, fill="#B7B7B7")
    canvas.create_rectangle(601, 78, 801, 276, fill="#B7B7B7")

    img_button_gray = PhotoImage(file="img/button_gray.png")
    img_button_green = PhotoImage(file="img/button_green.png")
    img_button_red = PhotoImage(file="img/button_red.png")
    img_button_yellow = PhotoImage(file="img/button_yellow.png")

    b_start = canvas.create_image(199, 186, image=img_button_gray)
    canvas.tag_bind(b_start, "<Button-1>", lambda event: machine_start())
    b_pause = canvas.create_image(450, 186, image=img_button_gray)
    canvas.tag_bind(b_pause, "<Button-1>", lambda event: machine_pause())
    b_shutdown = canvas.create_image(701, 186, image=img_button_gray)
    canvas.tag_bind(b_shutdown, "<Button-1>", lambda event: machine_shutdown())


def machine_start():
    if label_current_status.cget("text") == "Выключен":
        canvas.itemconfig(b_start, image=img_button_green)
        canvas.itemconfig(b_pause, image=img_button_gray)
        canvas.itemconfig(b_shutdown, image=img_button_gray)
        label_current_status.configure(text="Работает", fg="green")


def machine_pause():
    if label_current_status.cget("text") == "Работает":
        canvas.itemconfig(b_pause, image=img_button_yellow)
        label_current_status.configure(text="Остановлен", fg="yellow")
    elif label_current_status.cget("text") == "Остановлен":
        canvas.itemconfig(b_pause, image=img_button_gray)
        label_current_status.configure(text="Работает", fg="green")


def machine_shutdown():
    global after_func
    label_current_status.configure(text="Выключен", fg="red")
    canvas.itemconfig(b_start, image=img_button_gray)
    canvas.itemconfig(b_pause, image=img_button_gray)
    canvas.itemconfig(b_shutdown, image=img_button_red)
    after_func = canvas.after(1500, lambda: canvas.itemconfig(b_shutdown, image=img_button_gray))


root = Tk()
root.title("Module4")
root.geometry("900x300")
root.resizable(width=False, height=False)
canvas = Canvas(
            height=300,
            width=900,
            )
canvas.place(x=0, y=0)
create_widjets()
root.mainloop()

