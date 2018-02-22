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
	list1=set()
	for element in texts:
		list1.add(element[0])
		list1.add(element[1])
	for element in calls:
	    list1.add(element[0])
	    list1.add(element[1])
	return "There are {} different telephone numbers in the records.".format(len(list1))
print(total_count(texts,calls))

