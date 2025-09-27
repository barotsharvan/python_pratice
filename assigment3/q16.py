#Q16

print("Enter all registered voters (space):")
all_voters = input().split()
all_voters_set = set(all_voters)

print("Enter voters who voted (spaces):")
voted = input().split()
voted_set = set(voted)

absent_voters = all_voters_set - voted_set

print("\nVoters who didn't vote:")
for voter in absent_voters:
    print(voter)

turnout_percentage = (len(voted_set) / len(all_voters_set)) * 100
print(f"\nVoter turnout percentage: {turnout_percentage:.2f}%")
