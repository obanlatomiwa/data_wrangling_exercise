# Datopian Data Wrangling Exercise
 Scripts to normalize data and return a CSV. All CSVs here use a comma `,` as the delimiter.

## Getting Started
To use this project locally you must have [python](https://www.python.org/downloads/) installed.

1. **Clone the repository:**
    ```sh
    git clone -b main https://github.com/obanlatomiwa/data_wrangling_exercise.git
    ```
2. **Setup the virtual environment by running:**
    ```sh
    virtualenv env
    source env/Scripts/activate # for windows
    source env/bin/activate # for unix based systems
    ```
    in the project root folder.
   
3. **Install External Dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
   
5. **Running the script**
    In the project root directory, run:
    ```sh
    python road_safety_in_europe/scripts/webscrapping_from_wikipedia.py
    ```

## Scripts

### Get European Union Road Safety Facts and Figures
Located at [road_safety_in_europe/scripts/webscrapping_from_wikipedia.py](road_safety_in_europe/scripts/webscrapping_from_wikipedia.py), 
this scripts scraps data from the European Union Road Safety Facts and Figures table from wikipedia [https://en.wikipedia.org/wiki/Road_safety_in_Europe](https://en.wikipedia.org/wiki/Road_safety_in_Europe).

## Data
The script result and required result is saved and located in this folder with the name "result.csv".
The wikipedia data is saved and located in the sub-folder named raw. The data is named "wikipedia_extracted_data.csv".

My Tabular Data Package is located at [https://github.com/obanlatomiwa/data_wrangling_exercise/blob/main/road_safety_in_europe/datapackage.json](https://github.com/obanlatomiwa/data_wrangling_exercise/blob/main/road_safety_in_europe/datapackage.json).
