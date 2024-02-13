import os


def PlaySound(path):
    os.system('clear')
    print("-------- 播放声音 --------")
    os.system('mplayer '+path+' < /dev/null > /dev/null 2>1&')

def PlayString(string):
    os.system('clear')
    print(">>>>>>>> "+string+" <<<<<<<<")

def Play(asset,assetType):
    playHandler=[PlaySound,PlayString]
    playHandler[assetType](asset)

class Card:
    def __init__(self,upsideAsset,upsideAssetType,downsideAsset,downsideAssetType):#Type 0 - Sound; 1 - String
        self.upside=(upsideAsset,upsideAssetType)
        self.downside=(downsideAsset,downsideAssetType)

    def run(self):
        Play(self.upside[0],self.upside[1])
        option=input("\n~~~~ 正面 ~~~~\n回车翻面")
        Play(self.downside[0],self.downside[1])
        option=input("\n~~~~ 卡背 ~~~~\n认识：A+回车\n不认识：回车")

        result=0
        if option!="":
            result=1

        return(result)


class CardNode:
    def __init__(self,card):
        self.card=card
        self.preNode=None
        self.nextNode=None
        self.nextSimilarNode=None

class CardNodeList:
    def __init__(self):
        self.head=None

    def insert(self,cardNode):#不安全头插，仅用于初始化链表
        cardNode.nextNode=self.head
        if self.head!=None:
            self.head.preNode=cardNode
        self.head=cardNode

    def delete(self,cardNode):#不安全删除
        if cardNode.nextNode!=None:
            cardNode.nextNode.preNode=cardNode.preNode

        if cardNode.preNode!=None:
            cardNode.preNode.nextNode=cardNode.nextNode
        else:
            self.head=cardNode.nextNode

    def deleteChain(self,cardNode):#不安全链式删除，递归删除cardNode及由cardNode的nextSimilarNode链接起来的子链
        if cardNode.nextSimilarNode!=None:
            self.deleteChain(cardNode.nextSimilarNode)

        cardNode.nextSimilarNode=None
        self.delete(cardNode)
        
    def insertByGap(self,cardNode,currentNode,gap):#不安全间隔插入，它会在currentNode的后方间隔gap长的位置上插入cardNode（gap==0意味着将成为currentNode的后继），如果链表不够长，那么则会在表尾插入；
        gapPointer=gap
        nodePointer=currentNode
        while(True):
            if gapPointer==0:break
            if nodePointer.nextNode==None:break

            gapPointer=gapPointer-1
            nodePointer=nodePointer.nextNode

        cardNode.preNode=nodePointer
        cardNode.nextNode=nodePointer.nextNode

        nodePointer.nextNode=cardNode
        if cardNode.nextNode!=None:
            cardNode.nextNode.preNode=cardNode
        
    def deleteHead(self,mode):#安全删除，当mode为1时仅删除表头，为0时对表头执行链式删除
        if mode==1:
            self.delete(self.head)
        elif mode==0:
            self.deleteChain(self.head)

