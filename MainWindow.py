from tkinter import *
from random import *
import pendulum #similar to datetime library
import webbrowser
import easygui #message box


#import other objects
# import TestDatabase as td
import MyDB as td
import NewsWebScraping as nws
import WeatherForcast as wf

class MainWindow:
    def __init__(self):
        #MISCELLANEOUS
        self.database = td.myDatabase()
        self.hacker_news = nws.HackerNews()
        self.weather_forcast = wf.Weather("Linz", "AT")
        self.stored_date = None
        self.stored_time = None
        self.stored_activity = None

        #WINDOW SET UP
        self.root = Tk()  # Create the top-level (or root) window
        self.root.title('My App')
        self.root.geometry("1100x800+180+0") #size and location
        self.leftFrame = Frame(self.root) # create left-hand side frame
        self.leftFrame.grid(column = 0, row = 1)
        self.centreFrame = Frame(self.root)  # create centre frame
        self.centreFrame.grid(column=1, row = 1)
        self.rightFrame = Frame(self.root) # create right-hand side frame
        self.rightFrame.grid(column=2, row = 1)

        #LEFT FRAME
        self.label1 = Label(self.leftFrame, text='Your events for this month: ', font='Baskerville 20 bold') #create label object
        self.label1.grid(row = 1)
        self.upcoming_activities_lbox = Listbox(self.leftFrame, font='Baskerville 20', width=30, height=5, borderwidth=0) #create listbox object
        self.upcoming_activities_lbox.configure(justify=CENTER)
        self.upcoming_activities_lbox.grid(row = 2)

        self.label2 = Label(self.leftFrame, text='Check events\nfor specific date (dd.mm.yy) ',font='Baskerville 20')  # create label object
        self.label2.grid(row=3)
        self.e2 = Entry(self.leftFrame)
        self.e2.grid(row=4)
        self.btnShow = Button(self.leftFrame, text="Show", font='Baskerville 20', command=self.getSpecificActivity)
        self.btnShow.grid(row=5)
        self.lbox_specific_activity = Listbox(self.leftFrame, width=30, height=5, font='Baskerville 20', borderwidth=0)
        self.lbox_specific_activity.grid(row=6)
        self.lbox_specific_activity.bind("<ButtonRelease-1>", self.select)  # bind event with an object (listbox)

        self.btnDone = Button(self.leftFrame, text="Done with Event", font='Baskerville 20', command=self.doneWithActivity)
        self.btnDone.grid(row=7)
        self.btnDelete = Button(self.leftFrame, text="Delete Event", font='Baskerville 20', command=self.deleteActivity)
        self.btnDelete.grid(row=8)

        self.btnUpdate = Button(self.leftFrame, text="Update Event", font='Baskerville 20', command=self.updateActivity)
        self.btnUpdate.grid(row=10)
        self.btnStore = Button(self.leftFrame, text="Store Event", font='Baskerville 20', command=self.storeUpdatedActivity)
        self.btnStore.grid(row=11)


        #CENTRE FRAME
        self.headline = Label(self.centreFrame, text='My Planner', font='Baskerville 30 bold', height=2)  # headline of the window
        self.headline.grid(row=0)
        self.day_date_lbox = Listbox(self.centreFrame, font='Baskerville 20', borderwidth=0, height=3, width=40)  # create listbox object
        self.day_date_lbox.configure(justify=CENTER)
        self.day_date_lbox.grid(row=1)
        # self.cv = Canvas(self.centreFrame, bg='white')
        # self.cv.grid(row = 0)
        #
        # self.image = Image.open('image1.jpeg')
        # self.image = self.image.resize((600, 600), Image.ANTIALIAS)  ## The (250, 250) is (height, width)
        # self.photo = ImageTk.PhotoImage(self.image)
        # self.cv.create_image(2, 2, image=self.photo, anchor='center')
        self.label_date = Label(self.centreFrame, text=f'Current Weather in {self.weather_forcast.city}', font='Baskerville 20 bold', height=1)  # create label object
        self.label_date.grid(row=2)
        self.weather_lbox1 = Listbox(self.centreFrame, font='Baskerville 20', borderwidth=0, height=1, width=40)  # create listbox object
        self.weather_lbox1.configure(justify=CENTER)
        self.weather_lbox1.grid(row=3)
        self.weather_lbox1.insert(END, f"{self.weather_forcast.getCurrentWeather()[1]}, {self.weather_forcast.getCurrentWeather()[2]},")
        self.weather_lbox2 = Listbox(self.centreFrame, font='Baskerville 20', borderwidth=0, height=2, width=40)  # create listbox object
        self.weather_lbox2.configure(justify=CENTER)
        self.weather_lbox2.grid(row=4)
        self.weather_lbox2.insert(END, f"{self.weather_forcast.getCurrentWeather()[3]}, {self.weather_forcast.getCurrentWeather()[4]}.")

        self.label_quote = Label(self.centreFrame, relief=GROOVE, text="Quote of the day", font='Baskerville 20 bold', borderwidth=0, anchor = 'center', width=40)  # creating object of data type Label
        self.label_quote.grid(row = 5)
        self.text_quote = Text(self.centreFrame, width=40, height = 5, font='Baskerville 20 italic', borderwidth=0)
        self.text_quote.grid(row = 6)

        self.label_date = Label(self.centreFrame, text='Date of Event (dd.mm.yy)', font='Baskerville 18', height=1)  # create label object
        self.label_date.grid(row=7)
        self.entry_date = Entry(self.centreFrame)  # create entry object
        self.entry_date.grid(row=8)
        self.label_time = Label(self.centreFrame, text='Time of Event (hh:mm)', font='Baskerville 18', height=1)  # create label object
        self.label_time.grid(row=9)
        self.entry_time = Entry(self.centreFrame)  # create entry object
        self.entry_time.grid(row=10)
        self.label_event = Label(self.centreFrame, text='Event', font='Baskerville 18', height=1)  # create label object
        self.label_event.grid(row=11)
        self.entry_event = Entry(self.centreFrame)  # create entry object
        self.entry_event.grid(row=12)
        self.btnAdd = Button(self.centreFrame, text="Add New Event", font='Baskerville 20', command=self.writeToDatabase)
        self.btnAdd.grid(row=13)



        # RIGHT FRAME
        self.txt_hacker_news = Text(self.rightFrame, font='Baskerville 20 bold', width=30, height=2)
        self.txt_hacker_news.grid(row=0, sticky="NWE")
        self.txt_hacker_news.insert(END, f'Most Popular News\nin Hacker News:')
        #article1
        self.txt_hacker_article1 = Text(self.rightFrame, font='Baskerville 20', width=30, height=3, cursor="hand1")
        self.txt_hacker_article1.grid(row=1, sticky="WE")
        self.txt_hacker_article1.insert(END, f'Title: {self.hacker_news.getTitles(0)}\nPoints: {self.hacker_news.getPoints(0)}')
        self.txt_hacker_article1.bind("<Button-1>", lambda x: self.callback(self.hacker_news.getLinks(0)))
        # #article2
        # self.txt_hacker_article2 = Text(self.rightFrame, font='Baskerville 20', width=30, height=3, cursor="hand1")
        # self.txt_hacker_article2.grid(row=2, sticky="WE")
        # self.txt_hacker_article2.insert(END, f'Title: {self.hacker_news.getTitles(1)}\nPoints: {self.hacker_news.getPoints(1)}')
        # self.txt_hacker_article2.bind("<Button-1>", lambda x: self.callback(self.hacker_news.getLinks(1)))
        # #article3
        # self.txt_hacker_article2 = Text(self.rightFrame, font='Baskerville 20', width=30, height=3, cursor="hand1")
        # self.txt_hacker_article2.grid(row=3, sticky="WE")
        # self.txt_hacker_article2.insert(END, f'Title: {self.hacker_news.getTitles(2)}\nPoints: {self.hacker_news.getPoints(2)}')
        # self.txt_hacker_article2.bind("<Button-1>", lambda x: self.callback(self.hacker_news.getLinks(2)))


    # METHODS
    def getCurrentDay(self):
        try:
            dt = pendulum.now()
            day = dt.format('[Today is] dddd')
            date = f"Date: {dt.to_formatted_date_string()}"
            self.day_date_lbox.insert(END, day)
            self.day_date_lbox.insert(END, date)
        except:
            self.handleError(self.getCurrentDay, "Current day can not be retrieved...")

    def getCurrentDate(self):
        try:
            for d in self.database.dates:
                self.day_date_lbox.insert(END, d)
        except:
            self.handleError(self.getCurrentDate, "Current date can not be retrieved...")

    def getActivityOfThisMonth(self):
        try:
            for a in self.database.getFromDatabase('activity'):
                if str(a[0])[3:5] == str(pendulum.now())[5:7]: #if current month equals to month in DB
                    if str(a[0])[:2] >= str(pendulum.now())[8:10]: # compare days, display only upcoming days
                        value = f"{str(a[0])[:2]}/{str(a[0])[3:5]}/{str(a[0])[8:10]} at {str(a[1])[:5]} o'clock: {a[2]}"
                        self.upcoming_activities_lbox.insert(0, value)
        except:
            self.handleError(self.getSpecificActivity, "Activities/Events of this month can not be retrieved...")

    def getQuote(self):
        try:
            quote = ""
            author = ""
            quote_of_the_day = choice(self.database.getFromDatabase('quote'))
            for i, x in enumerate(quote_of_the_day):
                if i == 1:
                    quote = x
                if i == 2:
                    author = x
            self.text_quote.insert(END, f"'{quote}'")
            self.text_quote.insert(END, f'\n{author}')
        except:
            self.handleError(self.getQuote, "Quote can not be retrieved...")

    def getSpecificActivity(self):
        try:
            counter = 0
            self.lbox_specific_activity.delete(0, END)
            for row in self.database.getFromDatabase('activity'):
                for i, element in enumerate(row):
                    if i == 0:
                        year = str(element)[8:10]
                        month = str(element)[3:5]
                        day = str(element)[0:2]
                        if self.e2.get()[:2] == day and self.e2.get()[3:5] == month and self.e2.get()[6:8] == year:
                            self.lbox_specific_activity.insert(END, f'{str(row[1])[:5]} → {row[2]}\n')
                            counter += 1
            if counter == 0:
                self.lbox_specific_activity.insert(END, f'Good news! :) No events...')
        except:
            self.handleError(self.getSpecificActivity, "Specific activity/event can not be retrieved...")

    def select(self, *args):
        try:
            selection = self.lbox_specific_activity.get(ANCHOR)
            # selection = self.lbox_specific_activity.index(self.lbox_specific_activity.curselection())
            return selection
        except:
            self.handleError(self.select, "Select does not work...")

    def doneWithActivity(self):
        try:
            check_activity = False
            check_date = False
            check_time = False
            new_activity = None
            new_date = None
            new_time = None
            activity = str(self.select()[8:-1])
            date = str(self.e2.get())
            time = str(self.select()[:5])
            result = ''
            for letter in activity:
                result = result + letter + '\u0336' # activity with strike-through
            sel = self.lbox_specific_activity.curselection()
            for index in sel[::-1]:
                self.lbox_specific_activity.delete(index)
                self.lbox_specific_activity.insert(index,result)
            for row in self.database.getFromDatabase('activity'):
                for i, element in enumerate(row):
                    if i == 2:  # if activity
                        if element == activity:
                            check_activity = True
                            new_activity = element
                    if i == 1:  # if time
                        if str(element)[:5] == time:
                            check_time = True
                            new_time = element
                    if i == 0:  # if date
                        # year = str(element)[2:4]
                        # month = str(element)[5:7]
                        # day = str(element)[8:10]
                        year = str(element)[8:10]
                        month = str(element)[3:5]
                        day = str(element)[0:2]
                        if date[:2] == day and date[3:5] == month and date[6:8] == year:
                            check_date = True
                            new_date = element
            if check_activity and check_date and check_time:
                self.database.doneUpdateDatabase('activity', new_date, new_time, new_activity)
        except:
            self.handleError(self.doneWithActivity, "Activity/Event can not be marked as 'Done'...")

    def updateActivity(self):
        try:
            date = str(self.e2.get())
            time = str(self.select()[:5])
            activity = str(self.select()[8:-1]) #activity
            self.entry_date.delete(0, END)
            self.entry_date.insert(0, date)
            self.entry_time.delete(0, END)
            self.entry_time.insert(0, time)
            self.entry_event.delete(0, END)
            self.entry_event.insert(0, activity)
            self.stored_date = f"{date[:6]}20{date[6:8]}"
            self.stored_time = str(time)
            self.stored_activity = str(activity)
        except:
            self.handleError(self.updateActivity, "Activity/Event can not be updated...")

    def storeUpdatedActivity(self):
        try:
            self.database.deleteFromDatabase('activity', self.stored_date, self.stored_time, self.stored_activity)
            new_date_entry = f"{self.entry_date.get()[:6]}20{self.entry_date.get()[6:8]}"
            new_time_entry = self.entry_time.get()
            new_event_entry = self.entry_event.get()
            self.database.addToDatabase(new_date_entry, new_time_entry, new_event_entry)
            self.entry_date.delete(0, END)
            self.entry_time.delete(0, END)
            self.entry_event.delete(0, END)
            self.e2.delete(0, END)
            self.e2.insert(0, "Update - successful")
        except:
            self.handleError(self.storeUpdatedActivity, "Updated activity/event can not be stored...")

    def deleteActivity(self):
        try:
            check_activity = False
            check_date = False
            check_time = False
            new_activity = None
            new_date = None
            new_time = None
            activity = str(self.select()[8:-1])
            date = str(self.e2.get())
            time = str(self.select()[:5])
            sel = self.lbox_specific_activity.curselection()
            for index in sel[::-1]:
                self.lbox_specific_activity.delete(index)
            for row in self.database.getFromDatabase('activity'):
                for i, element in enumerate(row):
                    if i == 2: #if activity
                        if element == activity:
                            check_activity = True
                            new_activity = element
                    if i == 1: #if time
                        if str(element)[:5] == time:
                            check_time = True
                            new_time = element
                    if i == 0: #if date
                        year = str(element)[8:10]
                        month = str(element)[3:5]
                        day = str(element)[0:2]
                        if date[:2] == day and date[3:5] == month and date[6:8] == year:
                            check_date = True
                            new_date = element
            if check_activity and check_date and check_time:
                self.database.deleteFromDatabase('activity', new_date, new_time, new_activity)
                self.e2.delete(0, END)
                self.e2.insert(0, "Delete - successful")
        except:
            self.handleError(self.deleteActivity, "Activity/Event can not be deleted...")

    def callback(self, url): # forward users to a specific article(url si given)
        try:
            webbrowser.open_new(url)
        except:
            self.handleError(self.callback, "Link can not be opened...")

    def writeToDatabase(self):
        try:
            date_entry = self.entry_date.get()
            time_entry = self.entry_time.get()
            event_entry = self.entry_event.get()
            date_updated = f"{self.entry_date.get()[:6]}20{self.entry_date.get()[6:8]}"
            self.database.addToDatabase(date_updated, time_entry, event_entry)
            self.entry_date.delete(0, END)
            self.entry_time.delete(0, END)
            self.entry_event.delete(0, END)
            self.e2.delete(0, END)
            self.e2.insert(0, "Adding - successful")
        except:
            self.handleError(self.writeToDatabase, "Item can not be stored in DB... ")

    def handleError(self, funct, msg):
        title = "'Oops, something is wrong'"
        if easygui.ccbox(msg, title):  # show a Try Again/Cancel dialog
            funct.__call__()  # user chose Try Again
        # else:  # user chose Cancel
        #     sys.quit()
        #     sys.exit(0)



mw1 = MainWindow() #Main Window object has been created
mw1.getCurrentDay() #call functions
mw1.getCurrentDate()
mw1.getQuote()
mw1.select()
mw1.getActivityOfThisMonth()



mainloop() # wait for user interaction

# insert into activity values ('12.31.2020', '10:00', 'running');

# insert into quote (quote, author) values ('Only a life lived for others is a life worthwhile.', 'Albert Einstein');

