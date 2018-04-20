import requests
from bs4 import BeautifulSoup
from credential import *
import json
from create_DB import *

'''
part1: scraping
'''

'''
LOGIN IN
'''
def login():
	global CLIENT
	CLIENT = requests.Session()
	HOMEPAGE_URL = 'https://www.linkedin.com'
	LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'
	html = CLIENT.get(HOMEPAGE_URL).content
	soup = BeautifulSoup(html, 'html.parser')
	csrf = soup.find(id="loginCsrfParam-login")['value']
	login_information = {
	    'session_key': LINKEDIN_NAME,
	    'session_password': LINKEDIN_PW,
	    'loginCsrfParam': csrf,
	}
	CLIENT.post(LOGIN_URL, data=login_information)

# '''
# After logged in
# '''

#
def getPrettifiedHtmlFromRequest(query_url):
	base_url = 'https://www.linkedin.com/'
	visit_url = base_url + query_url
	global CLIENT

	print("requesting page", visit_url)
	page_text = CLIENT.get(visit_url).text
	soup = BeautifulSoup(page_text, 'html.parser')
	print("OK")
	page_structure=soup.prettify()

	return page_structure

def getSearchResultPageHtml(keywords, page_number):
	global CLIENT
	keywords = keywords.replace(' ', '%20')

	query_url = 'search/results/index/?keywords=' + keywords + '&origin=GLOBAL_SEARCH_HEADER'
	if page_number > 1:
		query_url += '&page=' + str(page_number)

	page_structure = getPrettifiedHtmlFromRequest(query_url)

	return page_structure

def getSearchResultPageList(keywords, total_page):
	page_structure_list = []
	for page_number in [ (index + 1)  for index in range(total_page) ]:
		page_structure = getSearchResultPageHtml(keywords, page_number)
		page_structure_list.append(page_structure)
	return page_structure_list

#
def getAllCodesFromHtml(html_page):
	# read in html
	soup = BeautifulSoup(html_page,'html.parser')
	# find all code
	code_results = soup.find_all('code')
	# convert to json
	code_dict = {}
	i = 0
	for code in code_results:
		json_plain_text = code.string
		i += 1
		try:
			code_dict[str(i)] = json.loads(json_plain_text)
		except:
			pass
	# store all in one dict
	return code_dict

def searchAndGenerateCodeFile(keywords, total_page, output_code_dictionaries_fileName):
	lst = getSearchResultPageList(keywords, total_page)

	'''
	caching
	'''
	with open('all_page_htmls', 'w') as file:
		file.write(json.dumps(lst))

	with open('all_page_htmls', 'r') as file:
		plain_text = file.read()
		lst = json.loads(plain_text)

	code_dictionaries = []
	for index, html_page in enumerate(lst):
		code_dict = getAllCodesFromHtml(html_page)
		code_dictionaries.append(code_dict)

	with open(output_code_dictionaries_fileName, 'w') as file:
		file.write( json.dumps(code_dictionaries) )

def getMeaningfulDataFromCode(code_dict, significant_keys, mining_degree):
	meaningful_data = [] # only store meaningful stuff in here
	if type(significant_keys) != type([]):
		significant_keys = [ significant_keys ]

	if mining_degree == 1:
		target_json_data = code_dict['13']['included'] # still lots of messy stuff, we want things within "the index interval" like [40:49] or [433:480] or whatever
		for data in target_json_data:
			if all(key in data for key in significant_keys):
				# meaningful stuff get!
				meaningful_data.append(data)
			else:
				pass
	elif mining_degree == 2:
		# print("hey", len(list(code_dict.values())))
		for first_degree in list(code_dict.values()):
			if 'included' in first_degree:
				step_in_dict = first_degree['included']
				for second_degree in step_in_dict:
					if all( [key in second_degree for key in significant_keys] ):
						meaningful_data.append(second_degree)
	return meaningful_data

def getAllPeopleDataFromSearch(code_dictionaries):
	all_people_result_data = []
	for code_dict in code_dictionaries:
		one_page_people = getMeaningfulDataFromCode(code_dict, "firstName", 1)
		all_people_result_data += one_page_people
	return all_people_result_data

