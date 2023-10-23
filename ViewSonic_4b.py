def Sum(nums: [int]):
    zero = 0
    positive = []
    negative = []
    ans = []
    for i in nums:
        if i == 0:
            zero += 1
        elif i > 0:
            positive.append(i)
        else:
            negative.append(i)

    p = set(positive)
    n = set(negative)
    positive.sort()
    negative.sort()
    if zero > 0:
        for i in n:
            if abs(i) in p and [i,0,-i] not in ans:
                ans.append([i,0,-i])
        if zero > 2:
            ans.append([0,0,0])
    for i in range(len(negative)-1):
        j = i+1
        for j in range(j,len(negative)):
            sums = negative[i] + negative[j]
            if -sums in p and [negative[i], negative[j], -sums] not in ans:
                ans.append([negative[i], negative[j], -sums])
    for i in range(len(positive)-1):
        j = i+1
        for j in range(j,len(positive)):
            sums = positive[i] + positive[j]
            if -sums in n and [positive[i], positive[j], -sums] not in ans:
                ans.append([positive[i], positive[j], -sums])   
     
    return ans





if __name__ == '__main__':
    print('請輸入List，並以空白或逗號區隔：\nEx:0,1,1')
    nums = input()
    nums_list = list(map(int,nums.replace(',', ' ').split()))
    combinations = Sum(nums_list)
    if not combinations:
        print('三個數字相加不等於0')
    else:
        print(combinations)
