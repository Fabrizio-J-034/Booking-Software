import mysql.connector
con=mysql.connector.connect(host="localhost",username="root",password="root",database="vistara")
cur=con.cursor()
cur.execute("use vistara")
def schedule():
    
    cur.execute("create table flight(date varchar(20),time varchar(15),departureplace varchar(20),arrivalplace varchar(20),flightname varchar(20) primary key)")
    n=int(input("number of flights to schedule?"))


    for i in range(n):
        date=input("Date to schedule:")
        time=input("Time to schedule:")
        departure_place=input("place to departure:")
        arrival_place=input("place to reach:")
        flight_name=input("Name of flight:")
        List=(date,time,departure_place,arrival_place,flight_name)
        mean="INSERT INTO flight (date,time,departureplace,arrivalplace,flightname) VALUES(%s,%s,%s,%s,%s)"
        cur.execute(mean,List)
        con.commit()
        cur.execute("create table "+flight_name+"seats(row_no varchar(2),A varchar(2),B varchar(2),C varchar(2),D varchar(2),E varchar(2),F varchar(2),Class varchar(20))")
        con.commit()
        for i in range(1,10,1):
            row=str(i)
            Acol="O"
            Bcol="O"
            Ccol="O"
            Dcol="O"
            Ecol="-"
            Fcol="-"
            Class="Business"
            Del=(row,Acol,Bcol,Ccol,Dcol,Ecol,Fcol,Class)
            ins="insert into "+flight_name+"seats (row_no,A,B,C,D,E,F,Class) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(ins,Del)
            con.commit()

        for i in range(11,31,1):
            row=str(i)
            Acol="O"
            Bcol="O"
            Ccol="O"
            Dcol="O"
            Ecol="O"
            Fcol="O"
            Class="Economic"
            Del=(row,Acol,Bcol,Ccol,Dcol,Ecol,Fcol,Class)
            ins="insert into "+flight_name+"seats (row_no,A,B,C,D,E,F,Class) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(ins,Del)
            con.commit()



def cancel():
    L=input("press 'y' to cancel scheduled flights: ")
    if L=="y":
        cur.execute("SELECT COUNT(*) FROM flight")
        num=cur.fetchone()
        print("no of flights going to cancel are",num[0])
        cur.execute("select flightname from flight")
        for k in range(num[0]):
            dropflights=cur.fetchmany(num[0])
            strdrop=dropflights
            print(strdrop)
            for i in range(len(strdrop)):
                z=strdrop[i][0]+"seats"
                y=strdrop[i][0]
                cur.execute("drop table {}".format(z))
                con.commit()
                book=input("press 'y' to cancel booking table: ")
                if book=='y':
                    exe="drop table {}".format(y)
                    cur.execute(exe)
                    con.commit()

                else:
                    continue
        cur.execute("drop table flight")
        con.commit()
        print("successfully deleted")
        con.close()
    else:
        print("you have cancelled the deletion")


