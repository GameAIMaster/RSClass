# 我有一份json文件，我希望帮我在所有的downLead对象下，随机抽取20%对象添加"labelShowOuter":"true",leadLineVisibleThreshold:"20",
# 再在剩余的中随机抽取5%加"labelShowOuter":"false",leadLineVisibleThreshold:"-9999"
#
import json
import random
def modify_json(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    #递归收集json中所有的downLead对象
    downLead = []
    def get_downLead(data):
        for key in data:
            if key == "downLead":
                downLead.append(data[key])
            elif isinstance(data[key], dict):
                get_downLead(data[key])
            elif isinstance(data[key], list):
                for item in data[key]:
                    if(isinstance(item, dict)):
                        get_downLead(item)


    # get_downLead(data)

    # 递归收集json中所有的hatch对象
    hatch = []
    def get_hatch(data):
        for key in data:
            if key == "hatch":
                hatch.append(data[key])
            elif isinstance(data[key], dict):
                get_hatch(data[key])
            elif isinstance(data[key], list):
                for item in data[key]:
                    if(isinstance(item, dict)):
                        get_hatch(item)

    get_hatch(data)
    # 对所有的hatch对象添加angle 和 ratio 属性，默认值都是为“-9999”
    for i in range(len(hatch)):
        if hatch[i] != None:
            hatch[i]["angle"] = "-9999"
            hatch[i]["ratio"] = "-9999"

    # for i in range(int(len(downLead)*0.2)):
    #     if downLead[i] != None:
    #         downLead[i]["downLeadPosition"] = "out"
    #         downLead[i]["downLeadThreshold"] = "20"
    # for i in range(int(len(downLead)*0.1)):
    #     if downLead[i] != None:
    #         downLead[i]["downLeadPosition"] = "in"
    #         downLead[i]["downLeadThreshold"] = "-9999"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

modify_json("E:\\pack\\WindowsNoEditor\\XR\\Content\\DBJCache\\Config.json")

