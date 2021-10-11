from os import close
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import Calendar
import time
import datetime
from playsound import playsound
from threading import *


######### Creating Gui ##############
root = Tk()
root.title('Home Screen')
root.geometry('600x600')
root.config(bg='#40E0D0')
root.iconbitmap(r'icons\calendar.ico')

frame1 = Frame(root)
frame1.config(background='#bed9e5')
frame1.place(x="100", y="50")


image = Image.open("BG_image\scenery.png")
resized_image = image.resize((500, 250))
pic = ImageTk.PhotoImage(resized_image)
picfinal = Label(image=pic).place(x=50, y=190)


frame2 = Frame(root)
frame2.config(background='#189AB4')
frame2.place(x="20", y="50")

frame3 = Frame(root)
frame3.config(background='#189AB4')
frame3.place(x="435", y="60")

############################ clock function ###############################


def clock():
    hour = time.strftime('%I')
    minute = time.strftime('%M')
    second = time.strftime('%S')
    day = time.strftime('%A')
    month = time.strftime('%B')
    am_pm = time.strftime('%p')
    date = time.strftime('%x')

    clock_label.config(text=f"{hour}:{minute}:{second}  {am_pm}")
    clock_label.after(1000, clock)

    clock_label2.config(text=f"{day} \n {month} \n {date} ", fg='black', bg='#189AB4')
############################ clock function ###############################


############################ clock ###############################
clock_label = Label(frame2, text="", font=(
    'Helvetica', 48), fg='black', bg='#189AB4')
clock_label.pack(pady=15)

clock_label2 = Label(frame3, text="", font=('Helvetica', 14))
clock_label2.pack(pady=10)
clock()

############################ clock ###############################

############################ new window_alarm function ###############################


def newWindowAlarm():

    newWindowAlarm = Toplevel(root)
    newWindowAlarm.title('Alarm')
    newWindowAlarm.geometry('600x600')
    newWindowAlarm.config(bg='#189AB4')
    frame4 = Frame(newWindowAlarm, bg='#6D9BF1')
    frame4.place(x="250", y="320")
    newWindowAlarm.iconbitmap(r'icons\clock.ico')

    alarm_sound_strvar = StringVar()
    sound_list = ["Lofi alarm 1.mp3", "Lofi alarm 2.mp3", "Lofi alarm 3.mp3", "yare yare.mp3", "chika dance.mp3",
                  "isabella lullaby.mp3","hisoka theme.mp3", "gojo.mp3","fukashigi no carte.mp3" ]
    options_sound = OptionMenu(newWindowAlarm, alarm_sound_strvar, *sound_list)
    alarm_sound_strvar.set(" Choose Your Tune ")
    options_sound.config(bg="#6D9BF1", width=30, height=1,  relief=RAISED, activebackground="cyan", font=" bold 10")
    options_sound.place(x=170, y=200)




    def Threading():
     t1=Thread(target=alarm)
     t1.start()
    
    def alarm():

        while True:

            set_alarm_time = f"{alarm_hour.get()}:{alarm_minutes.get()}:{alarm_second.get()}"

            time.sleep(1)

            current_time = datetime.datetime.now().strftime("%I:%M:%S")
            print(current_time, set_alarm_time)

            if current_time == set_alarm_time:
                
                if alarm_sound_strvar.get()=="chika dance.mp3":
                 playsound('alarms/chika dance.mp3')
                 break
                
                if alarm_sound_strvar.get()=="fukashigi no carte.mp3":
                 playsound('alarms/fukashigi no carte.mp3')
                 break

                if alarm_sound_strvar.get()=="gojo.mp3":
                 playsound('alarms/gojo.mp3')
                 break

                if alarm_sound_strvar.get()=="hisoka's theme.mp3":
                 playsound('alarms/hisoka theme.mp3')
                 break

                if alarm_sound_strvar.get()=="isabella lullaby.mp3":
                 playsound('alarms/isabella lullaby.mp3')
                 break

                if alarm_sound_strvar.get()=="Lofi alarm 1.mp3":
                 playsound('alarms/Lofi alarm 1.mp3')
                 break

                if alarm_sound_strvar.get()=="Lofi alarm 2.mp3":
                 playsound('alarms/Lofi alarm 2.mp3')
                 break 

                if alarm_sound_strvar.get()=="Lofi alarm 3.mp3":
                 playsound('alarms/Lofi alarm 3.mp3')
                 break

                messagebox.showinfo("Alarm complete", "Time is up")

                Alarm_history = open("alarm_history.txt", 'a')
                Alarm_history.write(
                    f'Alarm set at {alarm_hour.get()}:{alarm_minutes.get()} {datetime.datetime.now():%p}\n')
                Alarm_history.close()

                def update():
                    alarm_status.config(text='')

                alarm_status = Label(
                    newWindowAlarm, text='Alarm Ended', bg='#6D9BF1')
                alarm_status.place(x=280, y=250)
                alarm_status.after(3000, update)

                break

    def History_Alarm():
        alarm_history = open("alarm_history.txt", 'r')
        labelhistory_stringvar.set(alarm_history.read())
        alarm_history.close()


############################ new window_alarm function ###############################


