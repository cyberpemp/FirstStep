content = open('/mnt/d/pemp/lesson1/file.txt', 'r').read()


def improver(bad_string):
    improve_string = bad_string.split('|')

    # class1 = improve_string[0]
    # class2 = improve_string[1]
    # class3 = improve_string[2]
    class1, class2, class3 = improve_string

    # class1_name = class1.split('-')[0]
    # class2_name = class2.split('-')[0]
    # class3_name = class3.split('-')[0]
    
    # class1_kids = class1.split('-')[1]
    # class2_kids = class2.split('-')[1]
    # class3_kids = class3.split('-')[1]

    class1_name, class1_kids = class1.split('-')
    class2_name, class2_kids = class2.split('-')
    class3_name, class3_kids = class3.split('-')

    school_classes = {
        class1_name: class1_kids,
        class2_name: class2_kids,
        class3_name: class3_kids,
    }
    
    return school_classes


user_input = input('Your class: ')
school_classes = improver(content)

print(school_classes.get(user_input, 'No class'))
# if user_input in school_classes:
#     print(improver(content)[user_input])
# else:
#     print('no class')





# if user_input in school_classes:
#     print(improver(content)[user_input])
# else:
#     print("no such class")












    









