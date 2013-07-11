# Authors: Keith Winstein and Devasia Manuel

# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
import urllib2
import re

def application(environ, start_response):
	status='200 OK' 

	request=Request(environ)
	url=str(request.path)+"?"+str(request.query_string)
	url=url[1:]

	req=urllib2.Request("http://"+url, None, request.headers)
	resp=urllib2.urlopen(req)
	html=resp.read()	
	
	response_headers = list(dict(resp.info()).items())
	#response_headers = [('Content-Type', 'text/html')]
	start_response(status, response_headers)

	return [html]
