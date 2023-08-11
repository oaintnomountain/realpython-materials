def print_three_members(member1, member2, member3, /):
    print(f"member1 is {member1}")
    print(f"member2 is {member2}")
    print(f"member3 is {member3}")


print_three_members("Frank", "Dean", "Sammy")

# This would be invalid:
# print_three_members(member1="Frank", member2="Sammy", member3="Dean")
# print_three_members("Frank", "Dean", member3="Sammy")
