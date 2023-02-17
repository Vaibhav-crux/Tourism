print("########################### WELCOME TO RANJEET TRAVELS###########################")
def options():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tGreat Summer Holidays Package")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Summer Holidays are")
    print("\t1.Rajasthan")
    print("\t2.Kochi")
    print("\t3.Manali")
    print("\t4.Goa")
    print("\t5.Kashmir")
    print("\t6.Exit")
    choice=input("Enter the place where you want to go ☺= ")
    while(choice.isdigit()==True):
        if(choice=="1"):
            Rajasthan()
            break
        elif(choice=="2"):
            Kochi()
        elif(choice=="3"):
            Manali()
        elif(choice=="4"):
            Goa()
        elif(choice=="5"):
            Kashmir()
        elif(choice=="6"):
            exit()
        else:
            print(choice,"is not in the option\nplease give the write input\n\n**********************")
            choice=input("Enter the place where you want to go ☺= ")
    while(choice.isdigit()!=True):
        print(choice,"is a alphabet which is not valid \nplease try again\n\n************************")
        choice=input("Enter the place where you want to go ☺= ")
def Rajasthan():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\t\tPopular Rajasthan Packages")    
    print("\t    Package Names\t\t\tPrice\t\t\tNight")    
    print("\t1.Contrasting Attractions\t\tRs 10,000\t\t4 Nights")    
    print("\t2.3 Beautiful Gems Of Rajasthan\t\tRs 22,600\t\t6 Nights")    
    print("\t3.Royalty Of Rajasthan\t\t\tRs 12,149\t\t4 Nights")    
    print("\t4.Boundless Rajasthan\t\t\tRs 34,002\t\t4 Nights")
    print("\n####################################################################################")
    packages=int(input("Enter the package you want to take = "))
    if(packages==1):
        print("You choosen \nContrasting Attractions\t\tRs 10,000\t\t4 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=\n\n\n")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=10000*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________
        
    if(packages==2):
        print("You choosen \n3 Beautiful Gems Of Rajasthan\t\tRs 22,600\t\t6 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=22600*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==3):
        print("You choosen \n3 Royalty Of Rajasthan\t\t\tRs 12,149\t\t4 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=12149*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==4):
        print("You choosen \n Boundless Rajasthan\t\t\tRs 34,002\t\t4 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=34002*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

def Kochi():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print("\t\t\tPopular Kochi Packages")
    print("\t    Package Names\t\t\tPrice\t\t\tNight")    
    print("\t1.Holidays In The Hills\t\tRs 14,899\t\t6 Nights")    
    print("\t2.Pleasant Coorg\t\tRs 55,712\t\t8 Nights")    
    print("\t3.Kerala's Best Splendours Of Nature\t\t\tRs 26,777\t\t6 Nights")    
    print("\t4.Serene Kovalam-Deluxe\t\t\tRs 20,559\t\t4 Nights")
    print("\n####################################################################################")
    packages=int(input("Enter the package you want to take = "))
    if(packages==1):
        print("You choosen \nHolidays In The Hills\t\tRs 14,899\t\t6 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=14899*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________
        
    if(packages==2):
        print("You choosen \nPleasant Coorg\t\tRs 55,712\t\t8 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=55712*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==3):
        print("You choosen \nKerala's Best Splendours Of Nature\t\t\tRs 26,777\t\t6 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=26777*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==4):
        print("Serene Kovalam-Deluxe\t\t\tRs 20,559\t\t4 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=20559*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

def Manali():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("\t\tPopular Manali Packages")    
    print("\t    Package Names\t\t\tPrice\t\t\tNight")    
    print("\t1.FabEscape Asia Holidays\t\tRs 1,026\t\t1 Nights")
    print("\t2.Sun Park Resort\t\tRs 1,113\t\t1 Nights")
    print("\t3.Snow Valley Resorts\t\t\tRs 2,057\t\t1 Nights")
    print("\t4.The Allure Grand\t\t\tRs 2,473\t\t1 Nights")
    print("\n####################################################################################")
    packages=int(input("Enter the package you want to take = "))
    if(packages==1):
        print("You choosen \nFabEscape Asia Holidays\t\tRs 1,026\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=1026*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________
        
    if(packages==2):
        print("You choosen \nSun Park Resort\t\tRs 1,113\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=1113*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==3):
        print("You choosen \nSnow Valley Resorts\t\t\tRs 2,057\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=2057*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==4):
        print("The Allure Grand\t\t\tRs 2,473\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=2473*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

def Goa():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print("\t\tPopular Manali Packages")  
    print("\t    Package Names\t\t\tPrice\t\t\tNight")
    print("\t1.FabEscape Asia Holidays\t\tRs 1,026\t\t1 Nights")
    print("\t2.Sun Park Resort\t\tRs 1,113\t\t1 Nights")
    print("\t3.Snow Valley Resorts\t\t\tRs 2,057\t\t1 Nights")
    print("\t4.The Allure Grand\t\t\tRs 2,473\t\t1 Nights")
    print("\n####################################################################################")
    packages=int(input("Enter the package you want to take = "))
    if(packages==1):
        print("You choosen \nFabEscape Asia Holidays\t\tRs 1,026\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=1026*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________
        
    if(packages==2):
        print("You choosen \nSun Park Resort\t\tRs 1,113\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=1113*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==3):
        print("You choosen \nSnow Valley Resorts\t\t\tRs 2,057\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=2057*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==4):
        print("The Allure Grand\t\t\tRs 2,473\t\t1 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=2473*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

def Kashmir():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")    
    print("\t\tPopular Kashmir Packages")
    print("\t    Package Names\t\t\tPrice\t\t\tNight")    
    print("\t1.Glorious Kashmir-Standard\t\tRs 16,788\t\t5 Nights")    
    print("\t2.Mesmerising Kashmir-Standard\t\tRs 38,136\t\t7 Nights")    
    print("\t3.Alluring Kashmir\t\t\tRs 11,500\t\t3 Nights")  
    print("\t4.Admirable Kashmir-Deluxe\t\t\tRs 32,688\t\t6 Nights")
    print("\n####################################################################################")
    packages=int(input("Enter the package you want to take = "))
    if(packages==1):
        print("You choosen \nGlorious Kashmir-Standard\t\tRs 16,788\t\t5 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=16788*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________
        
    if(packages==2):
        print("You choosen \nMesmerising Kashmir-Standard\t\tRs 38,136\t\t7 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=38136*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==3):
        print("You choosen \nAlluring Kashmir\t\t\tRs 11,500\t\t3 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=11500*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________

    if(packages==4):
        print("Admirable Kashmir-Deluxe\t\t\tRs 32,688\t\t6 Nights")
        total=int(input("Enter the total members which are going on tour ☺="))
        for i in range(total):
            print(i+1,"Details to fill")
            name=input("Enter the name = ")
            age=int(input("Enter the age = "))
            addhar=int(input("Enter your addhar number = "))
        start_days=input("Enter the date when have to go (DD/MM/YYYY) ☺=")
        end_days=input("Enter the last date (DD/MM/YYYY) ☺=")
    #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        amount=32688*total
        print("Total amount of",total,"person ☺= ",amount)
        print("=======================================================================================\n")
        print("\t\tTo take advance press 1\n\t\tTo pay full amount press 2")
        fee=int(input("Choose any one ☺= "))
        if(fee==1):
            give=int(input("Enter the advance amount to pay ☺= "))
            left=amount-give
            if(left<amount):
                print("you paid",give,"& to give later",left)
                print("---------------------------PENDING----------------------------\n\n")
                options()
            else:
                print("wrong input plese try again")
                options()
        elif(fee==2):
            print("You Paid",amount)
            options()
#______________________________________________________________________________________________________________________    
options()
