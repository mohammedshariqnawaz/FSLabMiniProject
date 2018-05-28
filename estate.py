import os
import pandas
import sys
# from text_file_indexer_demo import index_text_file
import time
data=[]
word_list=[]
class estateDetails:
    def __init__(self,estateName,estateAddress,estateSize,estatePrice,estateOwner,estateCondition):
        self.estateName=estateName
        self.estateAddress=estateAddress
        self.estateSize=estateSize
        self.estatePrice=estatePrice
        self.estateOwner=estateOwner
        self.estateCondition=estateCondition

    def display_data(self):
        print("\nESTATE NAME -"+self.estateName+"\nESTATE ADDRESS - "+self.estateAddress+"\nESTATE SIZE -"+self.estateSize+"\nESTATE PRICE - "+self.estatePrice+"\nESTATE OWNER -"+self.estateOwner+"\nESTATE CONDITION -"+self.estateCondition)
        #print(st)

    def pack(self,file):
        buf=self.estateName+"|"+self.estateAddress+"|"+self.estateSize+"|"+self.estatePrice+"|"+self.estateOwner+"|"+self.estateCondition+"|"
        buf+="\n"
        file.write(buf)

class index:
    def __init__(self,name):
        self.name=name

    def pack(self,file):
        buf1=self.name
        buf1+="\n"
        file.write(buf1)



def unpack():
    with open("fulldetails.txt","r") as fp:
        for line in fp:
            fields=line.strip('\n').split("|")[:-1]#[:-1] is needed to not include last | char
            s.append(estateDetails(fields[0],fields[1],fields[2],fields[3],fields[4],fields[5]))
    with open("index.txt","r") as fp:
        for line in fp:
            fields=line.strip('\n')#[:-1] is needed to not include last | char
            p.append(index(fields))


print("\n**************************WELCOME TO ESTATE PORTAL***************************")
print("\nENTER YOUR CHOICE")
while True:
    choice=input("1.Insert a record\n2.Search a record\n3.Modify a record\n4.Delete record\n5.Visualize\n6.Exit\n")
    if choice=="1":
        estateName=input("Enter Estate Name\n")
        estateAddress=input("Enter Estate Address\n")
        estateSize=input("Enter Estate Size\n")
        estatePrice=input("Enter Estate Price\n")
        estateOwner=input("Enter Estate Owner\n")
        estateCondition=input("Enter Estate Condition\n")
        temp=estateDetails(estateName,estateAddress,estateSize,estatePrice,estateOwner,estateCondition)
        with open("fulldetails.txt","a+") as fp:
            temp.pack(fp)

        txt_fil = open("fulldetails.txt", "r")

        words2=[]
        word_occurrences = {}
        line_num = 0

        for lin in txt_fil:
            line_num += 1
            words = lin.split('|')
            words2.append(words[0])
        fp=open("index.txt","w").close()
        for word in sorted(words2):
            temp1=index(word)
            with open("index.txt","a+") as fp:
                temp1.pack(fp)
        txt_fil.close()

    elif choice == "2":
        ts1 = time.time()
        print("Searching...")
        p=[]
        s=[]
        unpack()
        name_srch=input("Enter the Name to search and modify\n")
        flag=0
        with open("index.txt",'r') as fp2:
            for line in fp2:
                field=line.split("\n")[:-1]
                if name_srch==field[0]:
                    for x in s:
                    # field2=line1.split("|")[:-1]
                        if name_srch==x.estateName:
                            flag=1
                            print("Record found\n")
                            print(x.estateName+ "|" + x.estateAddress + "|" + x.estateSize + "|" + x.estatePrice +"|" + x.estateOwner+"|" + x.estateCondition + '\n')

    elif choice=="3":
        ts1 = time.time()
        print("Searching...")
        p=[]
        s=[]
        unpack()
        name_srch=input("Enter the Name to search and modify\n")
        flag=0
        with open("index.txt",'r') as fp2:
            for line in fp2:
                field=line.split("\n")[:-1]
                if name_srch==field[0]:
                    for x in s:
                    # field2=line1.split("|")[:-1]
                        if name_srch==x.estateName:
                            flag=1
                            print("Record found\n")
                            #print(x.estateName+ "|" + x.estateAddress + "|" + x.estateSize + "|" + x.estatePrice +"|" + x.estateOwner+"|" + x.estateCondition + '\n')
                            #print(x.estateSize)
                            #print(x.estatePrice)
                            #print(x.estateOwner)
                            #print(x.estateCondition)
                            ch=input("Select the field to modify\n1.Address\n2.Size\n3.Price\n4.Owner\n5.Condition\n")
                            if ch=="1":
                                newadd=input("Enter the new address\n")
                                x.estateAddress=newadd
                            elif ch=="2":
                                newsize=input("Enter the new size\n")
                                x.estateSize=newsize
                            elif ch=="3":
                                newprice=input("Enter the new price\n")
                                x.estatePrice=newprice
                            elif ch=="4":
                                newowner=input("Enter the new owner\n")
                                x.estateOwner=newowner
                            elif ch=="5":
                                newcond=input("Enter the new condition\n")
                                x.estateCondition=newcond
                            else:
                                print("invalid option")

        if flag==0:
            print("House does not exist")

        with open("fulldetails.txt","w+") as fp:
        #            fp.seek(0)
        #            fp.truncate()
            for x in s:
                x.pack(fp)
        ts2 = time.time()
        # print("difference = "+str(ts2-ts1))


    elif choice=="4":
        s=[]
        p=[]
        unpack()
        name_srch=input("Enter the Name of the house to be Deleted\n")
        flag=0
        with open("index.txt",'r') as fp2:
            for line in fp2:
                field=line.split("\n")[:-1]
                if name_srch==field[0]:
                    for x in s:
                    # field2=line1.split("|")[:-1]
                        if name_srch==x.estateName:
                            flag=1
                            print("Record found")
                            with open("fulldetailsdup.txt","w+") as fp:
                            #            fp.seek(0)
                            #            fp.truncate()
                                for x in s:
                                    if name_srch!=x.estateName:
                                        x.pack(fp)

                            with open("indexdup.txt","w+") as fp:
                            #            fp.seek(0)
                            #            fp.truncate()
                                for x in p:
                                    if name_srch!=x.name:
                                        x.pack(fp)

                            with open("fulldetailsdup.txt","r") as fp, open('fulldetails.txt', 'w') as fp1:
                                for line in fp:
                                    fp1.write(line)

                            with open("indexdup.txt","r") as fp, open('index.txt', 'w') as fp1:
                                for line in fp:
                                    fp1.write(line)

        if flag==0:
            print("House does not exist")


        # with open("fulldetailsdup.txt","w+") as fp:
        # #            fp.seek(0)
        # #            fp.truncate()
        #     for x in s:
        #         x.pack(fp)

    elif choice=="5":
        os.system("python mixvisualize.py")

    elif choice=="6":
        exit()

    else :
        print("Invalid print")
