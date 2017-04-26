from flask import Flask,render_template,flash,redirect,url_for,request,session
from pymysql import escape_string as thwart
from wtforms import * 
from passlib.hash import sha256_crypt
from dbconnect import connection
import content_management 
from content_management import *
import gc

from functools import wraps

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("homepage.html")
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash("you need to login first")
			return redirect(url_for('login_page'))
	return wrap
@login_required
@app.route("/logout/")
def logout():
	session.clear()
	#flash("You have been logged out!")
	fileo=open("templates/new_dashboard_stu.html","w")
	inputst="""{% extends "new_dashboardheader.html" %}
	{% block body %}
	{% endblock %}"""
	fileo.write(inputst)
	fileo.close()
	fileo=open("templates/new_dashboard_co.html","w")
	inputst="""{% extends "new_dashboardheader.html" %}
	{% block body %}
	{% endblock %}"""
	fileo.write(inputst)
	fileo.close()					
				
				
	gc.collect()
	return redirect(url_for('home'))


@app.route('/test/')
def prin():
	return redirect(url_for('prinxt',s="not swapnil "))
	
	
@app.route('/test/<s>')
def prinxt(s):
	flash(s)
	return render_template("test.html",s=s)
	#return redirect(url_for(prin),s='swapnil')


@app.route('/dashboard/')
def dash():
	try:
		
		return render_template("dashboard.html",tempdoc=navtabcontent())
	except Exception as e:							
		return str(e)


	
@app.route('/justtest/')
def testi():
	#return render_template("new_dashboard_stu.html",st='swapnil')
	return render_template("new_dashboard.html")
@app.route('/login/',methods=["GET","POST"])
def login_page():	
	error=None
	try:
		
		return render_template("login_jais.html",error=error)
	except Exception as e:
		if e: flash(e)
		return render_template("login_jais.html",error=error)
@app.route('/login_stu/',methods=["GET","POST"])
def login_page_stu():	
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
			notempty=c.execute("SELECT * FROM users where name=%s and password =%s",(username,password))
	
			if notempty :	
				flash("welcome")	
				session['logged_in']=True
				session['username']=username			
				#return redirect(url_for('dashs',sess=True))#it redirects to the url of dash
				"""fileo=open("stu_files/%s.txt"%(username),'r')
				lis=fileo.readlines()
				arglis=lis[0].rstrip().split(' ')
				fileo.close()"""
				datanum=c.execute("SELECT * FROM company as c INNER JOIN users as u on c.field=u.preference WHERE u.name=%s",(username))	
				print(datanum)
				datalis=c.fetchall()
				n=len(datalis)
				if datanum==1:
					n=1
				"""fileo=open("templates/new_dashboard_stu.html",'a+')
				fileo.seek(
				fileo.read"""
				inputst=''
				print(datalis)
				for i in range(n):
					dataitemtup=datalis[i]
					filename="co_files/"+dataitemtup[1]+".txt"
		
					fileo=open(filename,'r')
					arglis=fileo.readlines()
					pq=len(arglis)
					lis1=arglis[0].rstrip().split(" ")
					print(lis1)
					field=lis1[3]
					co_name=lis1[0]
					link=lis1[1]
					if pq>1:
						for i in range(2,pq):
							arglis[1]+=arglis[i]
					else:	
						arglis.append(arglis[0])
					st="""
						<div class="row">
					  		<div class="col-md-12 panel-warning">
					  			<div class="content-box-header panel-heading">
				  					<div class="panel-title ">%s</div>
						
									<div class="panel-options">
										<a href="#" data-rel="collapse"><i class="glyphicon glyphicon-refresh"></i></a>
										<a href="#" data-rel="reload"><i class="glyphicon glyphicon-cog"></i></a>
									</div>
					  			</div>
					  			<div class="content-box-large box-with-header">
						  			<a href="%s" >%s </a>
						  			<br>
						  			%s
									<br /><br />
								</div>
					  		</div>
					  	</div>
					  	"""%(field,link,co_name,arglis[1])
					inputst+=st
				fileo=open("templates/new_dashboard_stu.html","w")
				inputst="""{% extends "new_dashboardheader.html" %}
	{% block body %}"""+inputst+"""\n{% endblock %}"""
				fileo.write(inputst)
				fileo.close()					
				return render_template("new_dashboard_stu.html")
				
				
			
				return redirect(url_for('dash'))
			else:
				error="invalid credentials"
			c.close()
			conn.close()
		#flash("first") in the first loop as there is no method given it reaches upto below stated return and call same html
		return render_template("login_jais.html",error=error)
	except Exception as e:
		if e: flash(e)
		return render_template("login_jais.html",error=error)


	
