# EA Part 1 Week 1 Day 1 Masterclass 01: Form 1040 Flow

기준일: 2026-04-24  
대상 문제: 1-10  
목표: `Form 1040`을 줄 번호가 아니라 흐름으로 이해한다.

## 한 줄 결론

`Form 1040`은 돈이 들어온 곳에서 시작해서 최종적으로 refund인지 balance due인지 결정하는 계산 지도다.

외울 문장:

`Gross income -> Adjustments -> AGI -> Deductions -> Taxable income -> Tax -> Credits -> Other taxes -> Payments -> Refund or balance due`

이 순서를 외우면 문제 1-10은 단순 암기가 아니라 구조 문제로 보인다.

## 왜 Form 1040 flow가 먼저인가

EA Part 1은 individual tax다. individual tax의 중심은 `Form 1040`, 즉 `U.S. Individual Income Tax Return`이다.

시험 문제는 어떤 항목을 던지고 묻는다.

`이건 income인가?`  
`AGI 전에 빠지는가?`  
`taxable income을 줄이는가?`  
`tax를 직접 줄이는가?`  
`이미 낸 tax payment인가?`  
`refund가 나오는가?`

이 질문들은 모두 Form 1040 flow 안에서 움직인다.

## 단계별로 머리에 넣기

### 1. Gross income

`Gross income`은 출발점이다. 돈, property, services처럼 value가 들어오면 일단 gross income 후보로 본다.

Day 1에서는 이렇게만 잡는다.

`Something came in. Is it income?`

나중에 exclusion을 배우더라도 출발점은 taxable 후보로 잡아야 한다. 그래야 gift, inheritance, child support 같은 exclusion도 정확히 보인다.

### 2. Adjustments to income

`Adjustments to income`은 AGI 전에 빠지는 항목이다.

문제 1에서 묻는 핵심이 이것이다. gross income 다음, AGI 전에 오는 것은 `adjustments to income`이다.

Day 1에서는 세부 adjustment를 다 외우는 날이 아니다. 위치만 정확히 잡는다.

`Adjustment`는 AGI를 만들기 전에 들어간다.

### 3. AGI

`AGI`는 `Adjusted Gross Income`의 약어다.

AGI는 단순한 중간 숫자가 아니다. 뒤의 여러 deduction, credit, limitation에서 기준점으로 자주 쓰인다.

문제에서 `starting point for limits`, `deduction limitation`, `credit eligibility`, `phaseout` 같은 표현이 보이면 AGI를 떠올린다.

### 4. Deductions

`Deduction`은 taxable income을 줄인다.

시험 초반에는 deduction과 credit을 반드시 구분한다.

`Deduction reduces taxable income.`  
`Credit reduces tax.`

Deduction은 tax 자체를 바로 깎는 것이 아니다. taxable income을 줄인 뒤 tax 계산에 영향을 준다.

### 5. Taxable income

`Taxable income`은 tax rate을 적용할 금액이다.

gross income에서 adjustments를 거쳐 AGI가 나오고, deduction을 빼면 taxable income으로 간다.

### 6. Tax

`Tax`는 taxable income에 세율을 적용해서 계산되는 regular tax를 생각하면 된다.

그 다음 credit과 other tax가 붙는다.

### 7. Credits

`Credit`은 tax를 직접 줄인다.

Deduction보다 훨씬 직접적이다.

예를 들어 tax가 $1,000인데 credit이 $300이면 tax가 $700으로 줄어드는 식이다. Day 1에서는 refundable/nonrefundable의 깊은 계산보다, credit의 위치를 잡는다.

### 8. Other taxes

`Other taxes`는 regular income tax 외에 붙는 tax다.

Form 1040에서 `Schedule 2`와 연결해서 생각한다. 문제 5의 핵심도 `Schedule 2 = additional taxes`다.

### 9. Payments

`Payments`는 이미 낸 tax다. withholding, estimated tax payments 같은 것들이 여기에 들어간다.

문제 9에서 `payments`는 amounts already paid toward tax와 연결된다.

### 10. Refund or balance due

마지막은 간단하다.

`Payments > total tax`이면 보통 refund.  
`Payments < total tax`이면 balance due.

문제 10은 이 구조를 묻는다.

