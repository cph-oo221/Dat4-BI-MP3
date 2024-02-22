
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd


def allCols(df, y):
    colList = []
    for col in df.columns:
        if col != y:
            colList.append(col)
    return colList
    

def bestLinReg(df, y):
    
    y_val = df[y].values.reshape(-1, 1)
    col = allCols(df, y)

    res_df = pd.DataFrame(columns=['x', 'R2', 'coef', 'intercept', 'y_predicted'])
    
    for col_name in col:
        
        X = df[col_name].values.reshape(-1, 1)

        X_train, X_test, y_train, y_test = train_test_split(X, y_val, random_state=123, test_size=0.25)

        myreg = LinearRegression()
        myreg.fit(X_train, y_train)

        a = myreg.coef_
        b = myreg.intercept_

        y_predicted = myreg.predict(X_test)

        R2 = myreg.score(X, y_val)

        
        res_df.loc[len(res_df)] = {'x': col_name, 'R2': round(R2, 5), 'coef': a, 'intercept': b, 'y_predicted': y_predicted}
        res_df = res_df.sort_values(by='R2', ascending=False)

    return res_df 
