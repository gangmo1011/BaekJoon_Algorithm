test_case=int(input(''))

# 행성 진입 횟수 리스트 
planet_in_counts=[0]*(test_case)

# 테스트 케이스 만큼 실행
for i in range(test_case):
    # 테스트 케이스마다 출발행성, 도착행성 x, y 좌표 찍음
    st_x,st_y,arr_x,arr_y=map(int,input('').split())
    # 행성의 갯수
    planet_counts=int(input(''))
    

    # 행성 갯수 만큼 반복
    for j in range(planet_counts):
        pl_x,pl_y,pl_radius=map(int,input('').split())
        if (st_x-pl_x)**2 + (st_y-pl_y)**2 < pl_radius**2:
            planet_in_counts[i] += 1
        if (arr_x-pl_x)**2 + (arr_y-pl_y)**2 < pl_radius**2:
            planet_in_counts[i] += 1
        if (st_x-pl_x)**2 + (st_y-pl_y)**2 < pl_radius**2 and (arr_x-pl_x)**2 + (arr_y-pl_y)**2 < pl_radius**2:
            planet_in_counts[i] -= 2
   
for k in planet_in_counts:
    print(k)