import tkinter as tk
from tkinter import *
from Factor import dao_factory
FC=dao_factory()
from classes import fig,plant,plant_pest,plant_fig,user,region
import datetime
from tkinter import messagebox
from tkinter import ttk
def create_plant_entry_gui(root,users):
    def save_entry():
        plant_name = name_entry.get()
        aliases = alias_entry.get()
        characteristics = characteristics_entry.get()
        value = value_entry.get()
        classification = classification_entry.get()
        province = province_combobox.get()
        city=city_combobox.get()
        county=county_combobox.get()
        environment = environment_entry.get()
        techniques=techniques_entry.get()
        # 检查必填项是否有填写
        if plant_name == "":
            tk.messagebox.showerror("错误", "必须输入植物名！")
            return

        # 将空值设为None
        if aliases == "":
            aliases = None
        if characteristics == "":
            characteristics = None
        if value == "":
            value = None
        if classification == "":
            classification = None
        if province == "":
            region = None
        if city == "":
            region = None
        if county == "":
            region = None
        if environment == "":
            environment = None
        if techniques=="":
            techniques=None
        today = datetime.date.today()
        # 在这里进行保存数据的操作，可以将数据写入文件或者数据库等
        plants=FC.create("plant")
        new_plant=plant.plant()
        new_plant.__int__(species_name=plant_name,alies=aliases,morphology=characteristics,value=value,key_tech=techniques,environment=environment,created_by=users._user_name,created_at=today,updated_at=today)
        plants.insert(new_plant)
        # 清空输入框
        name_entry.delete(0, tk.END)
        alias_entry.delete(0, tk.END)
        characteristics_entry.delete(0, tk.END)
        value_entry.delete(0, tk.END)
        classification_entry.delete(0, tk.END)
        province_combobox.delete(0, tk.END)
        city_combobox.delete(0, tk.END)
        county_combobox.delete(0, tk.END)
        environment_entry.delete(0, tk.END)
        techniques_entry.delete(0,tk.END)
    # 创建子窗口
    window = tk.Toplevel(root)
    window.title("植物信息输入界面")

    # 创建标签和输入框
    name_label = tk.Label(window, text="植物名：")
    name_label.pack()
    name_entry = tk.Entry(window)
    name_entry.pack()

    alias_label = tk.Label(window, text="别名：")
    alias_label.pack()
    alias_entry = tk.Entry(window)
    alias_entry.pack()

    characteristics_label = tk.Label(window, text="形态特征：")
    characteristics_label.pack()
    characteristics_entry = tk.Entry(window)
    characteristics_entry.pack()

    value_label = tk.Label(window, text="应用价值：")
    value_label.pack()
    value_entry = tk.Entry(window)
    value_entry.pack()

    classification_label = tk.Label(window, text="分类：")
    classification_label.pack()
    classification_entry = tk.Entry(window)
    classification_entry.pack()

    selected_province = tk.StringVar()
    selected_city = tk.StringVar()
    selected_county = tk.StringVar()
    regions=FC.create("region")
    new_region = region.region()
    provinces=regions("select region_id,region_name where rank=0")
    province_label = ttk.Label(root, text="省份：")
    province_label.pack(row=0, column=0, padx=10, pady=10)

    province_combobox = ttk.Combobox(root, textvariable=selected_province, values=provinces[1:2])
    province_combobox.pack(row=0, column=1, padx=10, pady=10)

    city_label = ttk.Label(root, text="城市：")
    city_label.pack(row=1, column=0, padx=10, pady=10)

    city_combobox = ttk.Combobox(root, textvariable=selected_city, state="disabled")
    city_combobox.pack(row=1, column=1, padx=10, pady=10)

    county_label = ttk.Label(root, text="县：")
    county_label.pack(row=2, column=0, padx=10, pady=10)

    county_combobox = ttk.Combobox(root, textvariable=selected_county, state="disabled")
    county_combobox.pack(row=2, column=1, padx=10, pady=10)

    def province_selected(event):
        selected_province_value = selected_province.get()
        if selected_province_value != "请选择省份" :
            selected_index = provinces.index(selected_province_value)
            cities=regions("select region_id,region_name where rank=1 and parent=%d",provinces[selected_index][0])
            cities_list = cities[selected_province_value]
            city_combobox.config(state="normal")
            city_combobox['values'] = cities_list
        else:
            city_combobox.set("")
            city_combobox.config(state="disabled")
            county_combobox.set("")
            county_combobox.config(state="disabled")

    def city_selected(event):
        selected_city_value = selected_city.get()
        if selected_city_value != "请选择城市":
            selected_index = provinces.index(selected_city_value)
            counties = regions("select region_id,region_name where rank=2 and parent=%d", cities[selected_index][0])
            counties_list = counties[selected_city_value]
            county_combobox.config(state="normal")
            county_combobox['values'] = counties_list
        else:
            county_combobox.set("")
            county_combobox.config(state="disabled")

    province_combobox.bind("<<ComboboxSelected>>", province_selected)
    city_combobox.bind("<<ComboboxSelected>>", city_selected)

    environment_label = tk.Label(window, text="生长环境：")
    environment_label.pack()
    environment_entry = tk.Entry(window)
    environment_entry.pack()

    techniques_label = tk.Label(window, text="栽培技术要点：")
    techniques_label.pack()
    techniques_entry = tk.Entry(window)
    techniques_entry.pack()
    # 创建保存按钮
    save_button = tk.Button(window, text="保存", command=save_entry)
    save_button.pack()

    # 进入主循环
    window.mainloop()
