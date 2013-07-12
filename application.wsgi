# Authors: Keith Winstein and Devasia Manuel
#
# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
from urllib2 import URLError
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
	
	try:
		#Passing request headers doesn't seem to work, get URL without passing request headers for now
		#req=urllib2.Request("http://"+url, None, dict(request.headers))
		resp=urllib2.urlopen(req)
		html=resp.read()
		
		d=dict(resp.headers)
		if "transfer-encoding" in d:
			del d["transfer-encoding"]
		
		head=list(d.items())
		start_response(status, head)
		return [str(html)]
	
	except:
		error="ERROR\n\nCannot load URL: http://"+url
		
		response_headers = [('Content-Type', 'text/plain')]
		start_response(status, response_headers)
		return [error+"\n\n"+"Request Header:\n\n"+str(request.headers)]
		