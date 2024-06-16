import tkinter as tk

def calculate():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())

        if 1 <= x <= 8 and 1 <= y <= 8:
            is_white = (x + y) % 2 == 0

            if is_white:
                label_result.config(text="Данное поле является белым.")
            else:
                label_result.config(text="Данное поле не является белым (черным)." )
        else:
            label_result.config(text="Ошибка: Введите координаты от 1 до 8." )
    except ValueError:
        label_result.config(text="Ошибка: Введите целые числа." )

root = tk.Tk()
root.title("Программа")

label_x = tk.Label(root, text="Введите координату x (1-8):")
label_x.grid(row=0, column=0)

entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1)

label_y = tk.Label(root, text="Введите координату y (1-8):")
label_y.grid(row=1, column=0)

entry_y = tk.Entry(root)
entry_y.grid(row=1, column=1)

button_calculate = tk.Button(root, text="Расчет", command=calculate)
button_calculate.grid(row=2, column=0, columnspan=2)

label_result = tk.Label(root, text="")
label_result.grid(row=3, column=0, columnspan=2)

root.mainloop()
