class Member:
    def __init__(self, name, age, socialStatus, netWorth):
        self.name = name
        self.age = age
        self.socialStatus = socialStatus
        self.netWorth = netWorth
    
    @staticmethod
    def gather_details():

        name = input("Name: ")
        age = int(input("Age: "))
        socialStatus = input("Social Status: ")
        netWorth = int(input("Networth: "))

        return Member(name, age, socialStatus, netWorth)


membersList = []
membersList.append(Member("Jack", 24, "Middle Class", 100))
membersList.append(Member("Byran", 154, "Workin' Class", 1))
membersList.append(Member("Boris", 55, "Upper Class", 5000000000000))

noAccess = True

while(noAccess):
    print("Welcome to the members club. Is your name on the list or are you looking to become a new member?")
    try:
        response = input("Enter 'list' if you are on the list or 'new' if you want to become a member.\n").strip().lower()
    except:
        print("Piss off with your non-word answers")
        
    if(response == "list"):
        print("You're a member? We will see about that")
        name = input("tell me your name then\n").strip().title()
        onList = False

        for item in membersList:
            if(item.name == name):
                activeMember = item
                onList = True
        if(onList):
            print("Lovely, come on in {}".format(activeMember.name))
            print("Your current listed age is: {}".format(activeMember.age))
            print("Your social class is: {}".format(activeMember.socialStatus))
            print("Your net worth is currently: {}".format(activeMember.netWorth))
            if(activeMember.netWorth < 1000):
                print("My my... we are poor aren't we!")
            noAccess = False
        else:
            print("That name isn't on the list, identify yourself!")           
    elif(response == "new"):
        print("You want to join the member's club? Good for you :)")
        print("You will need to tell me a bit about yourself so I can add you")
        membersList.append(Member.gather_details())
    else:
        print("that wasnt an option, and now my robotic script will start again")


