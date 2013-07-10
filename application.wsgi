# Authors: Keith Winstein and Devasia Manuel
# Description: this script acts like a proxy server; it intercept GET requests and prints them to the screen
# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
import urllib2

def application(environ, start_response):
	status = '200 OK' 

	request = Request(environ)
	url=str(request.path)+"?"+str(request.query_string)
	url=url[1:]

	head=str(request.headers)

	res = urllib2.urlopen("http://"+url)
	html = res.read()
	
	response_headers = [('Content-type', 'text/html')]
	start_response(status, response_headers)

	return [head]
