from NewsWebScraping import *
from WeatherForcast import *
from MyDB import *
from MainWindow import *
import pytest

# test NewsWebScraping.py
def testGetTitlesWithCorrectIndex():
    hn = HackerNews()
    index0 = 0
    index1 = 1
    index2 = 2
    outcome0 = hn.getTitles(index0)
    outcome1 = hn.getTitles(index1)
    outcome2 = hn.getTitles(index2)
    assert type(outcome0) == str
    assert type(outcome1) == str
    assert type(outcome2) == str

def testGetLinksWithCorrectIndexes():
    hn = HackerNews()
    index0 = 0
    index1 = 1
    index2 = 2
    outcome0 = hn.getLinks(index0)
    outcome1 = hn.getLinks(index1)
    outcome2 = hn.getLinks(index2)
    assert type(outcome0) == str
    assert type(outcome1) == str
    assert type(outcome2) == str

def testGetPointsWithCorrectIndexes():
    hn = HackerNews()
    index0 = 0
    index1 = 1
    index2 = 2
    outcome0 = hn.getPoints(index0)
    outcome1 = hn.getPoints(index1)
    outcome2 = hn.getPoints(index2)
    assert type(outcome0) == int
    assert type(outcome1) == int
    assert type(outcome2) == int

def testTypeFromGetCustomHN():
    hn = HackerNews()
    outcome = hn.get_custom_hn()
    assert type(outcome) == list

def testNumberOfItemsFromGetCustomHN():
    hn = HackerNews()
    outcome = hn.get_custom_hn()
    assert len(outcome) == 3


# test WeatherForcast.py
def testGetNumberOfReturnedItemsFromGetCurrentWeather():
    city = "Linz"
    country_abbreviation = "AT"
    Linz_weather = Weather(city, country_abbreviation)
    outcome = Linz_weather.getCurrentWeather()
    # assert type(returned_list) == list
    assert len(outcome) == 5

def testReturnedTypeFromGetCurrentWeather():
    city = "Linz"
    country_abbreviation = "AT"
    Linz_weather = Weather(city, country_abbreviation)
    outcome = Linz_weather.getCurrentWeather()
    assert type(outcome) == list

# test MyDB.py
def testGetFromDB():
    table_name1 = "quote"
    table_name2 = "activity"
    db = myDatabase()
    outcome = db.getFromDatabase(table_name1)
    assert type(outcome) == list

def testAddToDB():
    date = "31.12.2020"
    time = "06:00"
    activity = "Study time"
    db = myDatabase()
    outcome = db.addToDatabase(date, time, activity)
    assert outcome == True

def testDeleteFromDB():
    table_name = "activity"
    date = "31.12.2020"
    time = "06:00"
    activity = "Study time"
    db = myDatabase()
    outcome = db.deleteFromDatabase(table_name, date, time, activity)
    assert outcome == True

def testUpdateDB():
    table_name = "activity"
    date = "31.12.2020"
    time = "06:00"
    activity = "Study time"
    db = myDatabase()
    outcome = db.doneUpdateDatabase(table_name, date, time, activity)
    assert outcome == True

# test MainWindow.py
def testGetQuote():
    mw = MainWindow()
    outcome1 = mw.getQuote()
    outcome2 = mw.getCurrentDate()
    outcome3 = mw.getCurrentDay()
    assert outcome1 == True
    assert outcome2 == True
    assert outcome3 == True




