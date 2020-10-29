from termcolor import colored


board = [0]*9

# TODO : add colors and indexes instead of "."

class Error(Exception):
	"""base"""
	pass
class Taken (Error):
	"""already taken val"""
# end of exceptions
def checkin () :
	while True :
		try :
			a=input()			
			val = int(a)
			if ( board [val] != 0 ) : raise Taken
			return val
		except ValueError :
			if (a=="q" ) : exit()
			print ("Error : only ints are allowed")	
			print ("retry")	
			#exit();
		except Taken:
			print ("Error : already taken")
			print ("retry")
		except IndexError:
			print ("Error : out of range ")
			print ("retry")
		
		
		#return val
	

def printboard (empty):
	print ()	
	for i in range (3) :
		print( "#" *13)
		for j in range (3*i , 3*i+3 , 1 ):
			print ( "# " ,  end = '')
			if board [j] == 0 : 
				if empty :
					a= str(j)
				else : a = "."
				print (colored(a +" ", 'yellow')  ,  end = '')
			if board [j] == 1 : 
				a= "O"
				print (colored(a +" ", 'red')  ,  end = '')
			if board [j] == 10 : 
				a= "X"
				print (colored(a +" ", 'blue')  ,  end = '')
			#else : a = "X"
			#print ( "# " + a +" " ,  end = '')
		print ( "#" ) 
	print( "#" *13)


# end pboard

def gameover ():
	draw = True
	for k in range(9) :
		if board [k] == 0 : 
			draw = False
			break
	if (draw ) : 
		print ("~~~ Draw ~~~")
		exit()
	sum_diag1 = board [0] + board [ 4] + board [8] 
	sum_diag2 = board [4 ] + board [2] + board [ 6]
	for i in range(3):
		sum = board [i] + board [i+3] + board [i+6]
		ai = 3*i
		sumv = board [ai] + board [ai+1] + board [ai+2]
		if ( (sum == 3) or (sumv == 3) or (sum_diag1 == 3) or (sum_diag2 == 3 ) )  : 
			print () 			
			print ( colored("~~~ O wins ~~~", 'red'))
			exit()
		if ((sum == 30) or (sumv == 30 )or (sum_diag1 == 30) or (sum_diag2 == 30 ) )  : 
			print () 
			print (colored("~~~ X wins ~~~" , 'blue'))
			print () 
			exit()
		# print ("sum = " + str(sum) + " sumv= " + str(sumv))
# end of gameover

if __name__ == "__main__":
	t = True
	print( "//  welcome to tic tac toe :: to play choose a value between 0 and 8 ,  press q to quit \\\ " )
	printboard (True)
	while (t):
		
		print ()
		print ("== O turn ==")
		#x1= int(input()) removed for better input
		x1 = checkin ()
		print ( "=" * len ("== X turn =="))
		board [x1] = 1
		printboard (False)
		gameover()

		print ()
		print ("== X turn ==")
		#x2= int(input())
		x2= checkin()
		print ( "=" * len ("== X turn =="))
		board [x2] = 10
		printboard (False)
		gameover()
		# if (x1 == 10 or x2 == 10 ) : t=False 
# implement check input

