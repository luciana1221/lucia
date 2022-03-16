"""
File: node.py
链表操作
"""
#先定一个node的类
class Node():                  #value + next
    def __init__ (self, value = None, next = None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self,new_value):
        self._value = new_value

    def setNext(self,new_next):
        self._next = new_next

#实现Linked List及其各类操作方法
class LinkedList():
    def __init__(self):      #初始化链表为空表
        self._head = None 
        #self._tail = None
        self._length = 0
        self._k = 0

    def setk(self,k):
        self._k = k

    #检测是否为空
    def isEmpty(self):
        #print(self._head == None)
        return self._head == None

    #检测是否满了
    def isFull(self):
        return self._length >= self._k

    #获取最小（链表头）
    def getMin(self):
        current = self._head
        return current.getValue()

    #add在链表前端添加元素:O(1)
    def add(self,value):
        newnode = Node(value,None)    #create一个node（为了插进一个链表）
        newnode.setNext(self._head)   
        self._head = newnode
        self._length += 1

    #index索引元素在链表中的位置(D未满)
    def index(self,value):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue()==value:
                found = True
            else:
                current=current.getNext()
        if found:
            return count
        else:
            raise ValueError ('%s is not in linkedlist'%value)
    
    #index索引元素在链表中的位置（D满）
    def indexFull(self,value):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue()==value:
                found = True
            else:
                current=current.getNext()
        if found:
            self._head = current
            self._length -= count-1
        else:
            raise ValueError ('%s is not in linkedlist'%value)

    #未满不空的链表中插入元素(D)
    def insert(self,value):
        current = self._head
        #print(current.getValue())
        pre = current

        if value < current.getValue():
            self.add(value)
            return
        else:
            while current != None:
                #重复数据
                if current.getValue() == value:
                    return
                elif current.getValue() < value:
                    #继续向前查找
                    if current.getNext() != None:
                        pre = current
                        current = current.getNext()
                    #表尾插入
                    else:
                        temp = Node(value)
                        current.setNext(temp)
                        self._length += 1
                        return
                #插入
                else:
                    temp = Node(value,current)
                    #print(current.getValue())
                    pre.setNext(temp)
                    #print(pre.getValue())
                    pre = pre.getNext()
                    self._length += 1
                    return




    #满链表中插入元素(D)
    def insertFull(self,value):
        current = self._head
        #print(current.getValue())
        pre = current

        if value <= current.getValue():
            return
        else:
            while current != None:
                #重复数据
                if current.getValue() == value:
                    return
                elif current.getValue() < value:
                    #继续向前查找
                    if current.getNext() != None:
                        pre = current
                        current = current.getNext()
                    #表尾插入
                    else:
                        temp = Node(value)
                        current.setNext(temp)
                        self._head = self._head.getNext()
                        return
                #插入
                else:
                    temp = Node(value,current)
                    #print(current.getValue())
                    pre.setNext(temp)
                    #print(pre.getValue())
                    pre = pre.getNext()
                    self._head = self._head.getNext()
                    return



    #有重复值的插入(S)
    def insertS(self,value):
        current = self._head
        #print(current.getValue())
        pre = current

        if value <= current.getValue():
            self.add(value)
            return
        else:
            while current != None:
                
                if current.getValue() < value:
                    #继续向前查找
                    if current.getNext() != None:
                        pre = current
                        current = current.getNext()
                    #表尾插入
                    else:
                        temp = Node(value)
                        current.setNext(temp)
                        self._length += 1
                        return

                #插入
                else:
                    temp = Node(value,current)
                    #print(current.getValue())
                    pre.setNext(temp)
                    #print(pre.getValue())
                    pre = pre.getNext()
                    self._length += 1
                    return

    def printl(self):
        current = self._head
        print("链表为：", end = "")
        while current != None:          
            print(current.getValue(),end = " ")
            current = current.getNext()