data1={'name':'priya','age':18,'id_no':1,'vc':0}
data2={'name':'bavya','age':19,'id_no':2,'vc':0}
data3={'name':'cibi','age':18,'id_no':3,'vc':0}
data4={'name':'aji','age':20,'id_no':4,'vc':0}
data5={'name':'ragavi','age':19,'id_no':5,'vc':0}
data6={'name':'naresh','age':21,'id_no':6,'vc':0}
data7={'name':'arjun','age':18,'id_no':7,'vc':0}
data8={'name':'sathya','age':19,'id_no':8,'vc':0}
data9={'name':'gowtham','age':20,'id_no':9,'vc':0}
data10={'name':'raj','age':21,'id_no':10,'vc':0}
list=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
count=0
while(1):
	no=raw_input('Enter a id-no:')
	if(int(no)<=10 and int(no)>0):
		for i in range(0,11):
			if(i==int(no)):
				list[i-1]['vc']=list[i-1]['vc']+1;
				print list[i-1];
			else:
				i=i+1;
		continue;
	elif(int(no)==0):
		break;
	else:
		print 'The id-no must be from 1 to 10';
		count=count+1
		if(count>=3):
			break;
		else:
			continue;		

