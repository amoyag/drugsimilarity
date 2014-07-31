
import os
import numpy as np
import pylab as plt
import random



title = 'Drug - PFAM (mapping)'

file = open('./results/pcc.txt', 'r')
lines = file.readlines()
np.array(lines)
file.close()
pcc = []
np.array(pcc)
for line in lines:
    line = line.replace("\n", "")
    vals = line.split("\t")
    kk = float(vals[2])
    pcc.append(kk)    

file = open('./results/similarity.txt', 'r')
lines = file.readlines()
np.array(lines)
file.close()
sim = []
np.array(pcc)
for line in lines:
    line = line.replace("\n", "")
    vals = line.split("\t")
    kk = float(vals[2])
    sim.append(kk)      

#zip the two data lists, make 5 lists for similarity intervals, sort pcc index in those intervals

set = zip(sim,pcc)

de0a02 =[]
de02a04 =[]
de04a06 =[]
de06a08 =[]
de08a1 =[]
for i in range(len(sim)):
    #set[i][0] similarity
    #set[i][1] pcc index
    if set[i][0] >=0. and set[i][0] < 0.2:
        de0a02.append(set[i][1])
    elif set[i][0] >=0.2 and set[i][0] < 0.4:
        de02a04.append(set[i][1])
    elif set[i][0] >=0.4 and set[i][0] < 0.6:
        de04a06.append(set[i][1])        
    elif set[i][0] >=0.6 and set[i][0] < 0.8:
        de06a08.append(set[i][1]) 
    elif set[i][0] >=0.8 and set[i][0] <= 1.0:
        de08a1.append(set[i][1])       

#select 300 random elements from de02a04 and de04a06. These bins are way too populated


de02a04 = random.sample(de02a04, 300)
de04a06 = random.sample(de04a06, 300)

# boxes=[de0a02,de02a04,de04a06,de06a08,de08a1]
boxes=[de0a02,de02a04,de04a06,de06a08,de08a1]
for box in boxes:
    print np.mean(box)
    print len(box)



#Plotting stuff

plt.figure()

bp = plt.boxplot(boxes, sym = '') 
plt.setp(bp['boxes'], color='grey',linewidth=1.5)
plt.setp(bp['medians'], color='black',linewidth=1.5)
plt.setp(bp['whiskers'], color='grey',linewidth=1.5)
plt.setp(bp['caps'], color='black',linewidth=1.5)


labels = ['0.0-0.2' + "\n" + str(len(de0a02)), '0.2-0.4' + "\n" + str(len(de02a04)), '0.4-0.6' + "\n" + str(len(de04a06)), '0.6-0.8' + "\n" + str(len(de06a08)), '0.8-1.0' + "\n" + str(len(de08a1))]

plt.xticks(range(1,6),labels, rotation=0)
plt.xlabel('Structure similarity')
plt.ylabel('PCC Association Index')
plt.title(title)
plt.ylim(-0.2,1.2)

means = [np.mean(x) for x in boxes]

plt.savefig('./results/PFAM_mapping-boxplot.pdf', format='pdf')
plt.show()


