#!/usr/bin/env python3
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parent
MASTERCLASS_DIR = ROOT / "week1-day2-masterclass"
DATE = "2026-04-27"

SOURCES = [
    ("IRS Sample SEE Questions and Answers", "https://www.irs.gov/tax-professionals/enrolled-agents/sample-special-enrollment-examination-questions-and-answers"),
    ("IRS Publication 501 (2025)", "https://www.irs.gov/publications/p501"),
    ("IRS About Form 1040", "https://www.irs.gov/forms-pubs/about-form-1040"),
]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def sources_md() -> str:
    return "\n".join(f"- {name}: {url}" for name, url in SOURCES)


QUESTIONS = [
    ("Which item is most directly affected by a taxpayer's filing status?", "Standard deduction and tax rate structure", ["The taxpayer's employer identification number", "Whether Form W-2 exists", "The taxpayer's state of birth"], "`Filing status`는 `standard deduction`, tax rate structure, filing requirement, 여러 credit eligibility에 영향을 준다. 단순한 label이 아니다."),
    ("How many basic filing statuses are listed for individual taxpayers?", "Five", ["Three", "Four", "Six"], "Individual taxpayer의 기본 `filing status`는 five: `Single`, `MFJ`, `MFS`, `HOH`, `QSS`다."),
    ("If more than one filing status applies, the taxpayer generally should choose the one that:", "Results in the lowest tax", ["Has the shortest name", "Requires no Social Security number", "Avoids all income reporting"], "Publication 501의 실전 감각은 여러 status가 가능하면 generally lowest tax를 주는 status를 선택하는 것이다."),
    ("`MFJ` stands for:", "Married Filing Jointly", ["Modified Federal Joint", "Marital Filing Judgment", "Maximum Family Joint"], "`MFJ`는 `Married Filing Jointly`다. spouses가 joint return으로 combined income/deductions를 신고하는 status다."),
    ("`MFS` stands for:", "Married Filing Separately", ["Minimum Federal Schedule", "Married Federal Statement", "Modified Filing Standard"], "`MFS`는 `Married Filing Separately`다. married taxpayers가 separate returns를 filing하는 status다."),
    ("`HOH` stands for:", "Head of Household", ["Home Office Holder", "Higher Ordinary Household", "Household Optional Help"], "`HOH`는 `Head of Household`다. unmarried 또는 considered unmarried taxpayer가 home cost와 qualifying person 요건을 충족할 때 사용하는 status다."),
    ("`QSS` stands for:", "Qualifying Surviving Spouse", ["Qualified Standard Schedule", "Quarterly Social Security", "Qualifying Separate Status"], "`QSS`는 `Qualifying Surviving Spouse`다. 배우자 사망 후 일정 요건에서 2년간 가능한 status다."),
    ("For filing-status purposes, marital status is generally determined as of:", "The last day of the tax year", ["The first day of the tax year", "The original filing due date", "The date wages were first paid"], "`Marital status`는 일반적으로 tax year의 last day, calendar-year taxpayer라면 December 31 기준으로 판단한다."),
    ("A taxpayer who is unmarried on December 31 and does not qualify for another status is generally:", "Single", ["Married Filing Jointly", "Married Filing Separately", "Qualifying Surviving Spouse automatically"], "Year-end에 unmarried이고 `HOH`나 `QSS` 같은 더 specific한 status가 없으면 일반적으로 `Single`이다."),
    ("A taxpayer legally separated under a final decree of divorce or separate maintenance on December 31 is generally considered:", "Unmarried", ["Married for the entire year", "A dependent of the former spouse", "Required to file MFJ"], "Final decree of divorce 또는 separate maintenance가 year-end에 있으면 generally unmarried로 본다. 단, state law와 decree finality가 중요하다."),
    ("A taxpayer married on November 30 and still married on December 31 generally starts the filing-status analysis as:", "Married", ["Single", "Head of Household automatically", "Qualifying surviving spouse"], "1년 대부분 unmarried였어도 December 31에 married이면 generally married로 시작한다."),
    ("A taxpayer divorced under a final decree on December 20 and not remarried by December 31 is generally:", "Unmarried for filing-status analysis", ["Married because most of the year was married", "Required to file MFJ", "Automatically QSS"], "Year-end status가 핵심이다. final divorce decree가 있고 December 31에 remarried하지 않았다면 generally unmarried다."),
    ("A taxpayer has only an interlocutory divorce decree on December 31, and the divorce is not final. The taxpayer is generally:", "Still considered married", ["Automatically Single", "Automatically QSS", "Not required to file a return"], "Divorce가 final이 아니면 generally still married로 본다. `interlocutory decree`는 final divorce decree와 구분한다."),
    ("Spouses who are married and living together on December 31 are generally considered:", "Married", ["Unmarried", "Legally separated", "Qualifying surviving spouses"], "Married and living together at year-end이면 generally married status에서 시작한다."),
    ("Spouses who are married but living apart on December 31 and not legally separated under a final decree are generally:", "Considered married", ["Always Single", "Always QSS", "Never required to file"], "단순히 living apart라고 해서 unmarried가 아니다. final divorce/separate maintenance decree가 없으면 generally married다."),
    ("A common-law marriage recognized by the relevant state generally means the taxpayers are:", "Considered married", ["Always considered Single", "Required to file MFS only", "Not allowed to file any federal return"], "Recognized common-law marriage는 federal filing status에서 generally married로 취급된다."),
    ("If a taxpayer's spouse died during 2025 and the taxpayer did not remarry in 2025, the taxpayer may be able to file for 2025 as:", "Married Filing Jointly", ["Single only", "QSS for the year of death only", "Head of Household automatically"], "Spouse가 사망한 year of death에는 요건 충족 시 deceased spouse와 `MFJ`가 가능할 수 있다. `QSS`는 보통 그 다음 2년을 본다."),
    ("If a surviving spouse remarries before the end of the year of the first spouse's death, the surviving spouse generally files with:", "The new spouse if filing a joint return", ["The deceased spouse on the same joint return", "No one because remarriage bars all filing", "The child as MFJ"], "Year-end에 remarried했다면 new spouse와 married status를 본다. deceased spouse와 joint return을 계속 쓰는 구조가 아니다."),
    ("A married couple with one spouse having no income may generally choose:", "Married Filing Jointly", ["Single for the spouse with no income", "HOH automatically", "QSS automatically"], "`MFJ`는 한 spouse에게 income이 없어도 가능할 수 있다. 핵심은 spouses가 joint return을 filing하는 것이다."),
    ("When spouses file a joint return, they generally report:", "Combined income and deductions on one return", ["Only the higher spouse's income", "Only separate income with no combined items", "Only nontaxable income"], "`MFJ`는 combined income/deductions를 하나의 joint return에 신고하는 구조다."),
    ("A general consequence of filing a joint return is that both spouses may be:", "Jointly and severally liable", ["Treated as unrelated taxpayers", "Automatically exempt from tax", "Required to file separate amended returns"], "`MFJ`에서는 generally joint and several liability가 생긴다. 즉 return상의 tax에 대해 양쪽 spouse가 책임질 수 있다."),
    ("A joint return generally must be signed by:", "Both spouses", ["Only the higher-income spouse in all cases", "Only the IRS", "Only a dependent child"], "Joint return은 generally both spouses가 sign해야 한다. special signing rules는 별도 상황에서 본다."),
    ("Which status is for married taxpayers who choose to file separate returns?", "Married Filing Separately", ["Single", "Head of Household", "Qualifying Surviving Spouse"], "`MFS`는 married taxpayers가 separate returns를 filing하는 status다. Single이 아니다."),
    ("A taxpayer using MFS generally reports:", "The taxpayer's own income, deductions, and credits under separate-return rules", ["All family income on one joint return", "Only the spouse's income", "No income at all"], "`MFS`는 separate return이다. community property 등 예외가 있을 수 있지만 Day 2에서는 separate-return rules의 기본 감각을 잡는다."),
    ("For 2025 filing requirements, MFS taxpayers generally have a very low gross income filing threshold of:", "$5", ["$0 always", "$10,000", "$31,500"], "2025 Publication 501 filing requirement chart에서 `MFS` threshold는 any age 기준 $5로 매우 낮다."),
    ("Which statement about MFS is generally correct?", "It often limits or disallows certain deductions and credits", ["It always gives every credit available to MFJ", "It is identical to Single", "It is only for unmarried taxpayers"], "`MFS`는 education credits 등 여러 benefits가 제한되거나 disallowed될 수 있다. 시험에서는 unfavorable status로 자주 출제된다."),
    ("A taxpayer filing MFS generally cannot claim which education benefit?", "American Opportunity Credit or Lifetime Learning Credit", ["Standard deduction in every case", "The right to sign a return", "The right to report wages"], "Education credits는 일반적으로 `MFS`에서 허용되지 않는다. IRS sample question에서도 education credit은 filing jointly 여부와 연결된다."),
    ("If one spouse itemizes deductions on a separate return, the other spouse generally:", "Cannot take the standard deduction", ["Must file Single", "Must claim HOH", "Automatically receives a refund"], "`MFS`에서 one spouse itemizes이면 other spouse는 generally standard deduction을 사용할 수 없다. 둘 다 itemized 쪽으로 맞춰야 하는 함정이다."),
    ("Which filing status is generally more likely to be disadvantageous for credits and deductions?", "Married Filing Separately", ["Married Filing Jointly", "Head of Household", "Qualifying Surviving Spouse"], "MFS는 many credits/deductions에서 제한이 많아 시험에서 자주 불리한 status로 나온다."),
    ("A married taxpayer living with a spouse for the entire year usually should not jump first to:", "Head of Household", ["MFJ or MFS", "Married status", "A year-end marital-status analysis"], "Married taxpayer가 spouse와 all year lived together라면 special facts 없이 `HOH`로 바로 가면 안 된다."),
    ("Head of Household generally requires the taxpayer to be:", "Unmarried or considered unmarried", ["Married and living with spouse all year", "A corporation", "A nondependent child"], "`HOH`는 unmarried 또는 considered unmarried가 출발점이다."),
    ("A core HOH requirement is that the taxpayer paid:", "More than half the cost of keeping up a home", ["Exactly half of the taxpayer's own support", "Any amount of the child's college tuition", "The dependent's federal income tax"], "HOH home-cost test는 `more than half the cost of keeping up a home`이다. exactly half가 아니다."),
    ("For HOH, `cost of keeping up a home` is most closely connected to:", "Household maintenance costs", ["A child's own support only", "Foreign account balances", "Education credits only"], "`Cost of keeping up a home`은 household 유지비다. dependent support와 구분한다."),
    ("Which item is generally included in the cost of keeping up a home for HOH?", "Rent", ["A vacation trip", "Life insurance premiums", "The dependent's medical care"], "Rent는 home upkeep cost에 들어간다. vacation, life insurance, medical care는 일반적으로 이 category가 아니다."),
    ("Which item is generally included in the cost of keeping up a home for HOH?", "Utilities", ["The taxpayer's clothing", "A child's tuition", "Transportation to work"], "Utilities는 home cost다. clothing, tuition, transportation은 home upkeep cost가 아니다."),
    ("Which item is generally not included in the cost of keeping up a home for HOH?", "Life insurance premiums", ["Real estate taxes on the home", "Repairs to the home", "Food eaten in the home"], "Life insurance premium은 home upkeep cost가 아니다. real estate taxes, repairs, food eaten in home은 home cost 후보다."),
    ("For HOH, paying exactly 50% of the cost of keeping up a home generally:", "Fails the more-than-half test", ["Passes because half equals more than half", "Creates MFJ", "Eliminates filing requirement"], "`More than half`는 50% 초과다. exactly 50%는 insufficient하다."),
    ("For HOH, a taxpayer who paid 60% of home upkeep costs satisfies which part?", "Home-cost test", ["Joint-return test", "MFS limitation", "QSS two-year rule"], "60%는 more than half이므로 HOH의 home-cost test를 충족할 수 있다. 다른 요건도 필요하다."),
    ("For HOH, `support` and `cost of keeping up a home` are:", "Different concepts", ["Always identical", "Both foreign reporting terms", "Both education credits"], "HOH는 home cost, dependent는 person support가 중심이다. 두 단어를 섞으면 틀린다."),
    ("A taxpayer is unmarried, paid more than half the cost of keeping up a home, and has no qualifying person. The taxpayer generally:", "Does not qualify for HOH", ["Automatically qualifies for HOH", "Must file MFJ", "Must file QSS"], "HOH는 status와 home cost만으로 부족하다. qualifying person도 필요하다."),
    ("Which fact most directly points to possible HOH status?", "Taxpayer paid more than half the cost of keeping up a home for a qualifying person", ["Taxpayer received bank interest", "Taxpayer had a foreign account", "Taxpayer used Schedule D"], "`HOH` trigger는 home cost + qualifying person이다. income type이나 foreign account가 핵심이 아니다."),
    ("For a married taxpayer to be considered unmarried for HOH, one requirement is generally that the taxpayer:", "Files a separate return", ["Files a joint return", "Has no income", "Owns the home outright"], "Considered unmarried rule에서는 generally separate return filing이 필요하다."),
    ("For the considered-unmarried HOH rule, the spouse generally must not have lived in the taxpayer's home during:", "The last 6 months of the tax year", ["Only the first week of January", "Exactly one day in April", "The entire prior year"], "Abandoned spouse style HOH rule에서는 spouse가 last 6 months 동안 home에 살지 않았는지가 핵심 trigger다."),
    ("For the considered-unmarried HOH rule, the home generally must have been the main home for more than half the year of the taxpayer's:", "Child, stepchild, or eligible foster child", ["Unrelated roommate only", "Employer", "Former accountant"], "Considered unmarried HOH rule은 child/stepchild/eligible foster child와 연결된다."),
    ("A married taxpayer files separately, pays over half the home cost, spouse did not live in the home during the last 6 months, and the home was the main home of the taxpayer's qualifying child for more than half the year. The taxpayer may be:", "Considered unmarried for HOH", ["Required to file MFJ", "Automatically QSS", "Unable to file any return"], "이 facts는 considered unmarried HOH analysis를 열어준다. 최종 status는 qualifying person 등 전체 요건을 확인한다."),
    ("A married taxpayer lived with the spouse for the entire last 6 months of the year. Without other special facts, the taxpayer generally:", "Fails the considered-unmarried last-6-months test", ["Automatically qualifies as HOH", "Becomes QSS", "Is legally separated"], "Spouse가 last 6 months 동안 home에 lived하면 considered unmarried rule의 핵심 요건에 걸린다."),
    ("For HOH, a qualifying person is generally required to be:", "A person who meets specific HOH qualifying-person rules", ["Any person the taxpayer likes", "Any coworker", "Any bank account"], "HOH qualifying person은 specific rules를 따른다. 모든 dependent나 모든 household member가 자동으로 되는 것은 아니다."),
    ("A taxpayer's qualifying child lived with the taxpayer for more than half the year. This fact is relevant to:", "HOH qualifying-person analysis", ["Only FBAR", "Only Form 8938", "Only corporate tax"], "Qualifying child가 taxpayer와 more than half year lived하면 HOH qualifying person 가능성이 생긴다."),
    ("A child away at college but returning home during breaks may be treated as:", "Temporarily absent", ["Never living with the taxpayer", "A foreign account", "A standard deduction"], "Education 때문에 away인 기간은 temporary absence로 볼 수 있다. residency를 자동 fail시키면 안 된다."),
    ("A qualifying person born during the year may qualify the taxpayer for HOH if the home was the person's home:", "For more than half the part of the year the person was alive", ["Only on December 31", "For the entire prior year", "For no time at all"], "Birth/death year에는 alive during year 기준으로 residency/home test를 조정해서 본다."),
    ("A dependent parent who qualifies the taxpayer for HOH generally:", "Does not always have to live with the taxpayer", ["Must always live in the taxpayer's home", "Must be under age 19", "Must be a full-time student"], "Dependent parent는 special rule이 있다. taxpayer가 parent의 home 유지비를 more than half 부담하는 경우 taxpayer와 같은 집에 살지 않아도 HOH 가능성이 있다."),
    ("For a dependent parent living in a separate apartment, the taxpayer's HOH analysis focuses on whether the taxpayer paid:", "More than half the cost of keeping up the parent's home", ["The parent's vacation costs only", "Exactly 10% of all costs", "The parent's Form 8938 fee"], "Parent special rule에서는 parent의 home upkeep cost를 누가 more than half 냈는지가 중요하다."),
    ("An unrelated friend qualifies as a dependent only by living with the taxpayer all year. For HOH qualifying-person purposes, the friend is generally:", "Not a qualifying person merely because of that dependency", ["Always a qualifying person", "Always a qualifying child", "Always a spouse"], "All-year household member인 unrelated friend는 QR dependent가 될 수 있어도 일반적으로 HOH qualifying person은 아니다."),
    ("Which relative may be a qualifying person for HOH even if not living with the taxpayer, if dependency and home-cost rules are met?", "Parent", ["Unrelated friend", "Employer", "Banker"], "Parent는 HOH에서 special rule이 있다. 같은 집에 살지 않아도 dependent parent rule을 검토한다."),
    ("If a child is treated as the qualifying child of the noncustodial parent for dependency purposes, the custodial parent may still need to examine:", "Whether the child can qualify the custodial parent for HOH", ["Whether FBAR replaces Form 8938", "Whether MFS becomes Single", "Whether QSS applies to corporations"], "Children of divorced/separated parents rules에서는 dependency claim과 HOH benefit이 완전히 같은 방향으로만 움직이지 않을 수 있다."),
    ("A child lived with the taxpayer for only 4 months, with no temporary absence or special birth/death rule. For HOH qualifying-person residency, this generally:", "Fails the more-than-half-year idea", ["Always passes", "Creates MFJ", "Creates QSS"], "HOH qualifying child analysis에서는 more than half the year residency가 중요하다. 4개월이면 일반적으로 부족하다."),
    ("A taxpayer's dependent father lived in his own home. The taxpayer paid 70% of the cost of keeping up the father's home. The father may help the taxpayer qualify for:", "HOH", ["MFJ", "MFS only", "Single only"], "Dependent parent + taxpayer pays more than half cost of parent's home이면 HOH special parent rule을 검토한다."),
    ("Which statement is generally correct about HOH and dependents?", "A dependent is not always a HOH qualifying person", ["Every dependent automatically creates HOH", "HOH never involves dependents", "Only spouses can be qualifying persons"], "Dependent와 HOH qualifying person은 겹치지만 동일하지 않다. 특히 unrelated friend 함정이 중요하다."),
    ("`QSS` applies most directly to a taxpayer whose:", "Spouse died in a prior year and who meets the surviving-spouse rules", ["Employer died", "Child opened a foreign account", "Friend moved out"], "`QSS`는 surviving spouse status다. spouse death와 qualifying child/home cost 요건을 함께 본다."),
    ("If a spouse died in 2025, the year 2025 is generally the year in which the survivor may be able to use:", "MFJ with the deceased spouse if otherwise qualified", ["QSS as the only possible status", "MFS only", "Single always"], "Year of death에는 generally MFJ 가능성을 먼저 본다. QSS는 보통 following 2 years다."),
    ("QSS may generally be available for how many years after the year of the spouse's death?", "Two years", ["One year", "Five years", "Forever"], "`Qualifying Surviving Spouse`는 spouse death year 다음 2년간 가능한 status다. indefinite status가 아니다."),
    ("To use QSS, the taxpayer generally must not have:", "Remarried before the end of the tax year", ["Paid rent", "Had wages", "Claimed any standard deduction"], "QSS는 surviving spouse가 remarried하지 않아야 한다. Remarriage는 status를 바꾼다."),
    ("One QSS requirement is that the taxpayer could have filed a joint return with the spouse for:", "The year the spouse died", ["Every year after death", "Only the year before marriage", "Only the child's birth year"], "QSS는 year of death에 spouse와 joint return을 file할 수 있었는지가 중요하다. 실제로 filed했는지보다 could have filed가 point다."),
    ("QSS generally requires a qualifying child or stepchild who:", "Qualifies as the taxpayer's dependent under the relevant rules", ["Is only an unrelated roommate", "Is the taxpayer's employer", "Is always over age 65"], "QSS는 child/stepchild dependent와 연결된다. 단순히 surviving spouse라는 사실만으로 충분하지 않다."),
    ("For QSS, the taxpayer generally must pay:", "More than half the cost of keeping up the home", ["Exactly half of the child's own support", "Only the spouse's medical costs", "Only foreign account fees"], "QSS도 home-cost concept가 있다. taxpayer가 home 유지비 more than half를 부담해야 한다."),
    ("For QSS, the home generally must be the main home of the qualifying child for:", "The entire year, except temporary absences", ["One weekend only", "Only December 31", "No part of the year"], "QSS는 qualifying child/stepchild의 main home requirement가 강하다. generally entire year except temporary absences다."),
    ("QSS gives the taxpayer the benefit of:", "Joint return tax rates and the highest standard deduction amount if not itemizing", ["Filing a joint return with a new spouse automatically", "No return filing requirement ever", "Corporate tax rates"], "QSS는 joint return rates와 highest standard deduction benefit을 줄 수 있지만, deceased spouse와 joint return을 filing하는 것은 아니다."),
    ("QSS is generally not available if the taxpayer:", "Has no qualifying child or stepchild for the status", ["Has wages", "Is under age 65", "Uses Form 1040"], "QSS는 qualifying child/stepchild 요건이 중요하다. wages나 age 자체가 핵심 제한은 아니다."),
    ("A taxpayer's spouse died in 2023. The taxpayer did not remarry and meets all other requirements. Which years may be QSS years?", "2024 and 2025", ["2023 only", "2026 and 2027 only", "Every year after 2023"], "QSS는 spouse death year 다음 2년이다. 2023 death이면 2024와 2025가 QSS 후보 years다."),
    ("A taxpayer's spouse died in 2024. The taxpayer did not remarry and meets all other requirements. For 2025, QSS is:", "Potentially available", ["Never available because death occurred before 2025", "Only available if the taxpayer remarries", "A corporate filing status"], "2024 death이면 following two years는 2025와 2026이 QSS 후보 years다."),
    ("A surviving spouse remarries in 2025. For 2025, QSS is generally:", "Not available", ["Always required", "The same as MFS", "Available forever"], "QSS는 taxpayer가 year-end 전에 remarried하지 않아야 한다. Remarriage blocks QSS."),
    ("Which status usually has a higher standard deduction than Single?", "Head of Household", ["MFS always", "Single itself", "No status affects standard deduction"], "HOH는 Single보다 higher standard deduction을 줄 수 있다. 그래서 Single로 바로 가기 전에 HOH를 확인한다."),
    ("Which status generally uses joint return tax rates without being a joint return?", "Qualifying Surviving Spouse", ["Single", "MFS", "HOH"], "QSS는 joint return tax rates/highest standard deduction benefit이 있지만, deceased spouse와 joint return을 filing하는 status는 아니다."),
    ("A taxpayer is unmarried, has no qualifying person, and no surviving-spouse facts. The likely status is:", "Single", ["HOH", "QSS", "MFJ"], "Unmarried + no qualifying person + no QSS facts라면 generally Single이다."),
    ("A taxpayer is unmarried and pays more than half the cost of a home for an unrelated roommate who is not a qualifying person. The taxpayer generally:", "Does not qualify for HOH based only on that roommate", ["Automatically qualifies for HOH", "Must file MFJ", "Must use QSS"], "Unrelated roommate는 qualifying person이 아닐 수 있다. home cost만 보고 HOH를 고르면 안 된다."),
    ("A taxpayer is unmarried, pays 40% of home costs, and has a qualifying child. The taxpayer generally:", "Fails the HOH home-cost test", ["Qualifies for HOH automatically", "Must file MFJ", "Becomes QSS"], "Qualifying child가 있어도 taxpayer가 more than half home cost를 부담하지 않으면 HOH가 안 된다."),
    ("A taxpayer is unmarried, pays 70% of home costs, and has a qualifying child who lived with the taxpayer all year. The taxpayer should consider:", "Head of Household", ["MFS only", "QSS only", "No filing status"], "Unmarried + more than half home cost + qualifying child = HOH 가능성을 강하게 본다."),
    ("A taxpayer is married, files a separate return, spouse lived elsewhere all of July through December, and the taxpayer's dependent child lived in the home all year. Which status should be examined?", "Head of Household through considered-unmarried rules", ["Single automatically", "QSS automatically", "No return status"], "Married라도 considered unmarried facts가 있으면 HOH를 검토한다. 자동 Single은 아니다."),
    ("A taxpayer's spouse lived in the home during September. For the considered-unmarried last-6-months rule, this fact:", "Creates a problem", ["Always helps HOH", "Creates QSS", "Means the taxpayer is legally separated"], "Last 6 months 동안 spouse가 home에 lived하면 considered unmarried rule이 어려워진다."),
    ("A taxpayer is eligible for both Single and HOH. Generally, the taxpayer should choose:", "HOH if it gives the lower tax and requirements are met", ["Single because it is alphabetically first", "MFS because every taxpayer can use it", "QSS without a deceased spouse"], "여러 status가 가능하면 lowest tax를 주는 status를 선택한다. HOH 요건이 충족되면 Single보다 유리할 수 있다."),
    ("A taxpayer is still married on December 31 but wants to file as Single because the spouses lived apart all year without legal separation. The taxpayer generally:", "Cannot file Single merely because of living apart", ["Must file Single", "Must file QSS", "Has no filing status"], "Living apart만으로 Single이 되는 것이 아니다. final decree나 considered unmarried HOH facts를 확인해야 한다."),
    ("Which trigger phrase most strongly suggests a filing-status question?", "Married on December 31", ["Received interest income", "Sold stock", "Paid estimated tax"], "Marital status/date facts는 filing status trigger다. income facts와 구분한다."),
    ("Which trigger phrase most strongly suggests a HOH question?", "Paid more than half the cost of keeping up a home", ["Received a Form 1099-INT", "Had gambling winnings", "Sold a car"], "`paid more than half the cost of keeping up a home`은 HOH trigger phrase다."),
    ("Which trigger phrase most strongly suggests a QSS question?", "Spouse died in a prior year and taxpayer has a dependent child", ["Taxpayer bartered services", "Taxpayer received unemployment", "Taxpayer has a foreign account"], "Spouse death + dependent child/home facts는 QSS trigger다."),
    ("Which trigger phrase most strongly suggests an MFS limitation?", "Married taxpayers choose separate returns", ["Unmarried taxpayer with qualifying child", "Spouse died two years ago", "Dependent parent in separate home"], "MFS limitations는 married taxpayers filing separate returns에서 나온다."),
    ("A taxpayer's filing status affects whether the taxpayer can claim certain:", "Deductions and credits", ["Employer forms only", "Bank routing numbers only", "State abbreviations only"], "Filing status는 deductions/credits eligibility에 영향을 준다. 특히 MFS limitations가 자주 나온다."),
    ("A taxpayer wants education credits but is MFS. The best first response is:", "Check the MFS restriction", ["Ignore filing status", "Automatically claim HOH", "Report the credit on FBAR"], "Education credit 문제에서 MFS이면 restriction부터 확인한다. IRS sample style에서도 filing status가 education credit eligibility와 연결된다."),
    ("A taxpayer's parent qualifies as a dependent and lives in a separate home. The taxpayer pays more than half the cost of keeping up that home. The best filing-status issue is:", "Potential HOH under the parent rule", ["MFS limitation only", "FBAR", "QSS automatically"], "Dependent parent separate-home fact pattern은 HOH parent rule이다."),
    ("A taxpayer's friend lives in the home all year and is claimed as a dependent. The best HOH warning is:", "A friend is generally not a qualifying person for HOH merely due to dependency", ["A friend always creates QSS", "A friend always creates MFJ", "A friend eliminates all tax"], "Friend dependent와 HOH qualifying person을 섞지 않는다. 이건 high-frequency trap이다."),
    ("A taxpayer's spouse died in 2025 and the taxpayer did not remarry. Which question comes first for 2025?", "Can the taxpayer file MFJ for the year of death?", ["Can the taxpayer file QSS forever?", "Can the taxpayer ignore filing status?", "Can the child file MFJ with taxpayer?"], "Spouse death year에는 MFJ 가능성을 먼저 본다. QSS는 following two years concept다."),
    ("A taxpayer's spouse died in 2023; taxpayer did not remarry; taxpayer has a dependent child and paid over half the home cost. For 2025, the best status to examine is:", "Qualifying Surviving Spouse", ["MFJ with deceased spouse for 2025", "MFS with deceased spouse", "Single only without analysis"], "Death year 2023이면 2025는 following second year라 QSS 후보가 된다. 요건 충족 여부를 확인한다."),
    ("Which status is generally for married taxpayers filing one combined return?", "Married Filing Jointly", ["MFS", "HOH", "Single"], "`MFJ`는 one combined joint return이다."),
    ("Which status is generally for married taxpayers filing separate returns?", "Married Filing Separately", ["MFJ", "Single", "QSS"], "`MFS`는 separate returns다."),
    ("Which status generally requires a qualifying person and more-than-half home cost?", "Head of Household", ["Single", "MFS", "MFJ"], "`HOH`의 3요소는 status, home cost, qualifying person이다."),
    ("Which status is generally connected to a spouse's death and two following years?", "Qualifying Surviving Spouse", ["MFS", "Single", "HOH only"], "`QSS`는 spouse death 이후 two-year window와 연결된다."),
    ("Which statement best summarizes Day 2 filing-status analysis?", "Start with year-end marital status, then test special statuses and limitations", ["Start with the taxpayer's favorite status", "Always choose Single first", "Ignore HOH unless the taxpayer owns a home"], "Day 2의 핵심은 year-end status에서 시작해 MFJ/MFS/HOH/QSS special rules를 순서대로 적용하는 것이다."),
    ("A taxpayer's divorce became final on January 5, 2026. On December 31, 2025, the divorce was not final. For 2025, the taxpayer generally starts as:", "Married", ["Single", "QSS", "HOH automatically"], "Filing status는 2025년 December 31 기준이다. Divorce가 January 5, 2026에 final이면 2025 year-end에는 generally still married다."),
    ("A taxpayer was legally separated under a decree of separate maintenance on December 31, 2025. The taxpayer is generally:", "Considered unmarried", ["Required to file MFJ", "Automatically QSS", "A qualifying child"], "Year-end에 separate maintenance decree가 있으면 generally unmarried로 본다. 단순 living apart와 구분한다."),
    ("Which statement about QSS is best?", "It can use joint return rates, but it is not the same as filing a joint return with the deceased spouse after the year of death", ["It is available forever after a spouse dies", "It never requires a child", "It is the same as MFS"], "`QSS`는 joint return rates/highest standard deduction benefit을 줄 수 있지만, year of death 이후 deceased spouse와 joint return을 filing하는 것과 같지 않다."),
    ("A married couple wants to claim an education credit and otherwise qualifies, but they plan to file MFS. The best filing-status warning is:", "MFS generally blocks the education credit", ["MFS always increases the credit", "Filing status never matters for education credits", "They must file HOH"], "Education credit 문제에서 `MFS`가 나오면 limitation warning을 켠다. 일반적으로 American Opportunity Credit/Lifetime Learning Credit은 MFS에서 허용되지 않는다."),
]


