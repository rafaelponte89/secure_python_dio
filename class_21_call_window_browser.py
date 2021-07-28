import webbrowser
import tkinter

root = Tk()

root.title('Open Browser') # title window
root.geometry('300x200') # size window

def google():
    webbrowser.open('www.google.com')


mygoogle = Button(root, text='Abrir o Google', command=google).pack(pad=20)

root.mainloop()