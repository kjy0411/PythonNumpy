import numpy as np
import pandas as pd

# GROUP BY
# COUNT => deptno

emp_df=pd.read_csv('C:/pydata/EMP.csv')
dept_df=pd.read_csv('C:/pydata/DEPT.csv')
"""
    SELECT deptno,COUNT(*)
    FORM EMP
    GROUP BY deptno
"""
print(emp_df.groupby('DEPTNO')['SAL'].mean())
print(emp_df.groupby('DEPTNO')['SAL'].sum())
print(emp_df.groupby('DEPTNO')['SAL'].max())
print(emp_df.groupby('DEPTNO')['SAL'].min())
print(emp_df.groupby('DEPTNO')['SAL'].count())
print(emp_df.groupby('DEPTNO')['SAL'].median())

print(emp_df.groupby('DEPTNO')['SAL'].agg(['mean','max','sum','min']))
# JOIN
"""
    groupby
      count() : 갯수
      median() : 중간값
      max() : 최대값
      min() : 최소값
      sum() : 합
      mean() : 평균
      
      JOIN => merge
"""
"""
    SELECT * FROM emp e,dept d
    WHERE e.deptno=d.deptno
"""
pf_join=pd.merge(emp_df,dept_df,on='DEPTNO',how='inner')
print(pf_join)
# ORDER BY
print(emp_df.sort_values(by=['SAL'],ascending=True))
"""
    파일 읽기 read_csv => DataFrame (table형식)
    file = open => scv.reader()
    
    => DataFrame
        = JOIN : merge
        = GROUP BY : groupby
                     -------
                     mean() / sum() / count()
"""