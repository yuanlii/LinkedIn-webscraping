import requests
from bs4 import BeautifulSoup
import json


#search API
from linkedin import linkedin
from requests_oauthlib import OAuth2Session

API_KEY = '86w6147zs87hbh'
API_SECRET = '49pdzgplUQStD5xt'
RETURN_URL = 'http://www.google.com'

# authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())

# print(authentication.authorization_url)

'''
https://www.linkedin.com/uas/oauth2/authorization?response_type=code&client_id=86w6147zs87hbh&scope=r_basicprofile%20r_emailaddress%20w_share%20rw_company_admin&state=27f2264218b090954a4a7b46496a3279&redirect_uri=http%3A//www.google.com
'''

'''
code=AQRPzWuFF1aGiUQIYfGNv2QV9GndNkJ77wUUkYq4zXKuRNMeYQp7Ny6f3T0pdi3NdNCDD7WuNk8Ymztd-KgTo1ZYNAwB7O2C_W-h5ZH7YEe3itFpiDGMo8fKIhRI0NSf7dKA6P70VT3Q-KpyxZ12-fwr0w9qXw
state=27f2264218b090954a4a7b46496a3279#!
'''

# authentication.authorization_code = 'AQRPzWuFF1aGiUQIYfGNv2QV9GndNkJ77wUUkYq4zXKuRNMeYQp7Ny6f3T0pdi3NdNCDD7WuNk8Ymztd-KgTo1ZYNAwB7O2C_W-h5ZH7YEe3itFpiDGMo8fKIhRI0NSf7dKA6P70VT3Q-KpyxZ12-fwr0w9qXw'

# result = authentication.get_access_token()
# print ("Access Token:", result.access_token)
# print ("Expires in (seconds):", result.expires_in)

# expire after 60 days
AUTH_CODE = 'AQRPzWuFF1aGiUQIYfGNv2QV9GndNkJ77wUUkYq4zXKuRNMeYQp7Ny6f3T0pdi3NdNCDD7WuNk8Ymztd-KgTo1ZYNAwB7O2C_W-h5ZH7YEe3itFpiDGMo8fKIhRI0NSf7dKA6P70VT3Q-KpyxZ12-fwr0w9qXw'
TOKEN = 'AQXasjc_75qLiEd1hk0zqpxkSLDmRYgYhor-YdI93_yDMiMwuH7HHKafGUfVZnuw97wqfTeHvgxijfHkR-vkEaBT9S4wt8n-Pa-ndbdVlDdP5aiCF-vkDuVdqO5IpC34AW3Eq4aRK8IF8A8rn7Rti3p8wvK4ebWFWc4S3fEYMCAt0HHRZ0kOt0vE0YVfHFdF56yGe_r1DAHNEl_-ihPZkIfCrrktzl0c-dVnPMMd8sV-rBL0sFsSM1ie3QmE1aj5F44dhRVB0dTc8Z-gEc5lA6hLyEJeO2ytuucSyuOWgk9-h4moKVqByJ90TbiELRJhTrVTJ1Q44B7HT6WOwljK-v95isCNkQ'


application = linkedin.LinkedInApplication(token=TOKEN)

'''
profile API
# '''
# print(application.get_profile(selectors = [
# 		'first-name', 'location','site-standard-profile-request'
# 	]))

# get("https://api.linkedin.com/v2/people/(id:{person ID})")


#people_search API - Deny
#print(application.search_profile(selectors=[{'people': ['first-name', 'last-name']}], params={'keywords': 'apple microsoft'}))

'''
company_search API
'''
company_results=[]
for i in list(range(6)):
	search_result = application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'Technology', 'start':20*i, 'count': 20})
	company_results.append(search_result['companies']['values'])

with open("tech_company.json","w") as file:
	file.write(json.dumps(company_results))


# company_results2=application.search_company(selectors=[{'companies': ['name', 'universal-name', 'website-url']}], params={'keywords': 'Technology', 'start':2, 'count': 20})
# company_results.update(company_results2)

# with open("UX_company.json","w") as file:
# 	file.write(json.dumps(company_results))



'''
job_search API - Deny
'''
# print(application.search_job(selectors=[{'jobs': ['id', 'customer-job-code', 'posting-date']}], params={'title': 'python', 'count': 2}))



# application = linkedin.LinkedInApplication(authentication)
# exit()


# client_id = '86w6147zs87hbh'
# client_secret = '49pdzgplUQStD5xt'
# redirect_uri = 'http://localhost:8000'

# oauth = OAuth2Session(client_id, redirect_uri=redirect_uri,
#                           scope=scope)


# request_token_url = 'https://www.linkedin.com/oauth/v2/authorization'

# oauth = OAuth2Session(API_KEY, API_SECRET,redirect_uri=RETURN_URL)
# fetch_response = oauth.fetch_token(request_token_url)
# resource_owner_key = fetch_response.get('oauth_token')
# resource_owner_secret = fetch_response.get('oauth_token_secret')
# exit()