@app.route('/login_co/',methods=["GET","POST"])
def login_page_co():	
	error=None
	try:
		if request.method=="POST":#the action part of form gives this feed
			email=request.form['email']
			password=request.form['password']#this username gets value from "{{request.form.username}}"(i.e. value) part of input tag in login.html
			#password=sha256_crypt.encrypt(password)
			#print(password)
			#flash(username)
			#flash(password)
			c,conn=connection()
			notempty=c.execute("SELECT * FROM company where email=%s and password =%s",(email,password))
			co_name=c.fetchone()[1]
			if notempty :	
				flash("welcome")	
				session['logged_in']=True
				session['co_name']=co_name			
				#return redirect(url_for('dashs',sess=True))#it redirects to the url of dash
				datanum=c.execute("SELECT * FROM users as u INNER JOIN company as c on c.field=u.preference WHERE c.co_name=%s",(co_name))	
				print(datanum)
				datalis=c.fetchall()
				n=len(datalis)
				if datanum==1:
					n=1
				"""fileo=open("templates/new_dashboard_stu.html",'a+')
				fileo.seek(
				fileo.read"""
				inputst=''
				
				print(datalis)
				for i in range(n):
					dataitemtup=datalis[i]
					filename="stu_files/"+dataitemtup[1]+".txt"
		
					fileo=open(filename,'r')
					arglis=fileo.readlines()
					lis1=arglis[0].rstrip().split(" ")
					print(lis1)
					username=lis1[0]
					pq=len(arglis)
					if pq>1:
						for i in range(2,pq):
							arglis[1]+=arglis[i]
					else:	
						arglis.append(arglis[0])
		
					st="""
						<div class="row">
					  		<div class="col-md-12 panel-warning">
					  			<div class="content-box-header panel-heading">
				  					<div class="panel-title ">%s</div>
						
									<div class="panel-options">
										<a href="#" data-rel="collapse"><i class="glyphicon glyphicon-refresh"></i></a>
										<a href="#" data-rel="reload"><i class="glyphicon glyphicon-cog"></i></a>
									</div>
					  			</div>
					  			<div class="content-box-large box-with-header">
						  			
						  			<br>
						  			%s
									<br /><br />
								</div>
					  		</div>
					  	</div>
					  	"""%(username,arglis[1])
					inputst+=st
				fileo=open("templates/new_dashboard_co.html","w")
				inputst="""{% extends "new_dashboardheader.html" %}
	{% block body %}"""+inputst+"""\n{% endblock %}"""
				fileo.write(inputst)
				fileo.close()					
				return render_template("new_dashboard_co.html")
				
				
			
				
			else:
				error="invalid credentials"
			c.close()
			conn.close()
		#flash("first") in the first loop as there is no method given it reaches upto below stated return and call same html
		return render_template("login_jais.html",error=error)
	except Exception as e:
		if e: flash(e)
		return render_template("login_jais.html",error=error)


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
			
			return redirect(url_for('dash'))
				
		return render_template("register.html",form=form)#on first time, above 'if' is ignored and directly this is run 	
			
	except Exception as e:
		return str(e)

@app.route('/register/',methods=["POST","GET"])
def register_page2():
	
	try:	
		return render_template("signup.html")
	except Exception as e:
		return str(e)
@app.route('/register_stu/',methods=["POST","GET"])
def register_page_stu():
	
	try:
		if request.method=="POST":
			c,conn=connection()
			username=request.form['Username']
			preference=request.form['preference']
			dob=request.form['DOB']
			password=request.form['password']
			repassword=request.form['repassword']
			email=request.form['email']
			aboutmyself=request.form['aboutmyself']
			if password!=repassword:
				error="two passwords must match!!"
				return render_template("signup.html",error=error)
			n=c.execute("select * from users where name=%s",username)
			if n:
				error="sorry, this name has already been taken"
				return render_template("signup.html",error=error)
			c.execute("insert into users (name,preference,dob,email,password) values (%s,%s,%s,%s,%s)",(username,preference,dob,email,password))
			fileo=open("stu_files/%s.txt"%(username),"w")
			fileo.write("%s %s %s %s %s\n%s"%(username,preference,dob,email,password,aboutmyself))
			fileo.close()
			c.execute("insert into stu_filetable (username,nameoffile) values (%s,%s)",(username,"stu_files/"+username+".txt"));
			flash("success!! welcome to shiteclub")
			flash(username)
			conn.commit()
			c.close()
			conn.close()
			gc.collect()
			flash("please login first")
			return redirect(url_for('home'))
			
		return render_template("signup.html")
	except Exception as e:
		return str(e)

@app.route('/register_co/',methods=["POST","GET"])
def register_page_co():
	
	try:
		if request.method=="POST":
			c,conn=connection()
			co_name=request.form['co_name']
			link=request.form['link']
			num=int(request.form['num'])
			field=request.form['field']
			email=request.form['email']
			password=request.form['password']
			repassword=request.form['repassword']
			aboutus=request.form['aboutus']
			print(aboutus)
			
			if password!=repassword:
				error="two passwords must match!!"
				return render_template("signup.html",error=error)
			n=c.execute("select * from company where co_name=%s",co_name)
			if n:
				error="sorry, no two company can have same name"
				return render_template("signup.html",error=error)
			c.execute("insert into company (co_name,link,num,field,email,password) values (%s,%s,%s,%s,%s,%s)",(co_name,link,num,field,email,password))
			fileo=open("co_files/%s.txt"%(co_name),"w")
			fileo.write("%s %s %s %s %s %s\n%s"%(str(co_name),str(link),str(num),str(field),str(email),str(password),aboutus))
			fileo.close()
			c.execute("insert into co_filetable (co_name,nameoffile) values (%s,%s)",(co_name,"co_files/"+co_name+".txt"));
			flash("success!! welcome to shiteclub, you are company")
			flash(co_name)
			conn.commit()
			c.close()
			conn.close()
			gc.collect()
			flash("please login first")
			return redirect(url_for('home'))
			
		return render_template("signup.html")
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
    
