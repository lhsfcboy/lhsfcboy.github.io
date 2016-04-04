#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import csv
import math
import datetime



debug = 0
x=0

f = open(sys.argv[1], 'r')

linestring = f.readline()
dict = {}
dict_allrecords = {}
list = []


while linestring:

	if linestring.count("35=D")+linestring.count("35=8") == 0:
		linestring = f.readline()	
		continue	

	if linestring.count("failed") != 0:
		linestring = f.readline()	
		continue	

	if linestring.count("LBClientSender") != 0:
		linestring = f.readline()	
		continue	

	timestampstr = linestring[16:42]
	#timestampstr = linestring[0:26]
	index_of_tag11 = linestring.find('11=')
	index_of_tag55 = linestring.find('55=')
	index_of_tag35 = linestring.find('35=')
	index_of_tag49 = linestring.find('49=')
	index_of_tag56 = linestring.find('56=')
	index_of_tag34 = linestring.find('34=')
	index_of_tag21 = linestring.find('21=')
	index_of_tag39 = linestring.find('39=')
	
	if linestring[(index_of_tag35+3):(index_of_tag35+4)] == 'D':
		#print "This is D message"
		id = linestring[(index_of_tag11+3):(index_of_tag55-1)]
		senderid   = linestring[(index_of_tag49+3):(index_of_tag56-1)]
		receiverid = linestring[(index_of_tag56+3):(index_of_tag34-1)]
		cid = id + '_' + senderid + '_' + receiverid
	elif linestring[(index_of_tag35+3):(index_of_tag35+4)] == '8':
		#print "This is 8 message"
		id = linestring[(index_of_tag11+3):(index_of_tag55-1)]
		senderid   = linestring[(index_of_tag49+3):(index_of_tag56-1)]
		receiverid = linestring[(index_of_tag56+3):(index_of_tag34-1)]
		cid = id + '_' + receiverid + '_' + senderid
	else:
		print "***************************************"
	
	
	
#	print cid
#	print cid," = ", timestampstr[:-7]
#	print cid," = ", timestampstr[-6:]
		
		
	if dict.has_key(cid):
#		print "dict has key", cid
#		time.mktime(time.strptime(timestampstr,r'%Y/%m/%d %H:%M:%S'))
		t2 = int(time.mktime(time.strptime(timestampstr[:-7],r'%Y/%m/%d %H:%M:%S'))) * 1000000 + int(timestampstr[-6:])
		t1 = int(time.mktime(time.strptime(dict[cid][:-7],r'%Y/%m/%d %H:%M:%S'))) * 1000000 + int(dict[cid][-6:])
		t1_seconds = int(time.mktime(time.strptime(dict[cid][:-7],r'%Y/%m/%d %H:%M:%S')))
		latency = t2-t1
		list.append(latency)
#		print cid, ", ", t2, " - ", t1, " = ", latency
		dict_allrecords[cid] = [cid, latency, t1, t2, t1_seconds,timestampstr]
		dict.pop(cid)
	else:		
		dict[cid]=timestampstr
	
	linestring = f.readline()

	if debug == 1:
		x = x - 1
		if x < 0:
			break

f.close()



def list_avg(list):
	sum = 0
	for elm in list:
		sum += elm
#	print "The average value of the list is: " + str(sum/(len(list)*1.0))
	return str(sum/(len(list)*1.0))

list.sort();

string_script_name = "script name: " + sys.argv[0]
string_paramater1  = "paramater1:  "  + sys.argv[1]
string_no_of_record= "latency record is " + str(len(list))
string_avg		   = "Avg is "            + str(list_avg(list))
string_min         = "Min is "            + str(min(list))
string_max         = "Max is "            + str(max(list))

def printsummary():	
	print string_script_name 
	print string_paramater1  
	print string_no_of_record
	print string_avg		   
	print string_min         
	print string_max         
#	print "script name: ", sys.argv[0]
#	print "paramater1: ",   sys.argv[1]
#	print "latency record is ", len(list)
#	
#	print "Min is ", min(list)
#	print "Max is ", max(list)
#	print "---------------------------"
	printpercentil()
	

no_of_records= len(list)
no_of_p99_9  = int(math.ceil(no_of_records * 0.999)) 
no_of_p99    = int(math.ceil(no_of_records * 0.99)) 
no_of_p90    = int(math.ceil(no_of_records * 0.90)) 
no_of_p50    = int(math.ceil(no_of_records * 0.50)) 

string_no_of_p99_9 = "no_of_p99_9 is " + str(no_of_p99_9) + " value is " + str(list[no_of_p99_9-1])
string_no_of_p99   = "no_of_p99   is " + str(no_of_p99)   + " value is " + str(list[no_of_p99-1])
string_no_of_p90   = "no_of_p90   is " + str(no_of_p90)   + " value is " + str(list[no_of_p90-1])
string_no_of_p50   = "no_of_p50   is " + str(no_of_p50)   + " value is " + str(list[no_of_p50-1])

