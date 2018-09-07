'''
Created on 2018年7月30日

@author: liminjie
'''

if __name__ == '__main__':
    pass


#-----选择排序--------------------------------
def selectOrder(arr):  #选择排序
    #lists=[1,3,5,3,4,55,7]
    list2=[]
    while len(arr)>0:    
        minValue=getMin(arr)
        list2.append(minValue)
        arr.remove(minValue)
    print(list2)

def getMin(arr):
    #arr=['a','b']
    smallValue=arr[0]   #记录最小值
    for i in range(1,len(arr)):
        if(arr[i]<smallValue):
            smallValue=arr[i]            
    return smallValue
 
def getMax(arr):
    arr=['a','b']
    maxValue=arr[0]   #记录最小值
    for i in range(1,len(arr)):
        if(arr[i]>maxValue):
            maxValue=arr[i]            
    return maxValue

#-----快速排序----------------------------------------
def fastOrder(arr):
    #arr=[1,3,5,3]
    if len(arr)<=1:
        return arr
    else:
        midValue=arr[0]
        leftArr=[]
        rightArr=[]
        for x in arr:
            if x<midValue:
                leftArr.append(x)
            elif x>midValue:
                rightArr.append(x)
        return fastOrder(leftArr)+[midValue]+fastOrder(rightArr)

def fastOrder2(arr):
    if arr==None:
        arr=[0,1,2]
    i=1
    j=len(arr)-1
    while(i<j):
        while(arr[i]<arr[0]):
            i+=1
        while(arr[j]>arr[0]):
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1


#-----希尔排序--------------
def shell(arr):
    n=len(arr)
    h=1
    while h<n/3:
        h=3*h+1
        while h>=1:
            for i in range(h,n):
                j=i
                while j>=h and arr[j]<arr[j-h]:
                    arr[j], arr[j-h] = arr[j-h], arr[j]
                    j-=h
                    h=h//3
    print(arr)

#-----广度优先搜索------
#---搜索当前深度的所有下一级节点，如下一级节点=目标节点，结束返回，否则添加到队列，然后继续
#--使用一个字典保存所有已搜索的路径，找到则直接退出，否则继续递归查找。
#dict={'1':['2','3','4']}
#startKeys=[1,2,3]
#pathDict={1:['1','2','6']} #保存已搜索的路径，即所有的下一级的搜索都是基于当前的路径进行搜索
#haveSearchKeys=[] #保存已搜索过的节点，如已搜索过，直接跳过
def Breadth_First_Search(findDict,pathDict,distKey,haveSearchKeys=[]):
    #pathDict为空或找到目标节点，结束查找。每递归一次查找一次深度
    if len(pathDict)==0:
        return None
    pathKeys=list(pathDict.keys())
    #找到最大的keys，以后每次都加1，然后删除已经查询过的路径
    maxKey=max(list(pathKeys))
    #检查每一条路径的下一层次节点是否是目标节点，如是结束    
    for pathKey in pathKeys:
        path=pathDict.get(pathKey) 
        #当前已查找的路径，找到路径最后一个节点，看这个节点能走到哪个节点，然后形成新的路径，附加pathDict中
        currPathLastNode=path[-1:][0] #获取到当前路径最后一个节点的编号
        nextNodes=findDict.get(currPathLastNode)
        try:
            for nextNode in nextNodes:
                if not (nextNode in haveSearchKeys):
                    #path.append(nextNode)
                    haveSearchKeys.append(nextNode)
                    if nextNode==distKey:
                        return path+[nextNode]
                    else:
                        pathDict[maxKey+1]=path+[nextNode]
                        maxKey+=1                
        except:
            pass
        finally:
            pathDict.pop(pathKey) #已检查完当前路径的所有后续路径
    return Breadth_First_Search(findDict,pathDict,distKey,haveSearchKeys)        
    

tu={'1':['2','3','4'],'2':['5','6'],'3':['5','7'],'4':['7','10'],'5':['8','9'],\
    '6':['10'],'9':['10']}

print(Breadth_First_Search(tu,{1:['1',]},'9',[]))


