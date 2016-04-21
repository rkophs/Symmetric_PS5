# -*- coding: utf-8 -*-
# @Author: ryan
# @Date:   2016-04-20 23:05:05
# @Last Modified by:   Ryan Kophs
# @Last Modified time: 2016-04-20 23:26:52

print "====Problem 7===="
sbox = [0x6, 0x4, 0xC, 0x5, 0x0, 0x7, 0x2, 0xE, 0x1, 0xF, 0x3, 0xD, 0x8, 0xA, 0x9, 0xB]
def diff_matrix(sbox):
	matrix = []
	for i in xrange(0, 16):
		matrix.append([])
		for j in xrange(0, 16):
			matrix[i].append(0)
			
	for i in xrange(0, 16):
		for j in xrange(0, 16):
			x = i
			y = sbox[x]
			x_ = j
			y_ = sbox[x_]
			a = x ^ x_
			b = y ^ y_
			matrix[a][b] = matrix[a][b] + 1
	return matrix

matrix = diff_matrix(sbox)
i = 0
while i < len(matrix):
	print(matrix[i])
	i = i + 1

print "====Problem 8===="
def lin_matrix(sbox):
	matrix = []
	for i in xrange(0, 16):
		matrix.append([])
		for j in xrange(0, 16):
			matrix[i].append(-8)
			
	for a in xrange(0, 16):
		for b in xrange(0, 16):
			for x in xrange(0, 16):
				y = sbox[x]

				ax = None
				by = None
				for i in xrange(0, 4):
					xi = (x >> 3 - i) & 0x1
					yi = (y >> 3 - i) & 0x1
					ai = (a >> 3 - i) & 0x1
					bi = (b >> 3 - i) & 0x1
					if ax == None:
						ax = ai * xi
					else:
						ax = ax ^ (ai * xi)

					if by == None:
						by = bi * yi
					else:
						by = by ^ (bi * yi)
				if ax == by:
					matrix[a][b] = matrix[a][b] + 1
	return matrix

matrix = lin_matrix(sbox)
i = 0
while i < len(matrix):
	print(matrix[i])
	i = i + 1