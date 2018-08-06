'''
Created on 2018年8月2日

@author: liminjie
'''
#import cmcc.nm.PathSearch as ps

if __name__ == '__main__':
    pass

a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
d = [[1,2],[3,4],[5,6]]

print(min([x[0] for x in d]))

d.clear()

 
tu={'1':['2','3','4'],'2':['5','6'],'3':['5','7'],'4':['7','10'],'5':['8','9'],\
    '6':['10'],'9':['10'],'8':['2']}
pathWeight={'1':[2,4,3],'2':[5,3],'3':[2,5],'4':[9,9],'5':[6,2],\
    '6':[10],'9':[-4],'8':[4]}

#print(ps.breadth_First_Search_weight(tu,pathWeight,'10',{'1':['1','2']}))
#print(ps.dijkstra_Search(tu,pathWeight,'10',{'1':['1','2']}))


