# EA Part 1 Week 1 Day 1 Deep Dive

기준일: 2026-04-24  
대상: EA Part 1 첫날, 하루 `5시간` 학습  
원본 노트: `part-1-week-1-day-1.md`

이 파일은 `Week 1 Day 1` 내용을 세부적으로 이해하기 위한 보강 노트다. 설명은 한국어로 하되, 시험에서 실제로 만나게 될 핵심 용어는 영어로 유지한다. 예를 들어 `filing status`, `dependent`, `qualifying child`, `qualifying relative`, `gross income`, `AGI`, `standard deduction`, `credit` 같은 말은 그대로 익힌다.

학습 방향은 하나다.

`Form first, taxpayer second, rule third.`

문제를 보자마자 세부 규정으로 뛰어들지 말고, 먼저 `Form 1040`에서 어디에 들어가는 문제인지 본다. 그 다음 누가 신고하는지, 어떤 `filing status`인지, `dependent`가 있는지 확인한다. 마지막에 세부 rule을 적용한다.

## 0. 먼저 풀어둘 약어와 핵심 용어

Day 1부터 약어가 계속 나온다. 처음에는 약어만 외우지 말고, 풀어쓴 말과 의미를 같이 잡는다.

| 약어 / 용어 | 풀어쓴 말 | 의미 |
|---|---|---|
| `EA` | `Enrolled Agent` | IRS 앞에서 납세자를 대리할 수 있는 연방 세무 전문가 자격 |
| `IRS` | `Internal Revenue Service` | 미국 연방 세무 당국 |
| `Form 1040` | U.S. Individual Income Tax Return | 개인 납세자의 기본 income tax return |
| `AGI` | `Adjusted Gross Income` | `gross income`에서 certain adjustments를 뺀 중간 subtotal |
| `MFJ` | `Married Filing Jointly` | 부부가 joint return을 filing하는 status |
| `MFS` | `Married Filing Separately` | married taxpayers가 separate return을 filing하는 status |
| `HOH` | `Head of Household` | unmarried 또는 considered unmarried taxpayer가 qualifying person 등 요건을 충족할 때 쓰는 status |
| `QSS` | `Qualifying Surviving Spouse` | 배우자 사망 후 일정 요건을 충족할 때 제한적으로 쓰는 status |
| `QC` | `Qualifying Child` | dependent 판단의 첫 번째 category |
| `QR` | `Qualifying Relative` | qualifying child가 아니면 검토하는 dependent category |
| `FMV` | `Fair Market Value` | 공정시장가치. property received for services 같은 문제에서 income amount를 잡을 때 중요 |
| `FBAR` | `Report of Foreign Bank and Financial Accounts` | foreign financial accounts가 일정 기준을 넘을 때 FinCEN에 하는 보고 |
| `FinCEN` | `Financial Crimes Enforcement Network` | FBAR를 받는 Treasury bureau |
| `BSA` | `Bank Secrecy Act` | FBAR filing system 이름에 나오는 법적 체계 |

이 노트에서는 처음에는 `Adjusted Gross Income, 즉 AGI`처럼 풀어 쓰고, 그 뒤부터는 `AGI`라고 부른다.

## 1. Day 1의 목표

Day 1은 세법 전체를 외우는 날이 아니다. 오늘은 아래 3개를 잡는 날이다.

- `Form 1040`의 큰 흐름
- `filing status`의 판단 순서
- `dependent`를 `qualifying child`와 `qualifying relative`로 나누는 감각

시험 초반 문제는 계산보다 분류가 중요하다. `이게 income 문제인가`, `filing status 문제인가`, `dependent 문제인가`, `credit eligibility 문제인가`를 먼저 알아야 한다.

## 2. Form 1040 흐름

`Form 1040`은 개인 납세자의 annual income tax return이다. Day 1에서는 line number를 다 외울 필요는 없고, 흐름을 외워야 한다.

기본 흐름은 아래와 같다.

`Gross income -> Adjustments -> AGI -> Deductions -> Taxable income -> Tax -> Credits -> Other taxes -> Payments -> Refund or balance due`

