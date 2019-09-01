import matplotlib.pyplot as plt 
f = open('01--Convert 2.txt', "r")
lines = f.readlines()
GRO=list()
for line in lines:
	words=line.split()
	for word in words:
		if word == "GRO":
			GRO.append(words)
			break
print(len(GRO))

f.close()

#sep=GRO[0].split()
x=list()
y=list()
#print(GRO[0])

for sep in GRO[0]:
	if '/' in sep:
		cor=sep.split('/')
		x.append(float(cor[0]))
		y.append(float(cor[1]))

print(x)
print(y)
 
plt.plot(x, y,color='k', linestyle='dashed', marker='o') 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('graph!') 
plt.show() 
