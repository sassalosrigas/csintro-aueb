import calendar
import csv
import datetime


month_list=['ΙΑΝ','ΦΕΒ','ΜΑΡ','ΑΠΡ','ΜΑΙ','ΙΟΥΝ','ΙΟΥΛ','ΑΥΓ','ΣΕΠ','ΟΚΤ','ΝΟΕ','ΔΕΚ']

global place_holder
place_holder={}
#σημερινή ημερομηνία_________________________________________________________________________________________________________________________________________________________________________________________________
currentdate= datetime.date.today()
month=currentdate.month
year=currentdate.year


day=0
event=True
place_holder={}



#μια συνάρτηση η οποία θα βρίσκει τον αριθμό του εκάστοτε μήνα-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def find_month(month):
    """
    >>> find_month(5)
    ΜΑΙ
    >>> print(find_month(1))
    ΙΑΝ    
    """
    month_name = month_list[month-1]
    return month_name    
      

#calendar_header-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def change(month,year):
    """
    >>> change(1,2002)
    ____________________________________________________________________________

    IAN   2002

    ____________________________________________________________________________

        ΔΕΥ    |   ΤΡΙ    |    ΤΕΤ   |    ΠΕΜ   |    ΠΑΡ   |    ΣΑΒ   |    ΚΥΡ
     
    """
    print('____________________________________________________________________________\n')
    print(find_month(month),' ',year)
    print('\n____________________________________________________________________________\n')

    print('  ','ΔΕΥ ','  |',' ','ΤΡΙ ','  |','  ','ΤΕΤ ',' |','  ','ΠΕΜ ',' |','  ','ΠΑΡ ',' |','  ','ΣΑΒ ',' |','  ','ΚΥΡ')
    return ''

#μια σύναρτηση που φτιάχνει το αρχικό ημερολόγιο--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def create_calendar(year, month, event, day):
    """
    >>> create_calendar(2002,4,True,2)
    [[' ', ' ', 1], ['*', ' ', 2], [' ', ' ', 3], [' ', ' ', 4], [' ', ' ', 5], [' ', ' ', 6], [' ', ' ', 7], [' ', ' ', 8], [' ', ' ', 9], [' ', 1, 0], [' ', 1, 1], [' ', 1, 2], [' ', 1, 3], [' ', 1, 4], [' ', 1, 5], [' ', 1, 6], [' ', 1, 7], [' ', 1, 8], [' ', 1, 9], [' ', 2, 0], [' ', 2, 1], [' ', 2, 2], [' ', 2, 3], [' ', 2, 4], [' ', 2, 5], [' ', 2, 6], [' ', 2, 7], [' ', 2, 8], [' ', 2, 9], [' ', 3, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]
    >>> create_calendar(2002,2,True,2)
    [[' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0], [' ', ' ', 1], ['*', ' ', 2], [' ', ' ', 3], [' ', ' ', 4], [' ', ' ', 5], [' ', ' ', 6], [' ', ' ', 7], [' ', ' ', 8], [' ', ' ', 9], [' ', 1, 0], [' ', 1, 1], [' ', 1, 2], [' ', 1, 3], [' ', 1, 4], [' ', 1, 5], [' ', 1, 6], [' ', 1, 7], [' ', 1, 8], [' ', 1, 9], [' ', 2, 0], [' ', 2, 1], [' ', 2, 2], [' ', 2, 3], [' ', 2, 4], [' ', 2, 5], [' ', 2, 6], [' ', 2, 7], [' ', 2, 8], [' ', 0, 0], [' ', 0, 0], [' ', 0, 0]]
    """
