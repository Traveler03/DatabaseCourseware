import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("地区选择")

# 定义省份、城市和县的数据
provinces = ["请选择省份", "北京市", "上海市", "广东省", "江苏省"]
cities = {
    "北京市": ["请选择城市", "北京市辖区"],
    "上海市": ["请选择城市", "上海市辖区"],
    "广东省": ["请选择城市", "广州市", "深圳市", "珠海市"],
    "江苏省": ["请选择城市", "南京市", "苏州市", "无锡市"]
}
counties = {
    "北京市辖区": ["请选择县"],
    "上海市辖区": ["请选择县"],
    "广州市": ["请选择县", "天河区", "越秀区", "海珠区"],
    "深圳市": ["请选择县", "福田区", "南山区", "罗湖区"],
    "珠海市": ["请选择县", "香洲区", "金湾区", "斗门区"],
    "南京市": ["请选择县", "玄武区", "鼓楼区", "建邺区"],
    "苏州市": ["请选择县", "姑苏区", "吴中区", "相城区"],
    "无锡市": ["请选择县", "崇安区", "南长区", "北塘区"]
}

selected_province = tk.StringVar()
selected_city = tk.StringVar()
selected_county = tk.StringVar()

province_label = ttk.Label(root, text="省份：")
province_label.grid(row=0, column=0, padx=10, pady=10)

province_combobox = ttk.Combobox(root, textvariable=selected_province, values=provinces)
province_combobox.grid(row=0, column=1, padx=10, pady=10)

city_label = ttk.Label(root, text="城市：")
city_label.grid(row=1, column=0, padx=10, pady=10)

city_combobox = ttk.Combobox(root, textvariable=selected_city, state="disabled")
city_combobox.grid(row=1, column=1, padx=10, pady=10)

county_label = ttk.Label(root, text="县：")
county_label.grid(row=2, column=0, padx=10, pady=10)

county_combobox = ttk.Combobox(root, textvariable=selected_county, state="disabled")
county_combobox.grid(row=2, column=1, padx=10, pady=10)


def province_selected(event):
    selected_province_value = selected_province.get()
    if selected_province_value != "请选择省份" :
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
        counties_list = counties[selected_city_value]
        county_combobox.config(state="normal")
        county_combobox['values'] = counties_list
    else:
        county_combobox.set("")
        county_combobox.config(state="disabled")


province_combobox.bind("<<ComboboxSelected>>", province_selected)
city_combobox.bind("<<ComboboxSelected>>", city_selected)

root.mainloop()