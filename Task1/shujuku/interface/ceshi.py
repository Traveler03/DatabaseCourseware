from tkinter import *
import tkinter as tk
import chardet
from tkinter import ttk, scrolledtext
from classes import fig, plant, plant_pest, plant_fig, user
from interface.registration import open_register_window
import Factor
FC=Factor.dao_factory()
class Pagination:
    def __init__(self, data, page_size):
        self.data = data
        self.page_size = page_size
        self.total_pages = (len(data) + page_size - 1) // page_size

    def get_page(self, page):
        start_index = (page - 1) * self.page_size
        end_index = start_index + self.page_size
        return self.data[start_index:end_index]


def display_detail(event,table,result):
    item = table.focus()
    row = table.index(item)
    column = table.identify_column(event.x)  # 获取鼠标点击的列
    column_index = int(column[1:]) - 1  # 根据列的ID计算出索引
    detail = result[row-1][column_index]  # 获取对应列的详细信息

    detail_window = tk.Toplevel()
    detail_window.title("详细信息")

    # 创建滚动文本区域显示详细信息
    text_area = scrolledtext.ScrolledText(detail_window, wrap=tk.WORD, width=50, height=10)
    text_area.insert(tk.INSERT, detail)
    text_area.pack(padx=10, pady=10)

def display_data(table, page_number):
    plants=FC.create("plant")
    result = plants.select("select species_name,alia,morphology,value,key_tech,environment from plant")
    # 分页显示数据
    pagination = Pagination(result, page_size=10)
    current_page = pagination.get_page(page_number)
    # 在界面中创建表格
    table = ttk.Treeview(table)
    table['columns'] = ("PlantName", "Alias", "Description", "Cultivation", "Value", "Environment")  # 列名
    table.column("#0", width=0, stretch=tk.NO)  # 隐藏第一列
    table.column("PlantName", anchor=tk.CENTER, width=100)
    table.column("Alias", anchor=tk.CENTER, width=100)
    table.column("Description", anchor=tk.CENTER, width=200)
    table.column("Cultivation", anchor=tk.CENTER, width=200)
    table.column("Value", anchor=tk.CENTER, width=100)
    table.column("Environment", anchor=tk.CENTER, width=150)

    table.heading("#0", text='', anchor=tk.CENTER)
    table.heading("PlantName", text="植物名", anchor=tk.CENTER)
    table.heading("Alias", text="别名", anchor=tk.CENTER)
    table.heading("Description", text="形态特征", anchor=tk.CENTER)
    table.heading("Value", text="应用价值", anchor=tk.CENTER)
    table.heading("Cultivation", text="栽培要点", anchor=tk.CENTER)
    table.heading("Environment", text="生长环境", anchor=tk.CENTER)

    for row in current_page:
        # 对text类型的列进行截断
        row = list(row)
        for i in range(1, len(row)):
            if isinstance(row[i], str) and len(row[i]) > 20:
                row[i] = row[i][:20] + '...'
        table.insert("", tk.END, values=row)
    table.bind("<Double-1>", lambda event: display_detail(event, table,current_page))
    table.pack()
    return pagination


def plant_main_window(root):
    table = tk.Toplevel(root)
    table.title("植物信息页面")

    # 生成数据并直接显示
    result = display_data(table, 1)
    if not result:  # 数据为空，直接返回
        return
    pagination = result

    # 创建分页按钮
    page_frame = ttk.Frame(table)
    page_frame.pack(pady=10)

    def generate_page_buttons():
        for i in range(1, pagination.total_pages + 1):

            button = ttk.Button(page_frame, text=str(i), command=lambda page=i: display_data(table, page))
            button.grid(row=0, column=i - 1, padx=5, pady=5)

    generate_page_buttons()
    table.mainloop()
root = Tk()
plant_main_window(root)
