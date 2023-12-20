import tkinter as tk
from tkinter import *
from tkinter import filedialog
from Factor import dao_factory
FC=dao_factory()
from tkinter import ttk
from classes import fig,plant,plant_pest,plant_fig,user
import datetime
from tkinter import messagebox
import os
import shutil
def create_plant_entry_gui(root,users):
    def save_entry():
        plant_name = name_entry.get()
        image = image_entry.get()
        photographer = photographer_entry.get()
        location = location_entry.get()
        description = description_entry.get()
        # 检查必填项是否有填写
        if plant_name == "":
            tk.messagebox.showerror("错误", "必须输入植物名！")
            return

        # 将空值设为None
        if image == "":
            image = None
        if photographer == "":
            photographer = None
        if location == "":
            location = None
        if description == "":
            description = None
        #对照片进行保存
        dest_folder = "..\\picture"  # 指定保存文件夹路径
        shutil.copy(image, dest_folder)
        filename = os.path.basename(image)  # 获取文件名
        dest_folder += "\\" + filename  # 将文件名添加到文件夹路径后面
        today = datetime.date.today()
        figs=FC.create("fig")
        # 在这里进行保存数据的操作，可以将数据写入文件或者数据库等
        news_fig=fig.fig()
        news_fig.__int__(image_path=dest_folder,image_photographer=photographer,image_location=location,image_description=description)
        figs.insert(news_fig)
        path="..\\\\picture"+"\\\\"+filename
        sql=("select fig_id from fig where fig_path=%s"%dest_folder)
        print(sql)
        fig_id_result=figs.select(sql)
        plant_figs=FC.create("plant_fig")
        new_plant_fig=plant_fig.plant_fig()
        selected_index = name_values.index(plant_name)  # 获取选中值在name_values列表中的索引位置
        plant_id = result[selected_index][0]  # 根据索引位置获取result结果集中的第一列数值
        new_plant_fig.__int__(plant_id=plant_id,image_id=fig_id_result)
        plant_figs.insert(new_plant_fig)
        # 清空输入框
        name_entry.delete(0, tk.END)
        image_entry.delete(0, tk.END)
        photographer_entry.delete(0, tk.END)
        location_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    # 创建子窗口
    window = tk.Toplevel(root)
    window.title("植物信息输入界面")
    plants = FC.create("plant")
    result=plants.select("select plant_id,species_name from plant")
    name_values = [r[1] for r in result]
    # 创建标签和输入框
    name_label = tk.Label(window, text="植物名：")
    name_label.pack()
    # 将查询结果放在植物名的下拉列表框中
    name_entry = ttk.Combobox(window, values=name_values)
    name_entry.pack()

    image_label = tk.Label(window, text="照片：")
    image_label.pack()
    image_entry = tk.Entry(window, state='disabled')
    image_entry.pack()

    def select_image():
        # 打开文件对话框，选择图片文件并复制到指定文件夹
        image_path = filedialog.askopenfilename(initialdir="/", title="选择图片文件",
                                                filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        if image_path:

            image_entry.config(state='normal')  # 允许修改输入框的内容
            image_entry.delete(0, tk.END)  # 清空输入框
            image_entry.insert(0, image_path)  # 将图片路径及名字插入输入框中
            image_entry.config(state='disabled')  # 禁止修改输入框的内容
    browse_button = tk.Button(window, text="浏览", command=select_image)
    browse_button.pack()
    photographer_label = tk.Label(window, text="拍摄人员：")
    photographer_label.pack()
    photographer_entry = tk.Entry(window)
    photographer_entry.pack()

    location_label = tk.Label(window, text="拍摄位置：")
    location_label.pack()
    location_entry = tk.Entry(window)
    location_entry.pack()

    description_label = tk.Label(window, text="图片描述：")
    description_label.pack()
    description_entry = tk.Entry(window)
    description_entry.pack()

    # 创建保存按钮
    save_button = tk.Button(window, text="保存", command=save_entry)
    save_button.pack()

    # 进入主循环
    window.mainloop()
root=Tk()
create_plant_entry_gui(root,None)