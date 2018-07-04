# to start interactive interpreter type
#		python
#	options
#		-d debug output
#		-O generatges optimized bytecode (.pyo)
#		-S do not run import site to look for python paths on startup
#		-v verbose
#		-X disable class-based built in exceptions; obsolete starting with 1.6
#		-c cmd	run pythin script sent in as cmd string
#		file run python script from given file
# 		-h help
#		must enter empty physical line to terminate a multiline statement in iis (interactive interpreter session)

# identifiers
#		class names start with upper case
#		all others start with lower
#		starting with single leading underscore means the identifier is private
#		starting with double leading underscore means the identifier is strongly private
#		if it also ends with double trailing underscore the identifier  is a language defines special name

# keywords
#		and		assert		break		class 		continue 	def
#		del		elif 		else 		except 		exec 		finally
#		for 	from 		global 		if 			import 		in
# 		is 		lambda 		not 		or 			pass 		print
# 		raise 	return 		try 		while 		with 		yield

# lines and indentation
#		no braces to indicate blocks of code or flow control
#		number of spaces is variable but all must be the same

# multi-line statements
#		statements typically end with a newline
#		does allow the continuation character \
#		statements contained within any bracket doesn't need a \

# quotations
#		(') 'word' (") "sentence" (''' or """) """para
#													graph"""
#		triple quotes are for spanning across multiple lines

# waiting for the user
#		raw_input("\n\nPress the enter key to exit.")
#		good trick to keep the console window open untilk the user is done with the application

# multiple statements on a single line
#		the semicolon ; allows for multiple statements on a single line
#		given that neither statement starts a new block of code

# multiple statement groups as suites
#		a group of individual statements, which make a single code block are called suites
#		compound or complex statements such as if, while, def, and class require a header line and a suite
#		header lines begin the statement (with the keyword) and terminate with a colon and are followed by one or more lines which make up the suite
# 		if expression:
# 			suite
# 		elif expression :
# 			suite

# multiple assignment
# 		allows a single value to be assigned to several variables simultaniously
# 			a = b = c = 1
#		or
#			a, b, c  = 1, 2, "john"

# data types
#		numbers -
#			number objects are created when you assign a value to them
# 			use del to delete the reference to a number object
#				del var1[,var2[,var3]]
#				del var, var_b
#			int (signed integers) 10
#			long (long integers, can be represented in octal or hex) 0x122, 122L use L
#			float (floating point real values) 7.7
#			complex (complex numbers) 3.14j, 45.j complex numbers consist of an ordered pair of real floating point numbers denoted by x + yj where x and y are real numbers and j is the imaginary unit
#		strings -
#			contiguous set of characters represented in the quotation marks
#			subsets can be taken using the slice operator ([] and [:]) with indexes starting at 0 at the beginning and working their way from -1 at the end
#			+ is the string concatenation operator and * is the repitition operator
#				print str[2:5] 		# prints the 3rd char to the 5th
#				print str * 2		# prints str 2 times
#				print str + "test" 	# prints concatenated string
#		lists -
#			most versitile of compound data types
#			a list contains items seperated by commas enclosed in square brackets
#				list = [777, 7.7, "Seven", 'seven']
#			similar to arrays in C to an extent. one difference is that the items belonging to a list can be of different data types
#			the values can be accessed using the slice operator (see strings above)
#		tuples -
#			essentially a read-only list that cannot be upgraded or changed
#				tuple = (777, 7.7, "Seven", 'seven')
#		dictionaries -
#			kind of hash table type
#			consist of key value pairs of almost any type but are usually numbers or strings
#			valuses can be any arbitrary object
#			created using {} and values can be accessed and assigned using []
#				dict = {}
#				dict['one'] = "This is one"
#				dict[2] 	= "This is two"
#			dictionaries have no concept of order amount elements they are simply unordered

# data type conversion
#			to convert between type simply use the type name as a function
#			these functions return a new object representing the converted values
#				int(x[,base])	converts x to an int. base specifies the base is x is a string
#				long(x[,base])	converts x to a long. base specifies the base is x is a string
#				float(x)		converts x to a floating point number
#				complex(real[,imag]) creates a complex number
#				str(x)			converts object x to a string
#				repr(x)			converts object x to an expression string
#				eval(str)		evaluates str and returns an object
#				tuple(s)		converts s to a tuple
#				list(s)			converts s to a list
#				set(s)			converts s to a set
#				dict(d)			creates a dictionary/ d must be a sequence of (key,value) tuples
#				frozenset(s)	converts s to a frozen set
#				chr(x)			converts an int to a char
#				unichr(x)		converts an int to a unicode char
#				ord(x)			converts a single char to its int value
#				hex(x)			converts an int to a hex string
#				oct(x)			converts an int to an octal string

