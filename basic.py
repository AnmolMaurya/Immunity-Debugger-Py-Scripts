#!/usr/bin/env python

import immlib
DESC = "Basic Scripting program , inlcudes processes, tables"

def main(args)
  imm = immlib.Debugger()
  
  imm.log()
  
  imm.updatelog() #To update the log at certain point of requirement
  
  id =  imm.createTable("Luftatko", ("PID","Name","Path","Services"))
  
  psList = imm.ps() #for getting the process list
  
  for process in psList:
    id.add(0,(str(process(0),process(1),process(2),str(process(3)))))
  
  #print "Welcome to immunity Debugger"
  
  return "Welcome to immunity Debugger"
  
  
