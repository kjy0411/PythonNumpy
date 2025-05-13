"""
    1. list => numpy 변경
        np.array(list)
    2. 배열 형태 (행,열)
        np.shape
    3. 연산처리
        + : add()
        - : substract()
        / : multiply()
        * : divide()

    ones()  => np.ones((2,3)) => 1로 채워진 2열 3행 배열 생성
                    [[1. 1. 1.],[1. 1. 1.]]
    zeros() => np.zeros((2,2)) => 0로 채워진 2열 2행 배열 생성
                    [[0. 0.],[0. 0.]]
    arange() => np.arange(10) => 0~9
                np.arange(5,10) => 5~9

    => 행렬 /합 / 평균 / 표준 편차
        행렬 : dot()
        합 : sum()
        평균 : mean()
        표준 편차 : std()

    행렬 계산
    [a b],[c d]
    [e f],[g h]
    => [a*c+b*g a*f+b*h],[c*e+d*g c*f+d*h]

    연산 처리 => numpy
    함수 처리 => pandas
    화면 처리 => matplotlib , seaborn
"""
import numpy as np
# 1차원 배열
a=np.array([1,2,3])
# 2차원 배열 *** 데이터 읽기 : ㅇㅁㅅㅁㄺ믇
# Table형식 => 2차원
b=np.array([[1,2,3],[4,5,6]])
# 3차원 배열 ***
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)
print(b)
print(c)
print(a.shape)
print(b.shape)
print(c.shape)

a=np.array([1,2,3])
b=np.array([4,5,6])
c=a+b # [5,7,9]
d=a*b # [4,10,18]
e=a+1 # [2,3,4]
print(c,d,e)
k1=np.sum(a)
k2=np.sum(b)
print(f"{k1}+{k2}={k1+k2}")
k1=np.mean(a)
k2=np.mean(b)
print(f"{k1}+{k2}={k1+k2}")
m1=np.min(a)
m2=np.min(b)
m3=np.max(a)
m4=np.max(b)
print(m1,m2,m3,m4)

n1=np.std(a)
n2=np.std(b)
print(n1,n2)