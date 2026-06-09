---
title: IV. Evaluation & Analysis
layout: default
nav_order: 5
has_children: true
---

# IV. Evaluation & Analysis


## 1. EDA

### 1-1. Finish Time Distribution by Age & Gender

![나이대별 완주 시간 분포]({{ '/assets/img/age_distribution.png' | relative_url }})

- **남성(M)**은 전 연령대에서 여성(F)보다 평균 완주 시간이 짧은 경향을 보였으나, **50대 이상 구간**에서 그 차이가 좁아지는 패턴이 관찰되었다.
- **30–39세 구간**이 남녀 모두 평균 완주 시간이 가장 짧은 "피크 퍼포먼스" 연령대로 확인되었다.
- 60세 이상 그룹은 완주 시간 분포의 분산이 커지며, 개인차가 두드러졌다.
- 성별 변수는 단독으로도 완주 시간과 통계적으로 유의미한 상관관계를 보였다 (p < 0.001).

### 1-2. Late-Race Pace Degradation by Temperature

![기온별 후반 페이스 저하율]({{ '/assets/img/temp_pace_degradation.png' | relative_url }})

- 대회 당일 **평균 기온이 15°C를 초과**하는 연도에서 30K 이후 구간의 평균 페이스 저하율이 더 높게 나타났다.
- 기온과 완주 시간 사이에는 **단순 선형 관계가 아닌 비선형 임계 패턴**이 관찰되었다. 특히 20°C 이상에서 기록 저하가 급격히 심화되는 경향이 보였다.
- 기온이 높은 연도일수록 **DNF(Did Not Finish)** 비율도 증가하는 상관관계가 확인되었다.

### 1-3. Hitting the Wall — Pace Degradation by Split

![구간별 페이스 저하 히트맵]({{ '/assets/img/split_heatmap.png' | relative_url }})

- **30K 이후 구간**에서 전체 러너의 페이스가 유의미하게 감소하는 "Wall" 현상이 확인되었다.
- 초반 10K 페이스가 빠를수록(과속 출발) 30K 이후 페이스 저하폭이 크게 나타났으며, 이는 페이스 일관성의 중요성을 시사한다.
- 파생 변수 **Fatigue Index** (30K 이후 페이스 / 초반 10K 페이스)의 분포는 완주 시간과 양의 상관관계를 보였다 (r = 0.400).

### 1-4. Feature Correlation

![변수 상관관계 히트맵]({{ '/assets/img/correlation_heatmap.png' | relative_url }})

| 변수 쌍 | Pearson r | 해석 |
|:---|---:|:---|
| Half — Official Time | 0.97 | 중간 기록이 완주 시간의 가장 강력한 예측 변수 |
| 30K — Official Time | **0.984** | 30K 통과 시간도 매우 높은 상관 |
| Fatigue Index — Official Time | 0.400 | 페이스 유지력이 기록에 직접적 영향 |
| Age — Official Time | 0.230 | 나이와 완주 시간은 약한 정(+)의 상관 |

---

## 2. Feature Engineering Results

### 2-1. Fatigue Index
- 값이 **1.0에 가까울수록** 페이스를 일관되게 유지한 러너
- 값이 **1.2 이상**이면 후반부에 심각한 페이스 저하가 발생한 것으로 판단
- 전체 데이터셋 평균 Fatigue Index: **1.126** (중앙값 1.094)
- FI > 1.1 비율: **47.9%** — 전체 러너의 절반 가까이가 후반 페이스 저하 경험

### 2-2. Pacing Variance
- 구간별 페이스(sec/km)의 표준편차로 정의. 값이 작을수록 일정한 페이스 유지
- Official Time과의 상관계수: **0.572** — 페이스 편차가 클수록 완주 시간이 느린 경향

---

## 3. Model Performance Comparison

> RMSE unit: seconds. Values in parentheses are in minutes. Full Model uses features up to 30K split.

### 3-0. Full Model (up to 30K)

| Model | RMSE | R² Score | MAE | 비고 |
|:------|-----:|---------:|----:|:---|
| **Ridge Regression** | **97s (1.61분)** | **0.9984** | **57s** | **최고 성능** |
| Lasso Regression | 97s (1.61분) | 0.9984 | 57s | — |
| Random Forest | 119s (1.99분) | 0.9975 | 52s | — |
| XGBoost | 172s (2.86분) | 0.9948 | 59s | — |
| LightGBM | 167s (2.78분) | 0.9951 | 55s | — |

30K 누적 기록이 완주 시간과 거의 선형 관계이기 때문에 Ridge 같은 선형 모델이 가장 우수한 성능을 보였다.

### 3-0b. Early Model (up to 10K)

| Model | RMSE | R² Score | 비고 |
|:------|-----:|---------:|:---|
| Ridge (Early) | 322s (5.37분) | 0.9821 | — |
| **Random Forest (Early)** | **240s (4.00분)** | **0.9901** | **최고 성능** |
| XGBoost (Early) | 259s (4.32분) | 0.9884 | — |
| LightGBM (Early) | 261s (4.35분) | 0.9882 | — |

10K 기록만 사용하는 Early Prediction에서는 비선형 모델(RF)이 선형 모델을 앞선다.

### 3-1. Performance Visualization

![모델 성능 비교 바 차트]({{ '/assets/img/model_comparison.png' | relative_url }})

### 3-2. Ridge Regression — Predicted vs Actual

![예측값 vs 실제값 산점도]({{ '/assets/img/pred_vs_actual.png' | relative_url }})

- 대부분의 예측값이 **y = x 대각선 근처에 밀집**하여 안정적인 예측력을 확인
- 완주 시간 **4시간 이상 구간**에서 예측 오차가 다소 증가하는 경향 (이 구간 러너의 페이스 변동성이 크기 때문)
- 잔차의 95% 구간: **±2.8분** 이내, |>5분| 오차: 전체의 약 1.2%

### 3-3. Feature Importance (Random Forest)

![변수 중요도]({{ '/assets/img/feature_importance.png' | relative_url }})

| 순위 | 변수 | 중요도 | 해석 |
|:---:|:---|---:|:---|
| 1 | `30K_s` (30K 누적 기록) | 0.9656 | 예측력의 96.6% 차지 |
| 2 | `Fatigue_Index` | 0.0178 | 파생 변수 중 기여도 1위 |
| 3 | `Pacing_Variance` | 0.0128 | 페이스 일관성 지표 |
| 4 | `25K_s` | 0.0009 | — |
| 5 | `Half_s` | 0.0007 | — |
| 6–11 | 나머지 구간 기록, Age, Gender | < 0.001 | — |

---

## 4. Insights Summary

- **30K 기록이 완주 시간을 결정한다**: RF 피처 중요도에서 30K 누적 기록이 예측력의 96.6%를 차지했다. 30K까지의 페이스가 최종 기록을 사실상 결정한다.
- **선형 모델이 Full Model에서 최고 성능**: 30K 기록과 완주 시간의 관계가 거의 선형이기 때문에 Ridge Regression이 RMSE 1.61분(R²=0.9984)으로 XGBoost·LightGBM을 제쳤다.
- **비선형 모델은 Early Prediction에서 강세**: 10K 기록만 사용하는 시나리오에서는 Random Forest(RMSE 4.00분)가 선형 모델(5.37분)보다 우수하다. 초반 페이스와 최종 기록의 관계는 비선형 패턴이 강하다.
- **페이스 일관성이 나이·성별보다 중요**: Pacing Variance(r=0.572)와 Fatigue Index(r=0.400)가 Age(r=0.230)보다 완주 시간과의 상관이 높다.
