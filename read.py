'''import glob
from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    header = []
    rows = []
    with open(file, 'r', newline="") as csvfile:
        reader = csv.reader(csvfile)
        #header = next(reader)
    
        for row in reader:
            #or len(row) <= 3
            if "" in row:
                raise ValueError
                break
            else:
                rows.append(tuple(row))
                

    #print(rows)
    rows.pop(0)
    return rows

#p = Path("/Users/abel/Downloads/Lab2_StarterCode/marchsurvey.csv")     
    
    
#readFile(p)


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    
    v = Path.cwd().glob('*.csv')
    sportclubs = []
    sports_dict = {}
    err = ""
    with open("report.txt", 'w') as r, open("error_log.txt", 'w') as e:
        file_count = 0
        line_count = 0
    for csvfile in v:
        try:
            a = readFile(csvfile)
            sportclubs.append(a)
            file_count += 1
        except ValueError:
            if str(csvfile) != "survey_database.csv":
                e.write(str(csvfile.name) + "\n")
            continue

            #err += str(csvfile) + "\n"

    for club in sportclubs:
        for x in club:
            key = (x[0], x[1], x[2])
            if key not in sports_dict:
                sports_dict[key] = club
            
            for team in a:
                #print("this is team",team)
                toAppend = True
                line_count += 1
                #x = list(team)
                city = team[0]
                name = team[1]
                sport = team[2]
                #x = SportClub(city, name, sport)
                
                #print("this is team object", x)
                for club in sportclubs:
                    #print("this is club", club)
                    y = SportClub()
                    y.city = club[0]
                    y.name = club[1]
                    y.sport = club[2]
                    #print("this is object of club", y)
                    #y = list(club)
                    #if x[0] == y[0] and x[1] == y[1] and x[2] == y[2]:
                    if x.name == y.name and x.city == y.city and x.sport == y.sport:
                        #y[3] += 1
                        y.count += 1
                        #sportclubs.remove(y)
                        sportclubs.append(y)
                        toAppend = False
                        break
                if toAppend:
                    x = SportClub()
                    x.setCity(city)
                    x.setName(name)
                    x.setSport(sport)
                    x.count = 1
                    #print("this is x objects", x)
                    #x.pop()
                    #x.append(1)
                    #sportclubs.append(tuple(x))
                    sportclubs.append(x)
                

        except:
            err += str(csvfile) + "\n"
    #print(sportclubs)
   
    

   '''
    #with open("error_log.txt", 'w') as e:
        #err += str(csvfile) + "\n"
        #e.write(err)
        #e.close()

    #with open("report.txt", 'w') as r:
        #r.write("Number of files read: "+str(file_count)+"\n")
        #r.write("Number of lines read: "+str(line_count)+"\n")
        #r.close()



'''
                     

    #for 
    #for i in lst:
       # if " " not in i:
               
        
#readAllFiles()'''

        
'''
import glob
from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    header = []
    rows = []
    with open(file, 'r', newline="") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
   
        for row in reader:
            if "" in row or len(row) < 3:
                raise ValueError("File contains missing data")
            else:
                rows.append(tuple(row))
               

    rows.pop(0)
    return rows


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read.
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    v = glob.glob('*.csv')
    sportclubs = []
    err = ""
    file_count = 0
    line_count = 0
    for csvfile in v:
        try:
            a = readFile(csvfile)
            file_count += 1      
            for team in a:
                toAppend = True
                line_count += 1
                city = team[0]
                name = team[1]
                sport = team[2]
               
                for club in sportclubs:
                    if club.city == city and club.name == name and club.sport == sport:
                        club.count += 1
                        toAppend = False
                        break
                if toAppend:
                    x = SportClub(city, name, sport)
                    x.count = 1
                    sportclubs.append(x)
               
        except ValueError:
            err += str(csvfile) + "\n"
           
    with open("error_log.txt", 'w') as e:
        e.write(err)

    with open("report.txt", 'w') as r:
        r.write("Number of files read: "+str(file_count)+"\n")
        r.write("Number of lines read: "+str(line_count)+"\n")

    return sportclubs'''  





import glob
from pathlib import Path
import csv
from sportclub import SportClub
from typing import List, Tuple
from collections import Counter


