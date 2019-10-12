#!/usr/bin/python3
# -*- conding:utf-8 -*-

#in registermode, if 2 password arent the same, return 2
#				if the username have been taken, return 3
#in loginmode, if the password are not correct, return 2
#              if the username doesnot exist, return 3
#用于本地验证用户注册和登录，需要等套接字完成后修改使用
#
#
import pygame
from popupwindow import popupwindow
import json
def confirm(username, password, check, registermode):
	if registermode:
		if password == '< 17 characters' or check == 'check password'\
		or username == '< 17 characters':
			popupwindow("You should enter your Username, Password")
			return True
		if check != password:
			popupwindow("Passwrods aren't consistent")
			return True
		with open("username&password.json") as file:
			dictionary_of_user = json.load(file)
			print(dictionary_of_user)
		for k in dictionary_of_user.keys():
			if username == k:
				popupwindow("The name have been taken")
				return True
		dictionary_of_user[username] = password
		with open("username&password.json",'w') as file:
			json.dump(dictionary_of_user,file)
		return False
	else:
		with open("username&password.json") as file:
			dictionary_of_user = json.load(file)
		for k,v in dictionary_of_user.items():
			if username == k and password != v:
				popupwindow("Passwrods incorrect")
				return True
			if username == k and password == v:
				return False 
				#the upper file will stop loop and enter the next window
		popupwindow("Username doesn't exist")
		return True


