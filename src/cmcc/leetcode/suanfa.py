'''
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums=[]
        nums.sort()
        y=0
        for x in nums:
            if x>target/2:
                break  #没找到
            y=target-x
            if(nums.index(y) and x!=y ):
                break #找到
        if(x!=y):
            print("两个数%s+%s=%s"%(x,y,target))
    #统计字典中的单词在指定字符串中的最长单词
    def  findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        #d=[]
        findWord=[]
        for x in d:
            if(self.isInWord(x,s)):
                findWord.append(x)
        lenList=[]
        for x in findWord:
            lenList.append(len(x))
        print(findWord[lenList.index(max(lenList))])
    def isInWord(self,distWord,words):
       # words=""
        for x in distWord:
            if(words.find(x)!=-1):
                words=words[words.find(x)+1:]
            else:
                return False
        return True
    #给定一个包含非负整数的数组，你的任务是统计其中可以组成三角形三条边的三元组个数，并输出
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums=[2, 2, 3, 4]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if(nums[i]+nums[j]>nums[k] and nums[j]+nums[k]>nums[i] and nums[k]+nums[i]>nums[j]):
                        print("%s %s %s"%(nums[i],nums[j],nums[k]))

    #城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。输入是建筑物轮廓用三元组表示[Li，Ri，Hi]
    def getSkyline(self, buildings=[[0,1,2]]):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        #buildings=[]
        #先计算横向坐标,最小、最大
        xMin=min(buildings)
        xMax=max(buildings)
        buildings.sort()
        mins=xMin[0:2]
        lrList=[]
        #计算横坐标的几个天际点
        for x in buildings[1:]: #以此比较横向各个坐标
            if(x[0]<mins[1]):
                mins=[mins[0],max(x[1],mins[1])]
            else:
                lrList.append(mins)
                mins=x[0:2]
        lrList.append(mins)

        hList=[]
        hPoint=[buildings[0][0],buildings[0][2]]
        hList.append(hPoint)
        for x in lrList:
            xPoint=[]
            for y in buildings:
                if(y[0]>=x[0] and y[0]<=x[1]):
                    xPoint.append([y[0],y[2]])
                    xPoint.append([y[1],y[2]])
            for x in xPoint:
                pass

        for x in buildings[1:]:
            if(x[2]>hPoint[1]):
                hList.append(hPoint)
                hList.append([x[0],hPoint[1]])


        print(lrList)

s = "abpcplea"
d = ["ale","apple","monkey","plea"]
nums=[ [2,9,10], [3,7,15], [5,12,12], [15,20,10], [19,24,8] ]
Solution().getSkyline(nums)