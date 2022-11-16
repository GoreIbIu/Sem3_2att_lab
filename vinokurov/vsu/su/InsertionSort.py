file = open("input3","r")
file1 = open("output3","w")
text = file.read()
file.close()
sample1 = [0, -1, 5, -2, 3]
sample = [int(i) for i in text.split()]
count = 0

for j in range(1,len(sample)):
    key = sample[j]
    i = j-1
    count+=1
    while((i>=0) and (sample[i]>key)):
        sample[i+1]=sample[i]
        i=i-1
    sample[i+1] = key

sample = [str(i) for i in sample]
file1.write(" ".join(sample))
file1.write("\n"+str(count))
file1.close()