def printpercentil():
	print string_no_of_p99_9
	print string_no_of_p99   
	print string_no_of_p90   
	print string_no_of_p50   	
#	print "no_of_p99_9 is ", no_of_p99_9, "value is ", list[no_of_p99_9-1]
#	print "no_of_p99   is ", no_of_p99  , "value is ", list[no_of_p99  -1]
#	print "no_of_p90   is ", no_of_p90  , "value is ", list[no_of_p90  -1]
#	print "no_of_p50   is ", no_of_p50  , "value is ", list[no_of_p50  -1]
	

def output_summary():
	outputfilename=sys.argv[1]+".summary.txt"
	with open(outputfilename, 'w') as f:
#	    f.write(u'工事中!!'.encode('utf-8'))
		f.write( string_script_name  + "\n" ) 
		f.write( string_paramater1   + "\n" )
		f.write( string_no_of_record + "\n" )
		f.write( string_avg		     + "\n" )
		f.write( string_min          + "\n" )
		f.write( string_max          + "\n" )
		f.write( string_no_of_p99_9  + "\n" )
		f.write( string_no_of_p99    + "\n" )
		f.write( string_no_of_p90    + "\n" )
		f.write( string_no_of_p50    + "\n" )		
		for items in list_records_count_in_second:
			f.write(items[1] + " " + str(items[2]) + "\n")

	

#for x in list:
#	print int(x)
def print_allrecords():
	for record in dict_allrecords:
		#print (record)
		for items in dict_allrecords[record]:
			print items,
		print 
dict_records_count_in_second = {}

def output_allrecords():
	outputfilename=sys.argv[1]+".csv"
	outputf = open(outputfilename, 'wb')
	csvWriter = csv.writer(outputf)
	for keyid,value_list in sorted(dict_allrecords.items(), key=lambda keyid:keyid[1][2]):
		#print "key:", key, "value_list", str(value_list)
		csvWriter.writerow(value_list)
	outputf.close()


listx = []
listy = []
for record in dict_allrecords:
	#print dict_allrecords[record][0], dict_allrecords[record][4]
	#print (record)
	id            =  dict_allrecords[record][0]
	seconds       =  dict_allrecords[record][4]
	readable_time =  dict_allrecords[record][5]
	
	if dict_records_count_in_second.has_key(seconds):
		dict_records_count_in_second[seconds]+=1			
	else:
		dict_records_count_in_second[seconds]=1
	#listx.append(int(str(dict_allrecords[record][2])[-9:]));
	listx.append(dict_allrecords[record][2]);
	listy.append(dict_allrecords[record][1]);
#import pprint
#pprint.pprint(listx )

list_records_count_in_second = []

for items in dict_records_count_in_second:
	print (items), datetime.datetime.fromtimestamp(int((items))).strftime('%Y-%m-%d_%H:%M:%S'),dict_records_count_in_second[items];
	list_records_count_in_second.append([(items),datetime.datetime.fromtimestamp(int((items))).strftime('%Y-%m-%d_%H:%M:%S'),dict_records_count_in_second[items]]);
#print "---------------------" 



printsummary()



def output_scatter():
	import numpy as np
	import matplotlib.pyplot as plt
	x = listx
	y = listy
#	plt.hist(listy)
#	plt.show()
	plt.scatter(x,y,s=1)
	plt.title('Scatter')
#	plt.figure(figsize=(10,8))	#inch, 4,3 means 400*300
	
	plt.hlines(list[no_of_p99-1], min(listx), max(listx), linestyles="dashed")
	plt.ylim(0 - 0.1 * abs(max(listy)), max(listy) * 1.1 )
	plt.xlim(min(listx) - 0.1 * (max(listx) - min(listx)), max(listx) + 0.1 * (max(listx) - min(listx)) )
	
	ScatterName=sys.argv[1]+".scatter.png"
	plt.savefig(ScatterName)
	

def output_hist():
	import numpy as np
	import matplotlib.pyplot as plt
	listx_new = []
	min_listx = min(listx)
	index = 0
	for items in listx:
		delta_ts = items - min_listx
		#print index,items,delta_ts
		index = index + 1
		listx_new.append(delta_ts)
	x = listx_new
	plt.hist(x, bins = 1000000)
#	plt.hist(x)
	
	plt.show()
	
	plt.title('ThroughPut')
#	plt.figure(figsize=(10,8))	#inch, 4,3 means 400*300
	
#	plt.hlines(list[no_of_p99-1], min(listx), max(listx), linestyles="dashed")
#	plt.ylim(0 - 0.1 * abs(max(listy)), max(listy) * 1.1 )
#	plt.xlim(min(listx) - 0.1 * (max(listx) - min(listx)), max(listx) + 0.1 * (max(listx) - min(listx)) )
	
	ScatterName=sys.argv[1]+".hist.png"
	plt.savefig(ScatterName)	
	
#output_hist()
	
output_scatter()
output_allrecords()
#print_allrecords()
output_summary()
