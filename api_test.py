import requests
import random, string
from assertpy import assert_that
from cnfg import *


user_id = "" # Global variable to carry the user_id into the scope of the test functions


# GET method to get user list
def test_list_users():
	r = requests.get(BASE_URL + 'users/')
	assert_that(r.status_code).is_equal_to(200)
	assert_that(r.json()['data']).is_not_empty()



# POST method to create a new user
def test_create_user():
	headers = {"Content-Type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
	body = '{"name":"Apipy %s", "gender":"male","email":"apipy@qa.com", "status":"active"}' % get_random_string()
	r = requests.post(BASE_URL + 'users/', headers = headers, data = body)
	assert_that(r.status_code).is_equal_to(201)
	global user_id
	user_id = r.json()['data']['id']



# PUT method to update an existing user
def test_update_user():
	headers = {"Content-Type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
	body = '{"name":"Apipy %s", "gender":"male","email":"apipy@qa.com", "status":"active"}' % get_random_string()
	r = requests.put(BASE_URL + 'users/' + str(user_id), headers = headers, data = body)
	assert_that(r.status_code).is_equal_to(200)



# DELETE method to delete an existing user
def test_delete_user():
	headers = {"Content-Type": "application/json", "Authorization": "Bearer " + API_ACCESS_TOKEN}
	r = requests.delete(BASE_URL + 'users/' + str(user_id), headers = headers)
	assert_that(r.status_code).is_equal_to(204)



# Function to create unique last names for each test cycle
def get_random_string():
    rndm_str = ''.join((random.choice(string.ascii_letters) for i in range(6)))
    return rndm_str



