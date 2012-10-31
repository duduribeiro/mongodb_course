import pymongo
import sys

def main():

	connection = pymongo.Connection("mongodb://localhost", safe=true)
	db = connection.m101

	people = db.people

	person = { 'name': 'Barack Obama', 'role': 'President', 'address': { 'adress': 'The White House', 
		'street': '1600 Pennsylvania Avenue', 'state': 'DC', 'city': 'Washington' }, 'interests': ['government', 'basketball', 'the middle east'] }

	people.insert(person)