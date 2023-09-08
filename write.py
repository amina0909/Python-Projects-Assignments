import csv
from sportclub import SportClub
from typing import List, Iterable

def separateSports(all_clubs: List[SportClub]) -> Iterable[List[SportClub]]:
    """Separate a list of SportClubs into their own sports

    For example, given the list [SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA"), SportClub("LA", "Angels", "MLB")],
    return the iterable [[SportClub("LA", "Lakers", "NBA"), SportClub("Houston", "Rockets", "NBA")], [SportClub("LA", "Angels", "MLB")]]

    Args:
        all_clubs: A list of SportClubs that contain SportClubs of 1 or more sports.

    Returns:
        An iterable of lists of sportclubs that only contain clubs playing the same sport. 
    """
    
    
    # TODO: Complete the function
    separate_dict = {}
    '''dict is empty first. if key is not in dictionary add it to dict. initialize by setting it equal to 0. in first sublist add first sport.

'''
    final_list = []
    for club in all_clubs:
        if club.getSport() in separate_dict:
            final_list[separate_dict[club.getSport()]-1].append(club)
        else:
            separate_dict[club.getSport()] = len(final_list)+1
            final_list.append([club])

    #print(final_list)
    return final_list
    #return iterateSport(final_list)
            
#separateSports()
    
    
#separateSports([("LA", "Lakers", "NBA"), ("Houston", "Rockets", "NBA"), ("LA", "Angels", "MLB")])

def sortSport(sport: List[SportClub]) -> List[SportClub]:
    """Sort a list of SportClubs by the inverse of their count and their name

    For example, given the list [SportClub("Houston", "Rockets", "NBA", 80), SportClub("LA", "Warriors", "NBA", 130), SportClub("LA", "Lakers", "NBA", 130)] 
    return the list [SportClub("LA", "Lakers", "NBA", 130), SportClub("LA", "Warriors", "NBA", 130), SportClub("Houston", "Rockets", "NBA", 80)]

    Args:
        sport: A list of SportClubs that only contain clubs playing the same sport

    Returns:
        A sorted list of the SportClubs  
    """
    # TODO: Complete the function
    # hint: check documentation for sorting lists 
    # ( https://docs.python.org/3/library/functions.html#sorted , https://docs.python.org/3/howto/sorting.html#sortinghowto )
    
    #b = sorted(sport,key=lambda a:(-a[3],a[1]))

    b = sorted(sport,key=lambda a: (-a.count, a.name))

    #print(b)
    return b

#sortSport([("Houston", "Rockets", "NBA", 80), ("LA", "Warriors", "NBA", 130), ("LA", "Lakers", "NBA", 130)])


def outputSports(sorted_sports: Iterable[List[SportClub]]) -> None:
    """Create the output csv given an iterable of list of sorted clubs

    Create the csv "survey_database.csv" in the current working directory, and output the information:
    "City,Team Name,Sport,Number of Times Picked" for the top 3 teams in each sport.

    Args:
        sorted_sports: an Iterable of different sports, each already sorted correctly
    """
    # TODO: Complete the function

    #for sport in separateSport(all_clubs):
        #sortSport(sport)[0:2]
    #for sport in sorted_sports:
        #sport[0:2]
    #separateSports(sorted_sports)
        
    with open("survey_database.csv", 'w', newline='') as csvfile:
        header = ["City","Team Name","Sport","Number of Times Picked"]
        writer = csv.writer(csvfile)
        writer.writerow(header)
        
        for sport in sorted_sports:
            #print(sport)
            ranking_teams = 0
            #for team in sport:
            for team in sport:
                x = tuple(team)
                
                if ranking_teams < 3:
                    #info = [x.getCity(team[0]),x.getName(team[1]),x.getSport(team[2]),x.count()]
                    #print(info)
                    #print(info)
                    writer.writerow(x)
                    ranking_teams += 1
                else:
                    break
        #csvfile.close()
        


#outputSports()    
#outputSports(sorted_sports)