여기서 `AGI`는 `Adjusted Gross Income`이다. `gross income`에서 법이 허용하는 certain adjustments를 뺀 중간 subtotal이라고 보면 된다.

| 단계 | 핵심 질문 | Day 1에서 잡을 감각 |
|---|---|---|
| `Gross income` | 이 항목이 원칙적으로 income인가 | 돈이나 가치가 들어오면 일단 taxable 후보로 본다 |
| `Adjustments` | `AGI`, 즉 `Adjusted Gross Income` 전에 빠지는가 | 자세한 규칙은 Week 2에서 하고, 위치만 익힌다 |
| `AGI` | 이후 제한 규정의 기준 숫자인가 | 여러 deduction/credit 제한의 출발점이다 |
| `Deductions` | `standard deduction`인가 `itemized deduction`인가 | `filing status`가 standard deduction에 영향을 준다 |
| `Taxable income` | 세율을 적용할 금액인가 | income에서 deduction을 뺀 결과다 |
| `Tax` | regular tax가 얼마인가 | 이후 credit이 이 tax를 줄인다 |
| `Credits` | tax를 직접 줄이는가 | deduction보다 직접적이다 |
| `Other taxes` | regular tax 외 추가 tax가 있는가 | `Schedule 2`를 떠올린다 |
| `Payments` | 이미 낸 세금이 있는가 | withholding, estimated payments 등이다 |
| `Refund or balance due` | 돌려받는가, 더 내는가 | 최종 결론이다 |

## 3. Schedule 1, Schedule 2, Schedule 3

Day 1에서는 아래 3개만 구분하면 충분하다.

| Schedule | 역할 | 기억법 |
|---|---|---|
| `Schedule 1` | additional income and adjustments | Form 1040 본문에 다 못 담는 income과 AGI 전 조정 |
| `Schedule 2` | additional taxes | regular tax 외 추가 tax |
| `Schedule 3` | additional credits and payments | 추가 credit과 payment |

예를 들어 `unemployment compensation`, `gambling winnings`, `student loan interest`, `self-employment tax`, `education credit`, `foreign tax credit` 같은 말이 나오면 Form 1040 본문만 보지 말고 어떤 schedule로 연결되는지 생각한다.

## 4. 문제 읽는 순서

Day 1 문제는 대부분 아래 순서로 처리한다.

1. 누가 return을 filing하는가?
2. `marital status`는 보통 `December 31` 기준으로 무엇인가?
3. 가능한 `filing status`는 무엇인가?
4. `Head of Household` 가능성이 있으면 home cost와 qualifying person을 본다.
5. `dependent`가 있으면 먼저 `qualifying child`인지 `qualifying relative`인지 나눈다.
6. income이 들어오면 먼저 taxable 후보로 보고, 특정 exclusion이 있는지 찾는다.
7. 이 이슈가 `Form 1040`, `Schedule 1`, `Schedule 2`, `Schedule 3`, 또는 별도 form 중 어디로 가는지 연결한다.

이 순서가 중요한 이유는 `filing status`와 `dependent`가 뒤의 `standard deduction`, tax rate, credit eligibility에 계속 영향을 주기 때문이다.

## 5. Filing Status

`Filing status`는 단순한 이름표가 아니다. 신고의 출발점이고, 아래 항목에 영향을 준다.

- filing requirement
- `standard deduction`
- tax rate structure
- credit eligibility
- final tax amount

### 5.1 기본 5개 status

| Status | 기본 의미 | Day 1 포인트 |
|---|---|---|
| `Single` | 연말 기준 unmarried이고 더 유리한 status가 없음 | 항상 `HOH` 가능성을 한 번 확인한다 |
| `Married Filing Jointly` 또는 `MFJ` | married taxpayers가 joint return filing | 보통 유리하지만 joint liability를 기억한다 |
| `Married Filing Separately` 또는 `MFS` | married taxpayers가 separate return filing | 많은 credit/deduction 제한이 생길 수 있다 |
| `Head of Household` 또는 `HOH` | unmarried 또는 considered unmarried + home cost + qualifying person | 시험 함정이 많다 |
| `Qualifying Surviving Spouse` | 배우자 사망 후 일정 요건 충족 시 제한적으로 사용 | Day 1에서는 존재만 잡는다 |

