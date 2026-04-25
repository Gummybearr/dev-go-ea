# EA Part 1 Week 1 Day 1 Masterclass 05: Gross Income, FBAR, and Form 8938

기준일: 2026-04-24  
대상 문제: 79-100  
목표: 들어온 value를 `taxable first`로 보고, `FBAR`와 `Form 8938`을 filing location 기준으로 구분한다.

## 한 줄 결론

`Gross income`은 taxable first, exclusion second.  
`FBAR`는 FinCEN/BSA E-Filing.  
`Form 8938`은 required이면 income tax return에 attach.

## Gross income의 기본 원칙

Publication 525의 기본 감각은 간단하다.

`Income is taxable unless specifically excluded by law.`

시험에서는 이렇게 바꿔 말한다.

`Value came in? Taxable candidate first. Then look for exclusion.`

돈, property, services가 들어오면 일단 gross income 후보로 본다. 그 다음 gift, inheritance, child support, life insurance death proceeds 같은 specific exclusion이 있는지 본다.

## Money, property, services

Income은 cash만이 아니다.

| 받은 것 | Day 1 판단 |
|---|---|
| money | taxable candidate |
| property | value를 봄 |
| services | value를 봄 |
| barter | FMV를 income으로 볼 수 있음 |

`FMV`는 `Fair Market Value`다. services 대가로 property나 services를 받으면 FMV가 중요해진다.

## Compensation은 이름표가 아니라 이유로 판단한다

시험에서 가장 흔한 함정은 gift와 compensation을 섞는 것이다.

누군가 property를 줬다고 해서 항상 gift가 아니다.

질문은 이것이다.

`Why did the taxpayer receive it?`

서비스를 제공했기 때문에 받았으면 compensation이다. `gift`라고 불러도 실질이 services 대가이면 taxable compensation 후보로 본다.

예:

Lawyer가 client에게 legal services를 제공했고, client가 painting worth $2,000을 줬다.

이건 true gift가 아니라 services 대가다. 일반적으로 FMV 기준 taxable compensation이다.

## Taxable로 보는 대표 항목

Day 1에서는 아래 항목을 taxable candidate로 잡는다.

| 항목 | 판단 |
|---|---|
| wages | taxable compensation |
| employer cash bonus | taxable compensation |
| cash gift card from employer | taxable compensation 후보 |
| property for services | FMV taxable compensation |
| barter services | FMV taxable income |
| illegal income | taxable |
| bribe | taxable |
| gambling winnings | taxable |
| unemployment compensation | taxable |

핵심은 moral judgment가 아니다. illegal income도 income이면 taxable이다.

## Excluded로 보는 대표 항목

아래 항목은 일반적으로 recipient gross income에서 excluded되는 방향으로 본다.

| 항목 | 판단 |
|---|---|
| true gift from parent | generally excluded |
| inheritance | generally excluded |
| child support received | generally not taxable to recipient |
| life insurance proceeds received by reason of death | generally excluded |

주의: exclusion은 specific rule이 있을 때만 적용한다. `gift`처럼 보여도 services 대가이면 compensation이다.

## 문제 79-95 연결

| 문제 | 포인트 | 반응 |
|---|---|---|
| 79 | Pub. 525 basic rule | taxable unless specifically exempted |
| 80 | painting for legal services | taxable compensation at FMV |
| 81 | FMV 약어 | Fair Market Value |
| 82 | true gift from parent | excluded |
| 83 | illegal income | included |
| 84 | gambling winnings | taxable |
| 85 | life insurance death proceeds | generally excluded |
| 86 | child support received | not taxable to recipient |
| 87 | inheritance | excluded |
| 88 | employer cash bonus | taxable compensation |
| 89 | barter services | barter income |
| 90 | employer cash gift card | taxable compensation |
| 91 | bribe | included |
| 92 | unemployment compensation | taxable |
| 93 | not taxable item | true gift from parent |
| 94 | compensation in property | included at FMV |
| 95 | taxable unless excluded mindset | money, property, services |

## 1타 강사식 income 판단 템플릿

Gross income 문제는 이 순서로 말하면서 푼다.