def answer_letter(index: int) -> str:
    letters = "ABCD"
    return letters[((index + 2) * 7) % 4]


def make_questions_md() -> str:
    lines = [
        "# EA Part 1 Week 1 Day 2: 100 Practice Questions",
        "",
        f"기준일: {DATE}",
        "시험 법 기준: IRS 공개 SEE sample question 안내에 맞춰 tax law through December 31, 2025 기준",
        "범위: `filing status`, `MFJ`, `MFS`, `HOH`, `considered unmarried`, `QSS`, filing-status traps",
        "",
        "중요: 아래 문제는 비공개 실제 SEE 문제나 brain dump가 아니다. IRS가 공개한 SEE sample question 형식과 공식 IRS Publication 501/Form 1040 자료를 기준으로 만든 Day 2 실전형 문제다. 실제 시험 대비를 위해 문제는 영어로 유지했다.",
        "",
        "## Questions",
        "",
    ]
    for idx, (question, correct, wrongs, _explanation) in enumerate(QUESTIONS, start=1):
        target = answer_letter(idx)
        options = {}
        wrong_iter = iter(wrongs)
        for letter in "ABCD":
            options[letter] = correct if letter == target else next(wrong_iter)
        lines.append(f"{idx}. {question}")
        for letter in "ABCD":
            lines.append(f"   - {letter}. {options[letter]}")
        lines.append("")
    lines.extend(["## Sources Used", "", sources_md()])
    return "\n".join(lines)


