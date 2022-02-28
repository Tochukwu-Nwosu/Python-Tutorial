

# def square_root(number):
#     return number ** (0.5)

# print(square_root(4))

# x = lambda number: number ** (0.5)
# print(x(4))

# Example
# def check_length(username):
#     return len(username) > 7

# def check_upper_case(username):
#     for char in username:
#         if char.isupper():
#             return True
#     else:
#         return False

# def check_digits(username):
#     for digit in username:
#         if digit.isnumeric():
#             return True
#     else:
#         return False

# def parse_username(*usernames):                                       # Write it's lambda
#     accepted_usernames = [user for user in usernames if check_length(user) and check_upper_case(user) and check_digits(user)]
#     return accepted_usernames

# filter
# scores = [11,12,90,14,60,75]
# scores_above_50 = list(filter(lambda score: score > 50, scores))    # give the list comprehension version
# print(scores_above_50)

# Maps
# scores = [11,12,90,14,60,75]
# score_added_with_20 = list(map(lambda score: score + 20, scores))
# # score_added_with_20 = [score + 20 for score in scores]
# print(score_added_with_20)

# student_ids = [20,301,500,762]
# student_ids_complete = list(map(lambda id: f"HiiT-{id}", student_ids))
# student_ids_complete = [f"HiiT-{id}" for id in student_ids ]
# print(student_ids_complete)