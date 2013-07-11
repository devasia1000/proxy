# Authors: Keith Winstein and Devasia Manuel

# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
import urllib2
import ast

def application(environ, start_response):
	status='200 OK' 

	request=Request(environ)
	url=str(request.path)+"?"+str(request.query_string)
	url=url[1:]

	#head=str(request.headers)

	req=urllib2.Request("http://"+url, None, request.headers)
	resp=urllib2.urlopen(req)
	html=resp.read()	
	
	#response_headers = resp.info().items()
	response_headers = [('Content-type', 'text/html')]
	start_response(status, response_headers)

	return [html]
