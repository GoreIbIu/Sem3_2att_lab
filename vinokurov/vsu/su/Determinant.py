import math
file = open("input1","r")
file1 = open("output1","w")
text = file.read()
file.close()
sample = text.split()
length = int(math.sqrt(len(sample)))
Mat = [0] * length
for i in range(length):
    Mat[i] = [0] * length
det = 1

for i in range(0,length,+1):
    for j in range(0,length,+1):
        Mat[i][j] = float(sample[length*i+j])
if (length==1): det = float(sample[0])
if (length==2): det = float(sample[0])*float(sample[3])-float(sample[1])*float(sample[2])
if(length>2):
    for x in range(0,length,1):
        delta  = Mat[x][x]
        for i in range(x+1,length,+1):
            delta1 = Mat[i][x]
            for j in range(0,length,+1):
                Mat[i][j] = Mat[i][j]-Mat[x][j]*delta1/delta

    for i in range(0,length,+1):
       det = det*Mat[i][i]


file1.write(str(det))
file1.close()