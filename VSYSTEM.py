#VOTING SYSTEM FOR STUDENTS COUNSELING SYSTEM

import os
from datetime import date
from datetime import datetime
import random

day=date.today()
now =datetime.now()
day = day.strftime("%B %d, %Y")

dtime = now.strftime("%H:%M:%S")

HeadBoyGirl=[] #Array storage for Headboys
hvcaptain=[]
dHeadBoyGirl=[]
volunteersnCMem=[]
proctor=[]
cservices=[]
regvoters=[]
pTags=['Name:','Grade:','Sec:','Symbol:']


while True:
 #os.system('clear')
 try:
    MENU='''
    1-HEADBOY           | 5-DEPUTY HEADBOY    |  9-PROCTOR
    2-HEADGIRL          | 6-DEPUTY HEADGIRL   | 10-COMMUNITY SERVICES
    3-HOUSE CAPTAIN     | 7-CAPTAIN VOLUNTEER | 11-LIST OF NOMINEES
    4-VICE CAPTAIN      | 8-COUNCIL MEMBER    | 12-REGISTER VOTER
    13-EXIT'''    

    print('======================================================================')
    print('                                M E N U                               ')
    print('======================================================================')
    print(MENU)
    print('                                                Date:', day)
    print('                                                Time:',dtime)

    print('======================================================================')
   
    choice=int(input('\t\tEnter your choice [1 to 13]: '))

    if choice==1:

     hbn=int(input('enter number of nominees for Head Boy: '))

     for i in range(1,hbn+1):

      while True:
       name=str(input('enter Head Boy name: '))
       if len(name)>10:
        print('Length must be with 10 characters!')
       else:
        break;
      HeadBoyGirl.append(name)
      grade=int(input('enter Grade : '))
      HeadBoyGirl.append(grade)  
      sec=str(input('enter section : '))
      HeadBoyGirl.append(sec)
      symbol=str(input('enter Campaign Symbol: '))
      HeadBoyGirl.append(symbol)
      print('\nRecord Added Successfully!')
      print('==========================')
      print('Name   : ',name)
      print('Grade  : ',grade)
      print('Section: ',sec)
      print('Symbol : ',symbol)
      print('==========================\n')

    elif choice==2:

     hgn=int(input('enter number of nominees for Head Girl: '))
     for i in range(1,hgn+1):
      name=str(input('enter Head Girl name: '))
      HeadBoyGirl.append(name)
      grade=int(input('enter Grade : '))
      HeadBoyGirl.append(grade)
      sec=str(input('enter section : '))
      HeadBoyGirl.append(sec)
      symbol=str(input('enter Campaign Symbol: '))
      HeadBoyGirl.append(symbol)

    elif choice==3:
     hc=int(input('enter number of nominees for House Captain: '))
     for i in range(1,hc+1):
      cname=str(input('enter Captain Name/s: '))
      hvcaptain.append(cname)
      grade=int(input('enter Grade : '))
      hvcaptain.append(grade)
      sec=str(input('enter section : '))
      hvcaptain.append(sec)
      symbol=str(input('enter Campaign Symbol: '))
      hvcaptain.append(symbol)

    elif choice==4:

     vc=int(input('enter number of nominees for Vice Captain: '))
     for i in range(1,vc+1):
      vname=str(input('enter Vice Captain Name/s: '))
      hvcaptain.append(vname)
      grade=int(input('enter Grade : '))
      hvcaptain.append(grade)
      sec=str(input('enter section : '))
      hvcaptain.append(sec)
      symbol=str(input('enter Campaign Symbol: '))
      hvcaptain.append(symbol)  
       
    elif choice==5:

     dhbn=int(input('enter number of nominees for Deputy Head Boy: '))

     for i in range(1,dhbn+1):
      name=str(input('enter Deputy Head Boy name: '))
      dHeadBoyGirl.append(name)
      grade=int(input('enter Grade : '))
      dHeadBoyGirl.append(grade)  
      sec=str(input('enter section : '))
      dHeadBoyGirl.append(sec)
      symbol=str(input('enter Campaign Symbol: '))
      dHeadBoyGirl.append(symbol)

    elif choice==6:


     hgn=int(input('enter number of nominees for Deputy Head Girl: '))
     for i in range(1,hgn+1):
      name=str(input('enter Deputy Head Girl name: '))
      dHeadBoyGirl.append(name)
      grade=int(input('enter Grade : '))
      dHeadBoyGirl.append(grade)
      sec=str(input('enter section : '))
      dHeadBoyGirl.append(sec)
      symbol=str(input('enter Campaign Symbol: '))
      dHeadBoyGirl.append(symbol)  

       
    elif choice==7:
     print('\n Volunteering For Captain')
     volc=int(input('enter number of nominees for Volunteering Captain: '))
     for i in range(1,volc+1):
      cname=str(input('enter Volunteer Name/s: '))
      volunteersnCMem.append(cname)
      grade=int(input('enter Grade : '))
      volunteersnCMem.append(grade)
      sec=str(input('enter section : '))
      volunteersnCMem.append(sec)
     
       
    elif choice==8:

     print('\n Register for Counsel Members')
     cm=int(input('enter number of nominees for Counselling Members: '))
     for i in range(1,cm+1):
      cname=str(input('enter Counselling Member Name/s: '))
      volunteersnCMem.append(cname)
      grade=int(input('enter Grade : '))
      volunteersnCMem.append(grade)
      sec=str(input('enter section : '))
      volunteersnCMem.append(sec)
     
    elif choice==9:
     print('\n Proctors')
     pro=int(input('enter number of nominees for Proctors: '))
     for i in range(1,pro+1):
      cname=str(input('enter Proctor Name/s: '))
      proctor.append(cname)
      grade=int(input('enter Grade : '))
      proctor.append(grade)
      sec=str(input('enter section : '))
      proctor.append(sec)
     



    elif choice==10:

     print('\n Community Services')
     pro=int(input('enter number of nominees for Community Services: '))
     for i in range(1,pro+1):
      cservname=str(input('enter Community Services: '))
      cservices.append(cservname)
      runby=int(input('enter Service Run by Grade : '))
      cservices.append(runby)
      roomname=str(input('enter Room Name : '))
      cservices.append(roomname)
      floor=int(input('enter Floor No: '))
      cservices.append(floor)

    elif choice==11:

     print(' 1- List of Head Boys')
     print(' 2- List of Head Girls')
     print(' 3- List of H.Captains')
     print(' 4- List of Vice Captains')
     print(' 5- List of Deputy Head Boys')
     print(' 6- List of Deputy Head Girls')
     print(' 7- List of Captain Volunteers')
     print(' 8- List of Counsel Members')
     print(' 9- List of Proctors')
     print('10- List of Community Services')
     print('11- List of Register Voters')
     plist=int(input('Enter your Choice: '))


     if plist==1:
        
        try:
          print("\n")
          print("Head Boys List")
          print("==============")
          print(*pTags,*HeadBoyGirl,sep="\n")
          print('---------------------') 
         
        except IndexError:
            print("There is an error, reading data from the fields. \nFailing to read from Arrays. \nRun option 1 first.\n")
   



        
        print('\n',HeadBoyGirl)
       
     elif plist==2:
        print('Head Girls List')
        print('==============')
        print('\n',HeadBoyGirl)

     elif plist==3:
        print('House Captains List')
        print('===================')
        print('\n',hvcaptain)
     elif plist==4:
        print('Vice Captains List')
        print('==================')
        print('\n',hvcaptain)
     elif plist==5:
        print('Deputy Head Boys List')
        print('=====================')
        print('\n',dHeadBoyGirl)
     elif plist==6:
        print('Deputy Head Girls List')
        print('======================')
        print('\n',dHeadBoyGirl)
     elif plist==7:
        print('Captain & Volunteer List')
        print('========================')
        print('\n',volunteersnCMem)
     elif plist==8:
        print('Counsel Member List')
        print('===================')
        print('\n',volunteersnCMem)
     elif plist==9:
        print('Proctors List')
        print('==============')
        print('\n',proctor)
     elif plist==10:
        print('Community Services List')
        print('=======================')
        print('\n',cservices)
     elif plist==11:
        print('Registered Voters List')
        print('======================')
        print('-----------------\n',*regvoters,sep='\n')
       
       
   
     else:
        print('Invalid Choice!')

    elif choice==12:
     print('\n Voter Registration')
     rv=int(input('enter number of voters to be registered: '))
     for i in range(1,rv+1):
      rvname=str(input('\nenter Voter Name: '))
      regvoters.append(rvname)
      grade=int(input('enter Voter Grade : '))
      regvoters.append(grade)
      sec=str(input('enter Section Name : '))
      regvoters.append(sec)
      voteid=(random.randint(1004,1501))
      regvoters.append(voteid)

      print('\nVoter Name: ',rvname)
      print('Grade     : ',grade)
      print('Section   : ',sec)
      print('Vote Id   : ',voteid)
      print('--------------------')

     

    elif choice==13:
     print('Thanks for using Students Counseling System!')
     exit(0)
    else:
     print('Invalid Choice, Choose from [1 to 13]')
 except ValueError:
     print('Options enteed must be integer/number!')
