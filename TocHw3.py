# -*- coding: utf-8 -*- #告訴直譯器要用utf-8
#!/usr/bin/python
#姓名:吳孟庭
#學號:F74006323
#系級:資訊104乙班

#程式碼簡介
#從argument抓要parse的區跟路名及年分
#將每一個總價元加總在除以總數即為答案
import urllib
import sys
import json

#如果沒有給齊參數的話
if len(sys.argv)< 5:
	print "no input is given"
else:
	content = urllib.urlopen(sys.argv[1]).read() #parse網頁下來
	####json_input = json.dumps(content) #takes a Python data structure and returns it as a JSON string
	json_input = json.loads(content) #takes a JSON string and returns it as a Python data structure
	####print content
	i = 0 #第幾行
	####print len(sys.argv[2]) #看長度可以知道他是unicode還是string
	area = sys.argv[2].decode('utf-8') #XX區
	road = sys.argv[3].decode('utf-8') #路段名
	year = int(sys.argv[4]+"00") #轉成int格式
	output = 0 #各個總價元總和
	num = 0 #答案個數
	for element in json_input:
		if(element[u"鄉鎮市區"] == area and road in element[u"土地區段位置或建物區門牌"] and int(element[u"交易年月"]) >= year):
			#print i, element[u"土地區段位置或建物區門牌"], element[u"交易年月"], element[u"總價元"]
			output += int(element[u"總價元"]) 
			num += 1
		i += 1
	if(num==0):
		print "There is no possible answer in the data."
	else:
		avg_price=output/num #輸出答案
		print avg_price