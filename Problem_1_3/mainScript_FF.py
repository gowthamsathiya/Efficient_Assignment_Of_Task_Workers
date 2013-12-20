# Main Script to call EK and FF

#!/usr/bin/env python 
import process_input as ip
import Modifygraph as mg
import FF_6_1 as FF1
import datetime
import compute_min_cut as mc

nim = []
ft = open('Result_Times.txt', 'ab')

def six_1():
	#process input and returns graph dictionary
	G = ip.process_input()

	for n in G:
		for m in G[n]:
			G[n][m]['max'] = 1
			G[n][m]['min'] = 0
	
	#Call to Ford Fulkerson algorithm 
	t0 = datetime.datetime.now()
	resultGraph = FF1.assign_task_workers(G)
	t1 = datetime.datetime.now()

	ft.write('\n 6.1 FF : ' + str((t1-t0).microseconds)+ ' ms')

def six_3():

	# Process input and returns graph dictionary
	G = ip.process_input_6_3()

        # Changing attributes of the graph to maintain different terms used; 
	# Pass boolean value to tell the method if a 'min' value is wanted in the graph
	newG = ip.changeGraphAttributes(G, False, 'ToCapFlow')

	ts1 = datetime.datetime.now()
	resG = FF1.fordfulkersan(newG)
	ts2 = datetime.datetime.now()
	ft.write('\n 6.3 FF :'+ str((ts2 - ts1).microseconds)+ 'ms')
	
	# Modify result graph to 'max' 
	newResG = ip.changeGraphAttributes(resG, False, 'ToMaxMin')

	A, B = mc.create_min_cut_sets(newResG, [], 'S', [])
	
	profit, output = mc.computeProfit_Output(A, B, G)
	
	file_result = open('Result_File_6.3.txt', 'ab')
	file_result.write('\nFF Tasks Chosen and Profit: \n')
	file_result.write('6.3: Tasks Chosen: '+ str(output)+'\n')
	file_result.write('6.3: Total Profit: ' + str(profit)+ '\n')

def assignments_FF():
	#Calls to the three problems
	ft.write('\n--- F-F  ---')
	t1 = datetime.datetime.now()
	six_1() #6.1
	t2 = datetime.datetime.now()
	ft.write('\n Total Time Taken to complete 6.1 F-F :'+ str((t2-t1).microseconds)+ ' ms')

	t3 = datetime.datetime.now()
	six_3() #6.3
	t4 = datetime.datetime.now()
	ft.write('\n Total Time Taken to complete 6.3 F-F :'+ str((t4-t3).microseconds)+ ' ms')
	ft.write('\n--- F-F  ---\n')

