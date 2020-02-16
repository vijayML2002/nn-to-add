Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> bos=pd.read_excel('D:\studies\cse\ml\addtwonumber\New Microsoft Excel Worksheet.xlsx')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 30-31: malformed \N character escape
>>> bos=pd.read_excel('D:\studies\cse\ml\addtwonumber\New Microsoft Excel Worksheet.xlsx')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 30-31: malformed \N character escape
>>> bos=pd.read_excel(r'D:\studies\cse\ml\addtwonumber\New Microsoft Excel Worksheet.xlsx')
>>> bos
     1  1.1   2
0    2    4   6
1    4    3   7
2    5    5  10
3    6    4  10
4   10    6  16
5    5    9  14
6    6    7  13
7   11    8  20
8    9    4  13
9   12    7  19
10   5    4   9
11   7    5  12
12   8    2  10
13   4    2   6
14   4    4   8
15   2    4   6
16   4    7  11
17   8    5  12
18   4    3   7
19  16    4  20
20   4    7  11
21   7    4  11
22   8    2  10
23   5   10  15
24   4    6  10
25   2    2   4
26   1    2   3
27   4    1   5
>>> type(bos)
<class 'pandas.core.frame.DataFrame'>
>>> dataset=pd.DataFrame(bos.data)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    dataset=pd.DataFrame(bos.data)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\pandas\core\generic.py", line 5179, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'DataFrame' object has no attribute 'data'
>>> dataset=pd.DataFrame(bos)

>>> dataset
     1  1.1   2
0    2    4   6
1    4    3   7
2    5    5  10
3    6    4  10
4   10    6  16
5    5    9  14
6    6    7  13
7   11    8  20
8    9    4  13
9   12    7  19
10   5    4   9
11   7    5  12
12   8    2  10
13   4    2   6
14   4    4   8
15   2    4   6
16   4    7  11
17   8    5  12
18   4    3   7
19  16    4  20
20   4    7  11
21   7    4  11
22   8    2  10
23   5   10  15
24   4    6  10
25   2    2   4
26   1    2   3
27   4    1   5
>>> dataset.columns=['X','Y','SUM']
>>> dataset
     X   Y  SUM
0    2   4    6
1    4   3    7
2    5   5   10
3    6   4   10
4   10   6   16
5    5   9   14
6    6   7   13
7   11   8   20
8    9   4   13
9   12   7   19
10   5   4    9
11   7   5   12
12   8   2   10
13   4   2    6
14   4   4    8
15   2   4    6
16   4   7   11
17   8   5   12
18   4   3    7
19  16   4   20
20   4   7   11
21   7   4   11
22   8   2   10
23   5  10   15
24   4   6   10
25   2   2    4
26   1   2    3
27   4   1    5
>>> from sklearn.model_selection import train_test_split
>>> import statsmodels.api as sm
>>> feature=sm.add_constant(dataset.columns)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    feature=sm.add_constant(dataset.columns)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\tools\tools.py", line 305, in add_constant
    is_nonzero_const = np.ptp(x, axis=0) == 0
  File "<__array_function__ internals>", line 6, in ptp
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\numpy\core\fromnumeric.py", line 2496, in ptp
    return _methods._ptp(a, axis=axis, out=out, **kwargs)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\numpy\core\_methods.py", line 232, in _ptp
    out
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> influe=['X','Y','SUM']
>>> feature=sm.add_constant(influe)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    feature=sm.add_constant(influe)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\tools\tools.py", line 305, in add_constant
    is_nonzero_const = np.ptp(x, axis=0) == 0
  File "<__array_function__ internals>", line 6, in ptp
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\numpy\core\fromnumeric.py", line 2496, in ptp
    return _methods._ptp(a, axis=axis, out=out, **kwargs)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\numpy\core\_methods.py", line 230, in _ptp
    umr_maximum(a, axis, None, out, keepdims),
TypeError: cannot perform reduce with flexible type
>>> influe=['X','Y']
>>> feature=sm.add_constant(dataset[influe])

Warning (from warnings module):
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\numpy\core\fromnumeric.py", line 2495
    return ptp(axis=axis, out=out, **kwargs)
