def remove_whitespace_from_end_of_strings(list):
    i = 0
    while i < len(list):
        while string_ends_in_white_space(list[i]):
            list[i] = remove_final_char_from_string(list[i])
        i += 1

def string_ends_in_white_space(s):
    return type(s) == str and len(s) > 0 and (s[-1] == ' ' or s[-1] == '\t' or s[-1] == '\n')

def remove_final_char_from_string(s):
    return s[0:-1]

file = open("p_fav_foods.txt")
p_favs = file.readlines()
file.close()
remove_whitespace_from_end_of_strings(p_favs)

file = open("d_fav_foods.txt")
d_favs = file.readlines()
file.close()
remove_whitespace_from_end_of_strings(d_favs)

def compare_favs(favs1, favs2):
    if favs1[0] == favs2[0]:
        print "Our favs are the same!!!"
    else:
        print "our favez are different :("

def compare_favs2(favs1, favs2):
    for fav in favs1:
        if fav in favs2:
            print "We both love %s!" % fav
        
compare_favs(p_favs, d_favs)
compare_favs2(p_favs, d_favs)
