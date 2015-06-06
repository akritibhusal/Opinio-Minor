#!usr/bin/python

from Tkinter import *
import analyze
import ts

pos,neg,net=1,1,1

result="result"
tot=pos+neg+net
labeltext=("Positive:"+str(pos)+"\nNegative:"+str(neg)+"\nNeutral:"+str(net)+"\nTotal:"+str(tot))
def frac(n): return 360. * n / tot

def drawcanvas():

	c = Canvas(width=200, height=200,bg='white')
	c.grid(row=1, column=8,rowspan=3,padx=50,pady=50)
	c.create_arc((2,2,198,198), fill="#e2e2e2", start=frac(0), extent = frac(pos))
	c.create_arc((2,2,198,198), fill="blue", start=frac(pos), extent = frac(neg+pos))
	c.create_arc((2,2,198,198), fill="green", start=frac(neg+pos), extent = frac(net))
	c.mainloop()


def searchtwitter():
	keyword = (E1.get('0.0',END)).strip()
	pos,neg,net=ts.main(keyword)
	tot=pos+neg+net
	labeltext=("Positive:"+str(pos)+"\nNegative:"+str(neg)+"\nNeutral:"+str(net)+"\nTotal:"+str(tot))
	label3.configure(text=labeltext)
	drawcanvas()
	print pos,neg,net

def textanalyze():
	keyword = (E1.get('0.0',END)).strip()
	result=analyze.final_result(keyword)
	label2.configure(text=result)
	print result

root= Tk()
root.geometry("1100x600")
root.configure(background = 'white')


logoImage=PhotoImage(file="op.png")
logo=Label(root,image=logoImage,bd=0)
logo.grid(row=1,column=1,padx=200,pady=50)


label = Label(root, bg="white",text="Enter Keyword",font=("",11))
label.grid(row=2, column=1,sticky=W,padx=300)


E1 = Text(root, bd =0,height=2,width=40,font=("",11))
E1.grid(row=4, column=1,padx=90,pady=10)


analyzeButton = Button(root, text="Analyze Sentence", command=textanalyze,font=("",11))
analyzeButton.grid(row=5, column=1)

twitterButton = Button(root, text="Twitter Analytics", command=searchtwitter,font=("",11))
twitterButton.grid(row=6, column=1)

label2 = Label(root, bg="white",text=result,font=("",24))
label2.grid(row=7, column=1,pady=30)



label3 = Label(root, bg="white",text=labeltext,font=("",11))
label3.grid(row=5,column=8)


root.mainloop()
