from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT = ("Title", 50, "normal")

# ------------------------------ UI SETUP------------------------------#
window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50,padx=50)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_back.png")

#Canvas
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
card.create_image(400, 263, image=card_back)
card.create_text(400, 263, text="TEXT IS NULL", font=FONT, )
card.grid(row=0, column=1)




window.mainloop()
