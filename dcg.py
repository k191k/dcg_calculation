import math
from collections import Counter

input_data = []
result_dic = {}
dup_check_list = []

try:
    while True:
        strip_str = input().strip()
        input_data.append(strip_str.split(" "))
except EOFError:
    pass

for d in input_data:
    
    math_data = 0
    sort_data = []
    
    #真の評価値を高い順にソート
    d = list(map(int,d))
    
    for i in range(len(d)):
        #DCGを計算
        if i == 0:
            math_data += d[i]
            continue
        
        math_data += d[i] / (math.log2((i + 1) + 1))

    result_dic[len(result_dic)] = math_data
    dup_check_list.append(math_data)
    
#重複チェック
dup = sorted({i: dup_check_list.count(i) for i in set(dup_check_list)}.items())
dup_list = {}

for v, k in dup:
    if k > 1 :
        dup_list[k] = v

result = [0] * len(result_dic)
rank = 1

dup_rank = {}

for pos, math_result in sorted(result_dic.items(), key=lambda x: -x[1]):
    
    for d_count , d_item in dup_list.items():
        #重複する値の順位
        if d_item == math_result and math_result in dup_rank.keys() :
            result[pos] = dup_rank[math_result]
            break
        elif d_item == math_result:
            dup_rank[math_result] = rank + (d_count - 1)
            result[pos] = dup_rank[math_result]
            rank = dup_rank[math_result] + 1
            break
    #重複しない値の順位
    if result[pos] == 0:
        result[pos] = rank
        rank+= 1

for i in result:
    print(i)