def readFile(file: Path) -> List[Tuple[str, str, str]]:
    """Read a CSV file and return its content

    A good CSV file will have the header "City,Team Name,Sport" and appropriate content.

    Args:
        file: a path to the file to be read

    Returns:
        a list of tuples that each contain (city, name, sport) of the SportClub

    Raises:
        ValueError: if the reading csv has missing data (empty fields)  
    """
    # TODO: Complete the function
    header = []
    rows = []
    with open(file, 'r', newline="") as csvfile:
        reader = csv.reader(csvfile)
        #header = next(reader)
    
        for row in reader:
            #or len(row) <= 3
            if "" in row:
                raise ValueError
                break
            else:
                rows.append(tuple(row))
                

    #print(rows)
    rows.pop(0)
    return rows

#p = Path("/Users/abel/Downloads/Lab2_StarterCode/marchsurvey.csv")     
    
    
#readFile(p)


def readAllFiles() -> List[SportClub]:
    """Read all the csv files in the current working directory to create a list of SportClubs that contain unique SportClubs with their corresponding counts

    Take all the csv files in the current working directory, calls readFile(file) on each of them, and accumulates the data gathered into a list of SportClubs.
    Create a new file called "report.txt" in the current working directory containing the number of good files and good lines read. 
    Create a new file called "error_log.txt" in the current working directory containing the name of the error/bad files read.

    Returns:
        a list of unique SportClub objects with their respective counts
    """
    # TODO: Complete the function
    #a.setName[0]
    #a = SportsClub(i = [0], 
    
    v = glob.glob('*.csv')
    #print(v)
    sportclubs = []
    obj_list = []
    err = ""
    file_count = 0
    line_count = 0
    #error_file = open("error_log.txt", "w")
    report_file = open("report.txt", "w")
    for csvfile in v:
        #remove = 0
        if csvfile == "survey_database.csv":
            continue
        try:
            a = readFile(csvfile)
            file_count += 1      
            for team in a:
                sportclubs.append(team)
                #print(sportclubs)
                line_count += 1  # double check this
        except ValueError:
            error_file = open("error_log.txt", "w")
            #remove = 1
            err += str(csvfile) + "\n"
            error_file.write(err)
            error_file.close()


        #if remove == 0:
            #file_count += 1

    report_file.write("Number of files read: " + str(file_count) + "\n")
    report_file.write("Number of lines read: " + str(line_count) + "\n")
        
        
    #error_file.close()
    report_file.close()


    x = Counter(sportclubs)
    for team in x:
        objs = SportClub(team[0],team[1],team[2], x[team])
        #print(objs)
        obj_list.append(objs)

    #print(obj_list)

    return obj_list

#readAllFiles()
        
        
            
                
'''       #print("this is team",team)
                toAppend = True
                #x = list(team)
                city = str(team[0])
                name = str(team[1])
                sport = str(team[2])
                #print("these are the team values", city, name, sport)
                #x = SportClub(city, name, sport)
                
                #print("this is team object", x)
                for club in sportclubs:
                    #print("this is club", club)
                    #y = SportClub()
                    #y.city = club[0]
                    #y.name = club[1]
                    #y.sport = club[2]
                    #print("this is object of club", y)
                    #y = list(club)
                    if x[0] == y[0] and x[1] == y[1] and x[2] == y[2]:
                        x = SportClub()
                        x.city = city
                        x.name = name
                        x.sport = sport
                        sportclubs.append(tuple(x))
                        obj_list.append(x)
                        
                    #if x.name == y.name and x.city == y.city and x.sport == y.sport:
                        y[3] += 1
                        #y.count += 1
                        sportclubs.remove(y)
                        sportclubs.append(y)
                        toAppend = False
                        break
                if toAppend:
                    first = SportClub()
                    first.city = city
                    first.name = name
                    first.sport = sport
                    first.count = 1
                    #print("this is x objects", x)
                    x.pop()
                    x.append(1)
                    sportclubs.append(tuple(x))
                    obj_list.append(first)
                

        except:
            err += str(csvfile) + "\n"
    #print(sportclubs)
   
    

    with open("error_log.txt", 'w') as e:
        #err += str(csvfile) + "\n"
        e.write(err)
        e.close()

    with open("report.txt", 'w') as r:
        r.write("Number of files read: "+str(file_count)+"\n")
        r.write("Number of lines read: "+str(line_count)+"\n")
        r.close()
                     
    return obj_list
    #for 
    #for i in lst:
       # if " " not in i:
               
        
readAllFiles()'''
