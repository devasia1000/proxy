def application(environ, start_response):
	status = '200 OK' 

	log=""     
	for key in environ:
		log=log+key+": "+str(environ[key])+"\n"			

	response_headers = [('Content-type', 'text/plain')]
	start_response(status, response_headers)

	return [log]