def make_answers_md() -> str:
    key_parts = []
    for start in range(1, 101, 10):
        key_parts.append("`" + " ".join(f"{i}{answer_letter(i)}" for i in range(start, start + 10)) + "`")
    lines = [
        "# EA Part 1 Week 1 Day 2: Answers and Detailed Explanations",
        "",
        f"기준일: {DATE}",
        "문제 파일: `part-1-week-1-day-2-100-practice-questions.md`",
        "",
        "중요: 이 해설은 비공개 실제 SEE 문제 해설이 아니다. IRS 공식 sample question 형식과 IRS Publication 501, Form 1040 공식 자료를 기준으로 만든 Day 2 실전형 문제 해설이다.",
        "",
        "## Answer Key",
        "",
        *key_parts,
        "",
        "## Detailed Explanations",
        "",
    ]
    for idx, (_question, correct, _wrongs, explanation) in enumerate(QUESTIONS, start=1):
        lines.append(f"{idx}. **{answer_letter(idx)}. {correct}**  ")
        lines.append(f"   {explanation}")
        lines.append("")
    lines.extend(["## Sources Used", "", sources_md()])
    return "\n".join(lines)


DEEP_DIVE = f"""
# EA Part 1 Week 1 Day 2 Deep Dive: Filing Status

기준일: {DATE}
시험 법 기준: tax law through December 31, 2025
대상: `part-1-week-1-day-2-100-practice-questions.md`

Day 2는 `filing status`를 깊게 파는 날이다. Day 1에서 `Form 1040 flow`와 전체 지도를 봤다면, Day 2는 taxpayer가 어떤 출발선에 서는지 결정한다.

`Filing status`는 단순한 이름표가 아니다. `standard deduction`, tax rate structure, filing requirement, credit eligibility, deduction limitation에 영향을 준다.

중요: 이 자료는 비공개 실제 SEE 문제나 brain dump를 사용하지 않는다. IRS 공개 SEE sample question 형식과 IRS Publication 501/Form 1040 자료를 기준으로 만든 학습 자료다.

## 0. Day 2 약어

| 약어 / 용어 | 풀어쓴 말 | 의미 |
|---|---|---|
| `SEE` | `Special Enrollment Examination` | EA 시험 |
| `IRS` | `Internal Revenue Service` | 미국 연방 세무 당국 |
| `MFJ` | `Married Filing Jointly` | married taxpayers가 one joint return으로 filing |
| `MFS` | `Married Filing Separately` | married taxpayers가 separate returns로 filing |
| `HOH` | `Head of Household` | unmarried 또는 considered unmarried + home cost + qualifying person |
| `QSS` | `Qualifying Surviving Spouse` | spouse death 이후 일정 요건에서 가능한 surviving spouse status |

## 1. Day 2 한 줄 공식

`Start with December 31, then test special statuses.`

문제 읽는 순서:

1. taxpayer의 `marital status`를 December 31 기준으로 본다.
2. married이면 `MFJ` 또는 `MFS`에서 시작한다.
3. unmarried이면 `Single`, `HOH`, `QSS` 가능성을 본다.
4. spouse death가 있으면 year of death의 `MFJ`와 following years의 `QSS`를 구분한다.
5. child/home facts가 있으면 `HOH` 또는 `QSS`를 검토한다.
6. MFS가 나오면 credit/deduction limitation을 의심한다.

## 2. 기본 filing status 5개

| Status | 언제 보는가 | 시험 함정 |
|---|---|---|
| `Single` | year-end unmarried이고 더 좋은 status가 없을 때 | HOH 가능성을 안 보고 바로 Single 선택 |
| `MFJ` | married taxpayers가 joint return filing | joint liability, education credit eligibility |
| `MFS` | married taxpayers가 separate returns filing | credits/deductions 제한 |
| `HOH` | unmarried 또는 considered unmarried + home cost + qualifying person | home cost와 support를 섞음 |
| `QSS` | spouse death 이후 2년 window | year of death MFJ와 혼동 |

## 3. December 31 rule

일반적으로 `marital status`는 tax year의 마지막 날 기준이다. Calendar-year taxpayer는 December 31 기준으로 본다.

예시:

- November 30에 결혼하고 December 31에도 married이면 married로 시작한다.
- December 20에 final divorce decree가 있고 December 31에 remarried하지 않았으면 unmarried로 시작한다.
- married but living apart는 final decree가 없으면 generally married다.
- common-law marriage가 state law상 recognized이면 generally married다.

시험에서는 날짜가 나오면 filing status 문제라고 표시한다.

## 4. MFJ

`MFJ`, 즉 `Married Filing Jointly`는 spouses가 combined income and deductions를 one joint return에 신고하는 status다.

핵심:

- one spouse에게 income이 없어도 가능할 수 있다.
- spouse died during the year이면, survivor가 remarried하지 않고 요건을 충족하면 year of death에 MFJ 가능성이 있다.
- joint return은 generally both spouses가 sign한다.
- joint return은 generally joint and several liability를 만든다.

## 5. MFS

`MFS`, 즉 `Married Filing Separately`는 married taxpayers가 separate returns를 filing하는 status다.

시험에서 MFS는 보통 limitation trigger다.

대표 감각:

- many credits/deductions가 limited 또는 disallowed될 수 있다.
- education credits는 generally MFS에서 불가능하다.
- one spouse itemizes deductions이면 other spouse도 generally standard deduction을 사용할 수 없다.
- 2025 Publication 501의 filing requirement chart에서 MFS gross income threshold는 `$5`로 매우 낮다.

MFS는 Single과 같은 말이 아니다. married status 안에서 separate return을 선택하는 것이다.

## 6. HOH

`HOH`, 즉 `Head of Household`는 세 문을 통과해야 한다.

1. taxpayer가 unmarried 또는 considered unmarried인가
2. taxpayer가 `more than half the cost of keeping up a home`을 paid했는가
3. qualifying person이 있는가

세 문 중 하나만 맞으면 안 된다. 반드시 함께 본다.

## 7. Cost of keeping up a home

HOH에서 `cost of keeping up a home`은 household 유지비다.

포함되는 대표 항목:

- rent
- mortgage interest
- real estate taxes
- insurance on the home
- repairs
- utilities
- food eaten in the home

일반적으로 포함하지 않는 항목:

- clothing
- education
- medical treatment
- vacations
- life insurance
- transportation

`More than half`는 50% 초과다. exactly 50%는 fail이다.

## 8. Considered unmarried

Married taxpayer도 certain facts가 있으면 HOH 목적상 `considered unmarried`가 될 수 있다.

핵심 trigger:

- taxpayer files a separate return
- taxpayer paid more than half the cost of keeping up the home
- spouse did not live in the home during the last 6 months of the tax year
- home was the main home of taxpayer's child, stepchild, or eligible foster child for more than half the year
- child is dependent, or would be dependent except for certain noncustodial-parent rules

이건 자동 Single이 아니다. married taxpayer가 HOH로 갈 수 있는 특별한 길이다.

## 9. Qualifying person for HOH

HOH qualifying person은 specific rules를 따른다.

중요 함정:

- qualifying child가 taxpayer와 more than half the year lived하면 HOH qualifying person 가능성이 크다.
- dependent parent는 taxpayer와 같이 살지 않아도 parent rule로 HOH qualifying person이 될 수 있다.
- unrelated friend는 all-year household member로 dependent가 되어도, 그 이유만으로 HOH qualifying person은 generally 아니다.
- temporary absence, birth/death year rules를 놓치지 않는다.

## 10. QSS

`QSS`, 즉 `Qualifying Surviving Spouse`는 spouse death 이후 일정 요건에서 사용하는 status다.

핵심:

- spouse died in one of the two years before the current tax year
- taxpayer did not remarry before the end of the tax year
- taxpayer could have filed a joint return with the deceased spouse for the year of death
- taxpayer has a qualifying child or stepchild for the status
- taxpayer paid more than half the cost of keeping up the home
- that home was the child's main home for the entire year, except temporary absences

Year of death에는 generally MFJ 가능성을 먼저 본다. QSS는 following two years다.

## 11. 문제 풀이 루틴

문제를 읽으면 아래처럼 적는다.

`date? spouse? child? home cost? status limitation?`

예:

- `married Nov 30, still married Dec 31` -> married status
- `divorced Dec 20 final decree` -> unmarried
- `spouse died in 2025` -> MFJ for year of death
- `spouse died in 2023, dependent child, no remarriage` -> QSS in 2025
- `paid more than half cost of keeping up home` -> HOH
- `unrelated friend dependent` -> HOH warning
- `MFS education credit` -> limitation warning

## 12. Day 2 반드시 외울 10문장

1. `Filing status` affects standard deduction, tax rates, filing requirements, and credit eligibility.
2. There are five filing statuses: `Single`, `MFJ`, `MFS`, `HOH`, and `QSS`.
3. Marital status is generally determined on the last day of the tax year.
4. Married taxpayers generally start with `MFJ` or `MFS`.
5. `MFS` often limits credits and deductions.
6. `HOH` requires status, home cost, and qualifying person.
7. `Cost of keeping up a home` is not the same as support of a person.
8. A married taxpayer may be considered unmarried for HOH only if specific tests are met.
9. A dependent parent does not always have to live with the taxpayer for HOH.
10. `QSS` is generally for the two years after the spouse's year of death.

## Sources Used

{sources_md()}
"""


