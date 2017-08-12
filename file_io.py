import json
def writedata(highscore, filename):
	with open(filename, 'w') as f_obj:
		json.dump(highscore, f_obj)
	
def readdata(filename):
	with open(filename, 'r') as f_obj:
		return json.load(f_obj)
	
	
	
