#run inside calculated field in Tableau
SCRIPT REAL('
	import numpy as np
	return np.corrcoef(_arg1,_arg2)[0,1]
	',
SUM([Sales]), SUM([Profit]))

#Returns Correlation Coefficient of Sales:Profit
