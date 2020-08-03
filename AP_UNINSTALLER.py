from tkinter import Tk,Label,Listbox,ANCHOR ,Button ,messagebox,Scrollbar
import tkinter as tk
import adbutils
from tkinter import *

def on_keyrelease(event):

    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from list1
    if value == '':
        data = list1
    else:
        data = []
        for item in list1:
            if value in item.lower():
                data.append(item)                

    # update data in listbox
    listbox1_update(data)


def listbox1_update(data):
    # delete previous data
    listbox1.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox1.insert('end', item)


def on_select1():
    newitem=listbox1.get(listbox1.curselection())
    listbox2.insert(0,newitem)
    listbox1.delete(ANCHOR)
    list2.append(newitem)
    list1.remove(newitem)
    print("list2==",list2)

def on_select2():
    newitem=listbox2.get(listbox2.curselection())
    listbox1.insert(0,newitem)
    listbox2.delete(ANCHOR)
    list1.append(newitem)
    list2.remove(newitem)
    print("list1==",list1)

def on_select1xx(event):
    newitem=listbox1.get(listbox1.curselection())
    listbox2.insert(0,newitem)
    listbox1.delete(ANCHOR)
    list2.append(newitem)
    list1.remove(newitem)
    print("list2==",list2)

def on_select2xx(event):
    newitem=listbox2.get(listbox2.curselection())
    listbox1.insert(0,newitem)
    listbox2.delete(ANCHOR)
    list1.append(newitem)
    list2.remove(newitem)
    print("list1==",list1)

   

def on_uninstall():
    print("UNINSTALL IN PROGRESS...")
    for package in list2:
        # pass
        # print(sp.getoutput('adb shell pm uninstall -k --user 0  {}'.format(package)))
        print(dev.shell('pm uninstall -k --user 0  {}'.format(package)))
    print("successfully uninstalled ",len(list2)," items")
    messagebox.showinfo("Title", "successfully uninstalled "+str(len(list2))+" items")
    listbox2.delete(0,"end")
    list2.clear()

def on_clearall():
    list1.extend(list2)
    listbox1_update(list1)
    listbox2.delete(0,"end")
    list2.clear()



# --- main ---
adb = adbutils.AdbClient(host="127.0.0.1", port=5037)
dev = adb.device()
out=dev.shell('pm list packages')
# out = sp.getoutput('pyadb shell pm list packages')
output=out.replace('package:','').split('\n')
# list1 = ['apple', 'banana', 'Cranberry', 'dogwood', 'alpha', 'Acorn', 'Anise', 'Strawberry' ]
list1=output
list2=[]
root = tk.Tk()
root.title("AP's ANDROID SYSTEM APPS UNINSTALLER v1")

frame=Frame()

l1= Label(frame, text="Search  ",font=("",20 ))
entry = tk.Entry(frame,font=("",20 ))


entry.bind('<KeyRelease>', on_keyrelease)
btn1 = Button( text = " > ",command=on_select1,font=("",20 ))
btn2 = Button( text = " < ",command=on_select2,font=("",20 ))
btn3 = Button( text = "UNINSTALL",command=on_uninstall, fg='blue',font=("",15,"bold" ))
btnclearall = Button( text = "<<",command=on_clearall,font=("",20 ))


root.geometry("1366x768")
# l1.pack()
frame.pack(pady=20,side=TOP)
l1.pack(side=LEFT)
entry.pack(side=LEFT)
listbox1 = tk.Listbox(root,width=30,height=20,font=("",20 ))
listbox1.pack(side='left', ipadx=20, padx=30)
# listbox1.place(x=200, y=200,height=800,width=300)

listbox2 = tk.Listbox(root,width=30,height=20,font=("",20 ))
listbox2.pack(side='right', ipadx=20, padx=30)
btn1.pack(pady=60)
btn2.pack(pady=60)
btnclearall.pack(pady=60)
btn3.pack(pady=60)




listbox1.bind('<Double-Button-1>', on_select1xx)
listbox2.bind('<Double-Button-1>', on_select2xx)

# listbox1.bind('<<ListboxSelect>>', on_select)
listbox1_update(list1)

root.mainloop()