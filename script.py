from sklearn import svm

def dipeptite_composition(file):
	data = file.readlines()
	data = data[1:]
	X=[]
	for line in data:
		string = list(line.split(","))
		seq = string[1]
		xx=[]
		for i in range(1,401):
			seq=string[i]
			xx.append(float(seq))
		X.append(xx)
	return X


def amino_composition(file,i):
	data = file.readlines()
	data = data[1:]
	X=[]
	for line in data:
		string = list(line.split(","))
		seq = string[i]
		if(seq[-1]=='\n'):
			seq = seq[:-1]
		n = len(seq)			
		dict={'A':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'K':0,'L':0,'M':0,'N':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'V':0,'W':0,'Y':0}
		feat=[]
		for char in seq:
				dict[char]+=1
		for k in dict:
			feat.append(100*(dict[k]/n))
		X.append(feat)
	return X

Y=[]
file = open("train.csv","r")
data = file.readlines()
data = data[1:]
for line in data:
	string = list(line.split(","))
	Y.append(int(string[1]))



X1=[]
file2=open("train.csv","r")
X1=amino_composition(file2,2)



X2=[]
file = open("dipeptide_result_train.csv","r")
X2=dipeptite_composition(file)

for i in range(len(X2)):
	for j in range(len(X1[i])):
		X2[i].append(X1[i][j])
# print(X2)


clf = svm.SVC(gamma ='scale')
clf.fit(X2, Y)
file.close()

# clf2=svm.SVC(gamma='scale')
# clf2.fit(X2,Y)

x1=[]
file_test = open("test.csv","r")
x1=amino_composition(file_test,1)

x2=[]
file = open("dipeptide_result_test.csv","r")
x2=dipeptite_composition(file)


for i in range(len(x2)):
	for j in range(len(x1[i])):
		x2[i].append(x1[i][j])
# print(x2)


out=clf.predict(x2)
# out2=clf2.predict(x2)
# out3=clf3.predict(x3)
# print(out3)
# Mean=[]
# for i in range(len(out)):
# 	mean=(out[i]+out2[i]+out[i])//3
# 	Mean.append(mean)


ofile = open("output.csv","w")
s="ID,Label\n"
ofile.write(s)
ind=0
file_test = open("test.csv","r")
data = file_test.readlines()
data = data[1:]

for line in data:
	s = list(line.split(","))
	l = s[0]+","+str(out[ind])+'\n'
	ofile.write(l)
	ind=ind+1
