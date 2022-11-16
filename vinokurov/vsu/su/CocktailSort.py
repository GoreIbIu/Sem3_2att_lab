file = open("input4","r")
file1 = open("output4","w")
text = file.read()
file.close()
sample = [int(i) for i in text.split()]
left = 0
right = len(sample) - 1
count = 0


while left <= right:
    for i in range(left, right, +1):
        count+=1
        if sample[i] > sample[i + 1]:
            sample[i], sample[i + 1] = sample[i + 1], sample[i]
    right -= 1

    for i in range(right, left, -1):
        count+=1
        if sample[i - 1] > sample[i]:
            sample[i], sample[i - 1] = sample[i - 1], sample[i]
    left += 1



sample = [str(i) for i in sample]
file1.write(" ".join(sample))
file1.write("\n"+str(count))
file1.close()