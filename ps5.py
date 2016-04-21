#Author: Ryan Kophs
#Collaborators: Abi Hertz, Vidit Jain

import math

print "\n====Problem 1===="
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

print "TOY(0x4, 0xA): " + hex(TOY(0x4, 0xA))

print "\n====Problem 2===="
# For message = 0x8 and ciphertext = 0x9: key = 0x6
def brute_force_TOY(message, ciphertext):
	for k in xrange(0, 16):
		if message == TOYinv(ciphertext, k):
			return k

print "brute_force_TOY(0x8, 0x9) = " + hex(brute_force_TOY(0x8, 0x9))

print "\n====Problem 3===="
# For message = 0x5 and key = 0x14: ciphertext = 0x0
def TwoTOY(message, key):
	k0 = (key >> 4) & 0xF
	k1 = key & 0xF
	return TOY(TOY(message, k0), k1)
print "TwoTOY(0x5, 0x14) = " + hex(TwoTOY(0x5, 0x14))

print "\n====Problem 4===="
# For message = 0xA and ciphertext = 0xB: k = 0x30
def mitm_TwoTOY(message, ciphertext):
	state = {}
	for k0 in range(0, 16):
		v = TOY(message, k0)
		state[v] = k0

	for k1 in range(0, 16):
		v = TOYinv(ciphertext, k1)
		if v in state.keys():
			return ((state[v] << 4) | k1)
	return None

print "mitm_TwoTOY(0xA, 0xB) = " + hex(mitm_TwoTOY(0xA, 0xB))

print "\n====Problem 5, 6 - See sage.py file===="

print "\n====Problem 7===="
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

print "\n====Problem 8===="
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

print "\n====Problem 9===="
def find_input_pair_candidates(a):
	pairs = []
	for i in xrange(0, 16):
		for j in xrange(0, 16):
			if (i ^ j) == a:
				pairs.append([i,j])
	return pairs

def path_and_approx_prob(sbox):
	matrix = diff_matrix(sbox)

	#Find the maximal probability and location
	p_max = 0
	a = 0
	b = 0
	for i in xrange(1,16):
		for j in xrange(1, 16):
			if matrix[i][j] > p_max:
				p_max = matrix[i][j]
				a = i
				b = j

	#Find next probability:
	n_max = 0
	c = 0
	for i in xrange(1, 16):
		if matrix[b][i] > n_max:
			n_max = matrix[b][i]
			c = i

	max_prob = (n_max*p_max)/float(16*16)
	#Generate all pairs satisfying p_max
	return {'p':max_prob, 'a':a, 'b':b, 'c':c, 'r1p': (p_max/float(16)), 'r2p': (n_max/float(16))}

def exact_probability(inDiff, outDiff):
	pairs = find_input_pair_candidates(inDiff)
	matches = 0
	for pair in pairs:
		for k in xrange(0, 256):
			b0 = TwoTOY(pair[0], k)
			b1 = TwoTOY(pair[1], k)
			if (b0 ^ b1) == outDiff:
				matches += 1
	return matches / float(len(pairs)*256)

res = path_and_approx_prob(sbox)
p_approx = res['p']
p_exact = exact_probability(res['a'], res['c'])
print "Path: "
print " (X XOR X': " + hex(res['a']) + ") -> (Y XOR Y': " + hex(res['b']) + ") -> (Z XOR Z': " + hex(res['c']) + ")"
print "P_approx = " + str(res['r1p']) + "*" + str(res['r2p']) + " = " + str(p_approx)
print "P_exact = " + str(p_exact)

print "\n====Problem 10===="
def NToy(n, msg, k):
	inMsg = msg
	for i in xrange(0, n):
		kIn = (k >> (4*(n - i - 1))) & 0xF
		inMsg = TOY(inMsg, kIn)
	return inMsg

def exact_n_probability(n, inDiff, outDiff):
	pairs = find_input_pair_candidates(inDiff)
	matches = 0
	for pair in pairs:
		for k in xrange(0, int(math.pow(16, n))):
			b0 = NToy(n, pair[0], k)
			b1 = NToy(n, pair[1], k)
			if (b0 ^ b1) == outDiff:
				matches += 1
	return matches / float(len(pairs)*math.pow(16, n))

print "Extra credit: (takes some time because it bruteforces each possible key)"
print "n = 2, p = " + str(exact_n_probability(2, res['a'], res['c']))
print "n = 3, p = " + str(exact_n_probability(3, res['a'], res['c']))
print "n = 4, p = " + str(exact_n_probability(4, res['a'], res['c']))



