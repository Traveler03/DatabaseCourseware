import tkinter as tk
from tkinter import *
def show_info_page(root):
    # 创建信息页面
    info_page = tk.Toplevel(root)
    info_page.title("信息页面")
    label = tk.Label(info_page, text="这是信息页面")
    label.pack()

def show_classification_page(root):
    # 创建植物分类页面
    classification_page = tk.Toplevel(root)
    classification_page.title("植物分类页面")
    label = tk.Label(classification_page, text="这是植物分类页面")
    label.pack()

def show_maintenance_page(root):
    # 创建养护管理页面
    maintenance_page = tk.Toplevel(root)
    maintenance_page.title("养护管理页面")
    label = tk.Label(maintenance_page, text="这是养护管理页面")
    label.pack()

def show_pest_control_page(root):
    # 创建病虫害防止页面
    pest_control_page = tk.Toplevel(root)
    pest_control_page.title("病虫害防止页面")
    label = tk.Label(pest_control_page, text="这是病虫害防止页面")
    label.pack()

def show_monitoring_page(root):
    # 创建监测管理页面
    monitoring_page = tk.Toplevel(root)
    monitoring_page.title("监测管理页面")
    label = tk.Label(monitoring_page, text="这是监测管理页面")
    label.pack()

def show_add_staff_page(root):
    # 创建增加工作人员页面
    add_staff_page = tk.Toplevel(root)
    add_staff_page.title("增加工作人员页面")
    label = tk.Label(add_staff_page, text="这是增加工作人员页面")
    label.pack()
def open_main_window(root):
    # 创建主界面
    main_window = Toplevel(root)
    main_window.title("管理系统")

    # 设置按钮大小和间隔
    button_width = 20
    button_height = 2
    button_padx = 10
    button_pady = 5

    # 创建按钮
    info_button = tk.Button(main_window, text="信息", width=button_width, height=button_height, padx=button_padx,
                            pady=button_pady, command=show_info_page)
    info_button.grid(row=0, column=0, padx=10, pady=10)

    classification_button = tk.Button(main_window, text="植物分类", width=button_width, height=button_height, padx=button_padx,
                                      pady=button_pady, command=show_classification_page)
    classification_button.grid(row=0, column=1, padx=10, pady=10)

    maintenance_button = tk.Button(main_window, text="养护管理", width=button_width, height=button_height, padx=button_padx,
                                   pady=button_pady, command=show_maintenance_page)
    maintenance_button.grid(row=1, column=0, padx=10, pady=10)

    pest_control_button = tk.Button(main_window, text="病虫害防止", width=button_width, height=button_height, padx=button_padx,
                                    pady=button_pady, command=show_pest_control_page)
    pest_control_button.grid(row=1, column=1, padx=10, pady=10)

    monitoring_button = tk.Button(main_window, text="监测管理", width=button_width, height=button_height, padx=button_padx,
                                  pady=button_pady, command=show_monitoring_page)
    monitoring_button.grid(row=2, column=0, padx=10, pady=10)

    add_staff_button = tk.Button(main_window, text="增加工作人员", width=button_width, height=button_height, padx=button_padx,
                                 pady=button_pady, command=show_add_staff_page)
    add_staff_button.grid(row=2, column=1, padx=10, pady=10)

    main_window.mainloop()
