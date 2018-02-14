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


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
def total_count(texts,calls):
	list1=[]
	total=0
	for element in range(len(texts)):
		if texts[element][0] not in list1:
			list1.append(texts[element][0])
		if texts[element][1] not in list1:
			list1.append(texts[element][1])
	for element in range(len(calls)):
	    if calls[element][0] not in list1:
	    	list1.append(calls[element][0])
	    if calls[element][1] not in list1:
	    	list1.append(calls[element][1])

	return "There are <{}> different telephone numbers in the records.".format(len(list1))
print(total_count(texts,calls))
