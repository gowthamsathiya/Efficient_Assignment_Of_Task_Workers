# Main Script to call EK and FF

#!/usr/bin/env python 

import process_input as ip
import edmond_karp as EK
import Modifygraph as mg
import compute_min_cut as mc
import datetime

nim = []
ft = open('Result_Times.txt', 'ab')

def six_1():
	#process input and returns graph dictionary
	G = ip.process_input()
	#ip.draw_graph(G, 'Original Graph')

	#Modify the graph to min = 0 and max = 1 for perfect bipartite matching
	for n in G:
		for m in G[n]:
			G[n][m]['max'] = 1
			G[n][m]['min'] = 0

	#Call to Edmond_Karp algorithm 
	t0 = datetime.datetime.now()
	max_flow, F, nim, RG = EK.edmond_karp(G, '6.1', None)
	t1 = datetime.datetime.now()
	ft.write('\n 6.1 EK : ' + str((t1-t0).microseconds)+ ' ms')


def six_3():

	#process input and returns graph dictionary
	G = ip.process_input_6_3()
	#ip.draw_graph(G, 'Original Graph_6.3')
	
	ts1 = datetime.datetime.now()
	max_flow, F, nim, RG = EK.edmond_karp(G, '6.3', None)
	ts2 = datetime.datetime.now()
	ft.write('\n 6.3 EK : '+ str((ts2 - ts1).microseconds)+ 'ms')

	#ip.draw_graph(RG, 'Residual Graph_6.3')
		
	#print RG, F
	A, B = mc.create_min_cut_sets(RG, F, 'S', nim)

	profit, output = mc.computeProfit_Output(A, B, G)
	
	file_result = open('Result_File_6.3.txt', 'ab')
	file_result.write('EK Tasks Chosen and Profit: \n')
	file_result.write('6.3: Tasks Chosen: '+ str(output)+'\n')
	file_result.write('6.3: Total Profit: ' + str(profit)+ '\n')

def assignments_EK():
	#Calls to the three problems
	ft.write('\n--- E-K  ---')

	t1 = datetime.datetime.now()
	six_1() #6.1
	t2 = datetime.datetime.now()
	ft.write('\n Total Time Taken to complete 6.1 E-K :'+ str((t2-t1).microseconds)+ ' ms')

	t3 = datetime.datetime.now()
	six_3() #6.3
	t4 = datetime.datetime.now()
	ft.write('\n Total Time Taken to complete 6.3 E-K :'+ str((t4-t3).microseconds)+ ' ms')

	ft.write('\n--- E-K  ---\n')
