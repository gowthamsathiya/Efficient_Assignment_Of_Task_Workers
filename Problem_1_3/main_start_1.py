#Main calling script that calls EK and FF assignment calls

#!/usr/bin/env python

import mainScript_EK as EK
import mainScript_FF as FF

def start():
	EK.assignments_EK()
	FF.assignments_FF()

