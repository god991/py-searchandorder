'''
Created on 2018年8月2日

@author: liminjie
'''

import math

if __name__ == '__main__':
    pass

'''-----'''
#-----广度优先搜索------
'''--搜索当前深度的所有下一级节点，如下一级节点=目标节点，结束返回，否则添加到队列，然后继续
使用一个字典保存所有已搜索的路径，找到则直接退出，否则继续递归查找。
dict={'1':['2','3','4']}
startKeys=[1,2,3]
pathDict={1:['1','2','6']} #保存已搜索的路径，即所有的下一级的搜索都是基于当前的路径进行搜索
haveSearchKeys=[] #保存已搜索过的节点，如已搜索过，直接跳过'''

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
    
#--带权重的最短路径搜索-
'''
1.从原点出发，搜索原点各个路径的权重。
2.使用两个字典，分别记录路径及总权重值
    pathDict={’5‘:['1','2','5'],’6‘:['1','3','6']} 每个key代表到达此节点的路径，后边是路径详细走法
    weightDict={’5‘:7,’6‘:5}                       每个路径的总体权重值
3.每搜索1个节点，都找相邻节点，并计算到相邻节点的最小权重，然后保存到dict中
4.如得到的权重比weightDict中记录的小，则更显路径及权重
'''
#pathDict={'5':['1','2','5'],'6':['1','3','6']}
#pathWeightDict={'5':7,'6':5}     
#findDict={}                  
def breadth_First_Search_weight(findDict,weightDict,distKey,pathDict,pathWeightDict={}): #带权重的路径查找
    '''遍历pathDict,更新路径权重，每遍历一次，进行一次递归调用
    第一次调用，初始时，weightDict是空，程序自动补充weight'''
    if len(pathWeightDict)==0: #第一次调用，pathDict必须时单个节点，没有路径
        startNode=list(pathDict.keys())[0]
        pathDict[startNode]=[startNode]
        pathWeightDict[startNode]=0
    haveUpdatePath=False
    distKeys=list(pathDict.keys())
    for currKey in distKeys: #'''每个节点后续节点及权重'''
        currPath=pathDict.get(currKey)  #'''当前路径'''
        currWeight=pathWeightDict.get(currKey)  #'''当前总权重'''
        nextNodes=findDict.get(currKey) #'''下一个节点'''
        nextWeights=weightDict.get(currKey) #''' 下一个节点权重 '''       
        '''计算每个到下一个节点的总权重，没有的或最小的更新到pathDict和weightDict中'''
        try:
            for x in zip(nextNodes,nextWeights):
                if pathWeightDict.get(x[0]) is None or (currWeight+x[1])<pathWeightDict.get(x[0]):
                    pathWeightDict[x[0]]=currWeight+x[1]
                    pathDict[x[0]]=currPath+[x[0]]
                    haveUpdatePath=True
        except :
            pass
        finally:
            pass
    #遍历了所有路径后，不再更新pathDict即比较完了所有路径
    if not haveUpdatePath:
        return pathDict.get(distKey)
    else:
        return breadth_First_Search_weight(findDict,weightDict,distKey,pathDict,pathWeightDict)

#--迪克斯特拉算法---
'''
从起点开始
1.每个节点计算邻居节点的最小开销，
2.如果比邻居本身节点开销小，则更新
重复1-2,对每个节点计算开销，从而计算出所有节点中最小开销
'''     
#haveSearchNodes=[]
def dijkstra_Search(distDict,allPathWeightDict,distNode,havePathDict={},havePathWeightDict={},haveSearchNodes=[]):
    '''遍历pathDict,要是节点不在haveSearchNodes中，则更新邻居路径开销，每遍历一次，进行一次递归调用
    第一次调用，初始时，weightDict是空，程序自动补充weight'''
    if len(havePathWeightDict)==0: #第一次调用，pathDict必须时单个节点，没有路径
        startNode=list(havePathDict.keys())[0]
        havePathDict[startNode]=[startNode]
        havePathWeightDict[startNode]=0
    #haveUpdatePath=False
    havePathNodes=list(havePathDict.keys())
    for currNode in havePathNodes: #'''每个节点后续节点及权重'''
        #如果当前节点计算过了，就不再统计当前节点及邻居节点
        if currNode in haveSearchNodes:
            continue #不再计算当前节点        
        currPath=havePathDict.get(currNode)  #'''当前路径'''
        currWeight=havePathWeightDict.get(currNode)  #'''当前总权重'''
        nextNodes=distDict.get(currNode) #'''下一个节点'''
        nextWeights=allPathWeightDict.get(currNode) #''' 下一个节点权重 '''       
        '''计算邻居节点的总体开销，如果邻居总体开销比记录的小，则更新'''
        try:
            for x in zip(nextNodes,nextWeights):
                if havePathWeightDict.get(x[0]) is None or (currWeight+x[1])<havePathWeightDict.get(x[0]):
                    havePathWeightDict[x[0]]=currWeight+x[1]
                    havePathDict[x[0]]=currPath+[x[0]]
                    #haveUpdatePath=True
        except :
            pass
        haveSearchNodes.append(currNode)
    #遍历了所有路径后，不再更新pathDict即比较完了所有路径
    if len(distDict)==len(haveSearchNodes):
        return havePathDict.get(distNode)
    else:
        return dijkstra_Search(distDict,allPathWeightDict,distNode,havePathDict,havePathWeightDict,haveSearchNodes)


#--动态规划（解决离散问题)----
'''
动态规划是从小问题解决起，从而逐步解决大问题的思路
1.先找到需要解决的几个问题中的最小规格
2.从小规格算起，计算出每个规格的最大价值
3.递归调用，函数每次返回的都是本次调用的最优解。
capacity:当前容量，只能做这么多事
cargoDict: 每件物品名称、所占容量、价值
haveTryCargo：已经计算过的货物名称
两个矩阵，分别存储已计算后的总价值及如何组合
valueArray: 每行对应一个物品组合方式的价值
cargoArray: 与valueArray对对应，valueArray的每个元素对应到此列表都是一个列表，表示物品组合方式
'''

#cargoDict={1:1,2:2}
def dynamicProgramming_Search(capacity,cargoDict={},haveTryCargo=[],valueArray=[],cargoArray=[],minCapa=0,calls=0):
    #取得所有物品中容量最小的物品容量，作为基准值
    if minCapa==0:
        minCapa=min([x[0] for x in cargoDict.values()])
        calls=math.ceil(len(cargoDict) / minCapa)

    copyCargoDict=cargoDict.copy()
    if len(cargoDict)>1:
        currItem=copyCargoDict.popitem()
        dynamicProgramming_Search(capacity,copyCargoDict,haveTryCargo,valueArray,cargoArray,minCapa,calls) #返回的是列表
        #把当前元素popItem加入矩阵，然后计算
        currCargo=list(currItem.keys())[0]
        haveTryCargo.append(currCargo)
        for i in range(0,calls):
            currCapa=(i+1)*minCapa
            if currCapa>=currItem.get(currCargo)[0]: #能存放下
                if currItem.get(currCargo)[1]>valueArray[len(haveTryCargo)-2][i]:
                    #当前价值大于上一行价值
                    pass
    elif len(cargoDict)==1:
        pass
    else:
        print('物品名称、价值字典长度为0或不是字典类型')

