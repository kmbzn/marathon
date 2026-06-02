---
title: III. Methodology
layout: default
nav_order: 4
---

# III. Methodology

## 1. Data Preprocessing

원본 데이터셋에는 중도 포기자(DNF), 문자열 형식의 시간 데이터, 범주형 변수 등
분석에 바로 사용하기 어려운 요소들이 포함되어 있습니다.
아래 순서로 전처리 파이프라인을 구성하였습니다.

### 1-1. 결측치 처리

DNF(Did Not Finish) 참가자는 30K, 35K, 40K 등 후반 구간 시간이 결측값으로
기록됩니다. 이 레코드들은 **예측 모델 학습 대상에서 제외**하되,
EDA 단계에서는 DNF 비율과 기온의 관계 분석에 활용합니다.

```python
# DNF 레코드 제거 (Official Time 결측 기준)
df = df.dropna(subset=['Official Time'])

# 구간 시간 결측치 확인
print(df.isnull().sum())
```

### 1-2. 시간 데이터 변환

모든 구간 시간은 `HH:MM:SS` 문자열로 수록되어 있습니다.
회귀 모델 입력을 위해 **초(seconds) 단위 정수형**으로 변환합니다.

```python
def time_to_seconds(t: str) -> int:
    """'HH:MM:SS' 문자열을 초 단위 정수로 변환"""
    if pd.isna(t):
        return None
    h, m, s = map(int, str(t).split(':'))
    return h * 3600 + m * 60 + s

time_cols = ['5K', '10K', '15K', '20K', 'Half',
             '25K', '30K', '35K', '40K', 'Official Time']

for col in time_cols:
    df[col] = df[col].apply(time_to_seconds)
```

### 1-3. 범주형 변수 인코딩

| 변수 | 처리 방법 | 비고 |
|:---|:---|:---|
| `M/F` | Binary Encoding (M=0, F=1) | 이진 변수이므로 One-Hot 불필요 |
| `Country` | One-Hot Encoding | 상위 20개국 외 `Other`로 통합 |
| `State` | One-Hot Encoding | 미국 참가자에 한해 적용 |

```python
# 성별 이진 인코딩
df['Gender'] = df['M/F'].map({'M': 0, 'F': 1})

# 국적 One-Hot Encoding (상위 20개국)
top_countries = df['Country'].value_counts().nlargest(20).index
df['Country'] = df['Country'].apply(
    lambda x: x if x in top_countries else 'Other'
)
df = pd.get_dummies(df, columns=['Country'], drop_first=True)
```

### 1-4. Train / Test Split

```python
from sklearn.model_selection import train_test_split

X = df.drop(columns=['Official Time'])
y = df['Official Time']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

---

## 2. Feature Engineering

원본 변수만으로는 포착하기 어려운 **페이스 전략의 질적 차이**를
수치화하기 위해 아래 두 가지 파생 변수를 추가합니다.

### 2-1. Fatigue Index (피로 지수)

30K 이후 구간의 평균 페이스를 초반 10K 페이스로 나눈 비율입니다.
값이 클수록 후반에 급격히 느려진 것을 의미합니다.

$$
\text{Fatigue Index} = \frac{\text{Pace}_{30K \to \text{Finish}}}{\text{Pace}_{0 \to 10K}}
$$

```python
# 구간 페이스 = 구간 소요 시간 / 구간 거리(km)
df['Pace_early'] = df['10K'] / 10                          # 0~10K 평균 페이스 (초/km)
df['Pace_late']  = (df['Official Time'] - df['30K']) / 12.195  # 30K~Finish 평균 페이스

df['Fatigue_Index'] = df['Pace_late'] / df['Pace_early']
```

| Fatigue Index 범위 | 해석 |
|:---:|:---|
| ~1.05 | 매우 일정한 페이스 유지 (Negative Split 또는 Even Split) |
| 1.05~1.20 | 정상적인 후반부 소폭 감속 |
| 1.20~1.40 | 페이스 저하 뚜렷 — Hitting the Wall 진입 구간 |
| 1.40~ | 심각한 페이스 붕괴 |

### 2-2. Pacing Variance (페이스 분산)

9개 구간 페이스의 변동계수(CV, Coefficient of Variation)로
**페이스 일관성**을 측정합니다.

$$
\text{Pacing Variance} = \frac{\sigma(\text{구간 페이스})}{\mu(\text{구간 페이스})}
$$

```python
split_cols = ['5K', '10K', '15K', '20K', 'Half', '25K', '30K', '35K', '40K']
distances  = [5, 5, 5, 5, 1.0975, 5, 5, 5, 5]  # 각 구간 거리(km)

# 구간별 페이스 계산
pace_cols = []
prev = 0
for col, dist in zip(split_cols, distances):
    pace_col = f'Pace_{col}'
    df[pace_col] = (df[col] - prev) / dist
    pace_cols.append(pace_col)
    prev = df[col]

