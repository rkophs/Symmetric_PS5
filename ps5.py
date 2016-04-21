# -*- coding: utf-8 -*-
# @Author: ryan
# @Date:   2016-04-20 20:38:11
# @Last Modified by:   Ryan Kophs
# @Last Modified time: 2016-04-20 21:01:15

#Problem 1

def S(x):
	s = [0x6, 0x4, 0xC, 0x5, 0x0, 0x7, 0x2, 0xE, 0x1, 0xF, 0x3, 0xD, 0x8, 0xA, 0x9, 0xB]
	return s[x]

def Sinv(x):
	s = [0x4, 0x8, 0x6, 0xA, 0x1, 0x3, 0x0, 0x5, 0xC, 0xE, 0xD, 0xF, 0x2, 0xB, 0x7, 0x9]
	return s[x]

# For message = 0x4 and key = 0xA: ciphertext = 0x9
def TOY(message, key):
	return S(message ^ key)

# For ciphertext = 0xF and key = 0x6: message = 0xF
def TOYinv(ciphertext, key):
	return Sinv(ciphertext) ^ key

# For message = 0x8 and ciphertext = 0x9: key = 0x6
def brute_force_TOY(message, ciphertext):
	for k in xrange(0, 16):
		if message == TOYinv(ciphertext, k):
			return k

def testToyAndToyInv():
	for i in xrange(0, 16):
		for k in xrange(0, 16):
			print (int(i) == int(TOYinv(TOY(i, k), k)))