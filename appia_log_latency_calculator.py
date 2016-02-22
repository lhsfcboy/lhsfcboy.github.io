import time

f = open(r'C:\Users\mluo\201601_Jan_onsite-install\PerformanceExplain\C20160128.log.Opt_CaseA_preWarmup_KHedit', 'r')
linestring = f.readline()
dict = {}
list = []

x=8

while linestring:

	timestampstr = linestring[16:42]
	index_of_tag11 = linestring.find('11=')
	index_of_tag55 = linestring.find('55=')
	index_of_tag35 = linestring.find('35=')
	index_of_tag49 = linestring.find('49=')
	index_of_tag56 = linestring.find('56=')
	index_of_tag34 = linestring.find('34=')
	id = linestring[(index_of_tag11+3):(index_of_tag55-1)]
	
	if linestring[(index_of_tag35+3):(index_of_tag35+4)] == 'D':
		#print "This is D message"
		senderid   = linestring[(index_of_tag49+3):(index_of_tag56-1)]
		receiverid = linestring[(index_of_tag56+3):(index_of_tag34-1)]
		cid = id + '_' + senderid + '_' + receiverid
	elif linestring[(index_of_tag35+3):(index_of_tag35+4)] == '8':
		#print "This is 8 message"
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
		latency = t2-t1
		list.append(latency)
#		print cid, ", ", t2, " - ", t1, " = ", latency

		dict.pop(cid)
	else:		
		dict[cid]=timestampstr
	
	linestring = f.readline()

	x = x - 1
#	if x < 0:
#		break

f.close()
print "latency record is ", len(list)
print "latency avg is ", sum(list)/len(list)





#for x in list:
#	print int(x)




def min(list):

	min = list[0]

	for elm in list:
		if elm < min:  			
			min = elm 			 	
	print "The minimum value in the list is: " + str(min) 	 

		
def max(list): 	
	max = list[0] 	 	
	for elm in list[1:]: 		
		if elm > max:
			max = elm

	print "The maximum value in the list is: " + str(max)


def avg(list):

	sum = 0
	for elm in list:
		sum += elm

	print "The average element of the list is: " + str(sum/(len(list)*1.0))
	

avg(list)
min(list)
max(list)

	



