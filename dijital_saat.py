from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("dijital saat")
app_window.geometry("420x150")
app_window.resizable(1,1)

text_font= ("Boulder", 68, 'bold')
background = "#000000"
foreground = "#ffffff"
border_width = 25

Label = Label(app_window,font=text_font,bg=background,fg=foreground,bd=border_width)
Label.grid(row=0, column=1)

def digital_clock():
  time_live = time.strftime("%H:%M:%S")
  Label.config(text=time_live)
  Label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
