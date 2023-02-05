# 보강3차시 메뉴추천코드
# 메뉴와 디저트를 추천받아, 랜덤하게 1개출력
# 함수사용, 입력종료시q사용,fstirng으로 print한줄에작성

import random as rd

def meal(category, lists):
    while True:
      x = input("메뉴입력(종료는 'q'입력):")
      if x == "q":
        break
      lists.append(x)
      
      inform = input(f"현재 {category}는 : {lists}입니다. \n더 고르시겠어요?( y or n 입력)")
      print(inform)
      while inform not in ["y", "n"]:
        print("y , n 중 입력해주세요")
        inform = input(f"현재 {category}는 : {lists}입니다. \n더 고르시겠어요?( y or n 입력)")
      if inform == "n":
        break

menu_list = []
meal("메뉴",menu_list)
menu_recommendation = rd.choice(menu_list)
print(f"추천메뉴는 {menu_recommendation}입니다. zzz")