# basic operations
#			+ - * / %
#			** exponent a**b
#			// floor division. the result is the quotient in which the digits after the decimal are removed. if one is negative the result is floored, rounded away from 0 towards -infinity
#
#			== != > < >= <=
#			<> if the values are not equal the condition becomes true (a <> b) is true similar to !=
#
#			= += -= *= /= %= **= //=
#
#			bitwise - a = 60 (means 0011 1100)		b = 13 (means 0000 1101)
#				a & b = 0000 1100 	& and	operator copies a bit to the result if it exists in both operands
#				a | b = 61 (means 0011 1101)	| or	it copies a bit if it exists in either operand
#				a ^ b = 49 (means 0011 0001)	^ xor	it copies the bit if it is set in one operand but not both
#				~a = -61 (means 1100 0011 in 2's complement form due to a signed binary number)		~ ones complement	unary and has the effect of 'flipping' bits
#				a << 2 = 240 (means 1111 0000)	<< left shift	left operands value is moved by the number of bits specified by the right
#				a >> 2 = 15 (means 0000 1111)	>> right shift	left operands value is moved by the number of bits specified by the right operand
#
#			logical - and, or, not (used to switch the logic)
#
#			membership - test for membership in a sequence (string, list, tuple)
#				in	evaluates to true if it finds a variable in the specified sequence and false otherwise
#				not in	evaluates to true if it does not find a variable in the specified sequence and false otherwise
#
#			identity - compare memory locations of two objects
#				is	evaluates to true if the variables on either side of the operatior point to the same object false otherwise
#				is not	evaluates to false if the variables on either side of the operatior point to the same object true otherwise
#
#			precedence -
#				**,	~ + -,	* / % //, + -,	>> <<,	&,	^ |,	<= < > >=,	<> == !=, = %= /= //= -= += *= **=, 	is is not,	in not in,	not or

# loops
#			while - repeats a statement / group of statements while a given condition is true. tests condition before executing the body
#			for - executes a sequence of statements multiple times and abbreviates the code that manages the loop variable
#			break - terminates the loop and transfers execution to the statement immediately following the loop
#			continue - causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating
#			pass - used when a statement is required syntatically but you do not want any command or code to execute

# numbers
#			math functions
#				abs(x) - positive distance between x and 0
#				ceil(x) - the smallest integer not less than x (the ceiling of x)
#				cmp(x,y) - -1 if x < y, 0 if x == y, or1 if x > y
#				exp(x) - exponential of x. e^x
#				fabs(x) - the abs of x
#				floor(x) - largest integer not greater than x (the floor of x)
#				log(x) - natural log of x for x > 0
#				log10(x) - base 10 log of x for x > 0
#				max(x1, x2,...) - the value closest to +infinity
#				min(x1, x2,...) - the value closest to -infinity
#				modf(x) - the fractional and integer parts of x in a two-item tuple. both parts have the same sign as x. the int part is returned as a float
#				pow(x,y) - the value of x**y
#				round(x[,n]) - x rounded to n digits from the decimal point. rounds away from 0 as a tie breaker. 0.5 is 1.0 -.05 is -1.0
#				sqrt(x)	- square root of x for x > 0

# random number functions
#			random numbers are used for games, simulations, testing, security, and privacy applications
#			choice(seq) - a random item from a list, tuple, or string
#			randrange([start,]stop[,step]) - a randomly selected element from range(start, stop, step)
#			random() - a random float r, such the 0 <= r && r < 1
#			seed(x) - sets the int starting value used in generating random numbers. call this function before calling any other random module function. returns none
#			shuffle(lst) - randomizes the items of a list in place. returns none
#			uniform(x,y) - a random float r, such that x <= r < y

# trig functions
#			acos(x) - return arc cosing of x in radians
#			asin(x) - return the arc sine of x in radians
#			atan(x) - return the arc tangent of x in radians
#			atan2(y,x) - return atan(y / x) in radians
#			cos(x) - return the cosine of x in radians
#			hypot(x,y) - return the Euclidean norm, sqrt(x*x + y*y)
#			sin(x) - return the sine of x in radians
#			tan(x) - return the tangent of x in radians
#			degress(x) - converts angle x from radians to degrees
#			radians(x) - converts angle x from degrees to radians
#
#			pi - constant
#			e - constant

# functions
#			function blocks begin with def followed by the function name and ()
#			the code block within every function starts with a : and is indented

# i/o
#			simplest way is using print
#			raw_input([prompt]) reads one line from the standard input and returns it a string without the trailing '\n'
#				str = raw_input("Enter input: ")
#				print "Received input is : ", str
#			input([prompt]) same as raw but it assumes the input is a valid python expression and returns the evaluated result to you.
#			open() creates a file object = open(file_name [, access_mode][, buffering])
#					file_name - string value argument that contains the name of the file
#					access_mode - the access_mode (read, write, append)
#					buffering - if the value is set to 0 no buffering takes place. if set to 1 buffering is preformed while accessing a file. if you specify the buffering value as an int greater than 1 then buffering action is performed with the indicated buffer size. if negative the buffer size is the system default
