# Python program to illustrate a stop watch
# using tkinter
#importing the required libraries
import tkinter as tkk
from datetime import datetime
import pytz
import os
dirpath="D:/TIMELOGS/"
if os.path.isdir(dirpath)==False:
    os.mkdir(dirpath)
else:
    print(os.path.isdir(dirpath))

counter = 66600
running = False
current_time = datetime.now(pytz.timezone('Asia/Kolkata'))
formate_datetime=current_time.day,"/",current_time.month,"/",current_time.year,"",current_time.hour,":",current_time.minute,":",current_time.second
formate_time=current_time.hour,":",current_time.minute,":",current_time.second
root = tkk.Tk()
root.geometry("750x270")
def counter_label(label):
    def count():
        if running:
            global counter

            # To manage the initial delay.
            if counter==66600:
                display="Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display=string

            label['text']=display # Or label.config(text=display)

            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(1000, count)
            counter += 1

    # Triggering the start of the counter.
    count()

# start function of the stopwatch
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
    open_popup()

# Stop function of the stopwatch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

# Reset function of the stopwatch
def Reset(label):
    global counter
    counter=66600

    # If rest is pressed after pressing stop.
    if running==False:
        reset['state']='disabled'
        label['text']='Welcome!'

    # If reset is pressed while the stopwatch is running.
    else:
        label['text']='Starting...'

def open_popup():
   top=tkk.Toplevel(root)
   top.geometry("750x250")
   top.title("Task Details")
   tkk.Label(top, text="Enter Task Name", font=('Arial 12')).grid(row=0)
   inputData = tkk.StringVar()
   tkk.Entry(top, width=30, textvariable=inputData).grid(row=6,padx=5,pady=5)
   tkk.Button(top, text="Save Data", command=lambda: save_file(inputData,top)).grid(row=7)


def save_file(inputData,top):
    taskDetail=inputData.get()
    filename1 = dirpath+"TIMELOGS-"+datetime.now().strftime("%d-%m-%Y")+".txt"
    file1 = open(filename1, "a")  # append mode
    text="%s => %s" % (datetime.now().strftime("%H:%M"),taskDetail)
    file1.write("\n")
    file1.write(text)
    file1.close()
    top.destroy()


root.title("Stopwatch")
# Fixing the window size.
# root.minsize(width=250, height=70)
label = tkk.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
timedate = tkk.Label(root, text=formate_datetime, fg="black", font="Verdana 12")
timedate.pack()
f = tkk.Frame(root)
start = tkk.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = tkk.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = tkk.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
changeTask = tkk.Button(f, text='Skip Task', width=12, command=lambda:open_popup())
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
changeTask.pack(side="left")
root.mainloop()