1. `Taxpayer received value?`
2. `Money, property, or services?`
3. `Why received? Services? employment? prize? illegal?`
4. `Taxable candidate first.`
5. `Specific exclusion이 있는가?`
6. `Gift처럼 보여도 compensation이면 taxable.`

## FBAR 기본

`FBAR`는 `Report of Foreign Bank and Financial Accounts`다.

FBAR는 income tax return에 붙이는 schedule이 아니다. Required이면 FinCEN의 BSA E-Filing System을 통해 electronic filing한다.

`FinCEN`은 `Financial Crimes Enforcement Network`다.  
`BSA`는 `Bank Secrecy Act`다.

Day 1 기준으로 기억할 threshold:

`aggregate value of foreign financial accounts exceeds $10,000 at any time during the calendar year`

즉 calendar year 중 어느 시점이든 foreign financial accounts aggregate value가 $10,000을 초과하면 FBAR issue가 생긴다.

## Form 8938 기본

`Form 8938`은 `Statement of Specified Foreign Financial Assets`다.

Required이면 annual income tax return에 attach한다.

중요한 점:

`Form 8938 does not replace FBAR.`

둘은 filing location도 다르고, requirement도 다를 수 있다. 둘 다 해당하면 둘 다 검토해야 한다.

## FBAR vs Form 8938

| 항목 | FBAR | Form 8938 |
|---|---|---|
| 무엇인가 | Report of Foreign Bank and Financial Accounts | Statement of Specified Foreign Financial Assets |
| 어디에 file | FinCEN BSA E-Filing | income tax return에 attach |
| Form 1040 schedule인가 | 아니다 | required이면 tax return attachment |
| 서로 대체하는가 | 아니다 | 아니다 |

## 문제 96-100 연결

| 문제 | 포인트 | 반응 |
|---|---|---|
| 96 | FBAR 약어 | Report of Foreign Bank and Financial Accounts |
| 97 | FBAR filing location | FinCEN BSA E-Filing |
| 98 | Form 8938 | attached to annual income tax return when required |
| 99 | Form 8938 vs FBAR | does not replace FBAR |
| 100 | FBAR threshold | over $10,000 at any time during calendar year |

## Mini Lecture Example 1: Property for services

Facts: Taxpayer performs accounting services and receives legal services in exchange.

분석:

1. Taxpayer received value.
2. Value is services, not cash.
3. It was received in exchange for taxpayer's services.
4. This is barter income.
5. FMV of services received is generally taxable.

결론: Cash가 없어도 income이 될 수 있다.

## Mini Lecture Example 2: FBAR and Form 8938

Facts: Taxpayer has foreign bank accounts over the FBAR threshold and also has specified foreign financial assets requiring Form 8938.

분석:

1. Foreign financial account가 있다.
2. FBAR threshold를 본다.
3. FBAR는 required이면 FinCEN BSA E-Filing으로 간다.
4. Form 8938은 required이면 tax return에 attach한다.
5. 하나가 다른 하나를 없애지 않는다.

결론: FBAR와 Form 8938은 따로 본다.

## 5분 Drill

1. Gross income은 taxable first인가, excluded first인가?
2. Services 대가로 받은 painting은 true gift인가, compensation인가?
3. FMV는 무엇의 약어인가?
4. Illegal income은 일반적으로 taxable인가?
5. FBAR는 Form 1040에 attach하는가, FinCEN BSA E-Filing으로 file하는가?
6. Form 8938 filing이 FBAR obligation을 없애는가?

정답:

1. taxable first
2. compensation
3. Fair Market Value
4. taxable
5. FinCEN BSA E-Filing
6. 아니다

## 30초 Recap

Gross income은 taxable first, exclusion second다. Money, property, services가 들어오면 taxable candidate로 본다. Services 대가로 받은 property는 FMV 기준 compensation이다. True gift, inheritance, child support, certain life insurance death proceeds는 generally excluded 방향이다. FBAR는 FinCEN BSA E-Filing이고, Form 8938은 required이면 tax return에 attach한다. Form 8938은 FBAR를 replace하지 않는다.

## Sources Used

- IRS Publication 525: https://www.irs.gov/publications/p525
- IRS Form 8938 vs FBAR comparison: https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements
- IRS SEE Sample Questions Part 1: https://www.irs.gov/tax-professionals/enrolled-agents/see-sample-test-questions-part-1
