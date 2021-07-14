import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


def webscrapping_from_wikipedia():
    # STEP 1
    # Use the following Wikipedia page and get the data from the “European Union Road Safety Facts and Figures” table:
    # https://en.wikipedia.org/wiki/Road_safety_in_Europe

    # Make a request to the wikipedia url and store the html response in a variable
    # It is not legal to scrape any website, so we check the status code.
    # 200 shows that you can go ahead and download it.

    # wikipedia url
    wikipedia_url = "https://en.wikipedia.org/wiki/Road_safety_in_Europe"

    # get the table class by inspecting the table on your web browser
    table_class = "wikitable sortable"
    response = requests.get(wikipedia_url)
    print("Response from Wikipedia", response.status_code)

    # response.status_code returns 200

    # now we can get parse the data from the html by passing the html tag in this case <table>
    # and the particular table class
    wiki_data = BeautifulSoup(response.text, 'html.parser')
    result = wiki_data.find('table', {'class': table_class})

    # read the html into a list of dataframe objects
    df = pd.read_html(str(result))

    # convert the list into a dataframe
    df = pd.DataFrame(df[0])

    # get current working directory and generate a filepath to the data folder
    file_path = os.getcwd()
    file_path = ''.join(file_path) + '/road_safety_in_europe/data/raw/' + 'wikipedia_extracted_data.csv'

    # save the csv to the dataset folder
    df.to_csv(file_path)

    # STEP 2
    # clean dataset
    # Resulting CSV file should only include the following columns: Country, Year, Area, Population, GDP per capita,
    # Population density, Vehicle ownership, Total road deaths, Road deaths per Million Inhabitants.
    # Note that “Year” column value is always 2018.

    # drop unwanted columns
    data = df.drop(["Road Network Length (in km) in 2013[29]", "Number of People Killed per Billion km[30]",
                    "Number of Seriously Injured in 2017/2018[30]"], axis=1)

    # rename columns
    data = data.rename(columns={"Area (thousands of km2)[24]": "Area",
                                "Population in 2018[25]": "Population",
                                "GDP per capita in 2018[26]": "GDP per capita",
                                "Population density (inhabitants per km2) in 2017[27]": "Population density",
                                "Vehicle ownership (per thousand inhabitants) in 2016[28]": "Vehicle ownership",
                                "Total Road Deaths in 2018[30]": "Total road deaths",
                                "Road deaths per Million Inhabitants in 2018[30]": "Road deaths per Million Inhabitants"
                                })

    # clean the column GDP per capita from unwanted characters '11,500†a' to '11500'
    data['GDP per capita'] = data['GDP per capita'].str.replace(r'[^0-9]+', '').astype(int)

    # clean the column Population from unwanted characters '82.792,351' to '82792351'
    data['Population'] = data['Population'].str.replace(r'[^0-9]+', '').astype(int)

    # insert a new column "Year" to the dataframe, at the index close to Column "Country" and fill it up with value
    # "2018"
    data.insert(1, "Year", 2018)

    # STEP 3
    # Data should be sorted by “Road deaths per Million Inhabitants” column.

    # sorting the dataframe
    # I am assuming ascending order here
    data = data.sort_values("Road deaths per Million Inhabitants")

    # get current working directory and generate a filepath to the data folder
    file_path = os.getcwd()
    file_path = ''.join(file_path) + '/road_safety_in_europe/data/' + 'result.csv'

    # save the csv to the dataset folder
    data.to_csv(file_path, index=False)
    print(data)


# Runs the script to extract data from wikipedia and generate a resulting csv
webscrapping_from_wikipedia()
