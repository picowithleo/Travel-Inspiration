"""
Assignment 1
CSSE1001/7030
Semester 1, 2019

"""

__author__ = "Jinyuan Chen"
__date__ = "22/03/2019"


from destinations import Destinations

def main():
    # Task 1: Ask questions here
    
    
    print("\nWelcome to Travel Inspiration!")
    name = str(input("\nWhat is your name? ", ))
    print("\nHi,",name+"!")
    
    print("\nWhich continent would you like to travel to?")
    print("  1) Asia\n  2) Africa\n  3) North America\n  4) South America\n  5) Europe\n  6) Oceania\n  7) Antarctica")
    choice1 =  input("> ")
    if choice1 == "1" :
        continent = "asia"
    elif choice1 == "2" :
        continent = "africa"
    elif choice1 == "3" :
        continent = "north america"
    elif choice1 == "4" :
        continent = "south america"
    elif choice1 == "5" :
        continent = "europe"
    elif choice1 == "6" :
        continent = "oceania"
    elif choice1 == "7" :
        continent = "antarctica"

    print("\nWhat is money to you?")
    print("  $$$) No object\n  $$) Spendable, so long as I get value from doing so\n  $) Extremely important; "
          "I want to spend as little as possible")
    choice2 = input("> ")
    if choice2 == "$$$" :
        cost = "$$$"
    elif choice2 == "$$" :
        cost = "$$"    
    elif choice2 == "$" :
        cost = "$"
    
    print("\nHow much crime is acceptable when you travel?")
    print("  1) Low\n  2) Average\n  3) High")
    choice3 = input("> ")
    if choice3 == "1" :
        crime = "low"
    elif choice3 == "2" :
        crime = "average"
    elif choice3 == "3" :
        crime = "high"    

    
    print("\nWill you be travelling with children?")
    print("  1) Yes\n  2) No")
    choice4 = input("> ")
    if choice4 == "1" :
        kids = True
    else:
        kids = False

    
    print("\nWhich season do you plan to travel in?")
    print("  1) Spring\n  2) Summer\n  3) Autumn\n  4) Winter")
    choice5 = input("> ")
    if choice5 == "1" :
         season_fator = "spring"
    elif choice5 == "2" :
         season_fator = "summer"
    elif choice5 == "3" :
         season_fator = "autumn"
    elif choice5 == "4" :
         season_fator = "winter"   
        

    print("\nWhat climate do you prefer?")
    print("  1) Cold\n  2) Cool\n  3) Moderate\n  4) Warm\n  5) Hot")
    choice6 = input("> ")
    if choice6 == "1" :
         climate = "cold"
    elif choice6 == "2" :
         climate = "cool"
    elif choice6 == "3" :
         climate = "moderate"
    elif choice6 == "4" :
         climate = "warm"   
    elif choice6 == "5" :
         climate = "hot"


    print("\nNow we would like to ask you some questions about your interests, on a scale " \
          "of -5 to 5. -5 indicates strong dislike, whereas 5 indicates strong interest, " \
          "and 0 indicates indifference.")
    print("\nHow much do you like sports? (-5 to 5)")
    interests1 = input("> ")
    
    
    print("\nHow much do you like wildlife? (-5 to 5)")
    interests2 = input("> ")

    
    print("\nHow much do you like nature? (-5 to 5)")
    interests3 = input("> ")

    
    print("\nHow much do you like historical sites? (-5 to 5)")
    interests4 = input("> ")

    
    print("\nHow much do you like fine dining? (-5 to 5)")
    interests5 = input("> ")

    
    print("\nHow much do you like adventure activities? (-5 to 5)")
    interests6 = input("> ")

    
    print("\nHow much do you like beach? (-5 to 5)")
    interests7 = input("> ")

    
    print("\nThank you for answering all our questions. Your next travel destination is:\n")
    

    for destination in Destinations().get_all():
        # Task 2+: Add comparison logic here
       if continent == destination.get_continent() :
           if len(cost) >= len(destination.get_cost()) :
               if crime >= destination.get_crime() :
                   if kids == destination.is_kid_friendly() :
                       if season_fator == destination.get_season_factor() :
                           if climate == destination.get_climate():
                               print(destination.get_name(),sep="")          


        season_fator == destination.get_season_factor(season_fator)

        score = season_factor * interest_score
        interest_score = response_sports * score_sports
                         + response_wildlife * score_wildlife
                         + response_nature * score_nature
                         + response_historical * score_historical
                         + response_cuisine * score_cuisine
                         + response_adventure * score_adventure
                         + response_beach * score_beach


             
        
      
if __name__ == "__main__":
    main()
