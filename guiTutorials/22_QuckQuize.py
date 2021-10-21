import os
from tkinter import *
from datetime import  datetime

# for i in range(1,len(allFiles)+1):
#     os.rename(f'Exercise_1/img/{i}.jpg',f'Exercise_1/img/{i}.png')

timestamp = datetime.now()

allImages = os.listdir('Exercise_1/img')
allNews = os.listdir('Exercise_1/news')

# GUI starts here 
root = Tk()
root.title("Today's Letest News")
root.geometry('600x500')

# news paper name label
paperName = Label(text="Manisha Time", font=("comicsansms", 30, 'bold'), bg='red', fg='white')
paperName.pack(fill=X)

# time label 
timeLabel = Label(text=f"At: {timestamp}", font=("comicsansms", 10, 'bold'))
timeLabel.pack(padx=10)

# news container here 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar2 = Scrollbar(root)
newsBox = Listbox(root, yscrollcommand=scrollbar.set)
for  i in range(1, len(allImages)):
    with open(f'Exercise_1/news/{i}.txt') as newsContent:
        news = newsContent.read()

    newsBox.insert(END, news[:27])
    newsBox.insert(END, news[27:])

newsBox.pack(fill=X)
scrollbar.config(command=newsBox.yview())
root.mainloop()