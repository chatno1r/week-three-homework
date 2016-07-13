speed_limit=int(raw_input ("what is the local speed limit? \n"))
drivers_speed=int(raw_input("how fast was the driver going? \n"))
overage=drivers_speed-speed_limit
base_ticket_cost=30


if overage<=5:
	action="you may dispute your ticket"
	print "your ticket cost is: ", base_ticket_cost
	print "your available action is: ", action
elif overage>5 and overage<=10:
	ticket_cost=base_ticket_cost+base_ticket_cost*0.1
	print "your ticket cost is:", ticket_cost
elif overage>10 and overage<=20:
	ticket_cost=base_ticket_cost+base_ticket_cost*0.25
	print "your ticket cost is:", ticket_cost
elif overage>20 and overage<=30:
	ticket_cost=base_ticket_cost+base_ticket_cost*.5
	action="you must attend driving school"
	print "your ticket cost is:", ticket_cost
	print "your available action is:", action
else:
	ticket_cost=base_ticket_cost+base_ticket_cost*.7
	action="your court date is set"
	print "your ticket cost is:", ticket_cost
	print "your available action is:", action


