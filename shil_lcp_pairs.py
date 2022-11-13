import sys 
 
class node: 
	def __init__(self, char):
		self.count = 0
		self.char = char
		self.children = [] 
		
root = node(None)

linecount = 0
words = 0
pairs = [0]
for line in sys.stdin:
	#print(len(line))
	if linecount == 0:
		words = str(line)
	else:
		curNode = root
		root.count = root.count + 1
		levelCount = 0		
		
		for char in line:
			if char == '\n':
				break
			levelCount = levelCount + 1
			while(len(pairs)<levelCount+1):
				pairs.append(0)
			#print(char)
			nextNode = None
			for child in curNode.children:
				if child.char == char:
					nextNode = child
					break
			if nextNode == None:
				newChild = node(char)
				curNode.children.append(newChild)
				nextNode = newChild
			
			nextNode.count = nextNode.count + 1
			if levelCount == len(line) or line[levelCount] == '\n':
				pairs[levelCount] = pairs[levelCount] + nextNode.count - 1
			
			pairs[levelCount-1] = pairs[levelCount-1] + (curNode.count - nextNode.count)
 
			curNode = nextNode
						
	linecount = linecount + 1		
 
pairs = [str(x) for x in pairs]
print(' '.join(pairs))			
			
