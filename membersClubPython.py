class Member:
    def __init__ (self, name, age, netWorth, socialStatus):
        self.name = name
        self.age = age
        self.netWorth = netWorth
        self.socialStatus = socialStatus
    

    @staticmethod
    def gather_details():
        name = input("name: ")
        age = input("age: ")
        netWorth = input("netWorth: ")
        socialStatus = input("socialStatus: ")

        return Member(name, age, netWorth, socialStatus)

    def change_netWorth(self, change):
        self.netWorth = self.netWorth + change


membersList = []
membersList.append(Member("Jack", 24, 1000, "posho"))
membersList.append(Member("Dave", 21, 0.5, "drunk"))
membersList.append(Member("Byran", 41, 5000000000, "Elitist"))
membersList[1].change_netWorth(5)


nameOnList = False
response = input("What's your name?")

for item in membersList:
    if(item.name == response):
        nameOnList = True
        break
    else:
        nameOnList = False


if (nameOnList):
    print("OK, I see your name is on the list")
else:
    joinOrNo = input ("your name is not on the list, would you like to join our club?")

if (joinOrNo == "yeah"):
    membersList.append(Member.gather_details())
    print("Thanks, you are member number ", str(len(membersList)))
elif (joinOrNo == "nahhh"):
    print("Piss off then")
else:
    print("fack off") 


