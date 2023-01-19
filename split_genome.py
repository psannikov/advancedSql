f = open("/home/lesson/python/genome1", "r") #Читаем геном 1
genom1=f.read().replace('\n','')
f.close()
f = open("/home/lesson/python/genome2", "r") #Читаем геном 2
genom2=f.read().replace('\n','')
f.close()
k = 9 # определяем на сколько будем делить геном в задче это озвученок как последовательность символов-шинглов
genom_1 = [] #список для геном 1
genom_2 = [] #список для геном 2
for i in range(0,len(genom1)): #заполнение списка геном 1
    if i+k<len(genom1)+1:
        str_1 = ''
        for x in range (0,k):
            str_1 += genom1[i+x]
        genom_1.append(str_1)
for i in range(0,len(genom2)): #заполнение списка геном 2
    if i+k<len(genom2)+1:
        str_2 = ''
        for x in range (0,k):
            str_2 += genom2[i+x]
        genom_2.append(str_2)   
with open(r"/home/lesson/sql/insertAdditionalHW2.sql", "a", encoding="utf-8") as file: #заполняем файл инсерта, меняя k=[2,5,9] получаем необходимое разбиение генома
    file.write('insert into additionalHW2 (genome,split,data) values' + '\n')
    for i in range(0,len(genom_1)):
        insert_str = f'(\'genom1\',{k},\'{genom_1[i]}\'),'
        file.write(insert_str)  
    for i in range(0,len(genom_2)):
        insert_str = f'(\'genom2\',{k},\'{genom_2[i]}\')'
        if i == len(genom_2)-1:
            insert_str+=';\n'
        else:
            insert_str+=','
        file.write(insert_str)        