# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
import urllib2

def application(environ, start_response):
	status = '200 OK' 

	request = Request(environ)
	url=str(request.path)+"?"+str(request.query_string)
	url=url[1:]	

	res = urllib2.urlopen("http://"+url)
	html = res.read()
	
	response_headers = [('Content-type', 'text/html')]
	start_response(status, response_headers)

	return [html]
