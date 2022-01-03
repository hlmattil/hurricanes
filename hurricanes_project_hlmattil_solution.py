#This project uses data for several hurricanes and manipulates that data in
#several ways to derive insights from the data

#This project is from the Codecademy Data Science Career Path
#Completed by hlmattil on 2. Jan, 2022

# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]




#1. Updated damages function 
#Function that converts abbreviated damage values into floats

def damages_float(damages_list):
    damages_list_float = []
    for cost in damages:
        if cost == 'Damages not recorded':
            damages_list_float.append(cost)
        elif 'B' in cost:
            damages_list_float.append(float(cost.strip('B'))* 1000000000)
        elif 'M' in cost:
            damages_list_float.append(float(cost.strip('M'))*1000000)
    return damages_list_float   

damages_adjusted = damages_float(damages)





#2. Construct hurricane dictionary function 
#Takes a list of hurricanes and their data and turns them into a dictionary, where each 
#hurricane name is a key and the data for the hurricane is the value, stored as a dictionary

def create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_updated, deaths):
    dictionary_of_hurricanes = {}
    for i in range(len(names)):
        dictionary_of_hurricanes.update({names[i]: {'Name' : names[i], 
                                                    'Month': months[i], 
                                                    'Year': years[i], 
                                                    'Max Sustained Wind': max_sustained_winds[i], 
                                                    'Areas Affected': areas_affected[i], 
                                                    'Damage': damages_adjusted[i], 
                                                    'Deaths': deaths[i]
                                                   }})
    return dictionary_of_hurricanes

hurricanes = create_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages_adjusted, deaths)

        




#3. Construct hurricane by year dictionary function 
#Takes a dictionary of hurricanes and their data and converts it into a dictionary where the keys are 
#years and the values are hurricanes that occurred in those years.

def hurricane_years (hurricane_dictionary):
    hurricanes_by_year = {}
    for hurricane in hurricane_dictionary:
        if hurricane_dictionary[hurricane]["Year"] not in hurricanes_by_year:
            hurricanes_by_year.update({hurricane_dictionary[hurricane]["Year"]: [hurricane_dictionary[hurricane]]})
        elif hurricane_dictionary[hurricane]["Year"] in hurricanes_by_year:
            value = hurricane_dictionary[hurricane]["Year"]
            hurricanes_by_year[value].append(hurricane_dictionary[hurricane])
        
    return hurricanes_by_year
hurricanes_by_year = hurricane_years(hurricanes)




#4. Count affected areas function 
#counts how often each area is listed as an affected area of a hurricane. 
#Store and return the results in a dictionary where the keys are the affected areas 
#and the values are counts of how many times the areas were affected

def count_areas_affected(hurricane_dictionary):
    final_counted_areas = {}
    for hurricane in hurricane_dictionary:
        for area in hurricane_dictionary[hurricane]['Areas Affected']:
            if area not in final_counted_areas:
                final_counted_areas[area]= 1

            elif area in final_counted_areas:
                final_counted_areas[area] +=1
            
    return final_counted_areas

final_areas_affected_count = count_areas_affected(hurricanes)
                




#5. Find most affected area function 
# Finds the area affected by the most hurricanes and how often it was hit

def most_affected_areas(affected_areas_count):
    tuples_list = affected_areas_count.items()
    new_list = sorted(tuples_list, key=lambda hurricane: hurricane[1], reverse = True)
    max_hits = new_list[0][1]
    for hurricane in new_list:
        if hurricane[1] == max_hits:
            print(hurricane[0] + " " + str(hurricane[1]))
        else:
            continue
            
most_affected_areas(final_areas_affected_count)




#6. Greatest number of deaths function 
#Finds the hurricane that caused the greatest number of deaths
#and how many deaths it caused

def greatest_number_deaths(hurricane_dictionary):
    highest_deaths_hurricane = ''
    highest_death_count = 0
    for hurricane in hurricane_dictionary:
        if hurricane_dictionary[hurricane]["Deaths"] > highest_death_count:
            highest_deaths_hurricane = hurricane
            highest_death_count = hurricane_dictionary[hurricane]["Deaths"]
    return print(highest_deaths_hurricane + ' ' + str(highest_death_count))

greatest_number_deaths(hurricanes)        




#7 Catgeorize by mortality function 
#Rates hurricanes on a mortality scale

def death_scale(hurricane_dictionary):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    death_scale_dict = {0: [],
                   1: [],
                   2: [],
                   3: [],
                   4: [],
                   5: []
                        }
    for hurricane in hurricane_dictionary:
        num_deaths = hurricane_dictionary[hurricane]["Deaths"]
        if num_deaths == mortality_scale[0]:
            death_scale_dict[0].append(hurricane_dictionary[hurricane])
        elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
            death_scale_dict[1].append(hurricane_dictionary[hurricane])
        elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
            death_scale_dict[2].append(hurricane_dictionary[hurricane])
        elif num_deaths> mortality_scale[2] and num_deaths <= mortality_scale[3]:
            death_scale_dict[3].append(hurricane_dictionary[hurricane])
        elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
            death_scale_dict[4].append(hurricane_dictionary[hurricane])
        elif num_deaths > mortality_scale[4]:
            death_scale_dict[5].append(hurricane_dictionary[hurricane])
    return death_scale_dict

death_scale_final = death_scale(hurricanes)

print(death_scale_final[5])





#8. Greatest damage function 
# Finds the hurricane that caused the greatest damage and how costly it was

def most_damage(hurricane_dictionary):
    most_damage_hurricane = ""
    most_damage_value = 0
    for hurricane in hurricane_dictionary:
        if type(hurricane_dictionary[hurricane]["Damage"]) == str:
            continue
        elif hurricane_dictionary[hurricane]["Damage"] > most_damage_value:
            most_damage_value = hurricane_dictionary[hurricane]["Damage"] 
            most_damage_hurricane = hurricane
    return most_damage_hurricane, str(most_damage_value)

most_damageing_hurricane = most_damage(hurricanes)

print(most_damageing_hurricane[0], most_damageing_hurricane[1])




#9. Catgeorize by damage function 
#Rates hurricanes on a damage scale
def damage_rate(hurricane_dictionary):
    damage_scale = {
                0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    hurricanes_rated = {
                'Unknown': [],
                0: [],
                1: [],
                2: [],
                3: [],
                4: [],
                5: []}
    for hurricane in hurricane_dictionary:
        damage = hurricane_dictionary[hurricane]['Damage']
        hurricane = hurricane_dictionary[hurricane]
        if damage == 'Damages not recorded':
            hurricanes_rated['Unknown'].append(hurricane)
        elif damage >= damage_scale[0] and damage <= damage_scale[1] :
            hurricanes_rated[1].append(hurricane)
        elif damage > damage_scale[1] and damage <= damage_scale[2] :
            hurricanes_rated[2].append(hurricane)
        elif damage > damage_scale[2] and damage <= damage_scale[3] :
            hurricanes_rated[3].append(hurricane)
        elif damage > damage_scale[3] and damage <= damage_scale[4] :
            hurricanes_rated[4].append(hurricane)
        elif damage > damage_scale[4] :
            hurricanes_rated[5].append(hurricane)
    return hurricanes_rated

hurricane_damage_rate = damage_rate(hurricanes)

print(hurricane_damage_rate[5])




