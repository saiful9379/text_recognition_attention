# from bn_classes import class_list_function
annot_path = "../raw_dataset/bn_annotation.txt"

# class_list = class_list_function()
new_cls_list = []
with open(annot_path,"r",encoding = 'utf-8') as file_:
    data = file_.read().split("\n")
    for i in data:
        for char in i.split(".png ")[-1]:
            if char == "\u200c" or char == "\u200d":
                continue
            if char not in new_cls_list:
                new_cls_list.append(char)
print(new_cls_list)