FutureWarning: Method .ptp is deprecated and will be removed in a future version. Use numpy.ptp instead.
>>> p=dataset['SUM']
>>> train_x,test_x,train_y,test_y=train_test_split(feature,p,train_size=0.9,random_state=0)
>>> reg=sm.OLS(train_y,train_x)
>>> reg=sm.OLS(train_y,train_x).fit()
>>> pred_y=reg.predict(train_x)
>>> pred_y
17    13.017347
5     14.076870
11    12.010663
24    10.010504
13     5.930928
20    11.030398
25     3.917560
16    11.030398
1      6.950822
10     8.977401
27     4.911034
26     2.910875
8     13.004138
6     13.043767
4     16.050610
18     6.950822
19    20.050928
9     19.083873
7     19.097082
23    15.096764
3      9.984085
0      5.957347
21    10.990769
15     5.957347
12     9.957666
dtype: float64
>>> diff=pred_y-test_y
>>> diff
0    NaN
1    NaN
2    NaN
3    NaN
4    NaN
5    NaN
6    NaN
7    NaN
8    NaN
9    NaN
10   NaN
11   NaN
12   NaN
13   NaN
14   NaN
15   NaN
16   NaN
17   NaN
18   NaN
19   NaN
20   NaN
21   NaN
22   NaN
23   NaN
24   NaN
25   NaN
26   NaN
27   NaN
dtype: float64
>>> pred_y
17    13.017347
5     14.076870
11    12.010663
24    10.010504
13     5.930928
20    11.030398
25     3.917560
16    11.030398
1      6.950822
10     8.977401
27     4.911034
26     2.910875
8     13.004138
6     13.043767
4     16.050610
18     6.950822
19    20.050928
9     19.083873
7     19.097082
23    15.096764
3      9.984085
0      5.957347
21    10.990769
15     5.957347
12     9.957666
dtype: float64
>>> test_Y
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    test_Y
NameError: name 'test_Y' is not defined
>>> test_y
2     10
22    10
14     8
Name: SUM, dtype: int64
>>> pred_y=reg.predict(test_x)
>>> pred_y
2     9.997294
22    9.957666
14    7.970716
dtype: float64
>>> test_y
2     10
22    10
14     8
Name: SUM, dtype: int64
>>> reg.summary2()
<class 'statsmodels.iolib.summary2.Summary'>
"""
                 Results: Ordinary least squares
=================================================================
Model:              OLS              Adj. R-squared:     0.996   
Dependent Variable: SUM              AIC:                12.7866 
Date:               2019-10-15 20:43 BIC:                16.4432 
No. Observations:   25               Log-Likelihood:     -3.3933 
Df Model:           2                F-statistic:        3128.   
Df Residuals:       22               Prob (F-statistic): 9.78e-28
R-squared:          0.996            Scale:              0.087285
-------------------------------------------------------------------
            Coef.    Std.Err.      t      P>|t|     [0.025   0.975]
-------------------------------------------------------------------
const      -0.1356     0.1549   -0.8754   0.3908   -0.4568   0.1857
X           1.0067     0.0176   57.1534   0.0000    0.9702   1.0432
Y           1.0199     0.0264   38.6986   0.0000    0.9652   1.0746
-----------------------------------------------------------------
Omnibus:              18.296       Durbin-Watson:          1.543 
Prob(Omnibus):        0.000        Jarque-Bera (JB):       81.620
Skew:                 -0.595       Prob(JB):               0.000 
Kurtosis:             11.772       Condition No.:          22    
=================================================================

"""
>>> dataset['SUM']
0      6
1      7
2     10
3     10
4     16
5     14
6     13
7     20
8     13
9     19
10     9
11    12
12    10
13     6
14     8
15     6
16    11
17    12
18     7
19    20
20    11
21    11
22    10
23    15
24    10
25     4
26     3
27     5
Name: SUM, dtype: int64
>>> data=pd.read_excel(r'D:\studies\cse\ml\addtwonumber\dataset1.xlsx')
>>> data
   17  45
0  34  74
1  45  67
2  43  46
>>> data.column'
SyntaxError: EOL while scanning string literal
>>> data.columns
Int64Index([17, 45], dtype='int64')
>>> infla=['X','Y']
>>> data.columns=[influa]
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    data.columns=[influa]
NameError: name 'influa' is not defined
>>> data.columns=['X','Y']
>>> data
    X   Y
0  34  74
1  45  67
2  43  46
>>> pre=sm.add_constant
>>> pre=sm.add_constant(dataset[infla])
>>> pred=sm.OLS(pre)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    pred=sm.OLS(pre)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\regression\linear_model.py", line 838, in __init__
    hasconst=hasconst, **kwargs)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\regression\linear_model.py", line 684, in __init__
    weights=weights, hasconst=hasconst, **kwargs)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\regression\linear_model.py", line 196, in __init__
    super(RegressionModel, self).__init__(endog, exog, **kwargs)
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\base\model.py", line 217, in __init__
    self.initialize()
  File "C:\Users\pkvij\AppData\Local\Programs\Python\Python36\lib\site-packages\statsmodels\regression\linear_model.py", line 203, in initialize
    self.nobs = float(self.wexog.shape[0])
