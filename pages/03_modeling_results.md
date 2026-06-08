---
title: "모델 학습 & 평가 결과"
layout: default
nav_order: 3
parent: "IV. Evaluation & Analysis"
---

# 모델 학습 및 평가 결과

> **분석 노트북**: [`03_modeling_and_evaluation.ipynb`](https://colab.research.google.com/github/kmbzn/marathon/blob/main/notebooks/03_modeling_and_evaluation.ipynb)

---

## 실험 설계

두 가지 예측 시나리오를 비교합니다.

| 시나리오 | 사용 피처 | 실용적 의미 |
|----------|-----------|-------------|
| **Full Model** | 30K 기록까지 + 인구통계 + Fatigue Index | 레이스 후반 기록 예측 |
| **Early Model** | 10K 기록까지 + 나이/성별 + Fatigue Index | 레이스 초반 완주 시간 예측 |

- Train/Test Split: 80% / 20% (random_state=42)
- Train: 21,061명 / Test: 5,266명
- 평가 지표: RMSE (낮을수록 좋음), R² (높을수록 좋음)

---

## Full Model 결과

| 모델 | RMSE | R² |
|------|------|-----|
| **Ridge Regression** | **1.62분 (97초)** | **0.9983** |
| Lasso Regression | 1.65분 (99초) | 0.9983 |
| Random Forest | 1.66분 (99초) | 0.9983 |
| XGBoost* | — | — |
| LightGBM* | — | — |

> *XGBoost / LightGBM은 설치 환경에 따라 추가 실행 가능 (`pip install xgboost lightgbm`)

**해석**: 30K 기록까지 알고 있을 때 완주 시간을 평균 **±1.6분** 오차로 예측합니다. R² 0.9983은 분산의 99.83%를 모델이 설명함을 의미합니다.

---

## Early Model 결과 (10K까지만 사용)

| 모델 | RMSE | R² |
|------|------|-----|
| Ridge (Early) | 5.37분 | 0.9821 |
| **Random Forest (Early)** | **3.99분** | **0.9901** |

**해석**: 레이스 초반 10K 기록만으로도 완주 시간을 평균 **±4분** 오차로 예측합니다. R² 0.990 수준으로, 초반 페이스 설정이 최종 기록과 매우 강한 상관성을 가짐을 확인합니다.

---

## 모델 성능 로그

```
=== Full Model ===
Ridge               RMSE = 1.62 min (97s)   R² = 0.9983
Lasso               RMSE = 1.65 min (99s)   R² = 0.9983
Random Forest       RMSE = 1.66 min (99s)   R² = 0.9983

=== Early Prediction (10K 기준) ===
Ridge (Early)       RMSE = 5.37 min         R² = 0.9821
RF (Early)          RMSE = 3.99 min         R² = 0.9901
```

---

## Random Forest 피처 중요도

| 순위 | 피처 | 중요도 |
|------|------|--------|
| 1 | `30K_s` (30K 누적 기록) | **0.9659** |
| 2 | `Fatigue_Index` | 0.0298 |
| 3 | `25K_s` | 0.0009 |
| 4 | `10K_s` | 0.0008 |
| 5 | `Half_s` | 0.0007 |
| 6–11 | 나머지 구간 기록, Age, Gender | < 0.001 |

**주요 발견**: 30K 구간 기록이 전체 예측력의 96.6%를 차지합니다. 30K까지 어떤 속도로 달렸는지가 최종 기록을 거의 결정한다는 의미입니다. Fatigue Index(피로도 지수)가 두 번째 중요 변수로, 페이스 관리의 중요성을 뒷받침합니다.

---

## 예측 정확도 분석

Ridge Full Model의 잔차(Residual) 분포는 평균 0 근처에서 대칭적인 정규분포를 보이며, 이는 모델이 체계적인 편향 없이 잘 작동하고 있음을 나타냅니다.

```
잔차 분포:
  - 95% 구간: ±3분 이내
  - 5분 이상 오차: 전체의 약 2%
```

---
