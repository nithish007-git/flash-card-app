BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import random
import pandas
window=Tk()
# tkiner main frame
window.title("flash card app")
window.config(bg=BACKGROUND_COLOR)
curret_cards={}
data_dict={}
try:
    data = pandas.read_csv("data/words.csv")
except :
    original_data=pandas.read_csv("data/french_words.csv")
    data_dict=original_data.to_dict(orient="records")

else:

     data_dict = data.to_dict(orient="records")

# reading the input
def french():
    global curret_cards,flip_timer
    window.after_cancel(flip_timer)
    curret_cards=random.choice(data_dict)
    value=curret_cards["French"]
    canvas.itemconfig(title,text="French")
    canvas.itemconfig(text_fre,text=f"{value}")
    canvas.itemconfig(image_front,image=image)
    flip_timer = window.after(3000, func=english)
def english():
    global curret_cards
    value1=curret_cards["English"]
    canvas.itemconfig(title,text="english")
    canvas.itemconfig(text_fre,text=value1)
    canvas.itemconfig(image_front,image=image_bac)

def known_words():
    data_dict.remove(curret_cards)
    data_csv=pandas.DataFrame(data_dict)
    data_csv.to_csv("data/words.csv",index=False)
    french()

flip_timer=window.after(3000,func=english)


#canvas
canvas=Canvas(width=800,height=526,highlightthickness=0)
image=PhotoImage(file="../flash-card-project-start/images/card_front.png")
image_bac=PhotoImage(file="../flash-card-project-start/images/card_back.png")
card_image=canvas.create_image(400,260,image=image_bac)
image_front =canvas.create_image(400,260,image=image)
canvas.config(bg=BACKGROUND_COLOR)


title=canvas.create_text(400,120,text="French",font=("arial",30,"italic"),)
text_fre=canvas.create_text(400,200,text="start",font=("arial",30,"bold"))
canvas.grid(column=2,row=2,padx=20,pady=20,columnspan=2)

#correct image
correct_img=PhotoImage(file="../flash-card-project-start/images/right.png")
button_cor=Button(image=correct_img,highlightthickness=0,command=known_words)
button_cor.grid(column=2,row=4,padx=10)
#x image
x_img=PhotoImage(file="../flash-card-project-start/images/wrong.png")
button_cor=Button(image=x_img,highlightthickness=0,command=french)
button_cor.grid(column=3,row=4,padx=10)






window.mainloop()