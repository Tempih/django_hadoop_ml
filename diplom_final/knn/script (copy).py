#!/usr/bin/env python
import sys
import os
import time
prediction = []
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0

test_data_tfidf = []
f = open("/home/parallels/Downloads/knn/dataset_test_knn_100.txt", "r")
for line in f:
    z = eval(line)
    test_data_tfidf.append(z)
f.close()
cmd = './write_k.py'
os.system(cmd)
cmd = 'rm sd'
os.system(cmd)
print(len(test_data_tfidf))
time.sleep(10)
for line in range(len(test_data_tfidf)):
    cmd = 'hadoop fs -get /knn_test' + str(line) + '/sd'
    os.system(cmd)
    f = open("/home/parallels/Downloads/knn/sd", "r")
    for line in f:
        prediction.append(eval(line))
    f.close()
    cmd = 'rm sd'
    os.system(cmd)
accuracy = getAccuracy(test_data_tfidf, prediction)
f = open("/home/parallels/Downloads/knn/result_pr.txt","w")
for j in range(len(prediction)):
    f.write("pr="+str(prediction[j])+",ac="+str(test_data_tfidf[j][1]))
    f.write('\n')
f.close
f = open("/home/parallels/Downloads/knn/result.txt","w")
f.write(str(accuracy))
f.close()









