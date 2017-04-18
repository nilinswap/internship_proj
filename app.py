from flask import Flask,render_template,flash,redirect,url_for,request,session
from pymysql import escape_string as thwart
from wtforms import * 
from passlib.hash import sha256_crypt
from dbconnect import connection
import content_management 
from content_management import *
import gc

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("main2.html")


@app.route('/test/')
def prin():
	return redirect(url_for('prinxt',s="not swapnil "))
	
	
@app.route('/test/<s>')
def prinxt(s):
	flash(s)
	return render_template("test.html",s=s)
	#return redirect(url_for(prin),s='swapnil')


@app.route('/dashboard/')
def dash(sess=False):
	try:
		return render_template("dashboard.html",tempdoc=navtabcontent_locked())
	except Exception as e:							
		return str(e)
@app.route('/dashboard/<sess>')
def dashs(sess=False):
	try:
		if sess:	
			return render_template("dashboard.html",tempdoc=navtabcontent_unlocked())#content management; this navtabcontent function lies in another python file, it returns content by some data structure
		else:
			return render_template("dashboard.html",tempdoc=navtabcontent_locked())
	except Exception as e:							
		return str(e)



@app.route('/login/',methods=["GET","POST"])
def login_page():	
	error=None
	try:
		if request.method=="POST":#the action part of form gives this feed
			username=request.form['username']
			password=request.form['password']#this username gets value from "{{request.form.username}}"(i.e. value) part of input tag in login.html
			#password=sha256_crypt.encrypt(password)
			#print(password)
			#flash(username)
			#flash(password)
			c,conn=connection()
			notempty=c.execute("SELECT * FROM users where username=%s and password =%s",(username,password))
			
			if notempty :	
				flash("welcome")	
				session['logged_in']=True
				session['username']=username			
				return redirect(url_for('dashs',sess=True))#it redirects to the url of dash
			else:
				error="invalid credentials"
			c.close()
			conn.close()
		#flash("first") in the first loop as there is no method given it reaches upto below stated return and call same html
		return render_template("login.html",error=error)
	except Exception as e:
		if e: flash(e)
		return render_template("login.html",error=error)


#below mentioned two snippets along with register.html and _formhelpers.html use flask wholly for registration page
#class for forms; here Form is definded under wtfs
class RegistrationForm(Form):
	username=TextField("Username",[validators.Length(min=4,max=20)])#that valid input must have this range of length
	email=TextField("Email Address",[validators.Length(min=6,max=50)])#TextField is defined under wtf, it returns an input object._formhelper's job's greatly reduced because TextField returns <input> element of html.
	password=PasswordField("Password",[validators.required(),validators.EqualTo('confirm',message="password must match")])#required fields; see EqualTo func compares 'confirm' variable to password and if the dont match gives above message
	confirm=PasswordField('Repeat Password',[validators.required()])
	accept_tos=BooleanField('I accept the <a>Terms of services</a> and the<a> Privacy Notice </a>(Last updated 5 Feb,2017.)')
		#check box


#@app.route('/register/',methods=["GET","POST"])
def register_page():	
	try:
		form=RegistrationForm(request.form)#request.form is a complex dictionary kind of.Initially it is empty then class shapes it to Reg...Form object for first time; for all rest form is not changed
		if request.method=="POST" and form.validate():#intially this's skipped here form.Validate gives pass only for all valid input
			username=form.username.data
			email=form.email.data
			password=form.password.data
			c,conn=connection()
			n=c.execute("select * from users where username=%s",thwart(username))#thwarting(thwart is made-up term for escpe_string) is to avoid sql injection 
			if n:
				flash("the username has already been alloted. Try something else")
				render_template("register.html",form=form)
			username=thwart(username)
			email=thwart(email)
			password=sha256_crypt.encrypt(thwart(password))
			c.execute("insert into users (username,mail_id,password) values (%s,%s,%s)",(username,email,password))#here variable name must be same as that in database
			conn.commit()
			c.close()
			conn.close()
			flash("thanks for registering...now go fuck off!!")
			gc.collect() #garbage collector
			session['logged_in']=True
			session['username']=username
			print("here session is "+str(session))
			return redirect(url_for('dash'))
				
		return render_template("register.html",form=form)#on first time, above 'if' is ignored and directly this is run 	
			
	except Exception as e:
		return str(e)

@app.route('/register/',methods=["POST","GET"])
def register_page2():
	
	try:
		if request.method=="POST":
			c,conn=connection()
			username=request.form['username']
			password=request.form['password']
			repassword=request.form['repassword']
			email=request.form['email']
			if password!=repassword:
				error="two passwords must match!!"
				return render_template("register2.html",error=error)
			n=c.execute("select * from users where username=%s",username)
			if n:
				error="sorry, this name has already been taken"
				return render_template("register2.html",error=error)
			c.execute("insert into users (username,mail_id,password) values (%s,%s,%s)",(username,email,password))
			flash("success!! welcome to shiteclub")
			flash(username)
			conn.commit()
			c.close()
			conn.close()
			gc.collect()
			
			return redirect(url_for('dash'))
			
		return render_template("register2.html")
	except Exception as e:
		return str(e)



@app.route('/user/<name>')
def currentlyfree(name):
	return "hello "+name+", umm.. you are not registered but for now it doesn't matter. So enjoy."#here 'name' is a variable.


@app.errorhandler(404)
def pagenotfound(e):
	#i've no idea why i can't put the flash statement here
	return render_template("error404.html")

@app.errorhandler(405)
def pagenotfound(e):
	#i've no idea why i can't put the flash statement here
	return render_template("error405.html")
		
if __name__ == "__main__":
    app.secret_key = 'many random bytes'
    app.run(debug=True)
    
