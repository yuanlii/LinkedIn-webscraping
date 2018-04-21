# 507final_project

This project aims to investigate more about user-experience researchers, in terms of their degree levels, locations, occupation titles, etc. to see if there are interesting insights that I can gain from the profile info of UX researchers. 

1. Data sources
The data of this project is based on the user profiles that I conducted scraping and crawling from LinkedIn. 

2. Code structure
1) web scraping and crawling
major file for implementation: linkedin_run.py (main file for this project)
[significant functions]:
- getPrettifiedHtmlFromRequest():get the results info from request and used BeautifulSoup to format it
- generateProfileObjListFromFile(): get all the information from the webpages and cache it into a Json file, based on which to build the data base and for further data processing and visualization

2) Push data in data base
major file for implementation: create_DB.py
[significant functions]:
- class Profile(): define a class and store the profile info into the class
- importBasicData(): import profile info from search into the data base
- safeImport(): do some data cleaning stuff to make our data valid
- init_db(): create data base
- createProfileTable(): create a table in db called including the basic profile info of each users
- createEduTable():create a education table in db including the degree and school info

3) Data Visualization
major file for implementation:
[significant functions]:all_visualize.py
[significant functions]:
- VisualizeWithUserPrompt(): add user interactions in terminal, and displayed different presentations in accordance with different user commands (1 - barchart, 2 - piechart, 3 - table, 4 - horizontal chart)

4) Unittest
major file for implementation: linkedin_unittest.py
[significant functions]:
- class TestDataBase(): to test if the data is properly stored in db














