#Author: Ryan Kophs
#Collaborators: Abi Hertz, Vidit Jain

S = mq.SBox(0x6, 0x4, 0xC, 0x5, 0x0, 0x7, 0x2, 0xE, 0x1, 0xF, 0x3, 0xD, 0x8, 0xA, 0x9, 0xB)

#====Problem 5====:
print "====Problem 5===="
#Linear Approx Matrix Output:
#[ 8  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
#[ 0  2  2  0  4 -2  2  0  2  0 -4 -2  2  0  0  2]
#[ 0  2  0  2  0  2  4 -2  2  0  2  0 -2 -4  2  0]
#[ 0  0  2 -2  0  0  2  6  0  0  2 -2  0  0  2 -2]
#[ 0 -2  2  0 -4 -2 -2  0  2  0  0 -2  2 -4  0  2]
#[ 0  0 -4  0  0 -4  0  0  0 -4  0  0  0  0  4  0]
#[ 0  0 -2 -2  0 -4  2 -2  0  4  2 -2  0  0 -2 -2]
#[ 0 -2  0 -6  0  2  0 -2  2  0 -2  0 -2  0  2  0]
#[ 0  4  0  0 -4  0  0  0  4  0  0  0  0  4  0  0]
#[ 0  2 -2  0  0  2 -2  0 -2  4  0 -2  2  0  4  2]
#[ 0 -2  0  2  0 -2  0  2  2  4 -2  4 -2  0  2  0]
#[ 0  0 -2 -2  0  0  2  2  0  0  2  2  0  0 -2  6]
#[ 0  2  2  0  0 -2 -2  0 -2  0  0 -2 -6  0  0  2]
#[ 0  0  0  0 -4  0  4  0 -4  0 -4  0  0  0  0  0]
#[ 0  4 -2 -2  0  0 -2  2  0  0 -2  2  0 -4 -2 -2]
#[ 0 -2 -4  2  0  2  0  2  2  0 -2 -4 -2  0 -2  0]
print "linear approximation matrix"
print S.linear_approximation_matrix()

#Difference Approx Matrix Output:
#[16  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0]
#[ 0  0  6  0  0  0  0  2  0  2  0  0  2  0  4  0]
#[ 0  6  6  0  0  0  0  0  0  2  2  0  0  0  0  0]
#[ 0  0  0  6  0  2  0  0  2  0  0  0  4  0  2  0]
#[ 0  0  0  2  0  2  4  0  0  2  2  2  0  0  2  0]
#[ 0  2  2  0  4  0  0  4  2  0  0  2  0  0  0  0]
#[ 0  0  2  0  4  0  0  2  2  0  2  2  2  0  0  0]
#[ 0  0  0  0  0  4  4  0  2  2  2  2  0  0  0  0]
#[ 0  0  0  0  0  2  0  2  4  0  0  4  0  2  0  2]
#[ 0  2  0  0  0  2  2  2  0  4  2  0  0  0  0  2]
#[ 0  0  0  0  2  2  0  0  0  4  4  0  2  2  0  0]
#[ 0  0  0  2  2  0  2  2  2  0  0  4  0  0  2  0]
#[ 0  4  0  2  0  2  0  0  2  0  0  0  0  0  6  0]
#[ 0  0  0  0  0  0  2  2  0  0  0  0  6  2  0  4]
#[ 0  2  0  4  2  0  0  0  0  0  2  0  0  0  0  6]
#[ 0  0  0  0  2  0  2  0  0  0  0  0  0 10  0  2]
print "difference distribution matrix:"
print S.difference_distribution_matrix()

#====Problem 6====:
print "====Problem 6===="
print "maximal linear bias absolute:"
print S.maximal_linear_bias_absolute()
print "maximal difference probability absolute:"
print S.maximal_difference_probability_absolute()