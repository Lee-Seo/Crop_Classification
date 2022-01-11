import pandas as pd
import csv
import os

path = "C:/Users/rkfrk/Downloads/sample/sample_data/sample_data" #폴더 경로 설정
file_list = os.listdir(path)
print(file_list)


for file_name_raw in file_list:
    file_name = "C:/Users/rkfrk/Downloads/sample/sample_data/sample_data/" + file_name_raw+"/"+file_name_raw+".csv" #실행 할 파일 경로 설정
    df = pd.read_csv(file_name)
    print(file_name)
    df.iloc[0]=["측정시각","내부 온도 1 평균","내부 온도 1 최고","내부 온도 1 최저","내부 온도 2 평균","내부 온도 2 최고","내부 온도 2 최저","내부 온도 3 평균","내부 온도 3 최고","내부 온도 3 최저","내부 온도 4 평균","내부 온도 4 최고","내부 온도 4 최저","내부 습도 1 평균","내부 습도 1 최고","내부 습도 1 최저","내부 습도 2 평균","내부 습도 2 최고","내부 습도 2 최저","내부 습도 3 평균","내부 습도 3 최고","내부 습도 3 최저","내부 습도 4 평균","내부 습도 4 최고","내부 습도 4 최저","내부 이슬점 평균","내부 이슬점 최고","내부 이슬점 최저","내부 CO2 평균","내부 CO2 최고","내부 CO2 최저","외부 풍속 평균","외부 풍속 최고","외부 풍속 최저","내부 EC 1 평균","내부 EC 1 최고","내부 EC 1 최저","내부 PH 1 평균","내부 PH 1 최고","내부 PH 1 최저","배지 중량 평균","배지 중량 최고","배지 중량 최저","양액 온도 평균","양액 온도 최고","양액 온도 최저","외부 풍향 수치","외부 풍향","외부 빗물 시간","외부 누적일사 평균","양액 급액 누적","양액 배액 누적"]
    df.to_csv(file_name,header = False, index = False, encoding='utf-8-sig')
