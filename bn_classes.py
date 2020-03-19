
def main(class_list):
    dic_class = []
    txt_file= open("new_class.txt","w")
    for i in class_list:
        if i in dic_class:
            continue
        else:
            dic_class.append(i)
            txt_file.write(i+"\n")
    txt_file.close()
    print(len(class_list))
    print(dic_class)

def class_list_function():
    PUNCHATION = ['।','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', ' ', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    SPACE = PUNCHATION+[" ",'্',"ি","ী","ু","ূ","ৃ","ৄ","ে","ৈ","ো","ৌ",'ঁ']
    NUMBER = ["০","১","২","৩","৪","৫","৬","৭","৮","৯"]
    SORBORNO = ["অ","আ","ই","ঈ","উ","ঊ","ঋ","এ","ঐ","ও","ঔ"]
    BENJONBORNO = ["ক","খ","গ","ঘ","ঙ","চ","ছ","জ","ঝ","ঞ","ট","ঠ","ড","ঢ","ণ","ত","থ","দ","ধ","ন","প","ফ","ব","ভ","ম","য","র","ল","শ","ষ","স","হ","ড়","ঢ়","য়"]
    SPETIAL = ["া"," ি"," ী"," ু"," ৃ"," ে"," ৈ"," ো"," ৌ"]
    SPETIAL1 = ["ৎ"," ং"," ঃ"," ঁ"," ্য","  ্র",]
    new_add = ['ক্ক', 'ক্ট', 'ক্ত', 'ক্ল', 'ক্ষ', 'ক্ষ্ণ', 'ক্ষ্ম', 'ক্স', 'খ', 'গ', 'গ্ধ', 'গ্ন', 'গ্ব', 'গ্ম', 'গ্ল', 'ঘ', 'ঘ্ন', 'ঙ', 'ঙ্ক', 'ঙ্ক্ত', 'ঙ্ক্ষ', 'ঙ্খ', 'ঙ্গ', 'ঙ্ঘ', 'চ', 'চ্চ', 'চ্ছ', 'চ্ছ্ব', 'ছ', 'জ', 'জ্জ', 'জ্জ্ব', 'জ্ঞ', 'জ্ব', 'ঝ', 'ঞ', 'ঞ্চ', 'ঞ্ছ', 'ঞ্জ', 'ট', 'ট্ট', 'ঠ', 'ড', 'ড্ড', 'ঢ', 'ণ', 'ণ্ট', 'ণ্ঠ', 'ণ্ড', 'ণ্ণ', 'ত', 'ত্ত', 'ত্ত্ব', 'ত্থ', 'ত্ন', 'ত্ব', 'ত্ম', 'থ', 'দ', 'দ্ঘ', 'দ্দ', 'দ্ধ', 'দ্ব', 'দ্ভ', 'দ্ম', 'ধ', 'ধ্ব', 'ন', 'ন্জ', 'ন্ট', 'ন্ঠ', 'ন্ড', 'ন্ত', 'ন্ত্ব', 'ন্থ', 'ন্দ', 'ন্দ্ব', 'ন্ধ', 'ন্ন', 'ন্ব', 'ন্ম', 'ন্স', 'প', 'প্ট', 'প্ত', 'প্ন', 'প্প', 'প্ল', 'প্স', 'ফ', 'ফ্ট', 'ফ্ফ', 'ফ্ল', 'ব', 'ব্জ', 'ব্দ', 'ব্ধ', 'ব্ব', 'ব্ল', 'ভ', 'ভ্ল', 'ম', 'ম্ন', 'ম্প', 'ম্ব', 'ম্ভ', 'ম্ম', 'ম্ল', 'য', 'র', 'ল', 'ল্ক', 'ল্গ', 'ল্ট', 'ল্ড', 'ল্প', 'ল্ব', 'ল্ম', 'ল্ল', 'শ', 'শ্চ', 'শ্ন', 'শ্ব', 'শ্ম', 'শ্ল', 'ষ', 'ষ্ক', 'ষ্ট', 'ষ্ঠ', 'ষ্ণ', 'ষ্প', 'ষ্ফ', 'ষ্ম', 'স', 'স্ক', 'স্ট', 'স্ত', 'স্থ', 'স্ন', 'স্প', 'স্ফ', 'স্ব', 'স্ম', 'স্ল', 'স্স', 'হ', 'হ্ন', 'হ্ব', 'হ্ম', 'হ্ল', 'ৎ', 'ড়', 'ঢ়', 'য়', '0', 'া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ', '0', 'ঁ', 'র্', 'র্য', '্য', '্র', '্র্য']


    GET_ALL_CLASSES = SPACE+NUMBER+SORBORNO+BENJONBORNO+SPETIAL+SPETIAL1+new_add
  
    return GET_ALL_CLASSES

if __name__=="__main__":
    all_list_cls= class_list_function()
    main(all_list_cls)

