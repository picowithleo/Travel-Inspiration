"""
Assignment 1
CSSE 7030
Semester 1, 2019
Student ID: 45758106
"""

__author__ = "Jinyuan Chen"
__date__ = "22/03/2019"


from destinations import Destinations
def name() :
    """
    (str) A name input function

    Parameters:
        (str): Name of the user.
    """
    print("Welcome to Travel Inspiration!")
    user_input = str(input("\nWhat is your name? ", ))
    print("\nHi, ", user_input + "!", sep='')


def continent_input() :
    """
    (str) Return continents that user input

    Parameters:
        (str): Name of the continent
    """
    continent_d1 = {"1": "asia", "2": "africa", "3": "north america", "4": "south america", "5": "europe",
          "6": "oceania", "7": "antarctica"}
    print("\nWhich continents would you like to travel to?")

    for key in continent_d1:
        print('  ', key, ') ', continent_d1[key].title(), sep='')

    user_input = input("> ").replace(" ", "").split(",")
    continent_list = []
    for i in user_input:
        if i in continent_d1.keys():
            if i.isdigit() and int(i) in range (1, 8):
                continent_list.append(continent_d1[i])
            else:
                print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
                return False
        else:
            print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
            return False
    return continent_list


def cost_input() :
    """
    (str) Return the cost that user input

    Parameters:
        (str): level of the cost
    """
    cost = []
    cost_d2 = {"$$$": "No object", "$$": "Spendable, so long as I get value from doing so",
               "$": "Extremely important; I want to spend as little as possible"}
    print("\nWhat is money to you?")
    for key in cost_d2:
        print('  ', key, ') ', cost_d2[key], sep='')
    user_input = input("> ")
    if user_input == "$$$":
        cost = ["$$$", "$$", "$"]
    elif user_input == "$$":
        cost = ["$$", "$"]
    elif user_input == "$":
        cost = ["$"]
    if user_input in cost_d2.keys() :
        return cost
    else:
        print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
        return False



def crime_input() :
    """
    (str) Return the crime level that user input

    Parameters:
    (str) Level of the crime
    """
    crime = []
    crime_d3 = {"1": "Low", "2": "Average", "3": "High"}
    print("\nHow much crime is acceptable when you travel?")
    for key in crime_d3:
        print('  ', key, ') ', crime_d3[key], sep='')
    user_input = input("> ")
    if user_input == "1":
        crime = ["low"]
    elif user_input == "2":
        crime = ["low", "average"]
    elif user_input == "3":
        crime = ["low", "average", "high"]
    if user_input in crime_d3.keys() :
        return crime
    else:
        print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
        return False


def kids_input() :
    """
    (bool) Return the kids friendly level that user input
    Parameter:
    (bool) Level of the kids friendly
    """
    kids_d4 = {"1": "Yes", "2": "No"}
    print("\nWill you be travelling with children?")
    for key in kids_d4:
        print('  ', key, ') ', kids_d4[key], sep='')
    user_input = input("> ")
    if user_input in kids_d4.keys() :
        return kids_d4[user_input]
    else:
        print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
        return False


def season_input() :
    """

    :return:
    """
    season_d5 = {"1": "spring", "2": "summer", "3": "autumn", "4": "winter"}
    print("\nWhich seasons do you plan to travel in?")
    for key in season_d5:
        print('  ', key, ') ', season_d5[key].title(), sep='')

    user_input = input("> ")
    if user_input in season_d5.keys():
        return season_d5[user_input]
    else:
        print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
        return False


def climate_input() :
    """


    :return:
    """
    climate_d6 = {"1": "Cold", "2": "Cool", "3": "Moderate", "4": "Warm", "5": "Hot"}
    print("\nWhat climate do you prefer?")
    for key in climate_d6:
        print('  ', key, ') ', climate_d6[key], sep='')
    user_input = input("> ")
    if user_input in climate_d6.keys() :
        return climate_d6[user_input]
    else:
        print("\nI'm sorry, but", user_input, "is not a valid choice. Please try again.")
        return False



def first_exact_match(destination_set, continent, cost, crime, climate, kids) :
    """
    Match the each option
    :param destination_set:str
    :param continent:str
    :param cost:str
    :param crime:str
    :param climate:str
    :param kids:bool
    :return:
    """

    destination_result = []
    for destination in destination_set :
        if destination.get_continent() in continent :
            if len(destination.get_cost()) <= len(cost) :
                crime_d = {"low": 1, "average": 2, "high": 3}
                if crime_d[destination.get_crime()] <= len(crime) :
                    if destination.get_climate() == climate.lower() :
                        if kids == "1" :
                            if destination.is_kid_friendly() :
                                destination_result.append(destination)
                        else:
                            destination_result.append(destination)
    return destination_result


