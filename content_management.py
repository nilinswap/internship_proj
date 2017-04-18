def navtabcontent_unlocked():#for logged in users
	tempdoc={"basics":[["basic c","/basic_c"],["python from beginning","/python_basics"]],"webd":[["flask","/flask"],["django","/django"]]}
	return tempdoc;
def navtabcontent_locked():#for logged out users; the values are nothing so I use ninja inside dashboard to show a message 								redirecting to login page
	tempdoc={"basics":[],"webd":[]}
	return tempdoc;
