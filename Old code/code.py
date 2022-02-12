# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]


#print county
# for county_dict in voting_data:
#     print(f"{county_dict['county']} has {county_dict['registered_voters']} votes")

my_list = [0,1,2,3,4,5]
list_within_a_list = [[0,1,2], [4,5,6]]
dict_within_list = [{"name":"Jon"},{"position":"worker"},{"hobby":"golfing"}]
                       

for item in dict_within_list:
    print(item[0]['name']) # expect to have 2 op: 0, 4
