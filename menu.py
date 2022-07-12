
dict_menu={}

def input_menu(food):
    price = input("%s의 가격을 입력하세요: "%food)
    dict_menu[food]=price
    print("메뉴가 등록되었습니다.")

def update_menu():
    while True:
        food=input("음식 이름을 입력하세요 주문종료는 q : ")
        if food =='q':
            print("등록을 종료합니다.")
            break
        elif food not in dict_menu:
            input_menu(food)
        else:
            print("**이미 등록된 메뉴입니다.**\n"
                  "가격은 %s입니다." % dict_menu[food])

def mk_file():
    f=open("./act/mkmenu.txt",'w',encoding='utf-8')
    dict_k=dict_menu.keys()
    dict_v=dict_menu.values()
    book=''
    for k in dict_k:
        book+= k+','
    book+= ':'
    for v in dict_v:
        book+= v+','
    f.write(book)
    f.close()

def read_file():
    f=open("./act/mkmenu.txt",'r',encoding='utf-8')
    lines=f.readlines()
    if lines == []:
        return 0
    output=lines[0].split(':')
    dict_k=output[0].split(',')[:-1]
    dict_v=output[1].split(',')[:-1]

    option=dict(zip(dict_k,dict_v))
    for item in list(option.items()):
        k,v = item
        dict_menu[k]=v
        return list(dict_v)
    print(list(dict_v))

def input_order():
    list_menu=[]
    while True:
        food=input("\n주문하세요: 주문완료는 q입력  ")
        if food =='q':
            break
        elif food not in dict_menu:
            print("%s는 저희 가게에 없는 메뉴입니다."%food)
        elif food in dict_menu:
            list_menu.append(dict_menu[food])
        else:
            pass
    bills(list_menu)

def bills(list_menu):
    total=0
    for i in range(len(list_menu)):
        total+=int(list_menu[i])

    money = int(input("지불할 돈을 입력하세요. = "))
    bill=money-total
    print("\n받은금액 : %d원\n"
          "음식 총 비용 : %d원\n"
          "거스름돈 : %d원\n"%(money,total,bill))



print("*********************음식주문 프로세스******************")

while True:
    print("\n  1. 메뉴판 등록"
          "  2. 주문 진행"
          "  3. 종료     ")
    order = input("\n진행할 메뉴를 입력하세요:   ")
    if order == '3':
        print("종료합니다.")
        mk_file()
        break
    elif order == '1':
        print("\n메뉴판을 생성하겠습니다. ")
        update_menu()
        print("*************메뉴***************")
        for item in dict_menu.items():
            print(item[0], '=', item[1], '원')
    elif order =='2':
        input_order()

