AttributeError: 'NoneType' object has no attribute 'shape'
>>> pred=reg.predict(pre)
>>> pred
0      5.957347
1      6.950822
2      9.997294
3      9.984085
4     16.050610
5     14.076870
6     13.043767
7     19.097082
8     13.004138
9     19.083873
10     8.977401
11    12.010663
12     9.957666
13     5.930928
14     7.970716
15     5.957347
16    11.030398
17    13.017347
18     6.950822
19    20.050928
20    11.030398
21    10.990769
22     9.957666
23    15.096764
24    10.010504
25     3.917560
26     2.910875
27     4.911034
dtype: float64
>>> pre
    const   X   Y
0     1.0   2   4
1     1.0   4   3
2     1.0   5   5
3     1.0   6   4
4     1.0  10   6
5     1.0   5   9
6     1.0   6   7
7     1.0  11   8
8     1.0   9   4
9     1.0  12   7
10    1.0   5   4
11    1.0   7   5
12    1.0   8   2
13    1.0   4   2
14    1.0   4   4
15    1.0   2   4
16    1.0   4   7
17    1.0   8   5
18    1.0   4   3
19    1.0  16   4
20    1.0   4   7
21    1.0   7   4
22    1.0   8   2
23    1.0   5  10
24    1.0   4   6
25    1.0   2   2
26    1.0   1   2
27    1.0   4   1
>>> pre=sm.add_constant(data[infla])
>>> pred=reg.predict(pre)
>>> pred
0    109.56382
1    113.49809
2     90.06695
dtype: float64
>>> pre
   const   X   Y
0    1.0  34  74
1    1.0  45  67
2    1.0  43  46
>>> reg.summary2()
<class 'statsmodels.iolib.summary2.Summary'>
"""
                 Results: Ordinary least squares
=================================================================
Model:              OLS              Adj. R-squared:     0.996   
Dependent Variable: SUM              AIC:                12.7866 
Date:               2019-10-15 21:05 BIC:                16.4432 
No. Observations:   25               Log-Likelihood:     -3.3933 
Df Model:           2                F-statistic:        3128.   
Df Residuals:       22               Prob (F-statistic): 9.78e-28
R-squared:          0.996            Scale:              0.087285
-------------------------------------------------------------------
            Coef.    Std.Err.      t      P>|t|     [0.025   0.975]
-------------------------------------------------------------------
const      -0.1356     0.1549   -0.8754   0.3908   -0.4568   0.1857
X           1.0067     0.0176   57.1534   0.0000    0.9702   1.0432
Y           1.0199     0.0264   38.6986   0.0000    0.9652   1.0746
-----------------------------------------------------------------
Omnibus:              18.296       Durbin-Watson:          1.543 
Prob(Omnibus):        0.000        Jarque-Bera (JB):       81.620
Skew:                 -0.595       Prob(JB):               0.000 
Kurtosis:             11.772       Condition No.:          22    
=================================================================

"""
>>> data=pd.read_excel(r'D:\studies\cse\ml\addtwonumber\dataset1.xlsx')
>>> data.columns=['X','Y']
>>> data
     X    Y
0  100  300
1  200  300
2  100  200
>>> infla=['X','Y']
>>> pre=sm.add_constant(data[infla])
>>> pred=reg.predict(pre)
>>> pred
0    406.501008
1    507.169443
2    304.511618
dtype: float64
>>> pre
   const    X    Y
0    1.0  100  300
1    1.0  200  300
2    1.0  100  200
>>> reg.summary2()
<class 'statsmodels.iolib.summary2.Summary'>
"""
                 Results: Ordinary least squares
=================================================================
Model:              OLS              Adj. R-squared:     0.996   
Dependent Variable: SUM              AIC:                12.7866 
Date:               2019-10-15 21:10 BIC:                16.4432 
No. Observations:   25               Log-Likelihood:     -3.3933 
Df Model:           2                F-statistic:        3128.   
Df Residuals:       22               Prob (F-statistic): 9.78e-28
R-squared:          0.996            Scale:              0.087285
-------------------------------------------------------------------
            Coef.    Std.Err.      t      P>|t|     [0.025   0.975]
-------------------------------------------------------------------
const      -0.1356     0.1549   -0.8754   0.3908   -0.4568   0.1857
X           1.0067     0.0176   57.1534   0.0000    0.9702   1.0432
Y           1.0199     0.0264   38.6986   0.0000    0.9652   1.0746
-----------------------------------------------------------------
Omnibus:              18.296       Durbin-Watson:          1.543 
Prob(Omnibus):        0.000        Jarque-Bera (JB):       81.620
Skew:                 -0.595       Prob(JB):               0.000 
Kurtosis:             11.772       Condition No.:          22    
=================================================================

"""
>>> 
