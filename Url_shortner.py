from tkinter import *
from pyshorteners import *

url = Shortener()

def shorten():
    # get the copied URL from long url and convert that to short url
    long = urlField1.get()
    shortened = url.tinyurl.short(long)
    urlField2.insert(0,shortened)

root = Tk()

# setting the title
root.title("My URL Shortener")

root.geometry("600x450")
root.configure(bg="#ff4d4d")

label1 = Label(root,text="Long URL Link",font=("verdana",18,"bold"),justify=CENTER)
label1.pack(side=TOP,pady=25)
label1.configure(bg="#80e5ff")

urlField1 = Entry(root,font=("verdana",18),justify=CENTER)
urlField1.pack(side=TOP,fill=X,padx=10,pady=10)
urlField1.configure(bg="#66ff66")

label2 = Label(root,text="Short URL Link",font=("verdana",18,"bold"),justify=CENTER)
label2.pack(side=TOP,pady=25)
label2.configure(bg="#80e5ff")

urlField2 = Entry(root,font=("verdana",18),justify=CENTER)
urlField2.pack(side=TOP,fill=X,padx=10,pady=10)
urlField2.configure(bg="#66ff66")

dBtn = Button(root, text="Generate Link",font=("verdana",18),relief="ridge",command=shorten)
dBtn.pack(side=TOP,pady=20)
dBtn.configure(bg="#ff1ac6")

root.mainloop()