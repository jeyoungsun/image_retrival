import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os
from tqdm import tqdm

# ORB 생성
orb = cv.ORB_create()

# ORB 계산 함수
def compute_orb(image):
    img = cv.imread(image, cv.IMREAD_GRAYSCALE)
    kp, des = orb.detectAndCompute(img, None)
    return kp, des

# 이미지 가져오는 함수
def get_image_files(directory):
    return [f for f in os.listdir(directory) if f.endswith('.jpg')]

# 이미지 디렉토리 지정
query_dir = 'C:/Users/jdudt/OneDrive - kaist.ac.kr/pytorch/ML2/takehome_dataset/query/'
database_dir = 'C:/Users/jdudt/OneDrive - kaist.ac.kr/pytorch/ML2/takehome_dataset/database/'

# 이미지 가져오기
query_files = get_image_files(query_dir)
database_files = get_image_files(database_dir)

# 결과 리스트
results = []

# FLANN 매개변수 설정 (LSH 기반)
FLANN_INDEX_LSH = 6
index_params = dict(algorithm=FLANN_INDEX_LSH, 
                    table_number=12,  # 해싱 테이블 개수
                    key_size=20,      # 해싱 키 크기
                    multi_probe_level=2)  # 탐색 레벨
search_params = dict(checks=50)  # 탐색 횟수

# 매칭
for query_file in tqdm(query_files, desc="Processing Query Images", unit="query"):
    query_path = os.path.join(query_dir, query_file)

    kp1, des1 = compute_orb(query_path)

    best_match = None
    best_number = 0

    for database_file in tqdm(database_files, desc="Processing Database Images", unit="database"):
        database_path = os.path.join(database_dir, database_file)

        kp2, des2 = compute_orb(database_path)

        flann = cv.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1, des2, k=2)

        good = []
        
        for match_pair in matches:  # k=2에 맞게 필터링
            if len(match_pair) == 2:  # 두 개의 매칭만 있는 경우에만
                m, n = match_pair  # 두 매칭을 언팩
                if m.distance < 0.75 * n.distance:  # 거리 비율 테스트
                    good.append([m])

        total_number = len(good)

        if total_number > best_number:
            best_number = total_number
            best_match = database_file
        
    results.append(f"query/{query_file} database/{best_match}")

# 결과 저장
with open('answer.txt', 'w') as f:
    for result in results:
        f.write(result + '\n')

print("Matching complete. Results saved in 'answer.txt'.")
