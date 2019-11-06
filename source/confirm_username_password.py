#!/usr/bin/python3
# -*- conding:utf-8 -*-

#in registermode, if 2 password aren't the same, return 2
#				if the username have been taken, return 3
#				if haven't enter username, return 4
#in loginmode, if the password are not correct, return 5
#              if the username doesnot exist, return 6
#if the result is correct, return 1
#用于本地验证用户注册和登录
#
#
import pygame
import json
def confirm(username, password, check, registermode):
	if registermode == 1:
		#if not enter enough information
		if password == '< 17 characters' or check == 'check password'\
		or username == '< 17 characters' or len(password) == 0\
		or len(check) == 0 or len(username) == 0:
			# popupwindow("You should enter your Username, Password")
			return 4
		#if two passwords arent consistent
		if check != password:
			# popupwindow("Passwrods aren't consistent")
			return 2
		#open file to further check the information
		with open("username&password.json") as file:
			dictionary_of_user = json.load(file)
			print(dictionary_of_user)
		for k in dictionary_of_user.keys():
			#when the username have been taken
			if username == k:
				# popupwindow("The name have been taken")
				return 3
		#save the new inforation about the user
		dictionary_of_user[username] = password
		with open("username&password.json",'w') as file:
			json.dump(dictionary_of_user,file)
		return 1
	else:
		with open("username&password.json") as file:
			dictionary_of_user = json.load(file)
		#if username or password is wrong
		for k,v in dictionary_of_user.items():
			if username == k and password != v:
				# popupwindow("Passwrods incorrect")
				return 5
			#when matched, approach
			if username == k and password == v:
				return 1 
				#the upper file will stop loop and enter the next window
		# popupwindow("Username doesn't exist")
		return 6