def season_interest_match(destination_set, season, sports, wildlife, nature, historical, cuisine, adventure, beach) :
    """
    Return the destination result
    Parameters:
    (str)
    """

    if len(destination_set) == 0 :
        return None
    destination_result = destination_set[0]
    max_factor = destination_set[0].get_season_factor(season.lower()) * \
                 calculation_interest_score(destination_set[0], sports, wildlife, nature, historical, cuisine, adventure, beach)
    for destination in destination_set :
        interest_score = calculation_interest_score(destination, sports, wildlife, nature, historical, cuisine, adventure, beach)
        if destination.get_season_factor(season.lower()) * interest_score > max_factor :
            max_factor = destination.get_season_factor(season.lower()) * interest_score
            destination_result = destination
    return destination_result


def calculation_interest_score(destination, sports, wildlife, nature, historical, cuisine, adventure, beach):
    """
    calculation of the interest score
    :param destination:
    :param sports:
    :param wildlife:
    :param nature:
    :param historical:
    :param cuisine:
    :param adventure:
    :param beach:
    :return:
    """

    return (sports * destination.get_interest_score('sports') +
            wildlife * destination.get_interest_score('wildlife') +
            nature * destination.get_interest_score('nature') +
            historical * destination.get_interest_score('historical') +
            cuisine * destination.get_interest_score('cuisine') +
            adventure * destination.get_interest_score('adventure') +
            beach * destination.get_interest_score('beach'))


def main():
    """
    collection of all functions
    :return:str
    """

    name()
    
    continent = continent_input()
    while continent is False :
        continent = continent_input()

    cost = cost_input()
    while cost is False :
        cost = cost_input()

    crime = crime_input()
    while crime is False :
        crime = crime_input()

    kids = kids_input()
    while kids is False :
        kids = kids_input()

    season = season_input()
    while season is False :
        season = season_input()

    climate = climate_input()
    while climate is False :
        climate = climate_input()

    print("\nNow we would like to ask you some questions about your interests, on a scale "
          "of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, "
          "and 0 indicates indifference.")

    while True :
        print("\nHow much do you like sports? (-5 to 5)")
        sports = input("> ")
        if sports in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"] :
            sports = int(sports)
            break
        else:
            print("\nI'm sorry, but", sports, "is not a valid choice. Please try again.")
    
    while True :
        print("\nHow much do you like wildlife? (-5 to 5)")
        wildlife = input("> ")
        if wildlife in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
            wildlife = int(wildlife)
            break
        else:
            print("\nI'm sorry, but", wildlife, "is not a valid choice. Please try again.")

    while True:
        print("\nHow much do you like nature? (-5 to 5)")
        nature = input("> ")
        if nature in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
            nature = int(nature)
            break
        else:
            print("\nI'm sorry, but", nature, "is not a valid choice. Please try again.")


    while True :
        print("\nHow much do you like historical sites? (-5 to 5)")
        historical = input("> ")
        if historical in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
            historical = int(historical)
            break
        else:
            print("\nI'm sorry, but", historical, "is not a valid choice. Please try again.")



    while True:
        print("\nHow much do you like fine dining? (-5 to 5)")
        cuisine = input("> ")
        if cuisine in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
            cuisine = int(cuisine)
            break
        else:
            print("\nI'm sorry, but", cuisine, "is not a valid choice. Please try again.")


    while True:
        print("\nHow much do you like adventure activities? (-5 to 5)")
        adventure = input("> ")
        if adventure in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
            adventure = int(adventure)
            break
        else:
            print("\nI'm sorry, but", adventure, "is not a valid choice. Please try again.")

    while True:
        print("\nHow much do you like the beach? (-5 to 5)")
        beach = input("> ")
        if beach in ["-5", "-4", "-3", "-2", "-1", "0", "1", "2", "3", "4", "5"]:
            beach = int(beach)
            break
        else:
            print("\nI'm sorry, but", beach, "is not a valid choice. Please try again.")


    destination_set = Destinations().get_all()


    first_exact_match_result = first_exact_match(destination_set, continent, cost, crime, climate, kids)


    final_result = season_interest_match(first_exact_match_result, season, sports, wildlife, nature, historical, cuisine, adventure, beach)


    print("\nThank you for answering all our questions. Your next travel destination is:")
    if final_result is None :
        print(None)
    else:
        print(final_result.get_name())

      
if __name__ == "__main__":
    main()
