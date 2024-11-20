# Продукт Dany's computer software comp.
from random import choice
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


# Функция генерации пароля
def generate_password():
    try:
        # Проверка длины пароля
        length = int(entry_length.get())
        if length < 8:
            messagebox.showerror("Ошибка", "Вы выбрали слишком маленькое число. Минимум - 8.")
            return
        if length > 30:
            messagebox.showerror("Ошибка", "Вы выбрали слишком большое число. Максимум - 30.")
            return

        # Проверка выбрана ли кириллица
        if use_special_symbols_2.get():
            numbers_main_use = numbers_rus
        else:
            numbers_main_use = numbers_main

        # Проверка выбраны ли дополнительные символы
        if use_special_symbols.get():
            numbers_main_use += numbers_dop

        # Генерация пароля длину которого мы указали, выбор случайного символа из списка
        password = ''.join(choice(numbers_main_use) for _ in range(length))
        entry_password.delete(0, END)  # Очищает текстовое поле для пароля
        entry_password.insert(0, password)  # Вставляет сгенерированный пароль в текстовое поле
    except ValueError:
        # Вызов ошибки если введено некорректное число
        messagebox.showerror("Ошибка", "Пожалуйста, введите корректное число.")


# Функция для копирования пароля в буфер обмена
def copy_to_clipboard():
    window.clipboard_clear()  # Очищает текущий буфер обмена
    window.clipboard_append(entry_password.get())  # Добавляет содержимое текстового поля с паролем в буфер обмена
    messagebox.showinfo("Информация", "Пароль успешно скопирован.")  # Вызов сообщения, что пароль был скопирован


# Функция для сохранения пароля в файл
def save_password_to_file():
    password = entry_password.get()  # Получение пароля из текстового поля
    # Проверка, есть ли сгенерированный пароль
    if not password:
        messagebox.showerror("Ошибка", "Сначала сгенерируйте пароль.")
        return
    # Открытие окна сохранения файла
    file_way = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_way:
        # Открытие файла и запись туда пароля
        with open(file_way, 'w') as file:
            file.write(password)
        messagebox.showinfo("Информация", f"Пароль сохранен в файл:\n{file_way}")  # Показ сообщения, что пароль успешно сохранен в файл


# Параметры окна
window = Tk()  # Создание окна
window.title("Генератор паролей DCS comp.")  # Название
window.geometry('350x350')  # Размер
window.resizable(width=False, height=False)  # Масштабирование не используется
window.configure(bg="#2e2e2e")  # Цвет
window.iconbitmap('icon/password.ico')  # Иконка

# Наборы символов
numbers_main = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
numbers_rus = 'йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ0123456789'
numbers_dop = "@!?{}[]().,/_-+=*:;%"

# Надпись для ввода длины пароля
label = Label(window, text="Длина пароля\n(от 8 до 30)", font="Roboto 18", bg="#2e2e2e", fg="white")
label.place(relx=0.35, y=50, anchor=CENTER)

# Поле для ввода длины пароля
entry_length = Entry(window, font="Roboto 24", width=4)
entry_length.place(relx=0.73, y=50, anchor=CENTER)

# Чекбокс для использования дополнительных символов
use_special_symbols = BooleanVar()
checkbox_1 = Checkbutton(window, text="Использовать доп. символы     ", font="Roboto 13", variable=use_special_symbols, bg="#2e2e2e", fg="white", selectcolor="black")
checkbox_1.place(relx=0.495, y=110, anchor=CENTER)

# Чекбокс для использования кириллицы
use_special_symbols_2 = BooleanVar()
checkbox_2 = Checkbutton(window, text="Использовать буквы кириллицы", font="Roboto 13", variable=use_special_symbols_2, bg="#2e2e2e", fg="white", selectcolor="black")
checkbox_2.place(relx=0.5, y=135, anchor=CENTER)

# Кнопка для генерации пароля
button = Button(window, text="Сгенерировать", font="Roboto 18", width=19, command=generate_password)
button.place(relx=0.5, y=190, anchor=CENTER)

# Поле для вывода сгенерированного пароля
entry_password = Entry(window, font="Roboto 18", width=21)
entry_password.place(relx=0.5, y=240, anchor=CENTER)

# Кнопка для копирования пароля в буфер обмена
copy_button = Button(window, text="Копировать", font="Roboto 18", width=9, command=copy_to_clipboard)
copy_button.place(relx=0.701, y=290, anchor=CENTER)

# Кнопка для сохранения пароля в файл
save_button = Button(window, text="Сохранить", font="Roboto 18", width=9, command=save_password_to_file)
save_button.place(relx=0.3, y=290, anchor=CENTER)

window.mainloop()
