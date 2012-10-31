import bottle
import pymongo

#handle the root url
@bottle.route("/")
def index():
	from pymongo import Connection
	connection = Connection('localhost', 27017)

	db = connection.test

	names = db.names

	item = names.find_one()

	return '<b>Hello %s!</b>' % item['name']

bottle.run(host='localhost', port=8080)