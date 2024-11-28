1) sift
너무 오래 걸려 시행 불가

2) orb -> bfmatcher - crossCheck:
유사도 측정 방법 모름

3) orb -> BFMatcher(defalt) -> knnmatch -> k=2 ratio test as per Lowe's paper 
ratio가 0.75일 때 정확도 0.87
0.8일 때 0.87
0.6일 때 0.82
k=3 ratio test:
처음 10개만 돌려본 결과 정확도 떨어짐

4) orb -> BFMatcher(cv.normhamming2) -> knnmatch k=2 ratio test as per Lowe's paper = 0.86

6) orb -> flann:
ratio 0.75일 때 0.84, 
bfmatcher보다 느림