### 5.2 December 31 rule

시험 기본 감각은 이것이다.

`Marital status is generally determined as of December 31.`

예를 들어 taxpayer가 2025년 11월 30일에 결혼했고 2025년 12월 31일에도 married 상태라면, 2025년 filing status 문제는 married status에서 시작한다. 1년 대부분을 unmarried로 지냈다고 해서 바로 `Single`이 되는 것이 아니다.

Trigger phrase:

- `married late in the year`
- `divorced by December 31`
- `spouse died during the year`
- `lived apart during the last 6 months`
- `legally separated`

이런 표현이 나오면 먼저 `filing status` 문제라고 표시한다.

## 6. Head of Household

`Head of Household`는 Day 1에서 가장 조심해야 할 status다. 말은 쉬운데 요건을 섞기 쉽다.

`HOH`는 `Head of Household`의 약어다. 아래 3개를 함께 본다.

| 요건 | 질문 | 함정 |
|---|---|---|
| Status | taxpayer가 unmarried 또는 considered unmarried인가 | married 상태로 spouse와 같이 살면 보통 HOH가 어렵다 |
| Home cost | taxpayer가 home 유지비의 절반 초과를 냈는가 | home cost와 support를 섞지 않는다 |
| Qualifying person | HOH용 qualifying person이 있는가 | dependent라고 해서 항상 HOH qualifying person은 아니다 |

### 6.1 Home cost와 support는 다르다

| 구분 | 보는 것 | 예시 |
|---|---|---|
| `Cost of keeping up a home` | household 유지 비용 | rent, mortgage interest, real estate tax, utilities, repairs, property insurance, food eaten in the home |
| `Support` | 한 사람을 부양하는 총 비용 | food, lodging, clothing, education, medical care, recreation, transportation |

문제에 `paid more than half the cost of keeping up a home`이 나오면 `HOH`를 떠올린다.  
문제에 `provided more than half of support`가 나오면 `dependent` 문제일 가능성이 크다.

## 7. Dependent 판단

`Dependent` 문제는 반드시 아래 둘로 나눈다.

`Qualifying Child` 또는 `Qualifying Relative`

항상 `qualifying child`를 먼저 본다. 그 사람이 `qualifying child`가 아니면 그 다음 `qualifying relative`를 본다.

줄여서 `Qualifying Child`를 `QC`, `Qualifying Relative`를 `QR`이라고 부르기도 한다. 하지만 초반에는 약어만 보고 넘기지 말고, `QC는 child category`, `QR은 relative/household category`라고 의미를 같이 떠올린다.

## 8. Qualifying Child

`Qualifying Child`는 아래 5개 test로 기억한다.

`Relationship -> Age -> Residency -> Support -> Joint return`

| Test | 질문 | 핵심 |
|---|---|---|
| `Relationship` | taxpayer의 child, stepchild, foster child, sibling, stepsibling 또는 그 descendant인가 | niece, nephew, grandchild도 가능할 수 있다 |
| `Age` | under 19, 또는 full-time student under 24, 또는 permanently and totally disabled인가 | full-time student가 자주 나온다 |
| `Residency` | taxpayer와 half of the year 초과 같이 살았는가 | temporary absence 예외를 나중에 학습한다 |
| `Support` | child가 자기 own support의 half 초과를 스스로 제공하지 않았는가 | 가장 큰 함정 |
| `Joint return` | married child가 joint return을 filing하지 않았는가 | refund-only exception 가능성은 따로 본다 |

### 8.1 QC support test의 핵심

`Qualifying Child support test`는 부모가 child support의 절반 초과를 냈는지 묻는 것이 아니다.

핵심 질문은 이것이다.

`Did the child provide more than half of the child's own support?`

즉 child가 자기 own support의 절반 초과를 스스로 제공했다면 실패한다. 반대로 child가 자기 support의 절반 초과를 제공하지 않았다면, 이 support test는 통과할 수 있다.

예시:

22세 full-time student가 parent와 all year 같이 살았고 자기 own support의 half 초과를 제공하지 않았다면, 다른 제한이 없다면 `qualifying child` 가능성이 있다.

## 9. Qualifying Relative

