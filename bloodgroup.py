class Blood:
    def __init__(self, bloodGroup, unitInHand):
        self.bloodGroup=bloodGroup
        self.unitInHand=unitInHand

class BloodBank:
    def __init__(self, bloodList):
        self.bloodList=bloodList
    def isBloodAvailable(self,bg,unit):
        for i in self.bloodList:
            if(i.bloodGroup==bg):
                if(unitInHand>=unit):
                    return True
                else:
                    return False
            else:
                return False
    def findMinBloodStock(self):
        min=99999999
        for i in self.bloodList:
            if(i.unitInHand<min):
                min=i.unitInHand
        for i in self.bloodList:
            if(i.unitInHand==min):
                print(i.bloodGroup)
if __name__=='__main__':
    bloodList=[]
    n=int(input())
    for i in range(n):
        bloodGroup=input()
        unitInHand=int(input())
        bloodObject=Blood(bloodGroup,unitInHand)
        bloodList.append(bloodObject)
    bloodBankObject=BloodBank(bloodList)
    bg=input()
    unit=int(input())
    state=bloodBankObject.isBloodAvailable(bg, unit)
    if state==True:
        print("Blood is available.")
    else:
        print("Blood not available.")
    bloodBankObject.findMinBloodStock()
