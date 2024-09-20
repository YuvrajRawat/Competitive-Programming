name = input("Enter your name : ").split()
class_ = int(input("Enter you class : "))
kbc = input("Do you want to Play KBC : ")

if kbc == 'yes':
    print("You are Playing KBC Now")
    print("You are Stage 1 ")
    first = int(input("1. who is the prime minister of india ?  \n\n1. Arvind Kejriwal    \n2. Amit Shah   \n3. Yogi   \n4. Narendra Modi  \nAns. "))
    if first == 4:
        print("WOW !!!! You are Right ")
        print("Next --->")
        second =int(input("2. what is oops language ?  \n\n1. Python    \n2. C   \n3. Selenium   \n4. R  \nAns. "))
        if second == 1:
            print("WOW !!!! You are Right \nNice !!!")
            print("\nNext --->")
            third = int(input("3. what is the color of buffalo ?  \n\n1. Blue    \n2. Black   \n3. Green   \n4. Red  \nAns. "))
            if third == 2:
                print("WOW !!!! You are Right \nYou are doing Great Yaaa")
                print("Next --->")
                fourth = int(input("3. what is the capital of West Bengal?  \n\n1. Delhi    \n2. Mumbai   \n3. Punjab   \n4. Kolkata  \nAns. "))
                if fourth == 4:
                    print("WOW !!!! You are Right")
                    print("Next --->")
                    fourth = int(input("3. what is the capital of West Bengal?  \n\n1. Delhi    \n2. Mumbai   \n3. Punjab   \n4. Kolkata  \nAns. "))
                else:
                    print("OHH NO !!! You are lose")
            else:
                print("OHH NO !!! You are lose")
        else:
             print("OHH NO !!! You are lose")
    else:
        print("OHH NO !!! You are lose")
else:
    print("Exit")

