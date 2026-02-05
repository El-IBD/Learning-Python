#ELVIS (DAVID) ETIM

#1. Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_numbers = [num for num in numbers if num <= 0]
print(filtered_numbers)


#2. Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list_of_lists = sum(list_of_lists, [])
print(flattened_list_of_lists)


#3. Using list comprehension create the following list of tuples
list_of_tuples = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)


#4.Flatten the following list to a new list
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries = [[country_name.upper(), country_name[0:3].upper(), city_name.upper()] for sublist in countries for country_name, city_name in sublist]
print(flattened_countries)


#5. Change the following list to a list of dictionaries
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dictionaries = [{'country': first.upper(), 'city': second.upper()} for sublist in countries for first, second in sublist]
print(list_of_dictionaries)

#6. Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [" ".join(n[0]) for n in names]
print(concatenated_names)
