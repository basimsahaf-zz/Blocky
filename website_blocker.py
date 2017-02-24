""" This program is written by Basim Sahaf (c)
    Everyone can freely use this code.
    Proper credits must be given if commericially used."""



from datetime import datetime as dt  #imports datetime from computer

"""For this application, we will need to get access to the host file
which is usually in: /etc/hosts (for mac users)"""

host=r"hosts"  #create a backup host file in the working directory
host_file="/etc/hosts" #address of the main host file
redirect="127.0.0.1"   #local host address
website_list=[]        # add all the websites in this list as strings.
                       #For eg ["www.example1.com","www.example2.com"]

while True:

    """The below code has two conditions. The below conditions allow the program
        to run within a specific time limit which can be user-defined."""

    #checks if we are in the working time or not!
    if(dt(dt.now().year,dt.now().month,dt.now().day,00)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23)):
        #default time set is from 12:00 AM to 11:00PM during that day.
        #time can be changed according to preference.

        with open(host_file,'r+') as file:  #opens the host_file as file in Python
            content=file.read()  #reads the file contents
            for website in website_list:
                if website in content:  #if the website already exits, we don't need to add it, hence pass.
                    pass
                else:
                    file.write(redirect + " " + website + "\n") #writes the website into the host file.

    else:
        with open(host_file,'r+') as file:
            contents=file.readlines() #reads the file line by line and stores each line as an element in a list.
            file.seek(0)
            for i in contents:
                if not any(website in i for website in website_list):  #checks if the file has string website 
                                                                        #from website_list
                    file.write(i)
                else:
                    pass
                file.truncate()  #clears everything below the pointer.
