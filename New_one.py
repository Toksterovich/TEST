#
# CODE = 1234
#
# def check_rest():
#     print(bankomat)
#
# import tkinter as tk
# win = tk.Tk()
# win.title('BCHBank')
# win.geometry('500x500')
#
#
# label_main = tk.Label(win, text='BCHBank',
#                    bg='red',
#                    fg='white',
#                    font=('Arial', 15, 'bold'),
#                    )
#
# label_pin = tk.Label(win, text='Введите код')
#
# name_pin = tk.Entry(win)
#
# def output_money():
#     add_label_sum()
#     add_entry_sum()
#     add_button_sum()
#
# def count():
#     num = entry_sum
#     for key in bankomat.keys():
#         a = int(num // key)
#         num -= a*key
#         bankomat[key] -= a
#         if a != 0:
#             tk.Label(win, text=(f"Получите номинал", {key}, "в количестве", {a})).pack()
#
#
# bankomat = {
#     100: 100,
#     50: 100,
#     20: 100,
#     10: 100,
#     5: 100,
#     2: 100,
#     1: 100
# }
#
# def add_label_error():
#     label_error = tk.Label(win, text='Неправильный код')
#     label_error.pack
#
# def add_label_sum():
#     label_sum = tk.Label(win, text='Введите сумму')
#     label_sum.pack
#
# def add_entry_sum():
#     global entry_sum
#     entry_sum = tk.Entry(win)
#     entry_sum.pack
#
# def add_button_sum():
#     button_sum = tk.Button(win, text='Ввод', command=count)
#     button_sum.pack
#
# def enter_pin():
#     if name_pin == CODE:
#         output_money
#     else:
#         add_label_error
#         enter_pin
#
# button_pin = tk.Button(win, text='Ввод',
#                      command=enter_pin,
#                      )
#
# # win.grid_columnconfigure(0)
# # win.grid_columnconfigure(1)
# label_main.pack()
# label_pin.pack()
# name_pin.pack()
# button_pin.pack()
# win.mainloop()
