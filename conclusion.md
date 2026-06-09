---
title: VI. Conclusion
layout: default
nav_order: 7
---

# VI. Conclusion

---

## Discussion

### Insight

**Hitting the Wall의 보편성**

30K 이후 구간에서 거의 모든 러너 그룹에서 페이스 저하가 관찰되었으며, 이는 나이·성별과 무관하게 나타나는 생리적 한계(글리코겐 고갈)에 따른 것으로 판단할 수 있다. 다만 그 정도는 초반 페이스 전략과 강한 상관관계를 보였다.

**기온의 비선형적 영향**

기온이 높을수록 완주 시간이 증가하는 경향이 나타났으나, 단순 선형 관계가 아니라 특정 임계 온도 이상에서 기록 저하가 급격해지는 패턴이 관찰되었다. 이는 heat stress가 인체의 운동 수행 능력에 미치는 비선형적 영향을 반영한다.

**앙상블 모델의 우위**

Ridge/Lasso 등 선형 회귀 모델 대비 XGBoost·LightGBM이 유의미하게 높은 예측 정확도를 보였다. 이는 구간 페이스 데이터 간의 복잡한 상호작용이 비선형 모델에서 더 효과적으로 포착됨을 시사한다.

**Fatigue Index의 예측력**

파생 변수로 설계한 Fatigue Index가 단순 구간 시간 원본 변수보다 완주 시간 예측에 높은 기여도를 보였다. 이는 "얼마나 빠른가"보다 "페이스를 얼마나 일관되게 유지하는가"가 완주 시간의 핵심 결정 요인임을 의미한다.

## Limitations

- **데이터 편향**: 보스턴 마라톤은 기록 조건(BQ 기준)을 통과한 러너만 참가하므로, 일반 대중 마라톤 참가자에 대한 일반화에 한계가 있다.
- **기상 데이터의 단순화**: 일평균 기온 하나의 변수만 사용했으며, 습도·풍속·일사량 등 복합 기상 요인은 미반영되었다.
- **개인 훈련 이력 부재**: 완주 시간에 가장 큰 영향을 미칠 수 있는 훈련량·주간 주행거리·대회 경험 횟수 등 사전 정보가 데이터셋에 존재하지 않는다.
- **연도별 코스 조건**: 보스턴 코스는 연도별로 날씨 편차가 크며, 코스 내 고도 변화(Heartbreak Hill 등)는 구간 페이스에 영향을 주지만 이를 보정하는 변수가 포함되지 않았다.

## Future Work

- 다른 대규모 마라톤(뉴욕, 시카고, 베를린) 데이터와 결합해 모델의 범용성을 검증한다.
- humidity · Wet Bulb Temperature 등 복합 기상 지수를 환경 변수로 추가한다.
- 구간 페이스 시퀀스를 시계열로 처리하는 LSTM 기반 모델을 실험해 예측 정확도를 개선한다.
- 예측 모델을 기반으로 목표 완주 시간에 최적화된 구간별 페이스 플랜을 역산하는 추천 시스템으로 확장한다.

## Contributions

| 멤버 | 이메일 | 담당 |
| --- | --- | --- |
| 양종빈 | goldon102@gmail.com | 데이터 & 전처리 — 결측치 처리, 시간 변환, 인코딩 등 파이프라인 구축 |
| 성시훈 | sihun0415@gmail.com | EDA & 시각화 — 나이/성별/기온 분석, Hitting the Wall 시각화, 구간 페이스 패턴 탐색 |
| 김병준 | kmbzn24@gmail.com | Blog 프론트 디자인, Feature Engineering & 모델링 — Fatigue Index 설계, Ridge/Lasso/RF/XGBoost/LightGBM 학습 및 튜닝 |
| 임성현 | beo00325@gmail.com | 평가 & 인사이트 — RMSE/R² 비교, 페이스 전략 도출, 문서화 |

## 🎥 Video

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; margin: 1em 0;">
  <iframe src="https://www.youtube.com/embed/VIDEO_ID"
          title="발표 영상"
          style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen></iframe>
</div>
