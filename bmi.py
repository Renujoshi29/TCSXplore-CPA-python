class Person:
    def __init__(self, name, height, weight, bmi=0, bmi_status=" "):
        self.name=name
        self.height=height
        self.weight = weight
        self.bmi = bmi
        self.bmi_status = bmi_status

    def calculateBmi (self):
        self.bmi=round(self.weight/(self.height*self.height))

class Society:
    def __init__(self, bmi_status, person_list):
        self.bmi_status = bmi_status
        self.person_list = person_list
    def calculateBmiAndStatusByName(self, pName):
        state=False
        for i in self.person_list:
            if ((i.name).lower()==(pName).lower()):
                state=True
                i.calculateBmi()
                print(i.bmi,end=" ")
                for j in bmi_status.keys():
                    tup=self.bmi_status[j]
                    if(tup[0]<=i.bmi and tup[1]>=i.bmi):
                        i.bmi_status=j
                        print(j)
        return state
    def removelnvalidPersons(self, bmiVal):
        invalid=[]
        for i in self.person_list:
            i.calculateBmi()
            if (i.bmi<bmiVal):
                invalid.append(i)
        return invalid

if __name__ == '__main__':
    person_list = []
    n = int(input())
    for i in range(n):
        name = input()
        height = int(input())
        weight = int(input())
        personObject = Person(name, height, weight)
        person_list.append(personObject)
    b = int(input())
    bmi_status={}
    for j in range(b):
        key=input()
        l_bmi=int(input())
        u_bmi = int(input())
        if l_bmi>u_bmi:
            l_bmi,u_bmi=u_bmi,l_bmi
        bmi_status[key]=(l_bmi,u_bmi)

    societyObject = Society(bmi_status,person_list)
    pName=input()
    ans1=societyObject.calculateBmiAndStatusByName(pName)
    if ans1==False:
        print("No person exists")
    bmiVal=int(input())
    ans2=societyObject.removelnvalidPersons(bmiVal)
    for i in ans2:
        print("{} {} ".format(i.name,i.bmi))