`Qualifying Relative`는 아래 4개로 기억한다.

`Not a qualifying child -> Member of household or relationship -> Gross income -> Support`

| Test | 질문 | 핵심 |
|---|---|---|
| `Not a qualifying child` | taxpayer 또는 다른 taxpayer의 qualifying child가 아닌가 | QC가 먼저다 |
| `Member of household or relationship` | all year 같이 살았거나 listed relative인가 | parent 같은 listed relative는 같이 살지 않아도 가능할 수 있다 |
| `Gross income` | gross income이 threshold 미만인가 | 2025 Publication 501 기준 threshold는 `$5,200` |
| `Support` | taxpayer가 그 사람 total support의 half 초과를 제공했는가 | QC support와 다르다 |

`Qualifying Relative`는 parent, adult child, relative, 또는 all-year household member 문제에서 자주 나온다.

## 10. QC vs QR 한 줄 구별

가장 중요한 차이는 support test다.

`QC support`, 즉 `Qualifying Child support` = child가 자기 own support의 half 초과를 냈는가?  
`QR support`, 즉 `Qualifying Relative support` = taxpayer가 그 사람 support의 half 초과를 냈는가?

| 항목 | `Qualifying Child` | `Qualifying Relative` |
|---|---|---|
| 판단 순서 | 먼저 본다 | QC가 아니면 본다 |
| Age test | 있음 | 없음 |
| Gross income test | 고정 threshold 없음 | threshold 있음 |
| Residency | 보통 half of year 초과 | all-year household member 또는 listed relative |
| Support | child의 own support를 봄 | taxpayer의 support 제공을 봄 |

## 11. Gross Income과 Exclusion

Day 1의 기본 원칙은 이것이다.

`If value comes in, assume taxable first. Then look for a specific exclusion.`

가치가 들어오면 일단 taxable income 후보로 본다. 그 다음 law가 specific exclusion을 주는지 확인한다.

| 항목 | Day 1 판단 |
|---|---|
| wages | 일반적으로 taxable |
| property received for services | 일반적으로 `FMV`, 즉 `Fair Market Value`로 taxable compensation |
| illegal income | 일반적으로 taxable |
| gambling winnings | 일반적으로 taxable |
| unemployment compensation | taxable 후보 |
| gift from parent | 일반적으로 recipient gross income에서 excluded |
| inheritance | 일반적으로 recipient gross income에서 excluded |
| child support | 일반적으로 recipient에게 taxable 아님 |

가장 흔한 함정은 `gift`와 `compensation`을 섞는 것이다. Client가 lawyer에게 legal services 후 artwork를 줬다면, 단어를 gift라고 불러도 실질은 compensation이다.

## 12. FBAR vs Form 8938

Day 1에서는 아래만 구분한다.

- `FBAR`는 `Report of Foreign Bank and Financial Accounts`의 약어다.
- `FBAR`는 required이면 `FinCEN`, 즉 `Financial Crimes Enforcement Network`의 `BSA E-Filing system`으로 electronic filing한다.
- `Form 8938`은 required이면 income tax return에 attach한다.
- 둘은 서로 대체하지 않는다.

문제에 `foreign bank account`가 나오면 `FBAR`, `Form 8938`, 또는 둘 다인지 구분한다.

## 13. Trigger Table

| Trigger phrase | 먼저 볼 것 |
|---|---|
| `married on November 30` | `filing status`, December 31 status |
| `divorced by year-end` | year-end marital status |
| `spouse died` | MFJ 가능성, qualifying surviving spouse 가능성 |
| `lived apart during last 6 months` | considered unmarried, possible HOH |
| `paid more than half the cost of keeping up the home` | HOH |
| `child lived with taxpayer all year` | qualifying child |
| `22-year-old full-time student` | QC age test |
| `child provided own support` | QC support test |
| `parent did not live with taxpayer` | qualifying relative, possible HOH parent rule |
| `friend lived with taxpayer all year` | QR 가능성은 있지만 HOH qualifying person 주의 |
| `filed joint return only for refund` | joint return exception |
| `foreign bank account` | FBAR vs Form 8938 |
| `gift from parent` | exclusion 후보 |
| `property for services` | taxable compensation 후보 |

