---
title: II. Datasets
layout: default
nav_order: 3
---

# II. Datasets
{: .no_toc }

<details open markdown="block">
  <summary>목차</summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

본 프로젝트는 Kaggle에 공개된 **Boston Marathon Dataset**을 기반으로 합니다.
해당 데이터셋은 2015–2017년 보스턴 마라톤 공식 기록을 포함하며,
러너의 인구통계학적 정보, 구간별 통과 시간, 대회 당일 기상 조건을 담고 있습니다.

- **출처**: [Kaggle — Boston Marathon Dataset](https://www.kaggle.com/datasets/rojour/boston-results)
- **수록 연도**: 2015, 2016, 2017
- **총 레코드 수**: 약 75,000건 (연도별 합산, DNF 포함)
- **라이선스**: CC0 (Public Domain)

---

## 1. Demographic Data

러너의 기본 신상 정보로, 완주 시간과의 인구통계학적 상관관계 분석에 활용됩니다.

| 변수명 | 타입 | 설명 |
|---|---|---|
| `Age` | Numeric | 러너의 만 나이 |
| `M/F` | Categorical | 성별 (`M` / `F`) |
| `Country` | Categorical | 국적 (ISO 국가 코드) |
| `State` | Categorical | 거주 지역 (미국 주 코드, 해외 참가자는 공란) |

---

## 2. In-Race Split Times

42.195km 코스 내 9개 구간의 통과 시간으로, 페이스 분석 및 Fatigue Index 산출의 핵심 변수입니다.
모든 구간 시간은 `HH:MM:SS` 문자열로 수록되며, 전처리 단계에서 seconds 단위 정수형으로 변환합니다.

| 변수명 | 거리 | 비고 |
|---|---|---|
| `5K` | 5km | — |
| `10K` | 10km | Fatigue Index 기준 구간 (초반) |
| `15K` | 15km | — |
| `20K` | 20km | — |
| `Half` | 21.0975km | 중간 기록 |
| `25K` | 25km | — |
| `30K` | 30km | Hitting the Wall 기준 구간 |
| `35K` | 35km | 페이스 저하 집중 관찰 구간 |
| `40K` | 40km | — |
| `Official Time` | 42.195km | Target Variable |

---

## 3. Environmental Data

대회 당일 기상 조건으로, 연도별로 단일 값이 적용됩니다.
기온이 러너의 후반부 페이스 저하에 미치는 영향 분석에 활용됩니다.

| 변수명 | 타입 | 설명 |
|---|---|---|
| `Temperature` | Numeric | 대회 당일 평균 기온 (°C) |
| `Weather` | Categorical | 기후 조건 (맑음, 흐림, 우천 등) |

> 기온은 연도별로 상이하며, 2012년 대회(기온 26°C)처럼 극단적 고온 사례가 기록 저하와의 연관성 분석에 중요한 참조점이 됩니다.

---

## 4. Target Variable

| 변수명 | 타입 | 설명 |
|---|---|---|
| `Official Time` | Numeric (변환 후) | 최종 마라톤 완주 시간. 원본은 `HH:MM:SS` 문자열이며, 분석 시 초 단위 정수형으로 변환하여 사용 |

DNF(Did Not Finish) 참가자는 `Official Time`이 결측값으로 처리되며,
예측 모델 학습 시 해당 레코드는 제외합니다.

---

## 5. Sample Data

아래는 데이터셋의 샘플 행입니다 (일부 컬럼 발췌).

| M/F | Age | Country | 10K | Half | 30K | 40K | Official Time |
|---|---|---|---|---|---|---|---|
| M | 34 | USA | 0:42:11 | 1:29:02 | 2:14:38 | 3:01:52 | 3:10:45 |
| F | 28 | KEN | 0:38:54 | 1:22:17 | 2:03:10 | 2:44:20 | 2:52:11 |
| M | 47 | JPN | 0:51:03 | 1:47:29 | 2:45:11 | 3:38:04 | 3:51:22 |
| F | 55 | USA | 0:58:44 | 2:04:15 | 3:10:07 | 4:11:30 | 4:24:09 |
| M | 22 | ETH | 0:37:22 | 1:19:03 | 1:58:44 | 2:38:15 | 2:46:03 |

> *위 수치는 예시이며, 실제 데이터셋의 값과 다를 수 있습니다.*
> *실제 샘플은 `data/` 디렉토리의 원본 CSV를 참조하세요.*
