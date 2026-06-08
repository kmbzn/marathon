import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


def prepare_splits(df: pd.DataFrame, feature_cols: list, target_col: str,
                   test_size: float = 0.2, random_state: int = 42):
    data = df[feature_cols + [target_col]].dropna()
    X = data[feature_cols]
    y = data[target_col]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)


def evaluate(model, X_test, y_test) -> dict:
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    r2 = r2_score(y_test, preds)
    return {'RMSE_s': rmse, 'RMSE_min': rmse / 60, 'R2': r2}


def train_all(X_train, X_test, y_train, y_test) -> pd.DataFrame:
    scaler = StandardScaler()
    X_tr_sc = scaler.fit_transform(X_train)
    X_te_sc = scaler.transform(X_test)

    models = {
        'Ridge': Ridge(alpha=1.0),
        'Lasso': Lasso(alpha=1.0),
    }
    results = {}
    for name, m in models.items():
        m.fit(X_tr_sc, y_train)
        results[name] = evaluate(m, X_te_sc, y_test)

    rf = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    results['Random Forest'] = evaluate(rf, X_test, y_test)
    results['Random Forest']['feature_importances'] = dict(
        zip(X_train.columns, rf.feature_importances_)
    )

    try:
        from xgboost import XGBRegressor
        xgb = XGBRegressor(n_estimators=200, random_state=42, verbosity=0)
        xgb.fit(X_train, y_train)
        results['XGBoost'] = evaluate(xgb, X_test, y_test)
    except ImportError:
        pass

    try:
        from lightgbm import LGBMRegressor
        lgbm = LGBMRegressor(n_estimators=200, random_state=42, verbose=-1)
        lgbm.fit(X_train, y_train)
        results['LightGBM'] = evaluate(lgbm, X_test, y_test)
    except ImportError:
        pass

    rows = {k: {'RMSE (min)': round(v['RMSE_min'], 2), 'R²': round(v['R2'], 4)}
            for k, v in results.items()}
    return pd.DataFrame(rows).T, results
