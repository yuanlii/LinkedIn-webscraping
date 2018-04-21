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
        self.first_name = self.safeImport(data, 'firstName')
        self.last_name = self.safeImport(data, 'lastName')
        self.urlId = self.safeImport(data, 'publicIdentifier')
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
            safe_string = data[keyName].replace("\'", " ").replace("\"", " ")
            targetVariable = safe_string
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

def check_tables(db_name):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

    '''
    test if tables already exists
    '''
    try:
        simple_check = 'SELECT * from LinkedIn_profiles' #if the table already exists, then execute
        cur.execute(simple_check)
        print("there is a table. drop it.")
        # if exists, prompt to user: "Table exists. Delete?yes/no"
        # user=input("LinkedIn_profiles Table already exists. Drop table? yes/no\n")
        user = "yes"

        # if user input is yes, drop table. Else, use move on and use existing table
        if user == "yes": 
            print("step into if statment")

            statement='''
            DROP table if exists 'LinkedIn_profiles';
            '''

            cur.execute(statement)

            statement='''
            DROP table if exists 'education';
            '''

            cur.execute(statement)
            conn.commit()
            print("ordered command")

    except Exception:
        print("get table LinkedIn_profiles or drop table failed")


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
def createProfileTable(db_name):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()
    try:
        statement='''   
            CREATE TABLE `LinkedIn_profiles` (
            `first_name`   TEXT NOT NULL,
            `last_name` TEXT NOT NULL,
            `occupation`  TEXT NOT NULL,
            `urlId`    TEXT NOT NULL,
            `location`    TEXT NOT NULL
            )
        '''
        cur.execute(statement)
        conn.commit()

    except:
        print("create LinkedIn_profile table failed")



def createCompanyTable(company_data):
    '''
    create company info table ( based on linkedin company search API )
    '''
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

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

#conn.close()

'''
create education table
'''
def createEduTable(db_name):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

    # try:
    statement='''   
    CREATE TABLE `education` (
    `first_name`   TEXT NOT NULL,
    `last_name` TEXT NOT NULL,
    `profile_url_id` TEXT NOT NULL,
    `degree_name`   TEXT NOT NULL,
    `school_name`   TEXT NOT NULL
    )
    '''
    cur.execute(statement)
    conn.commit()

    # except Exception:
    #     print("create education table failed", Exception)
    #     exit()



'''
insert info into db
'''

def insertLinkedinProfileData(profiles,db_name):
    #add code to connect to database and get a Cursor
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

    for profile in profiles:
        # try:
        statement='''
        INSERT INTO LinkedIn_profiles (first_name,last_name,occupation,urlId,location)
        values('{}','{}','{}','{}','{}')
        '''.format(profile.first_name, profile.last_name, profile.occupation, profile.urlId, profile.location) 

        print("SQL command is: ", statement)

        cur.execute(statement)
        conn.commit()

        # except:
        #     print("insert linkedin detail info into db failed")

def insertEduData(profiles,db_name):
    conn=sqlite3.connect(db_name)
    cur=conn.cursor()

    for profile in profiles:
        # try:
        if len(profile.educations) == 0:
            profile.educations.append( {'degree_name': '', 'school_name': ''} )

        statement='''
        INSERT INTO education (first_name, last_name, degree_name, school_name, profile_url_id)
        values('{}', '{}', '{}','{}', '{}')
        '''.format(profile.first_name, profile.last_name, profile.educations[0]['degree_name'], profile.educations[0]['school_name'], profile.urlId) 

        print("SQL command is: ", statement)

        cur.execute(statement)
        conn.commit()
        # except Exception:
        #     print(profile.urlId)
        #     profile.printEdu()
        #     print(Exception)
        #     exit()



def insertCompanyData(company_data):
    '''
    insert data into company_search table
    '''
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
        #   print("insert linkedin_search info into db failed")

#conn.close()


if __name__ == "__main__":

    db_name ="linkedIn.sqlite"

    init_db(db_name)
    check_tables()

    createProfileTable(profile_class)
    # createCompanyTable(company_data)

    insert_linkedin_profile_data(profile_class)
    # insertCompanyData(company_data)







