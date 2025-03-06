# pandas
import pandas as pd
import os

wd = r"D:\Python\python_course_py4econ\5_Visualization\data"
wd = wd.replace (os.sep, '/')
os.chdir(wd)
os.getcwd()

# import data
df_2404 = pd.read_csv('2404.csv')
df_2405 = pd.read_csv('2405.csv')
df_2406 = pd.read_csv('2406.csv')
df_2407 = pd.read_csv('2407.csv')
df_2408 = pd.read_csv('2408.csv')
df_2409 = pd.read_csv('2409.csv')
df_2410 = pd.read_csv('2410.csv')
df_2411 = pd.read_csv('2411.csv')
df_2412 = pd.read_csv('2412.csv')

# Датаг босоогоор нь нийлүүлэх
df_merge = pd.concat([df_2404,df_2405, df_2407,df_2408,df_2409,df_2410,df_2411,df_2412])
df_merge.columns

# NA утгуудыг тоолно уу


