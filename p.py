#!/usr/bin/python
p=[]
bt=[]
wt=[None] * 20
ft=[None] * 20
pri=[]
tat=[None] * 20
comp=[None] * 20

i=0
j=0
temp=0
n=int(raw_input('Enter the no. of Processes: '))
for i in range(0,n):
	p.append([])
	print 'P',i+1
	p[i].append(i+1)
	p[i].append(int(raw_input("Enter Arrival Time: ")))
	pri.insert(i,int(raw_input("Enter Process Priority")))
	bt.insert(i,int(raw_input("Enter Burst Time: ")))

for i in range(0,n):
	for j in range (0,n-i-1):
		if pri[j]<pri[j+1]:
			temp=pri[j]
			pri[j]=pri[j+1]
			pri[j+1]=temp

			temp=bt[j]
			bt[j]=bt[j+1]
			bt[j+1]=temp

			temp=p[j][0]
			p[j][0]=p[j+1][0]
			p[j+1][0]=temp

			temp=p[j][1]
			p[j][1]=p[j+1][1]
			p[j+1][1]=temp

p1=0
availP=0

for i in range(0,n):
	if p[i][0]==1:
		p1=i
		wt.insert(p[i][0],0)
		ft.insert(p[i][0],p[i][1]+bt[i])
		comp.insert(p[i][0],1)
		availP=ft[p[i][0]]
		ii=p[i][0]
count=1



print ("Process#   Priority   Arrival Time   Burst Time   FinishTime   Waiting Time   TurnAroundTime")
bool=0
for j in range(0,n):
	for i in range(0,n):
		if p[i][1]<=availP:
			print "i=",i,comp[p[i][0]]
			if comp[p[i][0]]!=1:
				wt.insert(p[i][0],ft[ii]-p[i][1])
				ft.insert(p[i][0],ft[ii]+bt[i])
			
				'''
				print "WT "+str(wt[p[i][0]])
				print "FT "+str(ft[p[i][0]])
				'''
				availP=ft[p[i][0]]
				comp.insert(p[i][0],1)
				count=count+1
				ii=p[i][0]
				break
				
	if count==n:
		break

for i in range(0,n):
	print str(ft[i+1])+" "
order=1
min=100

for i in range(0,n):
	for j in range(0,n):
		if p[j][0]==order:
			print str(p[j][0])+"\t\t"+str(pri[j])+"\t\t"+str(p[j][1])+"\t\t"+str(bt[j])+"\t\t"+str(ft[p[j][0]])+"\t   "+str(wt[p[j][0]])+"\t\t "+str(ft[p[j][0]]-p[j][1])
			order=order+1
			break
