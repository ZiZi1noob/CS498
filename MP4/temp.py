temp = {111: 1684, 'new': 1077, 'county': 1020,  'list': 1948, 'school': 1065}
sorted_dic = sorted(temp.items(), key=lambda x: x[1], reverse=False)
#sorted_word_dict = sorted(dict(sorted_word_dict).items(), key=lambda x: x[0], reverse=False)
#temp.update({'tay':1})
print(type(list(temp.keys())[0]))