# Authors: Keith Winstein and Devasia Manuel
#
# For full documentation, please see: http://werkzeug.pocoo.org/docs/wrappers/

from werkzeug import Request
from urllib2 import URLError
from werkzeug import EnvironHeaders
import urllib2
import re
import zlib

def application(environ, start_response):
			
	status="200 OK"
	
	host_dict={"youtube.com" : "173.194.43.33"}
	log("Contents of Host-to-IP dictionary:\n\n"+str(host_dict)+"\n\n")
	
	request=Request(environ)

	#if request.query_string is "":
	#	url=str(request.path)
	#else:
	#	url=str(request.path)+"?"+str(request.query_string)
	
	#url=url[1:]
	
	request_dict=dict(request.headers)
	hostname=request_dict["Host"]
	ip=host_dict[hostname]
	log("Converted '"+hostname+"' to '"+ip+"'\n\n")
	
	#response_headers = [('Content-Type', 'text/plain')]
	#start_response(status, response_headers)
	#return [str(ip)]
	
	try:
		
		#Passing request headers doesn't seem to work, get URL without passing request headers for now
		#req=urllib2.Request("http://"+url, None, dict(request.headers))
		req=urllib2.Request("http://"+ip)#, None, request_dict)	
		resp=urllib2.urlopen(req)
		html=resp.read()
		log("Downloaded HTML:\n\n"+str(html)+"\n\n")
		
		d=dict(resp.headers)
		if "transfer-encoding" in d:
			del d["transfer-encoding"]
			log("Removed 'transfer-encoding' in Response header")
		
		head=list(d.items())
		start_response(status, head)
		return [str(html)]
	
	except URLError:
		error="ERROR\n\nCannot load URL: http://"+ip
		log(error+"\n\n"+"Request Header:\n\n"+str(request.headers))
		
		response_headers = [('Content-Type', 'text/plain')]
		start_response(status, response_headers)
		return [error+"\n\n"+"Request Header:\n\n"+str(request.headers)]
	
def log(message):
	with open("/home/devasia/Desktop/cgi-bin/log.txt", "a") as myfile:
		myfile.write(message)
	
	
		