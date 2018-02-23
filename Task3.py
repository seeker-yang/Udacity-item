"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def dail(calls):
	area_code=[]
	dir_code={}
	for element in calls:
		if element[0].startswith("(080)"):
			el=element[1]    #尽量不要用嵌套，如用element【0】【0】来表示第一个号码的第一位，而是一行代码写一个递进，
			if el[0]=="(":   #虽然题目说区号以0开头，但不可用el[1]==1来做判断，因为有的长途号码第二位也是1
			    area_code.append(el[1:el.find(')')])	    
			elif el[0] in ["7","8","9"]:
				area_code.append(el[:4])
	print("The numbers called by people in Bangalore have codes:")
	for element in area_code:
		dir_code[element] = " "    #用字典来排序可以排除重复的区号，如果用列表虽然方便，但还要排重
	sort_code=sorted(dir_code.items(),key=lambda item: item[0])
	for index in range(len(sort_code)):
		print("{}".format(sort_code[index][0]))
	percent=area_code.count("080")/len(area_code)*100
	return round(percent,2)	
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
	.format(dail(calls)))

"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。

第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