MODULES = [
    {
        "slug": "00-roadmap",
        "title": "Roadmap",
        "questions": "전체",
        "md": """
# EA Part 1 Week 1 Day 2 Masterclass 00: Roadmap

기준일: 2026-04-27
대상 문제: `part-1-week-1-day-2-100-practice-questions.md` 전체

Day 2는 `filing status`를 1타 강사식으로 쪼개는 날이다.

한 줄 공식:

`Start with December 31, then test special statuses.`

## 5초 문제 읽기 루틴

1. `December 31` 상태를 본다.
2. married인지 unmarried인지 가른다.
3. spouse death가 있으면 year of death `MFJ`와 following-year `QSS`를 분리한다.
4. child/home facts가 있으면 `HOH` 또는 `QSS`를 의심한다.
5. `MFS`가 보이면 limitation warning을 켠다.

## Module 순서

| Module | 주제 | 연결 문제 |
|---|---|---|
| 00 | roadmap | 전체 |
| 01 | five statuses and year-end marital status | 1-18 |
| 02 | MFJ and MFS | 19-30 |
| 03 | HOH core tests and considered unmarried | 31-46 |
| 04 | HOH qualifying person and parent/friend traps | 47-61 |
| 05 | QSS and mixed filing-status traps | 62-100 |

## 오늘의 목표

정답을 외우는 것이 아니라, 문제를 읽고 바로 topic label을 붙인다.

예:

- `Q13 - interlocutory decree`
- `Q25 - MFS filing threshold`
- `Q43 - considered unmarried`
- `Q52 - dependent parent HOH`
- `Q72 - QSS two-year window`

## Recap

Day 2는 taxpayer의 출발선을 정하는 날이다. `filing status`가 틀리면 standard deduction, tax rate, credit eligibility가 같이 흔들린다.
""",
        "audio": """
EA Part 1, Week 1 Day 2, Masterclass zero. Roadmap.

Day 2는 filing status를 깊게 파는 날입니다. Filing status는 단순한 이름표가 아닙니다. Standard deduction, tax rate structure, filing requirement, credit eligibility, deduction limitation에 영향을 줍니다.

오늘의 한 줄 공식은 이것입니다. Start with December 31, then test special statuses.

문제를 읽으면 먼저 December 31 상태를 봅니다. Married인지 unmarried인지 가릅니다. Spouse death가 있으면 year of death의 MFJ와 following-year QSS를 분리합니다. Child와 home facts가 있으면 HOH 또는 QSS를 의심합니다. MFS가 보이면 limitation warning을 켭니다.

Day 2 module은 다섯 갈래로 갑니다.

Module one은 five statuses and year-end marital status입니다. Single, MFJ, MFS, HOH, QSS를 잡고 December 31 rule을 훈련합니다.

Module two는 MFJ and MFS입니다. Married Filing Jointly와 Married Filing Separately를 구분하고, MFS limitation을 봅니다.

Module three는 HOH core tests and considered unmarried입니다. Head of Household의 세 문, status, home cost, qualifying person을 봅니다.

Module four는 HOH qualifying person traps입니다. Dependent parent, unrelated friend, temporary absence 같은 함정을 봅니다.

Module five는 QSS and mixed traps입니다. Qualifying Surviving Spouse와 status selection 문제를 섞어서 훈련합니다.

오늘 목표는 정답을 외우는 것이 아닙니다. 문제를 읽고 topic label을 붙이는 것입니다. Interlocutory decree, MFS threshold, considered unmarried, dependent parent HOH, QSS two-year window. 이런 label이 바로 떠올라야 합니다.

Day 2는 taxpayer의 출발선을 정하는 날입니다. Filing status가 틀리면 뒤의 계산도 같이 틀립니다.
""",
    },
    {
        "slug": "01-five-statuses-year-end",
        "title": "Five Statuses and Year-End Status",
        "questions": "1-18",
        "md": """
# EA Part 1 Week 1 Day 2 Masterclass 01: Five Statuses and Year-End Status

대상 문제: 1-18

## 한 줄 결론

`Filing status`는 December 31에서 시작한다.

## 기본 5개 status

| Status | 풀어쓰기 | 핵심 |
|---|---|---|
| `Single` | Single | unmarried이고 더 좋은 status가 없을 때 |
| `MFJ` | Married Filing Jointly | married taxpayers가 one joint return |
| `MFS` | Married Filing Separately | married taxpayers가 separate returns |
| `HOH` | Head of Household | unmarried 또는 considered unmarried + home cost + qualifying person |
| `QSS` | Qualifying Surviving Spouse | spouse death 이후 일정 요건 |

## December 31 rule

Calendar-year taxpayer는 generally December 31 marital status를 본다.

| Fact | 시작점 |
|---|---|
| married Nov 30 and still married Dec 31 | married |
| final divorce decree Dec 20 and no remarriage | unmarried |
| interlocutory decree, divorce not final | married |
| married but living apart, no final decree | married |
| recognized common-law marriage | married |

## Spouse death

Spouse died during the current year이면 current year에는 `MFJ` 가능성을 먼저 본다.

`QSS`는 보통 spouse death year 다음 2년이다.

## Drill

1. November 30 marriage, still married December 31 -> married or unmarried?
2. Final divorce decree on December 20 -> married or unmarried?
3. Interlocutory decree only -> final divorce인가?
4. Spouse died in current year -> year-of-death status로 무엇을 먼저 보는가?

정답: married, unmarried, 아니다, MFJ.
""",
        "audio": """
Masterclass one. Five statuses and year-end status.

이번 module의 한 줄 결론은 filing status는 December 31에서 시작한다는 것입니다.

기본 filing status는 다섯 개입니다. Single. MFJ, Married Filing Jointly. MFS, Married Filing Separately. HOH, Head of Household. QSS, Qualifying Surviving Spouse.

Single은 unmarried이고 더 좋은 status가 없을 때 봅니다. MFJ는 married taxpayers가 one joint return을 filing하는 status입니다. MFS는 married taxpayers가 separate returns를 filing하는 status입니다. HOH는 unmarried 또는 considered unmarried taxpayer가 home cost와 qualifying person 요건을 충족할 때 봅니다. QSS는 spouse death 이후 일정 요건에서 봅니다.

Calendar-year taxpayer는 generally December 31 marital status를 봅니다. November 30에 결혼했고 December 31에도 married이면 married로 시작합니다. December 20에 final divorce decree가 있고 December 31에 remarried하지 않았다면 unmarried로 시작합니다.

Interlocutory decree는 final divorce decree가 아닙니다. Divorce가 final이 아니면 generally still married입니다.

Married but living apart도 주의합니다. 그냥 따로 산다고 Single이 아닙니다. Final divorce 또는 separate maintenance decree가 없으면 generally married입니다.

Common-law marriage가 state law상 recognized이면 generally married입니다.

Spouse death도 정리합니다. Spouse died during the current year이면 그 current year에는 MFJ, Married Filing Jointly 가능성을 먼저 봅니다. QSS, Qualifying Surviving Spouse는 보통 spouse death year 다음 two years입니다.

문제를 읽을 때 날짜가 나오면 멈추세요. November 30, December 20, December 31, spouse died. 이런 말은 filing status trigger입니다.
""",
    },
    {
        "slug": "02-mfj-mfs",
        "title": "MFJ and MFS",
        "questions": "19-30",
        "md": """
# EA Part 1 Week 1 Day 2 Masterclass 02: MFJ and MFS

대상 문제: 19-30

## 한 줄 결론

Married taxpayer는 보통 `MFJ` 또는 `MFS`에서 시작하고, `MFS`는 limitation warning이다.

## MFJ

`MFJ`는 `Married Filing Jointly`다.

핵심:

- spouses가 combined income and deductions를 one return에 신고한다.
- one spouse에게 income이 없어도 가능할 수 있다.
- generally both spouses sign.
- generally joint and several liability가 생긴다.
- spouse died during the year이면 survivor가 remarried하지 않고 요건을 충족할 때 year-of-death MFJ 가능성이 있다.

## MFS

`MFS`는 `Married Filing Separately`다.

핵심:

- married taxpayers가 separate returns를 filing한다.
- Single과 같은 말이 아니다.
- 2025 filing requirement threshold가 very low: `$5`.
- education credits는 generally MFS에서 불가능하다.
- one spouse itemizes이면 other spouse generally cannot take standard deduction.
- many credits/deductions가 limited 또는 disallowed될 수 있다.

## 시험 반응

`MFS`가 보이면 이렇게 생각한다.

`What benefit is being limited?`

Education credit, student loan interest, EITC, standard deduction coordination 같은 제한을 의심한다.

## Drill

1. MFJ는 combined return인가 separate returns인가?
2. MFS는 Single과 같은가?
3. MFS가 나오면 어떤 warning을 켜야 하는가?
4. One spouse itemizes이면 other spouse의 standard deduction은 안전한가?

정답: combined, 아니다, limitation warning, 아니다.
""",
        "audio": """
Masterclass two. MFJ and MFS.

이번 module의 한 줄 결론은 married taxpayer는 보통 MFJ 또는 MFS에서 시작하고, MFS는 limitation warning이라는 것입니다.

MFJ는 Married Filing Jointly입니다. Spouses가 combined income and deductions를 one joint return에 신고합니다. One spouse에게 income이 없어도 MFJ가 가능할 수 있습니다. Joint return은 generally both spouses가 sign합니다. 그리고 generally joint and several liability가 생깁니다. 즉 return상의 tax에 대해 두 spouse가 모두 책임질 수 있습니다.

Spouse died during the year이면 year of death에는 MFJ 가능성을 먼저 봅니다. Survivor가 remarried하지 않고, otherwise qualified이면 deceased spouse와 joint return을 file할 수 있는 경우가 있습니다.

MFS는 Married Filing Separately입니다. Married taxpayers가 separate returns를 filing하는 status입니다. MFS는 Single이 아닙니다. Married status 안에서 separate로 filing하는 것입니다.

시험에서 MFS는 limitation warning입니다. 2025 Publication 501에서 MFS filing threshold는 5 dollars로 very low입니다. Education credits는 generally MFS에서 불가능합니다. One spouse itemizes deductions이면 other spouse generally cannot take the standard deduction. Many credits and deductions가 limited 또는 disallowed될 수 있습니다.

그래서 MFS가 보이면 이렇게 묻습니다. What benefit is being limited?

Education credit인가. Student loan interest인가. EITC인가. Standard deduction coordination인가. MFS는 항상 조심해서 봅니다.

정리하면 MFJ는 one combined return. MFS는 separate returns. MFS is not Single. MFS is a limitation trigger.
""",
    },
    {
        "slug": "03-hoh-core-considered-unmarried",
        "title": "HOH Core Tests and Considered Unmarried",
        "questions": "31-46",
        "md": """
# EA Part 1 Week 1 Day 2 Masterclass 03: HOH Core Tests and Considered Unmarried

대상 문제: 31-46

## 한 줄 결론

`HOH`는 status, home cost, qualifying person 세 문을 통과해야 한다.

## HOH 3문

1. taxpayer가 unmarried 또는 considered unmarried인가
2. taxpayer가 more than half the cost of keeping up a home을 paid했는가
3. qualifying person이 있는가

## Cost of keeping up a home

포함 후보:

- rent
- mortgage interest
- real estate tax
- insurance on the home
- repairs
- utilities
- food eaten in the home

일반적으로 제외:

- clothing
- education
- medical treatment
- vacations
- life insurance
- transportation

`More than half`는 exactly 50%가 아니다.

## Considered unmarried

Married taxpayer도 HOH 목적상 considered unmarried가 될 수 있다.

대표 요건:

- separate return
- paid more than half home cost
- spouse did not live in home during the last 6 months
- home was main home of child, stepchild, or eligible foster child for more than half the year
- child is dependent or would be dependent except for certain noncustodial-parent rules

## Drill

1. HOH의 세 문은?
2. Rent는 home cost인가?
3. Life insurance premium은 home cost인가?
4. Exactly 50%는 more than half인가?
5. Married taxpayer가 HOH가 되는 길을 무엇이라 부르는가?

정답: status/home cost/qualifying person, yes, no, no, considered unmarried.
""",
        "audio": """
Masterclass three. HOH core tests and considered unmarried.

이번 module의 한 줄 결론은 HOH는 status, home cost, qualifying person 세 문을 통과해야 한다는 것입니다.

HOH는 Head of Household입니다. 첫 번째 문은 taxpayer가 unmarried 또는 considered unmarried인가입니다. 두 번째 문은 taxpayer가 more than half the cost of keeping up a home을 paid했는가입니다. 세 번째 문은 qualifying person이 있는가입니다. 세 문 중 하나만 맞으면 안 됩니다. 함께 봅니다.

Cost of keeping up a home은 household 유지비입니다. Rent, mortgage interest, real estate tax, insurance on the home, repairs, utilities, food eaten in the home 같은 항목입니다.

반대로 clothing, education, medical treatment, vacations, life insurance, transportation은 일반적으로 home upkeep cost가 아닙니다.

More than half도 조심합니다. Exactly 50 percent는 more than half가 아닙니다. 50 percent 초과가 필요합니다.

Married taxpayer도 certain facts가 있으면 HOH 목적상 considered unmarried가 될 수 있습니다. Separate return을 file하고, more than half home cost를 paid하고, spouse가 last 6 months 동안 home에 살지 않았고, home이 child, stepchild, or eligible foster child의 main home for more than half the year였고, child dependency requirement가 맞아야 합니다.

이건 자동 Single이 아닙니다. Married taxpayer가 특별한 길을 통해 HOH를 검토하는 것입니다.

정리합니다. HOH equals status, home cost, qualifying person. Home cost와 support를 섞지 마세요. More than half는 exactly half가 아닙니다. Considered unmarried는 married taxpayer의 special HOH path입니다.
""",
    },
    {
        "slug": "04-hoh-qualifying-person-traps",
        "title": "HOH Qualifying Person Traps",
        "questions": "47-61",
        "md": """
# EA Part 1 Week 1 Day 2 Masterclass 04: HOH Qualifying Person Traps

대상 문제: 47-61

## 한 줄 결론

Dependent라고 해서 항상 `HOH qualifying person`은 아니다.

## Qualifying child

Qualifying child가 taxpayer와 more than half the year lived하면 HOH qualifying person 가능성이 크다.

Temporary absence를 기억한다. Education 때문에 away at college인 기간은 자동 fail이 아니다.

## Birth/death year

Qualifying person이 born 또는 died during the year이면 alive during year 기준으로 home test를 조정해서 볼 수 있다.

## Parent rule

Dependent parent는 taxpayer와 같이 살지 않아도 HOH qualifying person이 될 수 있다.

핵심:

- parent가 taxpayer의 dependent여야 한다.
- taxpayer가 parent의 home을 keeping up 하는 cost의 more than half를 paid해야 한다.
- parent가 separate home에 살아도 가능성이 있다.

## Friend trap

Unrelated friend는 all-year household member로 dependent가 될 수 있어도, 그 이유만으로 HOH qualifying person은 generally 아니다.

이건 Day 2에서 반드시 잡아야 하는 함정이다.

## Drill

1. Dependent parent는 taxpayer와 반드시 같이 살아야 하는가?
2. Unrelated friend dependent는 자동 HOH qualifying person인가?
3. Away at college는 residency를 자동 fail시키는가?
4. Parent separate apartment cost의 70%를 taxpayer가 냈다면 어떤 status를 검토하는가?

정답: 아니다, 아니다, 아니다, HOH.
""",
        "audio": """
Masterclass four. HOH qualifying person traps.

이번 module의 한 줄 결론은 dependent라고 해서 항상 HOH qualifying person은 아니라는 것입니다.

Qualifying child가 taxpayer와 more than half the year lived하면 HOH qualifying person 가능성이 큽니다. 여기서 temporary absence를 기억해야 합니다. Education 때문에 away at college인 기간은 residency를 자동 fail시키지 않습니다.

Birth 또는 death year도 조심합니다. Qualifying person이 born 또는 died during the year이면 alive during year 기준으로 home test를 조정해서 볼 수 있습니다.

Parent rule은 매우 중요합니다. Dependent parent는 taxpayer와 같이 살지 않아도 HOH qualifying person이 될 수 있습니다. Parent가 taxpayer의 dependent이고, taxpayer가 parent의 home을 keeping up 하는 cost의 more than half를 paid했다면, parent가 separate home에 살아도 HOH 가능성이 있습니다.

Friend trap도 반드시 잡아야 합니다. Unrelated friend는 all-year household member로 dependent가 될 수 있습니다. 하지만 그 이유만으로 HOH qualifying person은 generally 아닙니다.

시험장에서 이렇게 구분하세요. Dependent parent separate home은 HOH 가능성. Unrelated friend dependent는 HOH warning. Qualifying child lived more than half year는 HOH 가능성. Away at college는 temporary absence 가능성.

정리합니다. HOH qualifying person은 dependent와 완전히 같은 말이 아닙니다. Parent는 special rule. Friend는 trap입니다.
""",
    },
    {
        "slug": "05-qss-mixed-traps",
        "title": "QSS and Mixed Filing-Status Traps",
        "questions": "62-100",
        "md": """
# EA Part 1 Week 1 Day 2 Masterclass 05: QSS and Mixed Filing-Status Traps

대상 문제: 62-100

## 한 줄 결론

Spouse death 문제는 `year of death MFJ`와 `following two years QSS`를 구분한다.

## QSS

`QSS`는 `Qualifying Surviving Spouse`다.

대표 요건:

- spouse died in one of the two years before the current tax year
- taxpayer did not remarry before the end of the tax year
- taxpayer could have filed a joint return with the spouse for the year of death
- taxpayer has a qualifying child or stepchild
- taxpayer paid more than half the cost of keeping up the home
- home was the child's main home for the entire year, except temporary absences

## Year of death vs QSS years

| Spouse death year | Current year | 먼저 볼 것 |
|---|---|---|
| 2025 | 2025 | MFJ for year of death |
| 2024 | 2025 | QSS 가능성 |
| 2023 | 2025 | QSS 가능성 |
| 2022 | 2025 | QSS window generally passed |

## Mixed trap labels

- `MFS education credit` -> limitation
- `unrelated friend` -> HOH warning
- `dependent parent separate home` -> HOH parent rule
- `spouse lived in home during last 6 months` -> considered-unmarried problem
- `spouse died current year` -> MFJ first
- `spouse died prior year + child + home cost` -> QSS

## Final Recap

Day 2 문제는 status label을 먼저 붙이면 쉬워진다.

`December 31 -> MFJ/MFS -> HOH -> QSS -> limitations`
""",
        "audio": """
Masterclass five. QSS and mixed filing-status traps.

이번 module의 한 줄 결론은 spouse death 문제는 year of death MFJ와 following two years QSS를 구분한다는 것입니다.

QSS는 Qualifying Surviving Spouse입니다. 대표 요건을 잡겠습니다.

Spouse died in one of the two years before the current tax year. Taxpayer did not remarry before the end of the tax year. Taxpayer could have filed a joint return with the spouse for the year of death. Taxpayer has a qualifying child or stepchild. Taxpayer paid more than half the cost of keeping up the home. The home was the child's main home for the entire year, except temporary absences.

Year of death와 QSS years를 분리합니다. Spouse died in 2025 and current year is 2025이면 MFJ for year of death를 먼저 봅니다. Spouse died in 2024 and current year is 2025이면 QSS 가능성이 있습니다. Spouse died in 2023 and current year is 2025이면 QSS 가능성이 있습니다. Spouse died in 2022 and current year is 2025이면 QSS two-year window가 generally passed입니다.

Mixed trap label도 정리합니다.

MFS education credit은 limitation.

Unrelated friend는 HOH warning.

Dependent parent separate home은 HOH parent rule.

Spouse lived in home during last six months는 considered-unmarried problem.

Spouse died current year는 MFJ first.

Spouse died prior year plus child plus home cost는 QSS.

Day 2의 마지막 공식은 이것입니다. December 31, then MFJ or MFS, then HOH, then QSS, then limitations.

Status label을 먼저 붙이면 문제는 훨씬 쉬워집니다.
""",
    },
]


