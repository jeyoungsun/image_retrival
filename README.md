시도한 방법들

1) sift: 너무 오래 걸려 시행 불가

2) orb -> BFMatcher(crossCheck=True): 유사도 측정 방법 모름

3) orb -> BFMatcher(defalt) -> knnmatch -> k=2 ratio test: ratio가 0.75일 때 정확도 0.87, 0.8일 때 0.87, 0.6일 때 0.82

4) orb -> BFMatcher(defalt) -> knnmatch -> k=2 ratio test: 처음 10개만 돌려본 결과 정확도 떨어짐

5) orb -> BFMatcher(cv.normhamming2) -> knnmatch k=2 ratio test: ratio가 0.75일 때 정확도 0.86

6) orb -> flann: ratio 0.75일 때 0.84, BFMatcher보다 확연히 느림

ML2_bfmatcher.py 은 3), 

ML2_flann.py는 6)을 시행한 코드이다.
