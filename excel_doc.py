import pandas as pd
import os


"""
    This grabs the desktop of any user
"""
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'OneDrive\Desktop')

"""
    Dataframes are also known as Tables 
"""
df = pd.DataFrame(
    {"x": [1, 2, 3],
     "y": [4, 5, 6]})
# print(df)


sf = pd.Series(["John", "Steve", "Walter"])
# print(sf)


ddf = pd.DataFrame({"Names": sf})
# print(ddf)


# TODO: Create excel.xlsx file from Mock Data

from Person import Person
import datetime


"""
    Establish current year to do a estimation of year born 
    
    **NOTES**
        Year born is only an estimation
        exact year born not calculated due to people being born end of year, etc. 
        
"""
current_year = datetime.date.today().year


"""
    Creation of Mock Data to use for Table Creation
"""
# DATA INDIVIDUALLY
william = Person("William", 23)
jerry = Person("Jerry", 40)
terry = Person("Terry", 32)
kelsi = Person("Kelsi", 29)
sonia = Person("Sonia", 54)


# MOCK DATA OF A COLLECTION OF INDIVIDUAL DATA
persons = [
    william,
    jerry,
    terry,
    kelsi,
    sonia
]


"""
    Creation of rows for the Table
"""
name_row = pd.Series([person.name for person in persons])
age_row = pd.Series([person.age for person in persons])
year_born_row = pd.Series([current_year - person.age for person in persons])
catch_fraise_row = pd.Series(person.say_hello() for person in persons)


"""
    Table Creation
"""
table_frame = pd.DataFrame({
    "Name":                name_row,
    "Age":                 age_row,
    "Year Born":           year_born_row,
    "Catch Fraise":        catch_fraise_row
})

print("\nTABLE TO BE EXPORTED... \n" + "\n" + str(table_frame))

"""
    Add table styling 
"""


"""
    Saves file to the Desktop
    Must have xlsxwriter to export as .xlsx file
"""
table_frame.to_excel(desktop + "/people_chart.xlsx", sheet_name="People Data", index=False)


