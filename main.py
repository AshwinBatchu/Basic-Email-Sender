import numpy as np
import pandas as pd
import smtplib as smt

def sendmail():
    CsvFile = pd.read_csv('data.csv')
    for i in range(0,n+1):
        Item1 = str(CsvFile['sender'][i])
        Item2 = str(CsvFile['receiver'][i])
        Item3 = str(CsvFile['message'][i])
        server.sendmail(Item1,Item2,Item3)
        
        
print("Enter upto which Idex of mail you want to send")
n=int(input())
print("Enter Sever Address")
a=str(input())
print("Enter Sever Code")
b=int(input())
print("Enter Login ID ")
x=str(input())
print("Enter Password")
y=str(input())
server=smt.SMTP_SSL(a,b)
server.login(x,y)
sendmail()
server.quit()