## 14. Worked Examples

### Example 1: Late-year marriage

Facts: Taxpayer married on November 30, 2025 and was still married on December 31, 2025.

분석:

1. 이건 `filing status` 문제다.
2. December 31 marital status를 본다.
3. 12월 31일에 married 상태다.
4. 기본 후보는 `MFJ` 또는 `MFS`다. `Single`에서 시작하지 않는다.

결론: filing-status purposes에서는 married status로 시작한다.

### Example 2: Head of Household

Facts: Unmarried taxpayer paid more than half the cost of keeping up a home. Dependent son lived with taxpayer all year.

분석:

1. 이건 `filing status` 문제다.
2. taxpayer는 unmarried다.
3. home cost의 half 초과를 냈다.
4. son은 qualifying person 후보가 될 수 있다.

결론: `Single`보다 `Head of Household`를 먼저 검토한다.

### Example 3: Full-time student

Facts: 22-year-old full-time student lived with parent all year and did not provide more than half of own support.

분석:

1. 이건 `dependent` 문제다.
2. 먼저 `qualifying child`를 본다.
3. child라면 relationship test 가능.
4. full-time student under 24이므로 age test 가능.
5. all year 같이 살았으므로 residency test 가능.
6. child가 own support의 half 초과를 제공하지 않았으므로 support test 가능.

결론: 다른 general limitation이 없다면 `qualifying child`가 될 수 있다.

### Example 4: Parent as dependent

Facts: Taxpayer paid more than half of parent’s support. Parent’s gross income is below the threshold. Parent lives in a separate apartment.

분석:

1. 이건 `dependent` 문제다.
2. parent는 보통 `qualifying child`가 아니므로 `qualifying relative`를 본다.
3. parent는 listed relative라 all-year household member일 필요가 없을 수 있다.
4. gross income threshold를 본다.
5. taxpayer가 total support의 half 초과를 제공했는지 본다.

결론: 요건을 충족하면 parent는 `qualifying relative`가 될 수 있다.

### Example 5: Gift vs compensation

Facts: Lawyer receives artwork worth $2,000 from a client after legal services.

분석:

1. 이건 `gross income` 문제다.
2. 가치 있는 property가 들어왔다.
3. 왜 받았는지 본다.
4. legal services 대가라면 `compensation`이다.

결론: gift exclusion이 아니라 taxable compensation 후보로 본다.

## 15. 5시간 루틴

| 시간 | 할 일 | 산출물 |
|---|---|---|
| 0:00-0:30 | Form 1040 전체 흐름 보기 | `1040 flow map` |
| 0:30-1:10 | filing status 학습 | `Filing status summary table` |
| 1:10-1:50 | HOH 집중 | `HOH 3요건 카드` |
| 1:50-2:00 | 휴식 | 없음 |
| 2:00-2:50 | Publication 501 dependent 파트 읽기 | `QC vs QR comparison table` |
| 2:50-3:40 | filing status/dependent 문제 20문제 | 틀린 문제 표시 |
| 3:40-4:20 | gross income/exclusion 문제 10문제 | taxable/excluded 리스트 |
| 4:20-4:45 | 오답노트 | `Day 1 오답 Top 5` |
| 4:45-5:00 | 소리내어 복습 | 핵심 10문장 암송 |

## 16. 반드시 외울 10문장

1. `Form 1040`은 `gross income`에서 시작해 `refund or balance due`로 끝난다.
2. `Filing status`는 `standard deduction`, tax rate, filing requirement, credit eligibility에 영향을 준다.
3. `Marital status`는 보통 `December 31` 기준으로 판단한다.
4. `Head of Household`는 status, home cost, qualifying person을 모두 본다.
5. `Cost of keeping up a home`과 support of a person은 같은 말이 아니다.
6. `Dependent`는 먼저 `qualifying child`인지 `qualifying relative`인지 가른다.
7. `Qualifying child support test`, 즉 `QC support test`는 child가 own support의 half 초과를 냈는지 본다.
8. `Qualifying relative support test`, 즉 `QR support test`는 taxpayer가 그 사람 support의 half 초과를 냈는지 본다.
9. 가치가 들어오면 먼저 taxable로 의심하고, specific exclusion을 찾는다.
10. `FBAR`와 `Form 8938`은 서로 다른 requirement이고, 하나가 다른 하나를 대체하지 않는다.

