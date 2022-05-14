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

# write your update damages function here:
#TODO: Write a function that returns a new list of updated damages where
# the recorded data is converted to float values and the missing data is retained as "Damages not recorded"
conversion = {"M": 1000000,
              "B": 1000000000}

# test function by updating damages
def convert_damages(damages):
  converted_damages = []
  for damage in damages:
    if damage == 'Damages not recorded':
      converted_damages.append('NA')
    elif damage[-1] == 'M':
      value = float(damage[:-1]) * conversion['M']
      converted_damages.append(value)
    else:
      value = float(damage[:-1]) * conversion['B']
      converted_damages.append(value)
  return converted_damages



# write your construct hurricane dictionary function here:
#TODO: Write a function that constructs a dictionary made out of the lists, where
# the keys of the dictionary are the names of the hurricanes,
# and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane
def construct_dict(names, months, years, max_sustained_winds, areas_affected, deaths):
  hurricanes_dict = {}
  keys = ['Names', 'Months', 'Years', 'Max_Sustained_Winds', 'Areas_Affected', 'Deaths']
  for i in range(len(names)):
    values = [names[i], months[i], years[i], max_sustained_winds[i], areas_affected[i] ,deaths[i]]
    hurricanes_dict[names[i]] = {key:value for key, value in zip(keys, values)}
  return hurricanes_dict

# Create and view the hurricanes dictionary
name_format_hurricanes = construct_dict(names, months, years, max_sustained_winds, areas_affected, deaths)
print(name_format_hurricanes.values())



# write your construct hurricane by year dictionary function here:
#TODO: Write a function that converts the current dictionary of hurricanes to a new dictionary, where
# the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.
def construct_dict_year(name_format_hurricanes, years):
    values = name_format_hurricanes.values()
    year_format_hurricanes = {}
    for i in range(len(years)):
        list_value = []
        for item in values:
            if years[i] == item['Years']:
                list_value.append(item)

        year_format_hurricanes[years[i]] = list_value
    return year_format_hurricanes


# create a new dictionary of hurricanes with year and key
year_format_hurricanes = construct_dict_year(name_format_hurricanes, years)
print("Year format")
print(year_format_hurricanes)


# write your count affected areas function here:
#TODO: Write a function that counts how often each area is listed as an affected area of a hurricane.
# Store and return the results in a dictionary where the keys are the affected areas and the values are
# counts of how many times the areas were affected
def count_damaged_areas(areas_affected):
  # flatten areas_affected into 1-D list
  new_format_areas_affected = []
  for item in areas_affected:
    for area in item:
      new_format_areas_affected.append(area)

  # counting
  areas = []
  for area in new_format_areas_affected:
    if area not in areas:
      areas.append(area)
  counting = []
  for area in areas:
    counting.append(new_format_areas_affected.count(area))

  counting_damaged_areas_dict = {key: value for key, value in zip(areas, counting)}
  return counting_damaged_areas_dict

# create dictionary of areas to store the number of hurricanes involved in
counting_damaged_areas_dict = count_damaged_areas(areas_affected)
print("Counting damaged areas")
print(counting_damaged_areas_dict)


# write your find most affected area function here:
#TODO: Write a function that finds the area affected by the most hurricanes, and how often it was hit.
def max_hurricane_counting(counting_damaged_areas_dict):
  # values list contain the amount of hurricanes in each area
  values = list(counting_damaged_areas_dict.values())
  keys = list(counting_damaged_areas_dict.keys())
  # find the maximum value in values
  max_value = max(values)
  max_list = []  # which contains areas with the most hurricanes
  for i in range(len(keys)):
    if values[i] == max_value:
      max_list.append(keys[i])

  return (max_list, max_value)

# find most frequently affected area and the number of hurricanes involved in
areas, max_value = max_hurricane_counting(counting_damaged_areas_dict)
print(f"The most frequently affected areas are {areas} and the number of hurricanes is {max_value}")


