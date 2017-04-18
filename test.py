from dbconnect import connectionfile

c,conn=connectionfile()
s="swapnil"
data=c.execute("select * from filetable where personname = %s",s)
data=c.fetchone()[2]
fileo=open(data,"r")
st=fileo.read()
print(st)
fileo.close()
print("done")
