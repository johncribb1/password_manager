import tkinter as tk

#Declare window height and width variables for use later
height = 500
width = 600


#Application beginning
root = tk.Tk()
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

frame1 = tk.Frame(root, bg='#5B78FF')
frame1.place(relheight="1", relwidth="1")

#Main Frame
frame2 = tk.Frame(frame1, bg="#eeeeee")
frame2.place(relx="0.1", rely="0.1", relheight="0.8", relwidth="0.8")

#Length Entry Frame
frame3 = tk.Frame(frame2, bg="#eeeeee")
frame3.place(relheight="0.3", relwidth="0.8")
length_label = tk.Label(frame3, text='Password Length?')
length_label.pack(side='left')
length_entry = tk.Entry(frame3, font='40')
length_entry.pack(side='right')


#Button
generate_button = tk.Button(frame2, text="Generate Password")
generate_button.pack(side='bottom')




root.mainloop()