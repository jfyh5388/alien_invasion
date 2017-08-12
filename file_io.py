def writedata(highscore, filename):
	with open(filename, 'w') as f_obj:
		f_obj.write(str(highscore))
	
def readdata(filename):
	with open(filename, 'r') as f_obj:
		return f_obj.read()
	
	
	
