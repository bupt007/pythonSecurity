#!/usr/bin/python
# coding:utf-8
# filename: webBrowser.py  author: pengfei

'''
	Building this file to learn owasp10 related knowledge.
'''
import mechanize
import logging

class WebBrowser(mechanize.Browser):
	'''
		This browser inherit from mechanize's Browser, and we extend it to support some
		user-defined parameters. Such as user agent and so on as parameters below:
		@parameter1 UserAgent(str): user can input user-defined agent, and default value is 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0'
		@parameter2 Gzip(bool): default support gzip function
		@parameter3 HttpEQUIV(bool): default to support http-equiv function
		@parameter4 Robots(bool): default not to follow robots.txt protocol
		@parameter5 Redirect(bool): default to allow Redirect
		@parameter6 Referer(bool): default to allow Referer
		@parameter7 Cookie(bool): default to support cookie
	'''
	def __init__(self,UserAgent=None,Gzip=True,HttpEQUIV=True,Robots=False,Redirect=True,Referer=True,Cookie=True):
		mechanize.Browser.__init__(self)
		self.set_handle_gzip(Gzip)
		self.set_handle_equiv(HttpEQUIV)
		self.set_handle_robots(Robots)
		self.set_handle_redirect(Redirect)
		self.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
		self.set_handle_referer(Referer)
		self.userAgent = UserAgent
		self.defaultAgent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:23.0) Gecko/20131011 Firefox/23.0'
		self.setAgent()
		self.cookie = Cookie
		self.setCookie()
		print "[+] Everything is OK"

	def setAgent(self):
		if self.userAgent :
			self.addheaders = [('User-Agent',self.userAgent)]
		else:
			self.addheaders = [('User-Agent',self.defaultAgent)]

	def setCookie(self):
		if self.cookie:
			cj = mechanize.CookieJar()
			self.set_cookiejar(cj)


class FormInjectionBrowser(WebBrowser):
	"""
	   The class inherit from WebBrowser above and focus on inject cases into forms
	"""
	def __init__(self,url,injectData=[],expectData=[]):
		"""
			@parameter1 injectData(list): input the injected data by user
			@parameter2 expectData(list): if expectData occurs, means injection is successful
			@parameter3 url(str): the url which user wants to inject to 
		"""
		WebBrowser.__init__(self)
		self.injectCase = injectData
		self.expectResult = expectData
		self.url = str(url)
		print "[+] form injecton browser is OK"

	def Inject(self):
		self.open(self.url)
		forms = self.forms()
		f_nr = 0
		injectable = False
		for form in forms:
			self.select_form(nr=f_nr)
			for inj in self.injectCase:
				for c in form.controls:
					if c.type == "text" or c.type == "password":
						self.form[c.name] = inj
				resp = self.submit()
				for e in self.expectResult:
					if e in resp.read():
						print "Injection %s is useful" % inj
						injectable = True
						break
				self.back()
			f_nr +=1
		if not injectable:
			print "There is no vulnerablity in page: %s" % (self.url)

if __name__=="__main__":
	ib = FormInjectionBrowser("http://www.baidu.com")
	ib.Inject()








