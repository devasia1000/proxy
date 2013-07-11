# Authors: Keith Winstein and Devasia Manuel

# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
import urllib2
import re
import zlib

def application(environ, start_response):

		
	status="200 OK"
	
	request=Request(environ)

	if request.query_string is "":
		url=str(request.path)
	else:
		url=str(request.path)+"?"+str(request.query_string)
	
	url=url[1:]
	
	req=urllib2.Request("http://"+url, None, request.headers)
	resp=urllib2.urlopen(req)
	html=resp.read()
		
	d=dict(resp.headers)
	if "transfer-encoding" in d:
		del d["transfer-encoding"]

	head=list(d.items())

	response_headers = [('Content-Type', 'text/plain')]
	start_response(status, head)
	return [str(html)]
