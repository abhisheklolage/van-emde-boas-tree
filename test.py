import vEB

# tree members 1 2 50 99 100 123 500

members = [1, 2, 50, 99, 100, 123, 500]

u = 10000
v = vEB.VEBtree(u)
print v.u

def checkMembershipInsDel(x):
	already_there = v.isMember(x)

	print str(x) + " is " + str(v.isMember(x))

	print "Deleting " + str(x)
	v.vebTreeDelete(x)

	print str(x) + " is " + str(v.isMember(x))

	print "Inserting " + str(x)
	v.vebTreeInsert(x)
	
	print str(x) + " is " + str(v.isMember(x))
	if not already_there:
		v.vebTreeDelete(x)	
		print "Deleting x from Tree as it was not there before"

for member in members:
	v.vebTreeInsert(member)

for member in members:
	print v.isMember(member)

print v.isMember(10)
print v.isMember(21)

#checkMembershipInsDel(1)
#checkMembershipInsDel(100)
#checkMembershipInsDel(101)
#print v.isMember(101)

for member in members:
	print str(member) + "'s predecessor is " + str(v.getPredecessor(member))
for member in members:
	print str(member) + "'s successor is " + str(v.getSuccessor(member))
