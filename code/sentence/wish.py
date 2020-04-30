# import xml.dom.minidom
# Using ElementTree
import xml.etree.ElementTree as Et
import random


class Wish:
    doc = Et.parse("/Users/navkar14/Desktop/smart-learning/code/sentence/templates/exclamatory/wish-exclamatory.xml")
    # doc = Et.parse("C:\\Users\\payal\\Desktop\\Navkar\\Smart_Learning\\code\\sentence\\templates\\simple0.xml")
    root = doc.getroot()

    # print(root.tag)
    # print(root.attrib)
    # print(et.tostring(root, encoding='utf8').decode('utf8'))
    # print([elem.tag for elem in root.iter()])
    for sentence in root:
        arr0 = []
        arr1 = []
        gender_list = ["male", "female"]
        # print(sentence.tag)
        # print(sentence.attrib)
        # print()
        for phrase in sentence:
            # print(phrase.tag)
            # print(phrase.attrib)
            # print()

            if phrase.tag == "SUBJECTPHRASE":

                class0 = phrase.attrib
                # print(class0["TAG"])
                # print(type(class0))
                # class0["TAG"]
                noun_dict = open(
                    "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                    "/abstract.txt")
                f1 = noun_dict.readlines()
                # j=1
                for i in f1:
                    if i.find(class0["class"] + ":", 0) == 0:

                        # print(j)
                        # j+=1
                        temp = i.split(":")
                        temp.remove("\n")
                        # print(temp)
                        arr0.append(random.choice(temp[1:]))

                        arr0.append("\b,")
                        arr02 = arr0[:]
                        # print("arr0 is : ", arr0)
                        arr1.append(temp[0])
                        # print(arr0)
                        # print(arr1)
                        # break
            class0=phrase.attrib
            if phrase.tag == "SNOUN":
                if  class0["class"] == "name":
                    class0 = phrase.attrib
                    noun_dict = open(
                        "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                        "/proper_nouns.txt")

                    f1 = noun_dict.readlines()
                    for i in f1:
                        if i.find(class0["class"] + ":", 0) == 0:

                            if i.find(random.choice(gender_list), 0) >= 0:
                                # print(j)
                                # j+=1
                                temp = i.split(":")
                                temp.remove("\n")
                                # print(temp)
                                # print("arr0 is : ", arr0)
                                arr0.append(random.choice(temp[3:]))
                                arr01 = arr0[:]

                                arr0.append("\b!")
                                arr01.append("and")
                                t=random.choice(temp[3:])
                                # print(arr0)
                                # print(arr01)
                                while t == arr01[-2]:
                                    # print("inloop")
                                    t=random.choice(temp[3:])
                                arr01.append(t)
                                arr01.append("\b!")
                                arr1.append(temp[1])
                                # print(arr0)
                                # print(arr01)
                                # print(arr1)
                                listToStr0 = ' '.join(map(str, arr0))
                                listToStr01 = ' '.join(map(str, arr01))
                                print(listToStr0)
                                print(listToStr01)
                                break
                if class0["class"] == "wish-subject":
                    class0 = phrase.attrib
                    noun_dict = open(
                        "/Users/navkar14/Desktop/smart-learning/code/sentence/noun_dict"
                        "/abstract.txt")
                    f1 = noun_dict.readlines()
                    for i in f1:
                        if i.find(class0["class"] + ":", 0) == 0:
                            temp = i.split(":")
                            temp.remove("\n")
                            # print("arr02 is : ", arr02)
                            # print("temp is : ", temp)
                            arr02.append(random.choice(temp[1:]))
                            check_str=arr02[-1]
                            # print(check_str)
                            arr02.append("\b!")
                            # print("arr02 is : ", arr02)
                            # print(check_str.find("to"))
                            if check_str.find("to")>=0:
                                arr02.remove("\b,")
                            listToStr02 = ' '.join(map(str, arr02))
                            print(listToStr02)