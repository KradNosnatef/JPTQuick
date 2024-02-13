from CardToolKits import Card,CardNode,CardNodeList
from HardCodedDB import Database
import time
import os

class Console:
    def __init__(self):

        self.cardNodeList=CardNodeList()
        self.database=Database()

        for tuple in self.database.db:
            card=Card(tuple[0],1,tuple[2],0)
            cardNode=CardNode(card)
            self.cardNodeList.insert(cardNode)

        for tuple in self.database.db:
            card=Card(tuple[1],1,tuple[2],0)
            cardNode=CardNode(card)
            self.cardNodeList.insert(cardNode)

        self.totalNum=2*len(self.database.db)
        self.count=0

    def run(self):
        option=input("按回车键开始任务")
        startTime=time.perf_counter()

        loopCount=0
        while(True):
            #入口检查
            if self.cardNodeList.head==None:break

            lastCardInChain=True#一致性上不安全的硬编码，临时措施
            if self.cardNodeList.head.nextSimilarNode!=None:
                lastCardInChain=False

            #运行表头卡
            result=self.cardNodeList.head.card.run()

            #按运行结果作出处理
            if result==1 and lastCardInChain==True:
                self.count=self.count+1
            
            if result==0:
                #执行红卡生成
                cardNode0=CardNode(Card(self.cardNodeList.head.card.upside[0],self.cardNodeList.head.card.upside[1],self.cardNodeList.head.card.downside[0],self.cardNodeList.head.card.downside[1]))
                cardNode1=CardNode(Card(self.cardNodeList.head.card.upside[0],self.cardNodeList.head.card.upside[1],self.cardNodeList.head.card.downside[0],self.cardNodeList.head.card.downside[1]))
                cardNode2=CardNode(Card(self.cardNodeList.head.card.upside[0],self.cardNodeList.head.card.upside[1],self.cardNodeList.head.card.downside[0],self.cardNodeList.head.card.downside[1]))
                cardNode3=CardNode(Card(self.cardNodeList.head.card.upside[0],self.cardNodeList.head.card.upside[1],self.cardNodeList.head.card.downside[0],self.cardNodeList.head.card.downside[1]))

                cardNode0.nextSimilarNode=cardNode1
                cardNode1.nextSimilarNode=cardNode2
                cardNode2.nextSimilarNode=cardNode3

                self.cardNodeList.insertByGap(cardNode0,self.cardNodeList.head,4)
                self.cardNodeList.insertByGap(cardNode1,cardNode0,8)
                self.cardNodeList.insertByGap(cardNode2,cardNode1,12)
                self.cardNodeList.insertByGap(cardNode3,cardNode2,16)

            #销毁旧表头
            self.cardNodeList.deleteHead(result)

            #处理数据展示页
            loopCount=loopCount+1
            if loopCount%10==0:
                os.system('clear')
                nowTime=time.perf_counter()
                passTime=(nowTime-startTime)/60
                print("完成数：{}/{}, 已用时间：{:.0f}, 完成数速率：{:.2f}".format(self.count,self.totalNum,passTime,self.count/passTime))
                input("按回车继续")