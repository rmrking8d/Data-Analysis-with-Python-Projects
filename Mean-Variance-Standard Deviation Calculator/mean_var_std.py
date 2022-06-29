import numpy as np


def calculate(list):
	#Error Check
	if len(list) < 9:
		raise ValueError("List must contain nine numbers.")
	#Inputted List -> 3x3 numpy array
	new = np.array(list).reshape(3, 3)

	#Calculations
	mean = [(new.mean(0).tolist()),
	        new.mean(1).tolist(),
	        np.mean(new).tolist()]
	variance = [(new.var(0).tolist()),
	            new.var(1).tolist(),
	            np.var(new).tolist()]
	sd = [(new.std(0).tolist()), new.std(1).tolist(), np.std(new).tolist()]
	max = [(new.max(0).tolist()), new.max(1).tolist(), np.max(new).tolist()]
	min = [(new.min(0).tolist()), new.min(1).tolist(), np.min(new).tolist()]
	sum = [(new.sum(0).tolist()), new.sum(1).tolist(), np.sum(new).tolist()]
	#Dict
	output = {
	    'mean': mean,
	    'variance': variance,
	    'standard deviation': sd,
	    'max': max,
	    'min': min,
	    'sum': sum
	}
	return output
