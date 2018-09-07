import  datetime

class base1():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("base1 init")

    def m1(self):
        print("base1-m1:%s %s"%(self.x , self.y))


class child1(base1):
    def __int__(self):
        print("child1-init:default")
    def __init__(self,x,y):
        self.x=x
        self.y=y
        super(child1, self).__init__(x, y)
        print("child1 init")
    def m1(self):
        print("child1-m1:%s %s" % (self.x, self.y))
        super().m1()



class child2(child1):
    def __init__(self,x,y):
        self.x=x
        self.y=y
        #super(child2,self).__init__(x,y)
        super().__int__(                                                                  )
        print("child2 init")
    def m1(self):
        #super().m1()
        print("child2-m1:%s %s" %(self.x , self.y))

#mychild=child2(1,2)
#mychild.m1()

class B:
    def __init__(self):
        print("B init")
    def f(self):
        self.g()
    def g(self):
        print("b.g called")

class C(B):
    # def __init__(self):
    #     print("C init")
    def g(self):

        print("c.g called")
    @classmethod
    def num(cls):
        pass


class  myTime:
    def __init__(self,hours,minutes,secondes):
        try:
            self.mytime=datetime.time(hours,minutes,secondes)
            self.hour=hours
            self.minute=minutes
            self.second=secondes
        except:
            raise ValueError("时间错误！")
    def hours(self):
        return self.hour
    def minutes(self):
        return  self.minute
    def seconds(self):
        return  self.second
    def __add__(self, other):
        tmpsec=self.seconds()+other.seconds()
        tmpmin=tmpsec//60+self.minutes()+other.minutes()
        tmphour=(tmpmin//60+self.hours()+other.hours())%24
        tmpsec %= 60
        tmpmin %= 60
        return myTime(tmphour,tmpmin,tmpsec)
    def __str__(self):
        return "{:02}:{:02}:{:02}".format(self.hours(),self.minutes(),self.mytime.second)

mytime=myTime(5,23,2)
print(mytime)