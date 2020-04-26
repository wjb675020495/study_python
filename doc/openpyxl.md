# openpyxl模块使用

![image-20200418000744995](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20200418000744995.png)

#### Excel文件三个对象

- workbook： 工作簿，一个excel文件包含多个sheet。
- sheet：工作表，一个workbook有多个，表名识别，如“sheet1”,“sheet2”等。
- cell： 单元格，存储数据对象





#### 创建或打开excel表

- ###### 创建worksheet

  方式一：

  ```
  worksheet = openpyxl.workbook.Workbook.active()  #得到worksheet
  ```

  其中_active_sheet_index属性, 默认会设置0，也就是第一个worksheet。除非手动修改，否则使用active方法得到都是第一个worksheet。

  方式二：

  ```
  worksheet = Workbook.create_sheet("message")     #插入到最后(default)
  worksheet = Workbook.create_sheet("Mysheet", 0)  #插入到最开始的位置
  ```

  创建的sheet的名称会自动创建，按照sheet，sheet1，sheet2自动增长，通过title属性可以修改其名称。

  ```
  ws.title = "New Title"
  ws = wb.create_sheet(title="Pip")
  ```

  当你设置了sheet的名称，可以将其看成workbook中的一个key。也可以使用

  ```
  openpyxl.workbook.Workbook.get_sheet_by_name() 
  ```





- ###### 读表

```
    #打开文件
    wb = openpyxl.load_workbook("E:/test.xlsx")
    #获取sheet：
	table = excel.get_sheet_by_name('Sheet1')  #通过表名获取
	rows=table.max_row  #获取行数
	cols=table.max_column  #获取列数
	Data=table.cell(row=row,column=col).value #获取表格内容，是从第一行第一列是从1开始的，注意不要丢掉 .value
```

```
#通过名字
  ws = wb["frequency"]
  #等同于 ws2 = wb.get_sheet_by_name('frequency')
  #不知道名字用index
  sheet_names = wb.get_sheet_names()
  ws = wb.get_sheet_by_name(sheet_names[index])# index为0为第一张表
#或者
  ws =wb.active
  # 等同于 ws = wb.get_active_sheet() #通过_active_sheet_index设定读取的表，默认0读第一个表
  #活动表表名
  wb.get_active_sheet().title
```



#### **单元格**

###### 	单元格赋值

```
sheet.cell(row=2,column=5).value=99
sheet.cell(row=3,column=5,value=100)
ws['A4'] = 4 #write 
```

###### 	单元格使用

```
c = ws['A4']
d = ws.cell(row = 4, column = 2) #行列读写
```

  表格所有行和列，两者都是可迭代的



###### 	逐行写

```
 ws.append(iterable)
 #添加一行到当前sheet的最底部（即逐行追加从第一行开始） iterable必须是list,tuple,dict,range,generator类型的。 1,如果是list,将list从头到尾顺序添加。 2，如果是dict,按照相应的键添加相应的键值。
 ws.append([‘This is A1', ‘This is B1', ‘This is C1'])
 ws.append({‘A' : ‘This is A1', ‘C' : ‘This is C1'})
 ws.append({1 : ‘This is A1', 3 : ‘This is C1'})
```

逐行读取

```
  #逐行读
  ws.iter_rows(range_string=None, row_offset=0, column_offset=0): 
  range-string(string)-单元格的范围：例如('A1:C4') row_offset-添加行 column_offset-添加列
  # 返回一个生成器, 注意取值时要用value,例如：
  for row in ws.iter_rows('A1:C2'):
    for cell in row:
      print cell
  #读指定行、指定列:
  rows=ws.rows#row是可迭代的
  columns=ws.columns#column是可迭代的
  #打印第n行数据
  print rows[n]#不需要用.value
  print columns[n]#不需要用.value
```

保存

```
    workbook.save('test.xlsx')
```





demo

```
workbook =openpyxl.load_workbook('E:\\Project//python//python_test_demo//res//book.xlsx')
ws = workbook.active
table_title = ['username', 'phone', 'remark']
 
for col in range(len(table_title)):
	ws.cell(row=1, column=c).value = table_title[col]
table_values = [['王剑波', '15160111032', 24, '测试数据'], ['阿毛', 		1516011133, 26, '测试数据']]

for row in range(len(table_values)):
	ws.append(table_values[row])
workbook.save('test.xlsx')
```

