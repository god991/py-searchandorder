
class subTree():
    def __init__(self,node):
        self.node=node
        self.leftSubNode=None
        self.rightSubNode=None
    def setLeftSubNode(self,leftSubNode):
        self.leftSubNode=leftSubNode
    def setRightSubNode(self,rightSubNode):
        self.rightSubNode=rightSubNode
    def setParentNode(self,parentNode):
        self.parentNode=parentNode
    def getLeftSubNode(self):
        return  self.leftSubNode
    def getRightSubNode(self):
        return  self.rightSubNode
    def getParentNode(self):
        return  self.parentNode

#print(preOrder[0:1])
#构建二叉树,根据前序查找和中序查找结果构建二叉树
def CreateSubTreeFromOrder(pOrder,iOrder):
    #pOrder=iOrder=[]
    if(len(pOrder)==1):
        subtree=subTree(pOrder[0])
        return subtree
    elif(len(pOrder)==2 and pOrder[0]==inOrder[0] and pOrder[1]==inOrder[1]):
        subtree = subTree(pOrder[0])
        subtree.setRightSubNode(subTree(pOrder[1]))
        return subtree
    else:
        rootNode=pOrder[0:1]
        subtree = subTree(rootNode[0])
        leftSubPOrder=pOrder[1:]
        leftSubIOrder=iOrder[0:iOrder.index(rootNode[0])]
        leftSubPOrder=leftSubPOrder[:len(leftSubIOrder)]
        subtree.setLeftSubNode(CreateSubTreeFromOrder(leftSubPOrder,leftSubIOrder))
        rightSubIOrder = iOrder[iOrder.index(rootNode[0])+1:]
        rightSubPOrder = pOrder[-len(rightSubIOrder):]
        if(len(rightSubIOrder)>=1):
            subtree.setRightSubNode(CreateSubTreeFromOrder(rightSubPOrder,rightSubIOrder))
    return subtree

#查找两个节点的最近公共顶点
#完善二叉树（每个顶点的父顶点），同时查找两个节点
def finishSubTree(rootNode=subTree('a')):
    if(rootNode.getLeftSubNode()):
        rootNode.getLeftSubNode().setParentNode(rootNode)
        finishSubTree(rootNode.getLeftSubNode())
    if(rootNode.getRightSubNode()):
        rootNode.getRightSubNode().setParentNode(rootNode)
        finishSubTree(rootNode.getRightSubNode())

def findSubTreeNode(rootNode,distNode):
    returnNode=None
    if(rootNode==None):
        return None
    elif(rootNode.node==distNode):
        return rootNode
    else:
        returnNode=findSubTreeNode(rootNode.getLeftSubNode(),distNode)
        if (returnNode != None):
            return returnNode
        returnNode =findSubTreeNode(rootNode.getRightSubNode(), distNode)
        if (returnNode != None):
            return returnNode

preOrder=[1,2,4,7,3,5,8,9,6]
inOrder=[4,7,2,1,8,5,9,3,6]
find1=6
find2=7

mySubTree=CreateSubTreeFromOrder(preOrder,inOrder)
finishSubTree(mySubTree)

#计算node1和node2的深度，然后深度一样时在一步一步推算公共父节点
node1=findSubTreeNode(mySubTree,find1)
deep1=1
while(node1.node!=mySubTree.node):
    node1=node1.getParentNode()
    deep1+=1
node1=findSubTreeNode(mySubTree,find1)

node2=findSubTreeNode(mySubTree,find2)
deep2=1
while(node2.node!=mySubTree.node):
    node2=node2.getParentNode()
    deep2+=1
node2=findSubTreeNode(mySubTree,find2)

if(deep1>deep2):
    while(deep1-deep2>0):
        node1=node1.getParentNode()
        deep1-=1
elif(deep2>deep1):
    while(deep2-deep1>0):
        node2=node2.getParentNode()
        deep2-=1

while(node1.node!=node2.node):
    node1=node1.getParentNode()
    node2=node2.getParentNode()

print(node1.node)