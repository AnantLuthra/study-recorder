
def getdate():
    import datetime
    return datetime.datetime.now()

print("[This is a Study Recorder programme which recordes your study topics on various subjects.]")

try:
    while (True):
        opinion = input("For recording a record enter 1 and to look a record of any subject enter 2\n")
        if opinion == '2':
            print("Your subjects:-\n1: Accounts\n2: Economics\n3: Business Studies\n4: English\n5: Music")
            Rsubject = input("Enter the subject's number which you want to\nsee the topics which you have learn\n")
            if Rsubject == "1":
                print("You chosed 1 for Accounts")
                a = open("accounts.txt")
                data = a.read()
                print(data)
            elif Rsubject == "2":
                print("You chosed 2 for Economics")
                a = open("economics.txt")
                data = a.read()
                print(data)
            elif Rsubject == "3":
                print("You chosed 3 for Business Studies")
                a = open("business Studies.txt")
                data = a.read()
                print(data)
            elif Rsubject == "4":
                print("You chosed 4 for English")
                a = open("english.txt")
                data = a.read()
                print(data)
            elif Rsubject =='5':
                print("You chosed 5 for Music")
                a = open("Music.txt")
                data = a.read()
                print(data)
            else:
                print("Invalid input !!!")
            last = input("To record or look the previous study topics enter 1\nand to exit enter 2\n")
            if last == '1':
                continue
            elif last == '2':
                break
            else:
                print("Invalid input !!!")
        elif opinion == '1':
            print("!!! Warning you can record only one topic of any one subject at a time !!! ")
            print("Your subjects:-\n1: Accounts\n2: Economics\n3: Business Studies\n4: English\n5: Music")
            Wsubject = input("Enter the subject's number in which you want to record a topic which you have learn\n")
            if Wsubject == '1':
                print("You chosed 1 for Accounts")
                a = open("accounts.txt", "a")
                record = input("Now enter your topic\n")
                a.write(str([str(getdate())]) + ": " +record + "\n")
                a.close()
                print("[", getdate(), "]", "[", record, "]\nYour data is recorded successfully... ")
                # print("Your data is recorded successfully...")
            elif Wsubject == '2':
                print("You chosed 2 for Economics")
                a = open("Economics.txt", "a")
                record = input("Now enter your topic\n")
                a.write(str([str(getdate())]) +": " + record + "\n")
                a.close()
                print("[", getdate(), "]", "[", record, "]\nYour data is recorded successfully... ")
            elif Wsubject == '3':
                print("You chosed 3 for Business Studies")
                a = open("Business Studies.txt", "a")
                record = input("Now enter your topic\n")
                a.write(str([str(getdate())]) + ": " +record + "\n")
                a.close()
                print("[", getdate(), "]", "[", record, "]\nYour data is recorded successfully...")
            elif Wsubject == '4':
                print("You chosed 4 for English")
                a = open("English.txt", "a")
                record = input("Now enter your topic\n")
                a.write(str([str(getdate())]) +": " + record + "\n")
                a.close()
                print("[", getdate(), "]", "[", record, "]\nYour data is recorded successfully...")
            elif Wsubject == '5':
                print("You chosed 5 for Music")
                a = open("Music.txt", "a")
                record = input("Now enter your topic\n")
                a.write(str([str(getdate())]) +": " + record + "\n")
                a.close()
                print("[", getdate(), "]", "[", record, "]\nYour data is recorded successfully...")
            else:
                print("Invalid subject number entered !!!")
            last = input("To record or look the previous study topics enter 1\nand to exit enter 2\n")
            if last == '1':
                continue
            elif last == '2':
                break
            else:
                print("Invalid input !!!")
        else:
            print("Invalid input !!!")
except Exception as e:
    print(e)