def booking():
    flt=input("Enter flight name:")
    sen="create table"+flt+"(S.NO integer,passenger varchar(20),adhaarnumber integer primary,seat varchar(5),date varchar(20),time varchar(5),departureplace varchar(20),arrivalplace varchar(20),age integer,type varchar(15))"
    cur.execute(sen)
    seat1=['1 A','1 B','1 C','1 D','2 A','2 B','2 C','2 D','3 A','3 B','3 C','3 D','4 A','4 B','4 C','4 D','5 A','5 B','5 C','5 D']
    seat2=['6 A','6 B','6 C','6 D','6 E','6 F','7 A','7 B','7 C','7 D','7 E','7 F','8 A','8 B','8 C','8 D','8 E','8 F','9 A','9 B','9 C','9 D','9 E','9 F','10 A','10 B','10 C','10 D','10 E','10 F']
    seat3=['11 A','11 B','11 C','11 D','11 E','11 F','12A','12 B','12 C','12 D','12 E','12 F','13 A','13 B','13 C','13 D','13 E','13 F','14 A','14 B','14 C','14 D','14 E','14 F','15 A','15 B','15 C','15 D','15 E','15 F']
    seat4=['16 A','16 B','16 C','16 D','16 E','16 F','17 A','17 B','17 C','17 D','17 E','17 F','18 A','18 B','18 C','18 D','18 E','18 F','19 A','19 B','19 C','19 D','19 E','19 F','20 A','20 B','20 C','20 D','20 E','20 F']
    seat5=['21 A','21 B','21 C','21 D','21 E','21 F','22 A','22 B','22 C','22 D','22 E','22 F','23 A','23 B','23 C','23 D','23 E','23 F','24 A','24 B','24 C','24 D','24 E','24 F','25 A','25 B','25 C','25 D','25 E','25 F']
    seat6=['26 A','26 B','26 C','26 D','26 E','26 F','27 A','27 B','27 C','27 D','27 E','27 F','28 A','28 B','28 C','28 D','28 E','28 F','29 A','29 B','29 C','29 D','29 E','29 F','30 A','30 B','30 C','30 D','30 E','30 F']

    def seatupdate():
        print("seat",seat,"is booked successfully")
        query="update "+flt+"seats SET "+col+"='X' where row_no='{}'".format(num)
        cur.execute(query)
        con.commit()
        ask=input("do you wish to see updated seat chart?(Y/N):")
        if ask=="Y" or ask=="y":
            sel="select * from "+flt+"seats"
            cur.execute(sel)
            data=cur.fetchall()
            for e in data:
                print(e)
        elif ask=="N" or ask=="n":
            return
        
    for i in range(170):
        still=input("would you like to close the counter?(Y/N)")

        if still=="N" or still=="n":
            
            Sno=1+i
            passenger=input("Enter passenger name:")
            adhaarNo=int(input("Enter Adhaar number:"))
            classchoose=input("select business or economic(E/B):")
            if classchoose=="B" or classchoose=="b":
                print("available seats are:-")
                print(seat1)
                seat=input("seat you would like to choose(format:(row number)(space)(column(caps)):")
                sdet=seat.split()
                print(sdet,seat1)
                num=str(sdet[0])
                col=str(sdet[1])
                print(str(num),col)
                
                if seat in seat1:
                    seat1.remove(seat)
                    seatupdate()

                elif seat not in seat1:

                    while True:
                        print("choose other than this seats",seat1)
                        seat=input("seat you would like to choose:")

                        if seat in seat1:
                            seat1.remove(seat)
                            seatupdate()
                
            
            elif classchoose=="E" or classchoose=="e":
                print("available seats are:-")
                print(seat2)
                print(seat3)
                print(seat4)
                print(seat5)
                print(seat6)
                seat=input("seat you would like to choose(format:(row number)(space)(column(caps))  ):")
                sdet=seat.split()
                num=sdet[0]
                col=sdet[1]
           
                if num in ('6','7','8','9','10'):

                    if seat in seat2:
                        seat2.remove(seat)  
                        seatupdate()

                    elif seat not in seat2:

                        while True:
                            print("choose other than this seats",seat2)
                            seat=input("seat you would like to choose:")

                            if seat in seat2:
                                seatupdate()

                elif num in ('11','12','13','14','15'):

                    if seat in seat3:
                        seat3.remove(seat)
                        seatupdate()

                    elif seat not in seat3:

                        while True:
                            print("choose other than this seats",seat3)
                            seat=input("seat you would like to choose:")

                            if seat in seat3:
                                seat3.remove(seat)
                                sseatupdate()

                        

                elif num in ('16','17','18','19','20'):
                    if seat in seat4:
                        seat4.remove(seat)
                        seatupdate()

                    elif seat not in seat4:

                        while True:
                            print("choose other than this seats",seat4)
                            seat=input("seat you would like to choose:")

                            if seat in seat4:
                                seat4.remove(seat)
                                seatupdate()

                elif num in ('21','22','23','24','25'):
                    if seat in seat5:
                        seat5.remove(seat)
                        seatupdate()

                    elif seat not in seat5:

                        while True:
                            print("choose other than this seats",seat5)
                            seat=input("seat you would like to choose:")

                            if seat in seat5:
                                seat5.remove(seat)
                                seatupdate()

                elif num in ('26','27','28','29','30'):
                    if seat in seat6:
                        seat6.remove(seat)
                        seatupdate()

                    elif seat not in seat6:

                        while True:
                            print("choose other than this seats",seat6)
                            seat=input("seat you would like to choose:")

                            if seat in seat6:
                                seat6.remove(seat)
                                seatupdate()
                else:
                    print("Error")


            cur.execute("select * from flight where flightname='{}'".format(flt))
            data=cur.fetchone()
            date=data[0]
            time=data[1]
            depature_place=data[2]
            arrival_place=data[3]
            age=input("Enter your age:")
            Type=input("Business or Economy")
            tuples=(Sno,passenger,adhaarNo,seat,date,time,depature_place,arrival_place,age,Type)
            string="insert into "+flt+" (SNO,passenger,adhaarnumber,seat,date,time,departureplace,arrivalplace,age,type) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(string,tuples)
            con.commit()
        else:
            break 
    print("seats are full")
        

def boarding():

    n=170
    for i in range(n):
        aadhar=int(input("Enter adhaar no:"))
        FNO=input("Enter flight no:")
        Query="select * from "+FNO+"where adhaarnumber='{}'".format(aadhar)
        cur.execute(Query)
        data=cur.fetchone()
        name=data[1]
        adhaarno=data[2]
        seat=data[3]
        age=data[8]
        Time=data[5]
        depature_place=data[6]
        arrival_place=data[7]
        class_type=data[9]
        print("Name:",name,"   ","adhaar no:",adhaarno,sep='')
        print("seat:",seat,"   ","age:",age,sep=' ')
        print("Time:",Time,"   ","class type:",class_type,sep=' ')
        print("departure:",depature_place,"   ","arrival:",arrival_place,sep=' ')
        n=n-1

        if n>=0:
            continue


        elif n==0:
            print("All passengers have received their boarding pass")


        else:
            print("Error:passenger count program error")