############################ alarm labels ###############################
    alarm_hour_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                       '08', '09', '10', '11', '12']

    alarm_minutes_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                          '08', '09', '10', '11', '12', '13', '14', '15',
                          '16', '17', '18', '19', '20', '21', '22', '23',
                          '24', '25', '26', '27', '28', '29', '30', '31',
                          '32', '33', '34', '35', '36', '37', '38', '39',
                          '40', '41', '42', '43', '44', '45', '46', '47',
                          '48', '49', '50', '51', '52', '53', '54', '55',
                          '56', '57', '58', '59', '60']

    alarm_second_list = ['00', '01', '02', '03', '04', '05', '06', '07',
                         '08', '09', '10', '11', '12', '13', '14', '15',
                         '16', '17', '18', '19', '20', '21', '22', '23',
                         '24', '25', '26', '27', '28', '29', '30', '31',
                         '32', '33', '34', '35', '36', '37', '38', '39',
                         '40', '41', '42', '43', '44', '45', '46', '47',
                         '48', '49', '50', '51', '52', '53', '54', '55',
                         '56', '57', '58', '59', '60']

    alarm_hour = Spinbox(newWindowAlarm, values=alarm_hour_list, width=5)
    alarm_hour.place(x=240, y=90)
    alarm_minutes = Spinbox(newWindowAlarm, values=alarm_minutes_list, width=5)
    alarm_minutes.place(x=290, y=90)
    alarm_second = Spinbox(newWindowAlarm, values=alarm_second_list, width=5)
    alarm_second.place(x=340, y=90)

    set_alarm = Button(newWindowAlarm, text="Set Alarm",bg="#6D9BF1", command=Threading)
    set_alarm.place(x=280, y=150)

    label_set = Label(newWindowAlarm, text="Set An Alarm",
                      font=('Ariel', 13, 'bold'), bg='#6D9BF1')
    label_set.place(x="250", y="30")

    Alarm_History_button = Button(newWindowAlarm, text="Show Alarm history", font="arial 13", command=History_Alarm, fg='black',
                                  bg='#6D9BF1')
    Alarm_History_button.place(x="210", y="280")

    labelhistory_stringvar = StringVar()
    labelhistory_stringvar.set("History")
    labelhistory = Label(
        frame4, textvariable=labelhistory_stringvar, bg='#6D9BF1')
    labelhistory.grid(row=2, column=0, pady=1, padx=2)
############################ alarm labels ###############################


############################ new window_reminder function ###############################
def newWindowReminder():
    newWindowReminder = Toplevel(root)
    newWindowReminder.title('Reminder')
    newWindowReminder.geometry('600x600')
    newWindowReminder.config(bg='#459fed')
    newWindowReminder.iconbitmap(r'icons\memo_icon.ico')
    frame5 = Frame(newWindowReminder, bg='#6D9BF1')
    frame5.place(x=250, y=470)

    def selectdate():
        print(cal.get_date())

        def reminder_notes():
            m = open("memos.txt", 'a')
            m.write(
                f'{reminder_entry.get()} set for {cal.get_date()} ({reminderfrequency_stringvar.get()}) \n')

            def update():
                status_label.config(text='')

            status_label = Label(
                newWindowReminder, text="Reminder set", bg='#459fed')
            status_label.place(x=140, y=370)
            status_label.after(1000, update)

        reminder_label = Label(
            newWindowReminder, text=f'Set reminder for {cal.get_date()}', bg='#459fed')
        reminder_label.place(x=350, y=370)
        reminder_entry = Entry(newWindowReminder, width=20, bg='#7999d9')
        reminder_entry.place(x=220, y=370)
        reminder_button = Button(
            newWindowReminder, text="Set Reminder", command=reminder_notes)
        reminder_button.place(x=250, y=400)

    def Show_reminders():
        reminder = open("memos.txt", 'r')
        reminder_stringvar.set(reminder.read())
        reminder.close()


############################ new window_reminder function ###############################


############################ reminder labels ###############################
    header = Label(newWindowReminder,
                   text='Please select a date:', font=('arial', 20), bg='#459fed')
    header.place(x=190, y=30)

    cal = Calendar(newWindowReminder, selectmode='day',
                   date_pattern='dd/MM/yyyy')
    cal.pack(padx=20, pady=100)

    select_date = Button(newWindowReminder,
                         text="Select this day", command=selectdate)
    select_date.place(x=250, y=300)

    reminderfrequency_stringvar = StringVar()
    reminder_list = ["Daily", "Weekly", "Monthly", "Yearly", "One Time Only", ]
    options = OptionMenu(
        newWindowReminder, reminderfrequency_stringvar, *reminder_list)
    reminderfrequency_stringvar.set("Choose Frequency Of reminder")
    options.config(bg="light blue", width=30, height=1, activebackground="cyan")
    options.place(x=180, y=330)

    show_reminder = Button(
        newWindowReminder, text="Show Reminder", command=Show_reminders)
    show_reminder.place(x=250, y=440)

    reminder_stringvar = StringVar()
    reminder_stringvar.set("Reminders set")
    labelhistory = Label(
        frame5, textvariable=reminder_stringvar, bg='#6D9BF1')
    labelhistory.grid(row=2, column=0, pady=1, padx=2)


############################ reminder labels ###############################


############################ selection buttons ###############################
photo = PhotoImage(file=r"Button_images\clock.png")
Set_alarm_button = Button(root, text="Set a new alarm", image=photo, font='arial  12',
                          fg='black', bg='#189AB4', command=newWindowAlarm)
Set_alarm_button.place(x=450, y=460)

photo2 = PhotoImage(file=r"Button_images\reminder.png")
Set_reminder_button = Button(
    root, text="Set a new reminder", image=photo2, font='arial  12', fg='black',
    bg='#189AB4', command=newWindowReminder)
Set_reminder_button.place(x=70, y=460)
############################ selection buttons ###############################

photo3 = PhotoImage(file=r"Button_images\exit.png")
exit_button = Button(root, text='   exit   ', image=photo3, font='arial  12', fg='black',
                     bg='#189AB4', command=root.quit).place(x=250, y=520)

root.mainloop()
