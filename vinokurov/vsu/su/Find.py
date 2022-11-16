file = open("input2","r")
file1 = open("output2","w")
text = file.read()
file.close()
sample = [int(i) for i in text.split()]
length = len(sample)
count = 0
countBin=0
countIn=0
def find(arr,a):
    counter = 0
    length = len(arr)
    for i in range(0,length-1):
        counter+=1
        if(a==arr[i]):
            break
    return counter

for i in range(0,length):
    count=count+find(sample,i)

count = count/length

file1.write("find = "+str(count)+" ")

def findBinary(arr,a):
    low = 0
    high = len(arr)-1
    counter=0
    while(low<=high):
        counter+=1
        mid = (low+high)
        midVal = arr[mid]

        if(midVal<a):
            low=mid+1
        else:
            if(midVal>a):
                high = mid-1
            else:
                break
    return counter#-(low+1)

for i in range(0,length):
    countBin=countBin+findBinary(sample,i)

countBin = countBin/length

file1.write("findBin = "+str(countBin)+" ")

def findInterpolation(arr,a):
    low = 0
    counter = 0
    high = len(arr)-1
    while((arr[low]<a)and(arr[high]>a)):
        counter+=1
        if(arr[high]==arr[low]):break
        mid = int(low+((a-arr[low])*(high-low))/(arr[high]-arr[low]))
        if(arr[mid]<a):low=mid+1
        else:
            if(arr[mid]>a):
                high=a-1
            else:break
    return counter
for i in range(0,length):
    countIn+=findInterpolation(sample,i)

countIn = countIn/length

file1.write("findIn = "+str(countIn))

#sample = [str(i) for i in sample]
#file1.write(" ".join(sample))
#file1.write("\n"+str(count))
file1.close()

