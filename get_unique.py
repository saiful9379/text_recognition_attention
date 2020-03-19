# from bn_classes import class_list_function
class_path = "new_class.txt"

annotation_path ="annotation_v1.0.txt"

new_cls_list = []
with open(class_path,"r",encoding = 'utf-8') as file_:
    data = file_.read().split("\n")
    for i in data:
        new_cls_list.append(i)

need_to_append = []
with open(annotation_path,"r",encoding = 'utf-8') as file_:
    data = file_.read().split("\n")
    for i in data:
        for char in i.split(".jpg ")[-1]:
            # print(char)
            if char not in new_cls_list:
                if char not in need_to_append:
                    need_to_append.append(char)

            # if char not in new_cls_list:
            #     new_cls_list.append(char)
print(new_cls_list)

print(need_to_append)