## 17. Mini Drill

답을 고르기 전에 각 문제 옆에 주제를 적는다: `filing status`, `dependent`, `gross income`, `form/reporting`.

### Questions

1. A taxpayer married on December 20 and remained married on December 31. What is the best first classification?
   - A. Single
   - B. Married status
   - C. Head of Household automatically
   - D. Dependent

2. Which is part of the Head of Household analysis?
   - A. Whether the taxpayer paid more than half the cost of keeping up the home
   - B. Whether the taxpayer itemized deductions
   - C. Whether the taxpayer had capital gains
   - D. Whether the taxpayer filed Schedule C

3. A 17-year-old child lived with a parent all year and did not provide over half of the child's own support. Which dependent category is checked first?
   - A. Qualifying relative
   - B. Qualifying child
   - C. Nonresident alien
   - D. Surviving spouse

4. Which statement best describes the qualifying child support test?
   - A. The taxpayer must always provide more than half of the child's support
   - B. The child must not have provided more than half of the child's own support
   - C. The child must have zero income
   - D. The parent must pay all education expenses

5. For a qualifying relative, which support statement is generally correct?
   - A. The person must be under age 19
   - B. The person must live with the taxpayer for more than half the year in every case
   - C. The taxpayer generally must provide more than half of the person's support
   - D. The person must be a full-time student

6. Which item is generally excluded from the recipient's gross income?
   - A. Gift from a parent
   - B. Wages
   - C. Gambling winnings
   - D. Property received for services

7. Property received in exchange for services is generally:
   - A. Never taxable
   - B. Taxable compensation measured by value
   - C. Always a gift
   - D. Reported only on FBAR

8. Schedule 2 is most closely associated with:
   - A. Additional taxes
   - B. Filing status
   - C. Dependent relationship test
   - D. Standard deduction only

9. Schedule 3 is most closely associated with:
   - A. Additional credits and payments
   - B. Gross income only
   - C. HOH qualifying person only
   - D. QR gross income test only

10. FBAR is:
   - A. Filed with Form 1040 as a schedule
   - B. A substitute for Form 8938
   - C. Filed electronically through FinCEN/BSA E-Filing when required
   - D. Only for domestic bank accounts

### Answers

1. B. December 31 기준 married status에서 시작한다.
2. A. HOH는 home cost의 half 초과 부담을 본다.
3. B. dependent는 qualifying child를 먼저 본다.
4. B. QC support test는 child의 own support를 본다.
5. C. QR support test는 taxpayer가 support half 초과를 제공했는지 본다.
6. A. true gift는 일반적으로 recipient gross income에서 excluded다.
7. B. services 대가로 받은 property는 compensation이다.
8. A. Schedule 2는 additional taxes다.
9. A. Schedule 3는 additional credits and payments다.
10. C. FBAR는 FinCEN/BSA E-Filing으로 filed된다.

## 18. 오답노트 템플릿

| Question | Topic | My answer | Correct answer | Why I missed it | Trigger for next time |
|---|---|---|---|---|---|
| 1 | filing status |  |  | December 31 status를 놓침 | married late in year |
| 2 | dependent |  |  | QC support와 QR support를 섞음 | own support vs taxpayer support |
| 3 | gross income |  |  | compensation을 gift로 봄 | property for services |

## 19. 공식 출처

- IRS About Form 1040: https://www.irs.gov/forms-pubs/about-form-1040
- IRS Publication 501: https://www.irs.gov/publications/p501
- IRS About Publication 501: https://www.irs.gov/forms-pubs/about-publication-501
- IRS Interactive Tax Assistant, filing status: https://www.irs.gov/help/ita/what-is-my-filing-status
- IRS Dependents overview: https://www.irs.gov/credits-deductions/individuals/dependents
- IRS Publication 525: https://www.irs.gov/publications/p525
- IRS Form 8938 vs. FBAR comparison: https://www.irs.gov/businesses/comparison-of-form-8938-and-fbar-requirements
