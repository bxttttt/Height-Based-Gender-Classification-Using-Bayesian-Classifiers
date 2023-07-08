import numpy as np
import matplotlib.pyplot as plt

filename = "500_Person_Gender_Height_Weight_Index.csv"
# 读取数据
gender = []
# male  1
# female  0
height = []
weight = []
with open(filename, "r") as lines:
    for line in lines:
        line = line.split(",")
        print(line)
        j = 0
        for data in line:
            if j == 0:
                if data == "Female":
                    gender.append(0)
                elif data == "Gender":
                    break
                else:
                    gender.append(1)
                j += 1
            elif j == 1:
                height.append(int((int(data))/1))
                j += 1
            else:
                weight.append(int((int(data))/1))

print(gender)
print(height)
print(weight)
# 划分训练集和测试集
gender_training=[]
height_training=[]
weight_training=[]
gender_test=[]
height_test=[]
weight_test=[]
for i in range(len(gender)):
    if i<0.8*len(gender):
        gender_training.append(gender[i])
        height_training.append(height[i])
        weight_training.append(weight[i])
    else:
        gender_test.append(gender[i])
        height_test.append(height[i])
        weight_test.append(weight[i])
print(len(gender_training))
print(len(gender_test))
# 统计训练集中male、female的个数
label_prob = {}
for i in range(0, len(gender_training)):
    if gender_training[i] in label_prob:
        label_prob[gender_training[i]] += 1
    else:
        label_prob[gender_training[i]] = 1
print(label_prob)
print("女生总数：", label_prob[0])
print("男生总数：", label_prob[1])
print(label_prob.keys())
# 计算不同身高、体重的总数
count_height_training={}
for i in range(len(height_training)):
    if height_training[i] in count_height_training:
        count_height_training[height_training[i]]+=1
    else:
        count_height_training[height_training[i]]=1
print("计算不同身高的总数：")
print(count_height_training)
count_weight_training={}
for i in range(len(weight_training)):
    if weight_training[i] in count_weight_training:
        count_weight_training[weight_training[i]]+=1
    else:
        count_weight_training[weight_training[i]]=1
print("计算不同体重的总数：")
print(count_weight_training)
# 计算不同身高下，是女生的概率
height_female={}
for i in range(len(height_training)):
    if height_training[i] in height_female:
        if gender_training[i]==0:
            height_female[height_training[i]]+=1
    else:
        if gender_training[i]==1:
            height_female[height_training[i]]=0
        else:
            height_female[height_training[i]]=1
print("计算不同身高下，是女生的概率：")
print(height_female)
for key in height_female.keys():
    height_female[key]/=label_prob[0]
print(height_female)
# 计算不同身高下，是男生的概率
height_male={}
for i in range(len(height_training)):
    if height_training[i] in height_male:
        if gender_training[i]==1:
            height_male[height_training[i]]+=1
    else:
        if gender_training[i]==0:
            height_male[height_training[i]]=0
        else:
            height_male[height_training[i]]=1
print("计算不同身高下，是男生的概率：")
print(height_male)
for key in height_male.keys():
    height_male[key]/=label_prob[1]
print(height_male)
# 计算不同体重下，是女生的概率
weight_female={}
for i in range(len(weight_training)):
    if weight_training[i] in weight_female:
        if gender_training[i]==0:
            weight_female[weight_training[i]]+=1
    else:
        if gender_training[i]==1:
            weight_female[weight_training[i]]=0
        else:
            weight_female[weight_training[i]]=1
print("计算不同体重下，是女生的概率：")
print(weight_female)
for key in weight_female.keys():
    weight_female[key]/=label_prob[0]
print(weight_female)
# 计算不同体重下，是男生的概率
weight_male={}
for i in range(len(weight_training)):
    if weight_training[i] in weight_male:
        if gender_training[i]==1:
            weight_male[weight_training[i]]+=1
    else:
        if gender_training[i]==0:
            weight_male[weight_training[i]]=0
        else:
            weight_male[weight_training[i]]=1
print("计算不同体重下，是男生的概率：")
print(weight_male)
for key in weight_male.keys():
    weight_male[key]/=label_prob[1]
print(weight_male)
# 测试
predict=[]
# print(len(height_test))
# print(len(weight_test))
# print(len(gender_test))
for i in range(len(gender_test)):
    if weight_test[i] not in weight_male:
        weight_male[weight_test[i]]=0
    if weight_test[i] not in weight_female:
        weight_female[weight_test[i]] =0
    if height_test[i] not in height_male:
        height_male[height_test[i]]=0
    if height_test[i] not in height_female:
        height_female[height_test[i]]=0
    p_male=weight_male[weight_test[i]]*height_male[height_test[i]]*label_prob[1]/len(gender_test)
    p_female=weight_female[weight_test[i]]*height_female[height_test[i]]*label_prob[0]/len(gender_test)
    # print(p_male,p_female)
    if p_male>p_female:
        predict.append(1)
    else:
        predict.append(0)
        # print(predict)
print(predict)
print(gender_test)
count=0
for i in range(len(predict)):
    if predict[i]==gender_test[i]:
        count+=1
print("正确率：")
print(count/len(predict))

t_w=120
t_h=180
p_male=weight_male[t_w]*height_male[t_h]
p_female=weight_female[t_w]*height_female[t_h]
print("身高120，体重180：")
if p_male > p_female:
    print("male")
else:
    print("female")

