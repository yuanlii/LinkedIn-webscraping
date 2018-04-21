import unittest

def getDegreeFromPersonName(person_first_name):
	conn=sqlite3.connect('linkedIn.sqlite')
	cur=conn.cursor()

	statement='''
	SELECT degree_name
	FROM education
	WHERE first_name = ?
	'''
	params = (person_first_name,)
	rows = cur.execute(statement,params).fetchall()
	for row in rows:
		print(row)

def getSchoolNameFromLastName(person_last_name):
	conn=sqlite3.connect('linkedIn.sqlite')
	cur=conn.cursor()

	statement='''
	SELECT school_name
	From education
	Where last_name = ?
	'''
	params = (person_last_name,)
	rows = cur.execute(statement,params).fetchall()
	for row in rows:
		print(row)

def getOccupationFromFirstName(person_first_name):
	conn=sqlite3.connect('linkedIn.sqlite')
	cur=conn.cursor()

	statement='''
	SELECT occupation
	From LinkedIn_profiles
	Where first_name='Patrick'
	'''
	params = (person_first_name,)
	rows = cur.execute(statement,params).fetchall()
	for row in rows:
		print(row)

'''
unittest
'''
class TestDataBase(unittest.TestCase):
	
	def getDegreeFromPersonName(self):
		self.assertEqual(getDegreeFromPersonName("Dr. Jay I."),"Ph.D. (Business Administration)")
		self.assertEqual(getDegreeFromPersonName("Ashton"),"Experienced Architecture Minor Entrepreneurship and Innovation")

		self.assertEqual(getDegreeFromPersonName("Kelly"),"Master of Arts")
		self.assertEqual(getDegreeFromPersonName("woo"),"Bachelor s degree")
		self.assertEqual(getDegreeFromPersonName("Prateek Kumar"),"Masterâs Degree")


	def getSchoolNameFromLastName(self):
		self.assertEqual("Sinha","University of Michigan - Stephen M. Ross School of Business")
		self.assertEqual("Keys","Michigan State University")
		self.assertEqual("Kowatch","The Ohio State University")
		self.assertEqual("deokgil","Academy of Art University")
		self.assertEqual("Pradeep","University of Michigan - School of Information")


	def getOccupationFromFirstName(self):
		self.assertEqual("Lu Joy","Product Designer at Clinc, Inc.")
		self.assertEqual("Roberta","Founding Dean of the College of Fine Arts and Mass Communication at Sam Houston State University")
		self.assertEqual("Anay","UX Researcher at Microsoft WDG.")
		self.assertEqual("Bill","Economic Strategist at Boenning & Scattergood")
		self.assertEqual("Josue","Librarian, Coordinator of Public Services & Outreach, Special Collections Research Center at Temple University Libraries")


