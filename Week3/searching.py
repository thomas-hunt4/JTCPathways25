# liner search


# import random 

# numbers = [5,2,3,1,4]
# target = random.randint(1,5)
# print(target)

## Coupon Code Problem

# list of valid coupon codes and the corresponding discount amounts (unsorted)
# gift_cards = [
#     {"code": "XFD890", "discount": 15},
#     {"code": "JLK321", "discount": 20},
#     {"code": "ABC123", "discount": 10},
#     {"code": "ZZZ999", "discount": 25}
# ]


# create a function that takes a coupon code and returns the discount amount or None if the code is not valid

# def check_coupon(coupon_code):
#     for card in gift_cards:
#         if card["code"] == coupon_code:
#             return card["discount"]
#     return None

# def check_coupon2(coupon_code):
#     return coupon_code in gift_cards


# linear search brute force auto comlete 

# with open("filename.") as file:
#     words = [line/strip() for line in file]


# prefix = input("Start typing...")

# results = []
# for word in words:
#     if word.startswith(prefix):
#         results.append(word)

# print(results)



# binary search

# left = 0
# right = len(words)

# full_word = ""
# first_match_idx = -1

# count = 0


# while left <= right:
#     mid = (left + right) // 2
#     if words [mid].startswith(prefix):
#         full_word = word[mid]
#         break
#     elif words[mid] < prefix:
#         left = mid + 1
#     else:
#         right = mid - 1




    


# user input coupon code
# coupon_code = input("Enter your coupon code: ")
# print(f"{check_coupon(coupon_code)}%")


# Binary Search Breakout Session

## Coupon Code Problem (Sorted List)

# list of valid coupon codes and the corresponding discount amounts (sorted by code)
gift_cards = [
    {"code": "ABC123", "discount": 10},
    {"code": "BXY456", "discount": 30},
    {"code": "CDE789", "discount": 12},
    {"code": "FGH012", "discount": 18},
    {"code": "IJK345", "discount": 22},
    {"code": "JLK321", "discount": 20},
    {"code": "MNO678", "discount": 28},
    {"code": "PQR901", "discount": 14},
    {"code": "STU234", "discount": 16},
    {"code": "VWX567", "discount": 24},
    {"code": "XFD890", "discount": 15},
    {"code": "YZA123", "discount": 19},
    {"code": "ZZZ999", "discount": 25}
]


# create a function that takes a coupon code and returns the discount amount or None if the code is not valid

def check_coupon_binary(coupon_code):
    left = 0
    right = len(gift_cards)

    
    while left <= right:
        mid = (left + right) // 2
        # mid_code = gift_cards[mid]['code']
        if gift_cards[mid]['code'] == coupon_code:
            return gift_cards[mid]['discount']
        elif gift_cards[mid]['code'] 
            left = mid + 1
        else:
            right = mid -1
        

    return None     
        





# user input coupon code
coupon_code = input("Enter your coupon code: ")
print(check_coupon_binary(gift_cards))