def make_masterclass_readme() -> str:
    rows = []
    for module in MODULES:
        slug = module["slug"]
        rows.append(f"| {slug[:2]} | `{slug}.md` | `{slug}.m4a` | {module['questions']} | {module['title']} |")
    return f"""
# EA Part 1 Week 1 Day 2 Masterclass

기준일: {DATE}
목표: Day 2 `filing status`를 실제 문제 풀이 단위로 쪼개서 공부한다.

## Study Order

| 순서 | Markdown | Audio | 연결 문제 | 주제 |
|---|---|---|---|---|
{chr(10).join(rows)}

## Recommended Loop

1. module markdown의 한 줄 결론을 읽는다.
2. `.m4a`를 들으며 판단 순서를 말로 따라 한다.
3. 연결 문제만 푼다.
4. answer file에서 해설을 확인한다.
5. 오답은 `trigger phrase -> status label -> rule` 순서로 적는다.

## Day 2 Core Sentences

1. `Filing status` is generally determined from year-end facts.
2. Married taxpayers generally start with `MFJ` or `MFS`.
3. `MFS` is a limitation warning.
4. `HOH` requires status, home cost, and qualifying person.
5. `Cost of keeping up a home` is not the same as support.
6. A married taxpayer may be `considered unmarried` only if specific tests are met.
7. A dependent parent does not always have to live with the taxpayer for HOH.
8. An unrelated friend dependent is generally not a HOH qualifying person merely because of that dependency.
9. Spouse death in the current year points first to possible `MFJ`.
10. `QSS` generally belongs to the two years after the spouse's year of death.
"""


def main() -> int:
    write(ROOT / "part-1-week-1-day-2-deep-dive.md", dedent(DEEP_DIVE))
    write(ROOT / "part-1-week-1-day-2-100-practice-questions.md", make_questions_md())
    write(ROOT / "part-1-week-1-day-2-100-practice-answers.md", make_answers_md())
    write(MASTERCLASS_DIR / "README.md", dedent(make_masterclass_readme()))
    for module in MODULES:
        slug = module["slug"]
        write(MASTERCLASS_DIR / f"{slug}.md", dedent(module["md"]) + "\n\n## Sources Used\n\n" + sources_md())
        write(MASTERCLASS_DIR / f"{slug}-audio-script.txt", dedent(module["audio"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