def getUniquePeopleData(all_people_result_data):
	unique_people_data = {}
	for people in all_people_result_data:
		fullName = people["firstName"] + " " + people["lastName"]
		if fullName not in unique_people_data:
			unique_people_data[fullName] = people
		else:
			# yes, already have this name in our dict
			if unique_people_data[fullName]["occupation"] == people["occupation"]:
				# print("- duplicated: " + fullName)
				pass
			else:
				# same name but different people
				print("- same name: " + fullName, people["occupation"])
				unique_people_data[fullName + ' ' + people["occupation"]] = people
	return unique_people_data

def getUniquePeopleDataFromCodeFile():
	'''
	Got all 30 search result pages saved in "all_page_codes"
	'''
	# read data from file "all_page_codes"
	code_dictionaries = []
	with open('all_page_codes', 'r') as file:
		t = file.read()
		code_dictionaries = json.loads(t)

	# all_people_result_data = [ person, person, preson, ...]
	all_people_result_data = getAllPeopleDataFromSearch(code_dictionaries)
	return getUniquePeopleData(all_people_result_data)

def generateProfileObjListFromFile():
	profiles = []
	file_name = 'user_experience_people.json'

	'''
	get python dict from file
	'''
	ux_people_dictionary = {}
	with open('user_experience_people.json','r') as file:
		t = file.read()   
		ux_people_dictionary = json.loads(t)

	'''
	each key-value pair in ux_people_dictionary is a person.
	for that person, we new a profile() class object.
	then we import all that person's data into profile object.
	once we're done, the profile is well prepared and ready to be appended to profiles list
	'''
	for key in ux_people_dictionary:
		ux_person = ux_people_dictionary[key]

		# TODO: generate a new profile class object
		ux_person_obj = Profile()

		# TODO: import data in ux_person to the profile object
		ux_person_obj.importBasicData(ux_person)

		# TODO: add this profile to profiles list
		profiles.append(ux_person_obj)

	return profiles

def generate_people_by_scrapping_saerch_results():
	login()

	''' 
	generate file "all_page_codes"
	'''
	searchAndGenerateCodeFile('user experience researcher', 30, 'all_page_codes')

	'''
	get unique data from code file (search result pages)
	'''
	unique_people_data = getUniquePeopleDataFromCodeFile() 

def cacheDict(file_path, dictionary):
	from pathlib import Path
	p = Path(file_path + ".json")
	if p.exists():
		pass
	else:
		p.write_text( json.dumps(dictionary) )

def tryGetCodeDictFromCache(url_id):
	from pathlib import Path
	p = Path(url_id + ".json")
	if p.exists():
		return json.loads(p.read_text())
	else:
		return False

def importDataByRequestingDetailProfilePage(profiles):
	login()
	for profile in profiles:
		# request page and get html
		code_dict = tryGetCodeDictFromCache('detail_profile/' + profile.urlId)
		if code_dict == False:
			print("no cache for", profile.urlId)
			
			print("logged in")
			prettified_html = getPrettifiedHtmlFromRequest('in/' + profile.urlId)

			# use soup and get soup obj

			# use soup to find all codes
			code_dict = getAllCodesFromHtml(prettified_html)
			cacheDict('detail_profile/' + profile.urlId , code_dict)

		# since code is in json format, convert codes into json == dict in python

		# now we get meaningful data by try - except. this is the education data.
		education_data_list = getMeaningfulDataFromCode(code_dict, "degreeName", 2)
		profile_overview = getMeaningfulDataFromCode(code_dict, ['locationName', 'firstName'], 2)[0]

		# finally, import education data into profile
		profile.importAllEducationData(education_data_list)
		profile.location = profile_overview['locationName']

if __name__ == "__main__":
	'''
	Part 1: Search UX Researchers
	'''
	# unique_people_data = generate_people_by_scrapping_saerch_results()

	'''
	Part 2: Detail Profile
	'''
	profile_list = generateProfileObjListFromFile() # total 446 profiles

	importDataByRequestingDetailProfilePage(profile_list) # total 446 profiles, so range [0:445]
	
	for profile in profile_list:
		if len(profile.educations ) > 0:
			# print(profile.educations)
			pass

	# TODO: push profiles in database (in other files)
	# for profile in profile_list: ...

	# TODO: unit test (in other files)

	# TODO: user interaction (user_input = input(...))
	# if-else: 1 = visualize education, 2 = visualize location, ...

	# TODO: visualization
	# visualizeEdu(), visualizeLocation(), ...

