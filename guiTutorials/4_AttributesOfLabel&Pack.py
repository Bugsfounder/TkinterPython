from tkinter import *
from tkinter import font

root = Tk()

root.geometry("700x600")
root.title("Manisha is a Genius Girl")

# IMPORTANT LABEL OPTIONS 
# text - ADDS THE TEXT 
# bd - BACKGROUND
# fg - FOREGROUND
# font - sets the font 
#   1. font=("comicsansms", 12, 'bold'),
#   2. font="comicsansms 19 bold"
# padx - x _Padding
# pady - y padding 
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text='''Abdul Rashid Salim Salman Khan  is an Indian actor, film \nproducer, singer, painter and television personality who works in Hindi films. In a \nfilm career spanning over thirty years, Khan has received numerous awards, including \ntwo National Film Awards as a film producer, and two Filmfare Awards for acting. He is \ncited in the media as one of the most commercially successful actors of Indian cinema. \nForbes included him in their 2015 list of Top-Paid 100 Celebrity Entertainers in the \nworld; Khan tied with Amitabh Bachchan for No. 71 on the list, both with earnings of \n$33.5 million.According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers \nin world, Khan was the highest-ranked Indian with 82nd rank with earnings of $37.7 \nmillion. He is also known as the host of the reality show, Bigg Boss since 2010. ''', bg='red', pady=98, padx=13, font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN, fg='white')

 
# IMPORTANT PACK OPTIONS 
# anchor - NW
# side - top, bottom , left, right 
# fill
# padx
# pady

# title_label.pack(anchor=NW)
# title_label.pack(anchor=NE)
# title_label.pack(side=BOTTOM, anchor=SE)
# title_label.pack(side=BOTTOM, anchor=SW)
# title_label.pack(side=BOTTOM)
# title_label.pack(side=TOP)
# title_label.pack(side=BOTTOM, anchor=SW, fill=X)
title_label.pack(side=LEFT, anchor=SW, fill=Y)



root.mainloop()