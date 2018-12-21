import requests
from tkinter import *
from tkinter import ttk

def sendPersonToServer(*args):
	r = requests.post("http://localhost:8080/suz_ma", json={"id":ma_id.get(), "name":name.get(), "mailAddress":mail.get(), "phoneNumber":phone.get()})
	print(r.status_code, r.reason)
	
	
def sendTaskToServer(*args):
	r = requests.post("http://localhost:8080/task", json={"id":id.get(), "title":title.get(), "type":type.get(), "workingDirectory":workingDirectory.get(), "taskmanager":taskmanagerid.get(), "contributors":contributors})
	print(r.status_code, r.reason)
	
def getSuzMaFromServer(*args):
	r = requests.get("http://localhost:8080/suz_ma")
	print(r.status_code, r.reason)
	data = r.json()
	for ma in data:
		suzMaTree.insert('', 'end', ma["id"], text=ma["name"], values = (ma["mailAddress"], ma["phoneNumber"])) 
		
def makeSuzMaTaskmanager(*args):
	curMa = suzMaTree.focus()
	taskmanagerid.set(curMa)
	taskmanagername.set(suzMaTree.item(curMa)["text"])
	
def makeSuzMaContributor(*args):
	curMa = suzMaTree.focus()
	contributors.append(curMa)
	contributor_entry.insert("end", suzMaTree.item(curMa)["text"])
	

	
root = Tk()
root.title("SUZkos Client")
root.minsize(640, 480)

root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

tabManager = ttk.Notebook(root)

content1 = ttk.Frame(tabManager, padding="3 3 3 3")
tabManager.add(content1, text = "Add Person")

content2 = ttk.Frame(tabManager, padding="3 3 3 3")
tabManager.add(content2, text = "Add Task")

content3 = ttk.Frame(tabManager, padding="3 3 3 3")
tabManager.add(content3, text = "Link Task")

tabManager.grid(row = 0, column = 0, sticky = (N,E, W, S))


# Add Person
name = StringVar()
mail = StringVar()
phone = StringVar()
ma_id = StringVar()

ttk.Label(content1, text="Name").grid(column=1, row=1, sticky=(E, W))
name_entry = ttk.Entry(content1, width=30, textvariable=name).grid(column=1, row=2, sticky=(E, W))

ttk.Label(content1, text="ID").grid(column=1, row=3, sticky=(E, W))
ma_id_entry = ttk.Entry(content1, width=30, textvariable=ma_id).grid(column=1, row=4, sticky=(E, W))

ttk.Label(content1, text="E-Mail").grid(column=1, row=5, sticky=(E, W))
mail_entry = ttk.Entry(content1, width=30, textvariable=mail).grid(column=1, row=6, sticky=(E, W))

ttk.Label(content1, text="Phone Number").grid(column=1, row=7, sticky=(E, W))
phone_entry = ttk.Entry(content1, width=30, textvariable=phone).grid(column=1, row=8, sticky=(E, W))

sendpersonbutton = ttk.Button(content1, text = "Send", command = sendPersonToServer).grid(column = 1, row = 9, sticky=(E, W))

# Add Task
title = StringVar()
id = StringVar()
type = StringVar()
workingDirectory = StringVar()
types = ("Kurzanfrage", "Task")
taskmanagerid = StringVar()
taskmanagername = StringVar()
contributors = []

taskEntryFrame = ttk.Frame(content2, padding="3 3 3 3")
taskEntryFrame.grid(column = 0, row = 0, sticky = (N,E,W))

taskMaFrame = ttk.Frame(content2, padding = "3")
taskMaFrame.grid(column = 1, row = 0, sticky = (N,E,W))

ttk.Label(taskEntryFrame, text="Task ID").grid(column=0, row=0, sticky=(N, E, W))
taskid_entry = ttk.Entry(taskEntryFrame, width=30, textvariable=id).grid(column=0, row=1, sticky=(N, E, W))

ttk.Label(taskEntryFrame, text="Title").grid(column=0, row=2, sticky=(N, E, W))
title_entry = ttk.Entry(taskEntryFrame, width=30, textvariable=title).grid(column=0, row=3, sticky=(N, E, W))

ttk.Label(taskEntryFrame, text = "Type").grid(column = 0, row = 4, sticky = (N, E, W))
type_combo = ttk.Combobox(taskEntryFrame, textvariable = type, state = "readonly", values = types).grid(column = 0, row = 5, sticky = (N, E, W))

ttk.Label(taskEntryFrame, text = "Local Path").grid(column = 0, row = 6, sticky = (N, E, W))
type_combo = ttk.Entry(taskEntryFrame, width=30, textvariable = workingDirectory).grid(column = 0, row = 7, sticky = (N, E, W))

ttk.Label(taskEntryFrame, text = "Task Manager").grid(column = 0, row = 8, sticky = (N, E, W))
tm_entry = ttk.Entry(taskEntryFrame, width=30, textvariable=taskmanagername).grid(column=0, row=9, sticky=(N, E, W))

ttk.Label(taskEntryFrame, text = "Contributor List").grid(column = 0, row = 10, sticky = (N, E, W))
contributor_entry = Listbox(taskEntryFrame, height = 10)
contributor_entry.grid(column = 0, row = 11, sticky = (N, E, W))

sendtaskbutton = ttk.Button(taskEntryFrame, text = "Send", command = sendTaskToServer)
sendtaskbutton.grid(column = 0, row = 12, sticky = (N, E, W))

suzMaTree = ttk.Treeview(taskMaFrame, columns=('mail', 'phone'))
suzMaTree.heading('mail', text='Mail')
suzMaTree.heading('phone', text='Phone')
suzMaTree.grid(column = 0, row = 0, columnspan=3, sticky=(N, E, W))
getmabutton = ttk.Button(taskMaFrame, text = "Refresh", command = getSuzMaFromServer)
getmabutton.grid(column = 0, row = 1, sticky = (N, E, W))
makematmbutton = ttk.Button(taskMaFrame, text = "Make Taskmanager", command = makeSuzMaTaskmanager)
makematmbutton.grid(column = 1, row = 1, sticky = (N, E, W))
makemaconbutton = ttk.Button(taskMaFrame, text = "Make Contributor", command = makeSuzMaContributor)
makemaconbutton.grid(column = 2, row = 1, sticky = (N, E, W))


# Watch Content


root.mainloop()