# write your greatest number of deaths function here:
#TODO: Write a function that finds the hurricane that caused the greatest number of deaths, and how many deaths it caused
def calculating_deadliest_hurricane(names, deaths):
  name_hurricanes = [] # because, it can be that several hurricanes with the same maximum deaths
  max_value = max(deaths)
  for i in range(len(names)):
    if deaths[i] == max_value:
      name_hurricanes.append(names[i])

  return name_hurricanes, max_value

# find highest mortality hurricane and the number of deaths
name_hurricanes, max_value = calculating_deadliest_hurricane(names, deaths)
print(f"The hurricanes which caused the greatest number of deaths are {name_hurricanes} and the number of deaths is {max_value}")


# write your catgeorize by mortality function here:
#TODO: Write a function that rates hurricanes on a mortality scale according to the following ratings,
# where the key is the rating and the value is the upper bound of deaths for that rating.
def rating_mortality(names, deaths):
  rating_mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5:[]}
  for i in range(len(names)):
    if deaths[i] == 0:
      rating_mortality_dict[0].append({names[i]: deaths[i]})
    elif deaths[i] < 100:
      rating_mortality_dict[1].append({names[i]: deaths[i]})
    elif deaths[i] < 500:
      rating_mortality_dict[2].append({names[i]: deaths[i]})
    elif deaths[i] < 1000:
      rating_mortality_dict[3].append({names[i]: deaths[i]})
    elif deaths[i] < 10000:
      rating_mortality_dict[4].append({names[i]: deaths[i]})
    else:
      rating_mortality_dict[5].append({names[i]: deaths[i]})
  return rating_mortality_dict

# categorize hurricanes in new dictionary with mortality severity as key
rating_mortality_dict = rating_mortality(names, deaths)
print(rating_mortality_dict)


# write your greatest damage function here:
#TODO: Write a function that finds the hurricane that caused the greatest damage, and how costly it was.
def greatest_damage(names, damages):
    converted_damages = convert_damages(damages)
    for i in range(len(damages)):
        if converted_damages[i] == 'NA':
            converted_damages[i] = 0.0

    greates_damage_hurricane = []
    greates_damage = max(converted_damages)
    for i in range(len(names)):
        if converted_damages[i] == greates_damage:
            greates_damage_hurricane.append(names[i])

    return greates_damage_hurricane, greates_damage


# find highest damage inducing hurricane and its total cost
greates_damage_hurricane, greates_damage = greatest_damage(names, damages)
print(f"The greates damage hurricane are {greates_damage_hurricane} with the amount of damage is {greates_damage}")

# write your catgeorize by damage function here:
#TODO: Write a function that rates hurricanes on a damage scale according to the following ratings,
# where the key is the rating and the value is the upper bound of damage for that rating.
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


# categorize hurricanes in new dictionary with damage severity as key
def scaling_damages(names, damages):
    # convert damages into a list of floating type
    converted_damages = convert_damages(damages)
    converted_damages_NA = converted_damages.copy()
    # if damage = 'NA', it equals to zero
    for i in range(len(damages)):
        if converted_damages_NA[i] == 'NA':
            converted_damages_NA[i] = 0
    # create a scaling_damages_dict
    scaling_damages_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for i in range(len(names)):
        if converted_damages_NA[i] == damage_scale[0]:
            scaling_damages_dict[0].append({names[i]: converted_damages[i]})
        elif converted_damages_NA[i] <= damage_scale[1]:
            scaling_damages_dict[1].append({names[i]: converted_damages[i]})
        elif converted_damages_NA[i] <= damage_scale[2]:
            scaling_damages_dict[2].append({names[i]: converted_damages[i]})
        elif converted_damages_NA[i] <= damage_scale[3]:
            scaling_damages_dict[3].append({names[i]: converted_damages[i]})
        elif converted_damages_NA[i] <= damage_scale[4]:
            scaling_damages_dict[4].append({names[i]: converted_damages[i]})
        else:
            scaling_damages_dict[5].append({names[i]: converted_damages[i]})

    return scaling_damages_dict


scaling_damages_dict = scaling_damages(names, damages)
print(scaling_damages_dict)
