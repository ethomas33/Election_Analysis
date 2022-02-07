# Import the datetime class from the datetime module. (module)
import datetime
# Use the now() attribute on the datetime class to get the present time. (class - date time variable - now)
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)


#____________________________________________________________________________________________


candidate_votes = int(input("How many votes did the candidate get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
message_to_candidate = (
    f"You recieved{candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}"
    f"You recieved{candidate_votes/total_votes:.2f}% of the total votes.")

print(message_to_candidate)

#_________________________________________________________________________________________

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#alternative

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#alternative

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")


#_________________________________________________________________________________________


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#print county+values
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#print county
for county_dict in voting_data:
    print(county_dict['county'])

#_________________________________________________________________________________________
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

