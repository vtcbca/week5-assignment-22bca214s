#WRITE A PROGRAM TO CREATE CSV FILE STUDENT.CSV:
import csv
with open('student.csv','w',newline='') as s:
    w=csv.writer(s)
    fields=['S_ID','S_NAME','CITY','CONTACT']
    w.writerow(fields)
    rows=[[1,'peru','surat',867508],
    [2,'Kisu','kamrej',888790],
    [3,'sanjna','bardoli',476878],
    [4,'raja','dhindoli',986998],
    [5,'salma','surat',596586]]
    w.writerows(rows)

#INSERT INPUT OF 5 RECORDS THROUGH USER:    
from csv import writer
with open('student.csv','a',newline='') as s:
    w=csv.writer(s)
    l=[]
    for i in range(5):
        s_id=int(input("ENTER STUDENT ID:"))
        s_name=input("ENTER STUENT NAME:")
        city=input("ENTER CITY:")
        contact=input("ENTER STUDENT CONTACT NUMBER:")
        t=(s_id, s_name,city,contact)
        l.append(t)
    w.writerows(l)
    
#READ THIS FILE USING CSV MODULE AND PRINTING IT:
from csv import reader
with open('student.csv','r',newline='') as s:
    w=reader()
    for row in w:
        print(row)
              
 