## Schedule 1, Schedule 2, Schedule 3

Day 1에서는 세 개만 확실히 구분한다.

| Schedule | 의미 | 시험식 반응 |
|---|---|---|
| `Schedule 1` | additional income and adjustments to income | income/adjustment bucket |
| `Schedule 2` | additional taxes | regular tax 외 추가 tax |
| `Schedule 3` | additional credits and payments | credit/payment bucket |

암기 문장:

`1은 income and adjustments.`  
`2는 taxes.`  
`3은 credits and payments.`

이렇게 숫자와 역할을 붙인다.

## Deduction vs Credit

이 구분은 Day 1에서 반드시 잡는다.

| 항목 | 줄이는 것 | 느낌 |
|---|---|---|
| `Deduction` | taxable income | tax 계산 전의 base를 줄임 |
| `Credit` | tax | 계산된 tax를 직접 줄임 |

문제에서 `reduces taxable income`이면 deduction.  
문제에서 `reduces tax directly`이면 credit.

## 문제 1-10 연결

| 문제 | 묻는 포인트 | 반응 |
|---|---|---|
| 1 | gross income과 AGI 사이 | adjustments to income |
| 2 | AGI 약어 | Adjusted Gross Income |
| 3 | limitations의 기준 subtotal | AGI |
| 4 | Schedule 1 | additional income and adjustments |
| 5 | Schedule 2 | additional taxes |
| 6 | Schedule 3 | additional credits and payments |
| 7 | deduction | reduces taxable income |
| 8 | credit | reduces tax directly |
| 9 | payments | tax toward already paid |
| 10 | payments exceed tax | refund |

## 함정 정리

### 함정 1: deduction과 credit을 같은 것으로 보는 것

둘은 위치가 다르다. deduction은 taxable income을 줄이고, credit은 tax를 줄인다.

### 함정 2: AGI를 최종 tax로 착각하는 것

AGI는 final tax가 아니다. AGI 뒤에 deductions, taxable income, tax, credits, other taxes, payments가 더 있다.

### 함정 3: Schedule 2와 Schedule 3를 섞는 것

`Schedule 2`는 additional taxes.  
`Schedule 3`는 additional credits and payments.

2는 tax 쪽, 3은 credit/payment 쪽이라고 붙인다.

## Mini Lecture Example

Facts: Taxpayer has wages, then claims an allowable adjustment, then takes the standard deduction, then applies a credit, then has withholding.

분석:

1. wages는 gross income에서 시작한다.
2. allowable adjustment는 AGI 전에 빠진다.
3. AGI가 나온다.
4. standard deduction이 taxable income을 줄인다.
5. tax가 계산된다.
6. credit이 tax를 직접 줄인다.
7. withholding은 payment로 들어간다.
8. total payments와 total tax를 비교해서 refund 또는 balance due가 나온다.

이 예시 하나에 Day 1 Form 1040 flow가 다 들어 있다.

## 5분 Drill

정답을 고르기 전에 각 문장 옆에 Form 1040 위치를 적는다.

1. `Adjusted Gross Income`은 무엇의 약어인가?
2. `Deduction`은 tax를 직접 줄이는가, taxable income을 줄이는가?
3. `Credit`은 tax를 직접 줄이는가, gross income을 줄이는가?
4. `Schedule 2`는 additional taxes인가, additional credits인가?
5. Payments가 total tax보다 크면 일반적으로 refund인가, balance due인가?

정답:

1. `AGI`
2. taxable income
3. tax directly
4. additional taxes
5. refund

## 30초 Recap

Form 1040 flow는 Day 1의 큰 도로다. `gross income`으로 시작해서 `adjustments`, `AGI`, `deductions`, `taxable income`, `tax`, `credits`, `other taxes`, `payments`, `refund or balance due`로 간다.

`Schedule 1`은 income and adjustments. `Schedule 2`는 additional taxes. `Schedule 3`는 additional credits and payments.

`Deduction`은 taxable income을 줄이고, `credit`은 tax를 직접 줄인다.

## Sources Used

- IRS About Form 1040: https://www.irs.gov/forms-pubs/about-form-1040
- IRS SEE Sample Questions Part 1: https://www.irs.gov/tax-professionals/enrolled-agents/see-sample-test-questions-part-1
