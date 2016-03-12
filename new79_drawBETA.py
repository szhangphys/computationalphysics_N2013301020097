try:
	from yFont import *
except:
	A = ['     *     ', '    * *    ', '   *   *   ', '  * * * *  ', ' *       * ', '*         *']
	Q=W=E=R=T=Y=U=I=O=P=S=D=F=G=H=J=K=L=Z=X=C=V=B=N=M=space = ['           ', '           ', '           ', '           ', '           ', '           ']
	print "To run this code, you'll need a font library which is by default named yFont.py provided by Mr. Y. Otherwise, only 'A' and space can be displayed.\n"



dic = {' ': space, 'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T, 'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}


def drawbeta(a_string):
	def draw(x):
		for i in range(len(x[0])):
			for m in x:
				print m[i],
			print
		print
	def str2var(char):
		return dic[char]
	lst = map(str2var, a_string)
	draw(lst)

#drawbeta('YYFHHH')
#drawbeta('HE HE HE HE')
#drawbeta('XYZW')
drawbeta('ABC AD')