df['Pacing_Variance'] = df[pace_cols].std(axis=1) / df[pace_cols].mean(axis=1)
```

---

## 3. Model Training & Evaluation

### 3-1. 평가 지표

$$
\text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2}
\qquad
R^2 = 1 - \frac{\sum(\hat{y}_i - y_i)^2}{\sum(\bar{y} - y_i)^2}
$$

- **RMSE**: 예측 오차를 초(seconds) 단위로 직관적으로 해석 가능
- **R² Score**: 모델이 완주 시간 분산을 얼마나 설명하는지 나타냄 (1.0에 가까울수록 우수)

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2   = r2_score(y_test, y_pred)
    mae  = np.mean(np.abs(y_pred - y_test))
    print(f"RMSE: {rmse:.1f}s ({rmse/60:.1f}분) | R²: {r2:.3f} | MAE: {mae:.1f}s")
    return rmse, r2
```

### 3-2. Ridge / Lasso Regression

선형 모델을 baseline으로 사용합니다.
정규화 강도 `alpha`는 Cross-Validation으로 탐색합니다.

```python
from sklearn.linear_model import RidgeCV, LassoCV

ridge = RidgeCV(alphas=[0.1, 1.0, 10.0, 100.0], cv=5)
ridge.fit(X_train, y_train)
evaluate(ridge, X_test, y_test)

lasso = LassoCV(alphas=[0.01, 0.1, 1.0, 10.0], cv=5, max_iter=5000)
lasso.fit(X_train, y_train)
evaluate(lasso, X_test, y_test)
```

| 하이퍼파라미터 | Ridge | Lasso |
|:---|:---|:---|
| `alpha` | CV 탐색 (0.1~100) | CV 탐색 (0.01~10) |
| `cv` | 5-Fold | 5-Fold |
| `fit_intercept` | True | True |

### 3-3. Random Forest Regressor

```python
from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(
    n_estimators=300,
    max_depth=None,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1
)
rf.fit(X_train, y_train)
evaluate(rf, X_test, y_test)
```

| 하이퍼파라미터 | 설정값 | 설명 |
|:---|:---|:---|
| `n_estimators` | 300 | 트리 개수 |
| `max_depth` | None | 완전 성장 허용 |
| `min_samples_split` | 5 | 내부 노드 분할 최소 샘플 수 |
| `max_features` | `'sqrt'` | 분할 시 고려할 변수 수 |

### 3-4. XGBoost Regressor

```python
from xgboost import XGBRegressor

xgb = XGBRegressor(
    n_estimators=500,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=1.0,
    random_state=42,
    n_jobs=-1,
    early_stopping_rounds=30
)
xgb.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    verbose=False
)
evaluate(xgb, X_test, y_test)
```

| 하이퍼파라미터 | 설정값 | 설명 |
|:---|:---|:---|
| `n_estimators` | 500 | 최대 부스팅 라운드 수 |
| `max_depth` | 6 | 트리 최대 깊이 |
| `learning_rate` | 0.05 | 학습률 (작을수록 정밀) |
| `subsample` | 0.8 | 매 트리 학습에 사용할 샘플 비율 |
| `colsample_bytree` | 0.8 | 매 트리 학습에 사용할 변수 비율 |
| `early_stopping_rounds` | 30 | 과적합 방지 조기 종료 |

### 3-5. LightGBM Regressor

```python
from lightgbm import LGBMRegressor

lgbm = LGBMRegressor(
    n_estimators=1000,
    num_leaves=64,
    max_depth=8,
    learning_rate=0.03,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=0.1,
    reg_lambda=1.0,
    min_child_samples=20,
    random_state=42,
    n_jobs=-1
)
lgbm.fit(
    X_train, y_train,
    eval_set=[(X_test, y_test)],
    callbacks=[lgbm.early_stopping(50), lgbm.log_evaluation(0)]
)
evaluate(lgbm, X_test, y_test)
```

| 하이퍼파라미터 | 설정값 | 설명 |
|:---|:---|:---|
| `n_estimators` | 1000 | 최대 트리 수 |
| `num_leaves` | 64 | 리프 노드 수 (복잡도 제어) |
| `learning_rate` | 0.03 | XGBoost보다 낮게 설정해 안정성 확보 |
| `min_child_samples` | 20 | 과적합 방지 최소 샘플 수 |
| `early_stopping` | 50 rounds | 검증 손실 개선 없으면 조기 종료 |

### 3-6. 전체 파이프라인 요약

```
Raw CSV
  │
  ▼
[Preprocessing]
  결측치 제거 → 시간 변환(초) → 인코딩
  │
  ▼
[Feature Engineering]
  Fatigue Index / Pacing Variance 산출
  │
  ▼
[Train / Test Split]  80% / 20%, random_state=42
  │
  ├──► Ridge / Lasso  ──► evaluate()
  ├──► Random Forest  ──► evaluate()
  ├──► XGBoost        ──► evaluate()
  └──► LightGBM       ──► evaluate()  ← 최고 성능 예상
```
