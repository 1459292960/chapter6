favorite_num={'pengbin':[3,6,9],'penghe':[0,5,7],
              'pengmengting':[9,3,0],
              'PengJiaJun':[5,6,7],'pengwei':[2,3,4]}
for name,nums in favorite_num.items():
    print(name+"'s favorite number are :")
    for num in nums:
        print('\t',num)