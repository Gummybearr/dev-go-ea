# EA Part 2 오답노트 템플릿

기준일: 2026-04-24

이 템플릿은 Part 2 오답을 `entity / form / basis / reporting path` 중심으로 남기기 위한 용도다.

## 사용 원칙

- 한 문제당 `3~6줄`
- 계산 전체보다 `어느 규칙을 놓쳤는지`만 적는다
- 아래 4개는 가능하면 매번 적는다:
  - entity
  - tax level
  - form
  - trigger next time
- 오답은 아래 3개 중 하나로 태그한다:
  - `business-entities`
  - `business-tax-preparation`
  - `specialized-returns-taxpayers`

## 가장 짧은 기본 템플릿

```md
### [날짜] [문제번호 또는 출처]
- Domain:
- Entity:
- Topic:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
```

## 권장 템플릿

```md
### 2026-06-02 | Q34 | Mixed Set B
- Domain: business-entities
- Entity: S corporation
- Topic: shareholder basis and loss limitation
- Question type: basis before deducting loss
- My wrong choice: C
- Why I missed it: flow-through라는 것만 보고 shareholder basis를 확인하지 않음
- Correct rule: S corp loss question은 보통 shareholder basis 또는 loan basis를 먼저 확인한다
- Trigger next time: S corp loss -> basis first
- Form / Schedule: Form 1120S / K-1
- Confidence after review: low / medium / high
- Review again on: 2026-06-04
```

## 복붙용 빈 템플릿 10개

```md
### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:

### YYYY-MM-DD | Q__ | Source:
- Domain:
- Entity:
- Topic:
- Question type:
- My wrong choice:
- Why I missed it:
- Correct rule:
- Trigger next time:
- Form / Schedule:
- Confidence after review:
- Review again on:
```

## 자주 나오는 `Question type` 예시

- entity classification
- partnership basis
- guaranteed payment vs distributive share
- C corp distribution / E&P
- section 351 formation
- S corp qualification
- shareholder basis
- COGS vs deduction
- capitalize vs repair
- depreciation / section 179 / bonus
- Form 4797 disposition
- accounting method change / Form 3115
- DNI / Form 1041
- UBTI / Form 990
- passive loss limitation

## `Why I missed it`를 쓰는 방식

나쁜 예:

- 헷갈림
- 계산 실수
- 개념 부족

좋은 예:

- entity를 partnership으로 봐야 하는데 S corp처럼 읽었다
- distribution 문제인데 E&P를 보지 않았다
- deduction인지 capitalization인지 먼저 구분하지 않았다
- 4797가 아니라 4562처럼 읽었다
- trust 문제에서 DNI를 놓쳤다

## `Trigger next time`를 쓰는 방식

좋은 예:

- `파트너십 손실 -> basis and K-1 first`
- `C corp distribution -> E&P first`
- `S corp loss -> shareholder basis first`
- `asset sale -> 4797 first`
- `method change -> 3115`
- `trust question -> DNI first`

## 주간 리뷰 템플릿

```md
## Week __ Review
- Total wrong answers:
- Most missed domain:
- Most missed entity/form:
- Most repeated trap:
- Rule I will re-read tomorrow:
- 3 triggers to memorize:
  - 
  - 
  - 
```

## 약점 추적표

```md
| Domain | Topic | Mistakes | Last Reviewed | Confidence |
|---|---|---:|---|---|
| business-entities | partnership basis | 0 | | |
| business-entities | S corp qualification | 0 | | |
| business-tax-preparation | depreciation cluster | 0 | | |
| business-tax-preparation | capitalize vs repair | 0 | | |
| specialized-returns-taxpayers | DNI / Form 1041 | 0 | | |
| specialized-returns-taxpayers | rental passive loss | 0 | | |
```

## 시험 직전 오답 압축 규칙

- `low confidence`만 남긴다
- 2번 이상 반복된 실수만 최종노트로 올린다
- 최종노트에는 `rule 문장 + trigger 문장`만 남긴다

예:

```md
- Partnership loss: basis and K-1 first
- C corp distribution: E&P first
- S corp loss: shareholder basis first
- Asset sale: think 4797
- Method change: think 3115
- Trust question: think DNI
```