#θεμέλια ημερολογίου_______________________________________________________________________________________________________________________________________________________________________________________________________________
    
    days_list=calendar.monthcalendar(year,month)
    starting_list=[]
    
    for i in range(int(len(days_list))*7): 
        starting_list.append([' ','',''])

    c=0
    for i in range(int(len(days_list))):
        
        week = days_list[i] #κάθε εβδομάδα μετατρέπεται σε ξεχωριστή λίστα
        
        for j in range(6):  #κάθε ημέρα της εβδομάδας i
            starting_list[c][2]=week[j]%10
            if (week[j]//10==0 and starting_list[c][2]!=0):
                starting_list[c][1]=' ' 
            else:
                starting_list[c][1]=week[j]//10
            c+=1
            if c==6 or c==13 or c==20 or c==27 or c==34:
                starting_list[c][1]=week[6]//10
                starting_list[c][2]=week[6]%10
                c+=1  
            
            if starting_list[13][1]==0 and starting_list[13][2]!=0:
                starting_list[13][1]=' '
            if starting_list[6][1]==0 and starting_list[6][2]!=0:
                starting_list[6][1]=' '

#προσθήκη και αφαίρεση γεγονότων___________________________________________________________________________________________________________________________________________________________________________________________________________
    days=calendar.monthrange(year,month)
    p=(month,year) #tuple που περιεχει τον τρέχον μήνα που επρόκειτο να επεξεργαστούμε
    if event==True : #σημαίνει πως θα γίνει προσθήκη γεγονότος
        key=False  # boolean

        for keys, values in place_holder.items():   #κάνει αναζήτηση στο dictionary ώστε να εντοπίσει αν έχουν καταχωρηθεί άλλα γεγονότα στον μήνα 
                if keys==p:
                    key=True
                    starting_list=values 
                    starting_list[(day-1)+days[0]][0]='*'
                    
                    place_holder.update({p:starting_list})   #κάνει update τη λίστα
        
        if key==False:
            
            starting_list[(day-1)+days[0]][0]='*'
            place_holder[p]=starting_list   #γίνεται νέα καταχώρηση στο dictionary

    if event==False: #σημαίνει πως θα γίνει διαγραφή γεγονότος

        key=False  # boolean
        for keys, values in place_holder.items():   #κάνει αναζήτηση στο dictionary ώστε να εντοπίσει αν έχουν καταχωρηθεί άλλα γεγονότα στον μήνα 
                if keys==p:     
        
                    key=True       #σημαίνει πως βρέθηκαν γεγονότα στον μήνα
                    starting_list=values
                    starting_list[(day-1)+days[0]][0]=' '
                    place_holder.update({p:starting_list})   #κάνει update τη λίστα

        if key==False:
                
                starting_list[(day-1)+days[0]][0]=' '
                place_holder[p]=starting_list  #γίνεται νέα καταχώρηση στο dictionary


    
    return starting_list

def print_calendar(hi, year, month):
    """
    >>> print_calendar(create_calendar(2002,4,True,2),2002,2)
      [   1 ] |  [ * 2 ] |  [   3 ] |  [   4 ] |  [   5 ] |  [   6 ] |  [   7 ] 

      [   8 ] |  [   9 ] |  [  10 ] |  [  11 ] |  [  12 ] |  [  13 ] |  [  14 ] 

      [  15 ] |  [  16 ] |  [  17 ] |  [  18 ] |  [  19 ] |  [  20 ] |  [  21 ] 

      [  22 ] |  [  23 ] |  [  24 ] |  [  25 ] |  [  26 ] |  [  27 ] |  [  28 ] 

      [  29 ] |  [  30 ] |        1 |        2 |        3 |        4 |        5 ''
    >>> print_calendar(create_calendar(2002,4,True,2),2002,10)
      [   1 ] |  [ * 2 ] |  [   3 ] |  [   4 ] |  [   5 ] |  [   6 ] |  [   7 ] 

      [   8 ] |  [   9 ] |  [  10 ] |  [  11 ] |  [  12 ] |  [  13 ] |  [  14 ] 

      [  15 ] |  [  16 ] |  [  17 ] |  [  18 ] |  [  19 ] |  [  20 ] |  [  21 ] 

      [  22 ] |  [  23 ] |  [  24 ] |  [  25 ] |  [  26 ] |  [  27 ] |  [  28 ] 

      [  29 ] |  [  30 ] |        1 |        2 |        3 |        4 |        5 ''
    """
    days=calendar.monthrange(year,month)
    days_list=calendar.monthcalendar(year,month)
    leftovers=[]
    for i in range(days[0]):
        leftovers.append(days[1]-i)
    #debug Φεβρουαριού
    if days[1]==28:
        leftovers.append(29)
        leftovers.append(31)
        leftovers.append(30)
    elif days[1]==29:
        leftovers.append(31)
        leftovers.append(30)

    leftovers=list(reversed(leftovers))

    #εκτυπώνει το ημερολόγιο χωρίς του υπολοίπου των προηγούμενων μηνών
    
    count1=0
    count2=0
    count3=1
    d=int(len(days_list))
    
    for i in range(d):
        liss=[]
        for j in range(7):
            
            liss.append(hi[count1])
            count1+=1
            
        for k in range(7):
            if i ==0 and k ==0:
                print(' ',end='')
            number=liss[k]
            
#___________το υπόλοιπο των ημερών του προηγούμενου/επόμενου________________________________________________________________________________________________________________________________________________           
            
            if number[1]==0 and number[2]==0 and i==0:      
                
                print('     ',leftovers[count2],'|', end=' ')
                count2+=1
            elif (number[1]==0 and number[2]==0) or (number[1]=='' and number[2]==''):
                
                if k<6: 
                    print('      ',count3,'|', end=' ')
                else:
                    
                    print('      ',count3, end=' ')
                count3+=1                
#__________________________________________________________________________________________________________________________________________________________________________________________________________                  
            else:
                number=''.join(str(i) for i in liss[k])
                if k<6:
                    
                    print('','[',number,']','|', end=' ')
                else:
                    
                    print('','[',number,']','\n\n', end=' ')

    
    return ''


#arxikopoihsh listwn
date_list= []
time_list= []
duration_list= []
title_list= []

create_calendar(year, 1, event, 1)


create_calendar(year, 2, event, 14)


create_calendar(year, 12, event, 25)


#loading pre-scheduled events from events.csv file
with open('events.csv', 'r') as csvfile:
    events_reader = csv.reader(csvfile)
    next(events_reader) #xwris thn prwth seira
    for row in events_reader:
        date_list.append(datetime.datetime.strptime(row[0], "%Y-%m-%d").date())
        time_list.append(datetime.datetime.strptime(row[1], "%H:%M:%S").time())
        duration_list.append(row[2])
        title_list.append(row[3])




#bonus 2: eidopoihseis gia shmerini mera
now= datetime.datetime.now()
current_date= now.date()
current_time= now.time()
flag=False #elegxei an yparxei estw kai ena gegonos shmera
for i in range(len(title_list)):
    if date_list[i] == current_date:
        event_time = datetime.datetime.combine(datetime.date.today(), time_list[i])
        time_dif= event_time - now
        print("Ειδοποίηση: σε",time_dif.seconds//3600,"ώρες και", time_dif.seconds%3600//60, "λεπτα από τώρα έχει προγραμματιστεί το γεγονός:", title_list[i])
        flag=True
if flag==False:
    print("Δεν υπάρχουν Προγραμματισμένα Γεγονότα Σήμερα.")

#αρχικό πριντ

print(change(month,year))
lis=create_calendar(year, month, event, day)
print(*print_calendar(lis, year, month))
print('\n____________________________________________________________________________\n')

#αρχή λειτουργιών

print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:\n\t"-" για πλοήγηση στον προηγούμενο μήνα\n\t"+" για διαχείριση των γεγονότων του ημερολογίου\n\t"*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')
answer= input('Επιλέξτε ενέργεια:')
while not answer=="q":
    if answer=="":
        if month==12:
            year+=1
            month=1
            print(change(month,year))
            lis=create_calendar(year, month, event, day)
            print(*print_calendar(lis, year, month))
            print('\n____________________________________________________________________________\n')
        else:
            month+=1
            print(change(month,year))
            lis=create_calendar(year, month, event, day)
            print(*print_calendar(lis, year, month))
            print('\n____________________________________________________________________________\n')
    elif answer=="-":
        if month==1:
            year=year-1
            month= 12
            print(change(month,year))
            lis=create_calendar(year, month, event, day)
            print(*print_calendar(lis, year, month))
            print('\n____________________________________________________________________________\n')
        else:
            month-=1
            print(change(month,year))
            lis=create_calendar(year, month, event, day)
            print(*print_calendar(lis, year, month))
            print('\n____________________________________________________________________________\n')

    elif answer=="+":
        year_to_return=year
        month_to_return=month
        print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:\n\t 1 Καταγραφή νέου γεγονότος\n\t 2 Διαγραφή γεγονότος\n\t 3 Ενημέρωση γεγονότος\n\t 0 Επιστροφή στο κυρίως μενού')
        answer2= int(input('Επιλέξτε ενέργεια:'))
        while not answer2==0:
            if answer2==1:
                #katagrafi gegonotos
                while True:
                    y=input("Εισάγετε Έτος:")
                    if y.isnumeric() and int(y)>2022:
                        y=int(y)
                        break
                    print("Λάθος Εισαγωγή.")
                while True:
                    m=input("Εισάγετε Μήνα:")
                    if m.isnumeric() and (int(m)>=1 and int(m)<=12):
                        m=int(m)
                        break
                    print("Λάθος Εισαγωγή.")
                while True:
                    d=input("Εισάγετε Μέρα:")
                    mrange= calendar.monthrange(y,m)[1]
                    if d.isnumeric() and (int(d)>=1 and int(d)<=mrange):
                        d=int(d)
                        break
                    print("Λάθος Εισαγωγή.")
                date= datetime.date(y,m,d)

                while True:
                    h=input("Εισάγετε Ώρα:")
                    if h.isnumeric() and (int(h)>=0 and int(h)<=23):
                        h=int(h)
                        break
                    print("Λάθος Εισαγωγή.")
                while True:
                    mi=input("Εισάγετε Λεπτά:")
                    if mi.isnumeric() and (int(mi)>=0 and int(mi)<=59):
                        mi=int(mi)
                        break
                    print("Λάθος Εισαγωγή.")
                time= datetime.time(h,mi)

                while True:
                    duration=input("Εισάγετε Διάρκεια:")
                    if duration.isnumeric() and int(duration)>0:
                        duration=int(duration)
                        break
                    print("Λάθος Εισαγωγή.")

                title= input("Εισάγετε Τίτλο:")
                title= title.replace(",","")
#Προσθήκη αστερίσκου στο ημερολόγιο_________________________________________________________________________________________________________________________________________________________________________________
                eve=True
               
                
                create_calendar(y, m, eve, d)
                
                

                date_list.append(date)
                time_list.append(time)
                duration_list.append(duration)
                title_list.append(title)
                
            elif answer2==2:
                #diagrafh gegonotos
                while True:
                    s_year=input("Εισάγετε Έτος:")
                    if s_year.isnumeric() and int(s_year)>2022:
                        s_year=int(s_year)
                        break
                    print("Λάθος Εισαγωγή.")
                while True:
                    s_month=input("Εισάγετε Μήνα:")
                    if s_month.isnumeric() and (int(s_month)>=1 and int(s_month)<=12):
                        s_month=int(s_month)
                        break
                    print("Λάθος Εισαγωγή.")
                c = 0
                event_indexes = []
                for i in range(len(title_list)):
                    if date_list[i].month == s_month and date_list[i].year == s_year:
                        event_indexes.append(i)
                        print(c, "-", title_list[i], date_list[i], time_list[i], duration_list[i])
                        c += 1

                if event_indexes!=[]:        
                    event_num = int(input("Εισάγετε αριθμό γεγονότος που θέλετε να διαγράψετε:"))                  
                    while event_num>c or event_num<0:            
                        print('Μη έγκυρη εισαγωγή.')
                        event_num = int(input("Εισάγετε αριθμό γεγονότος που θέλετε να διαγράψετε:"))
                    event_index = event_indexes[event_num]               
                #άμα υπάρχει το γεγονός τότε σβήνεται 
                    d=date_list[event_index].day
                    eve=False
               
                    create_calendar(s_year,s_month, eve, d)
                    
                    title_list.pop(event_index)
                    date_list.pop(event_index)
                    time_list.pop(event_index)
                    duration_list.pop(event_index)

                    print("\nΤο γεγονός διεγράφη")
                else:
                    print('Δεν υπάρχουν εγγεγραμμένα γεγονότα.')
                    
            elif answer2==3:
                #enhmerwsh gegonotos
                while True:
                    s_year=input("Εισάγετε Έτος:")
                    if s_year.isnumeric() and int(s_year)>2022:
                        s_year=int(s_year)
                        break
                    print("Λάθος Εισαγωγή.")
                while True:
                    s_month=input("Εισάγετε Μήνα:")
                    if s_month.isnumeric() and (int(s_month)>=1 and int(s_month)<=12):
                        s_month=int(s_month)
                        break
                    print("Λάθος Εισαγωγή.")
                c = 1
                event_indexes = []
                for i in range(len(title_list)):
                    if date_list[i].month == s_month and date_list[i].year == s_year:
                        event_indexes.append(i)
                        print(c, "-", title_list[i], date_list[i], time_list[i], duration_list[i])
                        c += 1

                if date_list!=[]:        
                    event_num = int(input("Επιλέξτε γεγονός προς ενημέρωση:"))
                    event_index = event_indexes[event_num-1]    
                    while event_num>c or event_num<1:            
                        print('Μη έγκυρη εισαγωγή.')
                        event_num = int(input("Επιλέξτε γεγονός προς ενημέρωση:"))

                    new_date = input(f"Ημερομηνία γεγονότος {str(date_list[event_index])}:")
                    if new_date:
                        date_list[event_index] = datetime.datetime.strptime(new_date, "%Y-%m-%d").date()
                    new_time = input(f"Ώρα γεγονότος {str(time_list[event_index])}:")
                    if new_time:
                        time_list[event_index] = datetime.datetime.strptime(new_time, "%H:%M").time()
                    new_duration = input(f"Διάρκεια γεγονότος {str(duration_list[event_index])}:")
                    if new_duration:
                        duration_list[event_index] = int(new_duration)
                    new_title = input(f"Τίτλος γεγονότος {title_list[event_index]}:")
                    if new_title:
                        title_list[event_index] = new_title
                    print(f"Το γεγονός ενημερώθηκε: <[{title_list[event_index]}] -> Date:{date_list[event_index]}, Time:{time_list[event_index]}, Duration:{duration_list[event_index]}>")
                    

            print('\nΔιαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:\n\t 1 Καταγραφή νέου γεγονότος\n\t 2 Διαγραφή γεγονότος\n\t 3 Ενημέρωση γεγονότος\n\t 0 Επιστροφή στο κυρίως μενού')
            answer2= int(input('Επιλέξτε ενέργεια:'))
        
        print(change(month_to_return, year_to_return))
        lis=create_calendar(year_to_return, month_to_return, event, day)
        print(*print_calendar(lis, year_to_return, month_to_return))
        print('\n____________________________________________________________________________\n')


    elif answer=="*":
        #emfanisi gegonoton
        print("=== Αναζήτηση γεγονότων ====")
        while True:
            s_year=input("Εισάγετε Έτος:")
            if s_year.isnumeric() and int(s_year)>2022:
                s_year=int(s_year)
                break
            print("Λάθος Εισαγωγή.")
        while True:
            s_month=input("Εισάγετε Μήνα:")
            if s_month.isnumeric() and (int(s_month)>=1 and int(s_month)<=12):
                s_month=int(s_month)
                break
            print("Λάθος Εισαγωγή.")
        c=0
        for i in range(len(title_list)):
            if date_list[i].month == s_month and date_list[i].year == s_year:
                c+=1
                print(c, title_list[i], date_list[i], time_list[i], duration_list[i])
        input("\nΠατήστε οποιοδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:")

    print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:\n\t"-"για πλοήγηση στον προηγούμενο μήνα\n\t"+" για διαχείριση των γεγονότων του ημερολογίου\n\t"*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')
    answer= input('Επιλέξτε ενέργεια:')

#transfer all data to the events.csv file
with open('events.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Date","Time","Duration","Title"])
    for i in range(len(title_list)):
        csvwriter.writerow([date_list[i], time_list[i], duration_list[i], title_list[i]])


