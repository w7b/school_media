def menu_p():
    while True:
        print(" - CALCULATE A SCHOOL MEDIA")
        print("[1] - Calculate your quarter media")
        print("[2] - Calculate your recuperation")
        print("[3] - Calculate your final media")
        print("[4] - End the program")

        select_p = input("\n - Select the option: ")

        if select_p == '1':
            sub_menu1()
        elif select_p == '2':
            sub_menu2()
        elif select_p == '3':
            sub_menu3()
        elif select_p == '4':
            print("Program ended!")
            break
        else:
            print("Error, this option is invalid")

def sub_menu1():
    while True:
        print("[1] Start Calc")
        print("[2] Return")

        select_a = input("\n - Select the option: ")
        if select_a == '1':
            av1 = float(input("Place your AV1 note: "))
            av2 = float(input("Place your AV2 note: "))
            trab = float(input("Place your Work note: "))
            mediaCalculator = float((av1 * 0.4 + av2 * 0.4 + trab * 0.2))
            if mediaCalculator >= float(59.6):
                    print(f"Good joob! You aproved: {mediaCalculator:.2f} media")
            else:
                print(f"You recovered with: {mediaCalculator:.2f} media")
        if select_a == '2':
            return

def sub_menu2():
    while True:
        a = 60
        print("[1] You have a recuperation note")
        print("[2] You havent a recuperation note")
        print("[3] Return")
        select_r = input("\n - Select the option: ")

        if select_r == '1':
            av1 = float(input("Place your AV1 note: "))
            av2 = float(input("Place your AV2 note: "))
            trab = float(input("Place your Work note: "))
            recnote = float(input("Place your Recuperation note: "))

            recCalc_s = float((av1 * 0.2 + av2 * 0.2 + recnote * 0.4 + trab * 0.2))
            if recCalc_s >= 60:
                print(f"You were left with: {recCalc_s:.2f} already with the recovery note")
            else:
                print(f"You got a red grade in the quarter, your quarterly grade was: {recCalc_s:.2f}")
            if recCalc_n != recCalc_s:
                print(f"You will need: {recCalc_n:.2f} to successfully pass a next quarter!")

        elif select_r == '2':
            av1 = float(input("Place your AV1 note: "))
            av2 = float(input("Place your AV2 note: "))
            trab = float(input("Place your Work note: "))
            recCalc_n = (a - (av1 * 0.2 + av2 * 0.2 + trab * 0.2)) / 0.4
            print(f"You need to take {recCalc_n:.2f} in recovery")
        elif select_r == '3':
            return
        else:
            print("Error, this option is invalid")

def sub_menu3():
    while True:
        a = 60
        print("[1] Start Calc")
        print("[2] Return")

        select_d = input("\n - Select the option: ")

        if select_d == '1':
            qa = float(input("Place your media in First Quarter: "))
            qb = float(input("Place your media in Second Quarter: "))
            qc = float(input("Place your media in Third Quarter: "))
            mAnnual = float ((qa * 0.3 + qb * 0.3 + qc * 0.4))
            print(f"Your media annual {mAnnual:.2f}")
        if select_d == '2':
            return
        

menu_p()