import sqlite3
import sys

'''
 make the linkedIn profiles that we scraped into a class 
'''

class Profile():
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.occupation = ''
        self.urlId = ''
        self.location = ''
        self.educations = []
        
        self.industry = ''

    def importBasicData(self,data):
        self.first_name = data['firstName']
        self.last_name = data['lastName']
        self.urlId = data['publicIdentifier']
        self.occupation = self.safeImport( data, 'occupation')
        self.location = self.safeImport( data, 'locationName')

    def importAllEducationData(self, data_list):
        for data in data_list:
            education = {
                "degree_name": "",
                "school_name": "",
            }
            education['degree_name'] = self.safeImport(data, 'degreeName')
            education['school_name'] = self.safeImport(data, 'schoolName')
            self.educations.append(education)

    def safeImport(self, data, keyName ):
        try:
            targetVariable = data[keyName]
        except:
            targetVariable = ''
        return targetVariable

    def printBasic(self):
        print('basic profile:', self.first_name, self.last_name, self.occupation, self.location)
        return

    def printEdu(self):
        print('edu profile:', self.first_name, self.last_name, "|", [ education['degree_name'] for education in self.educations  ] )

'''
create database
'''
def init_db(db_name):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

    # test if LinkedIn_detail table already exists
    try:
        simple_check = 'SELECT * from LinkedIn_detail' #if the table already exists, then execute
        cur.execute(simple_check)
        print("there is a table")
        # if exists, prompt to user: "Table exists. Delete?yes/no"
        user=input("LinkedIn_detail Table already exists. Drop table? yes/no\n")

        # if user input is yes, drop table. Else, use move on and use existing table
        if user == "yes": 
            print("step into if statment")

            statement='''
            DROP table if exists 'LinkedIn_detail'; 
            '''

            cur.execute(statement)
            conn.commit()
            print("ordered command")

    except Exception:
        print("get table LinkedIn_detail or drop table failed")


    # test if LinkedIn_search table already exists
    try:
        simple_check = 'SELECT * from LinkedIn_search' #if the table already exists, then execute
        cur.execute(simple_check)
        print("there is a table")
    		 # if exists, prompt to user: "Table exists. Delete?yes/no"
        user=input("LinkedIn_search Table already exists. Drop table? yes/no\n")

    	# if user input is yes, drop table. Else, use move on and use existing table
        if user == "yes": 
            print("step into if statment")

            statement='''
            DROP table if exists 'LinkedIn_search'; 
            '''

            cur.execute(statement)
            conn.commit()
            print("ordered command")

    except Exception:
        print("get table LinkedIn_search or drop table failed")


    # test if Company_search table already exists
    try:
        simple_check = 'SELECT * from Company_search' #if the table already exists, then execute
        cur.execute(simple_check)
        print("there is a table")
    	# if exists, prompt to user: "Table exists. Delete?yes/no"
        user=input("Company_search Table already exists. Drop table? yes/no\n")

		 # if user input is yes, drop table. Else, use move on and use existing table
        if user == "yes": 
            print("step into if statment")

            statement='''
            DROP table if exists 'Company_search'; 
            '''

            cur.execute(statement)
            conn.commit()
            print("ordered command")

    except Exception:
        print("get table LinkedIn_search or drop table failed")



    '''
    create detail profile table 
    '''

    try:
        statement='''   
            CREATE TABLE `LinkedIn_detail` (
            `User_id`   INTEGER NOT NULL,
            `LinkedIn_id`   TEXT NOT NULL,
            `FirstName` TEXT NOT NULL,
            `LastName`  TEXT NOT NULL,
            `degreeName`    TEXT NOT NULL,
            `schoolName`    TEXT NOT NULL,
            `summary`    TEXT NOT NULL
            )
        '''
        cur.execute(statement)
        conn.commit()

    except:
        print("create LinkedIn_detail table failed")

# create linkedin search table ( search key word: 'user experience researcher' )
    try:
        statement='''   
            CREATE TABLE `LinkedIn_search` (
            `User_id`   INTEGER NOT NULL,
            `LinkedIn_id`   TEXT NOT NULL,
            `FirstName` TEXT NOT NULL,
            `LastName`  TEXT NOT NULL,
            `Occupation`    TEXT NOT NULL,
            `Location`    TEXT NOT NULL
            )
        '''
        cur.execute(statement)
        conn.commit()

    except:
    	print("create LinkedIn_search table failed")

	# create company info table ( based on linkedin company search API )
    try:
        statement='''   
        CREATE TABLE `Company_search` (
        `Company_id`   INTEGER NOT NULL,
        `name`   TEXT NOT NULL,
        `websiteUrl` TEXT NOT NULL,
        )
        '''
        cur.execute(statement)
        conn.commit()

    except:
    	print("create company_search table failed")


    conn.close()


def insert_linkedin_data(profiles):
    #add code to connect to database and get a Cursor
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

    for profile_obj in profiles:
        # try:
        statement='''
        INSERT INTO LinkedIn_detail (User_id,LinkedIn_id,FirstName,LastName,degreeName,schoolName,summary)
        values('{}','{}',{},'{}','{}','{}',{})
        '''.format(profile_obj.firstName, profile_obj.lastName, profile_obj.degreeName, profile_obj.schoolName, profile_obj.summary ) 

        print("SQL command is: ", statement)
        print("========ready to excute SQL command")
        cur.execute(statement)
        print("SQL exe succeed")
        conn.commit()

        # except:
        #     print("insert linkedin detail info into db failed")

        # try:
        statement='''
        INSERT INTO LinkedIn_search (User_id,LinkedIn_id,FirstName,LastName,Occupation,Location)
        values('{}','{}',{},'{}','{}','{}',{})
        '''.format( profile_obj.firstName, profile_obj.lastName, profile_obj.Occupation, profile_obj.Location ) 

        print("SQL command is: ", statement)
        print("========ready to excute SQL command")
        cur.execute(statement)
        print("SQL exe succeed")
        conn.commit()

        # except:
        #     print("insert linkedin_search info into db failed")

     # insert data into company_search table
    tech_company_lst = []

    with open('tech_company.json','r') as file:
        t = fire.read()
        tech_company_lst = json.loads(t)

        for sub_lst in tech_company_lst:
            for dictionary in sub_lst:
                company_name = dictionary['name']
                company_url = dictionary['websiteUrl']

		# try:
                statement='''
                INSERT INTO Company_search ( name, websiteUrl )
                values('{}',{})
                '''.format( company_name, company_url) 

                print("SQL command is: ", statement)
                print("========ready to excute SQL command")
                cur.execute(statement)
                print("SQL exe succeed")
                conn.commit()

		# except:
		# 	print("insert linkedin_search info into db failed")

    conn.close()


if __name__ == "__main__":

    db_name ="linkedIn.sqlite"

    profiles = [] # get a list of profile objects
    for profile_dict in profiles_dict: 
        profile_obj = Profile(profile_dict)
        profiles.append(profile_obj)

        print("============== step into init_db")
        x = init_db( db_name )
        print("============= step into linkedin db")
        y = insert_linkedin_data( profiles )





