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

for  i in range(1, len(allImages)):
    newsImage = PhotoImage(file=f'Exercise_1/img/{i}.png', width=300, height=200)
    newsImgLabel = Label(image=newsImage)
    newsImgLabel.pack(padx=10)

    with open(f'Exercise_1/news/{i}.txt') as newsContent:
        news = newsContent.read()

    newsLabel = Label(text=news[:27], fg='red', font=("comicsansms", 14,'bold'))
    newsLabel.pack( padx=10)
    newsCont = Label(text=news[27:], font=("comicsansms", 12))
    newsCont.pack(padx=10)

root.mainloop()