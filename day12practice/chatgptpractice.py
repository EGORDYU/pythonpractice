# items = {'apple': 5, 'banana': 12, 'orange': 8, 'grape': 15, 'melon': 20}
# # Your code here to filter and sum values over $10


# def total_cost_over_10(items_dict):
#     return sum(price for item, price in items_dict.items())

# # Call the function and print the result
# print(total_cost_over_10(items))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# movies = {
#     'The Grand Adventure': (4.7, 150),
#     'Mystery of the Lost City': (3.9, 250),
#     'Superhero Chronicles': (4.5, 300),
#     'Love in the Mountains': (4.1, 100)
# }

# def average_rating(dict):
#     score = 0
#     adding = 0
#     for movie, (rating, reviews) in movies.items():
#         adding += reviews
#         score += rating*reviews
#         return score / adding
        

# print(average_rating(movies))
    

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# text = "it was the best of times it was the worst of times"
# text = text.lower()
# words =  text.split()
# # Your code here to count word frequencies

# def count_string(words_list):
#     word_counts = {}
#     for word in words_list:
#         if word in word_counts:
#             word_counts[word] += 1
#         else:
#             word_counts[word] = 1
#     return word_counts
    


# word_counts = count_string(words)
# print(word_counts)


diana_skins = {
    "bloodmoon": ("red", 7),
    "winterblessed": ("blue", 9),
    "darkwaters": ("darkblue", 8)
}


index_values = [diana_skins[name] for name in diana_skins]
print(index_values)


for skin, (color, rating) in diana_skins.items():
    print(f"The skin is {skin} the color is {color} and the rating is {rating}/10")