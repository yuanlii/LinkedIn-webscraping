# LinkedIn web scraping project

People with similar background to you can provide insights in terms of making reasonable career decisions. For this project, I am intended to build a tool for people to investigate other people with similar background to you, and thus provide guidance in deciding career paths of ourselves.

## Data sources
The data of this project is based on the user profiles that I conducted scraping and crawling from LinkedIn. 

## Code structure
### web scraping and crawling
major file for implementation: 
* linkedin_run.py (main file for this project)

major functions include:
* getPrettifiedHtmlFromRequest() - get the results info from request and used BeautifulSoup to format it
* generateProfileObjListFromFile() - get all the information from the webpages and cache it into a Json file, based on which to build the data base and for further data processing and visualization

### Push data in data base
major file for implementation: 
* create_DB.py

major functions include:
* class Profile() - define a class and store the profile info into the class
* importBasicData() - import profile info from search into the data base
* safeImport() - do some data cleaning stuff to make our data valid
* init_db() - create data base
* createProfileTable() - create a table in db called including the basic profile info of each users
* createEduTable() - create a education table in db including the degree and school info

### Data Visualization
major file for implementation:
* all_visualize.py

implementation of core functions:
* VisualizeWithUserPrompt() - add user interactions in terminal, and displayed different presentations in accordance with different user commands (1 - barchart, 2 - piechart, 3 - table, 4 - horizontal chart)

### Unittest
major file for implementation: 
* linkedin_unittest.py

implementation of major functions:
* class TestDataBase() - to test if the data is properly stored in db














