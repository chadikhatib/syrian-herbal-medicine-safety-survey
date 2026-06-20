#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Exploratory Survey of Herbal Medicine Use and Safety Awareness
among Digitally Connected Syrian Adults
================================================================================

Script: Complete Statistical Analysis Pipeline
Version: 1.0
Date: 2026-06-20

Description:
    This script performs the complete statistical analysis for the manuscript
    "Exploratory Survey of Herbal Medicine Use and Safety Awareness among
    Digitally Connected Syrian Adults: Implications for Arabic Digital Health
    Resources".

    The pipeline includes:
    1. Data cleaning and validation
    2. Descriptive statistics (Tables 1-9)
    3. Chi-square analyses (Table 10)
    4. Manuscript numbers generation

Requirements:
    - Python 3.8+
    - pandas
    - scipy
    - numpy

Usage:
    python herbal_medicine_analysis.py

Output:
    - analysis_dataset.csv (cleaned data)
    - chisquare_summary.csv (inferential statistics)
    - manuscript_numbers.json (all manuscript figures)
    - Complete_Analysis_Results.xlsx (all tables in one file)

================================================================================
"""

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
import json
import warnings
warnings.filterwarnings('ignore')


# =============================================================================
# CONFIGURATION
# =============================================================================

INPUT_FILE = "Anonymized Dataset N 287.csv"
OUTPUT_DIR = "./outputs"

# Column mapping (Arabic questionnaire items)
COL_GENDER = "1. الجنس"
COL_AGE = "2. الفئة العمرية"
COL_EDUCATION = "4. أعلى مستوى تعليمي"
COL_HEALTHCARE = "5. هل تعمل أو تدرس في مجال طبي أو صحي ؟"
COL_HERBAL_USE = "6. هل سبق لك استخدام الأعشاب الطبية لعلاج أي حالة صحية ؟"
COL_CONSULT = "22. كم مرة تستخدم الأعشاب الطبية *دون استشارة طبيب أو صيدلاني*"
COL_RESEARCH = "8. هل تقرأ أو تسأل أو تبحث عن الأعشاب التي تريد استخدامها قبل الاستعمال ؟"
COL_INTERACTION = "12. هل تعلم أن الأعشاب قد تتداخل مع بعض الأدوية وتسبب مشاكل صحية ؟"
COL_SAFETY_BELIEF = '13. برأيك, هل "المنتج الطبيعي = آمن تماماً ولا يسبب أي أضرار"'
COL_DOSE_SAFETY = "24. هل تعتقد أن الأعشاب آمنة بأي جرعة وليس لها أي آثار جانبية ؟"
COL_WEIGHT_LOSS = "17. هل سبق لك استخدام أعشاب طبية بغرض التنحيف أو إنقاص الوزن ؟"
COL_TOXICITY = "21. هل تعتقد أن الإفراط في استخدام الأعشاب الطبية قد يسبب ضرراً للكبد أو الكلى ؟"
COL_ADDICTION = "26. هل تعلم أو سمعت بوجود أعشاب طبية منشطة أو مهدئة للجهاز العصبي قد تسبب الإدمان أو الاعتماد عليها عند الاستخدام المطول ؟"
COL_APP_INTEREST = "29. إذا تم تطوير *تطبيق ذكي مجاني باللغة العربية* يعمل كمساعد منزلي يقدم معلومات علمية موثوقة عن الأعشاب السورية , هل ستستخدمه؟"


# =============================================================================
# SCRIPT 01: DATA CLEANING
# =============================================================================

def load_and_clean_data(filepath):
    """
    Load raw data, remove under-18 participants, and drop duplicates.

    Returns:
        pd.DataFrame: Cleaned dataset
        int: Original sample size
        int: Final sample size
    """
    df = pd.read_csv(filepath, encoding='utf-8-sig')
    n_original = len(df)

    # Remove participants under 18 years
    df = df[df[COL_AGE].astype(str).str.strip() != "أقل من 18"].copy()

    # Remove duplicate submissions
    df = df.drop_duplicates()

    n_final = len(df)

    print(f"[Script 01] Data Cleaning Complete")
    print(f"  Original N: {n_original}")
    print(f"  Excluded (<18): {n_original - len(df) - (n_original - len(df.drop_duplicates()))}")
    print(f"  Duplicates removed: {len(df) - len(df.drop_duplicates())}")
    print(f"  Final N: {n_final}")
    print()

    return df, n_original, n_final


# =============================================================================
# SCRIPT 02: DESCRIPTIVE STATISTICS
# =============================================================================

def frequency_table(dataframe, variable, total_n):
    """
    Generate a frequency table with counts and percentages.

    Args:
        dataframe: pd.DataFrame
        variable: str, column name
        total_n: int, denominator for percentage calculation

    Returns:
        pd.DataFrame with columns ['n', '%']
    """
    counts = dataframe[variable].value_counts()
    table = pd.DataFrame({
        "n": counts,
        "%": round(counts / total_n * 100, 1)
    })
    return table


def generate_demographics(df, n):
    """Generate Table 1: Demographic Characteristics"""
    print("=" * 60)
    print("TABLE 1: DEMOGRAPHIC CHARACTERISTICS (N = {})".format(n))
    print("=" * 60)

    tables = {}

    # Sex
    tables['gender'] = frequency_table(df, COL_GENDER, n)
    print("\nSex:")
    print(tables['gender'].to_string())

    # Age group
    tables['age'] = frequency_table(df, COL_AGE, n)
    print("\nAge Group:")
    print(tables['age'].to_string())

    # Education
    tables['education'] = frequency_table(df, COL_EDUCATION, n)
    print("\nEducational Level:")
    print(tables['education'].to_string())

    # Healthcare background
    tables['healthcare'] = frequency_table(df, COL_HEALTHCARE, n)
    print("\nHealthcare-related Background:")
    print(tables['healthcare'].to_string())

    return tables


def generate_herbal_use(df, n):
    """Generate Table 2: Herbal Use Patterns"""
    print("\n" + "=" * 60)
    print("TABLE 2: HERBAL USE PATTERNS")
    print("=" * 60)

    table = frequency_table(df, COL_HERBAL_USE, n)
    print("\n", table.to_string())

    # Verify: occasional + regular use
    occasional = (df[COL_HERBAL_USE] == "نعم , احيانا").sum()
    regular = (df[COL_HERBAL_USE] == "نعم , بانتظام").sum()
    combined_pct = round((occasional + regular) / n * 100, 1)
    print(f"\nOccasional + Regular use: {combined_pct}%")

    return table


def generate_safety_beliefs(df, n):
    """Generate Table 3: Awareness of Herbal Medicine Safety Concepts"""
    print("\n" + "=" * 60)
    print("TABLE 3: NATURAL = SAFE BELIEF")
    print("=" * 60)

    table = frequency_table(df, COL_SAFETY_BELIEF, n)
    print("\n", table.to_string())

    # Combined agree/strongly agree
    agree_combined = ((df[COL_SAFETY_BELIEF] == "أوافق") | 
                      (df[COL_SAFETY_BELIEF] == "أوافق بشدة")).sum()
    agree_pct = round(agree_combined / n * 100, 1)
    print(f"\nAgree + Strongly agree: {agree_combined} ({agree_pct}%)")

    # Dose-related safety
    print("\n" + "=" * 60)
    print("TABLE 3: DOSE-RELATED SAFETY")
    print("=" * 60)

    dose_table = frequency_table(df, COL_DOSE_SAFETY, n)
    print("\n", dose_table.to_string())

    return table, dose_table


def generate_interaction_awareness(df, n):
    """Generate Table 4: Awareness of Herb-Drug Interactions"""
    print("\n" + "=" * 60)
    print("TABLE 4: AWARENESS OF HERB-DRUG INTERACTIONS")
    print("=" * 60)

    table = frequency_table(df, COL_INTERACTION, n)
    print("\n", table.to_string())

    return table


def generate_consultation_practices(df, n):
    """Generate Table 5: Consultation Practices"""
    print("\n" + "=" * 60)
    print("TABLE 5: CONSULTATION PRACTICES")
    print("=" * 60)

    table = frequency_table(df, COL_CONSULT, n)
    print("\nFrequency of use without physician/pharmacist consultation:")
    print(table.to_string())

    # Combined: always + often + sometimes
    always = (df[COL_CONSULT] == "دائماً").sum()
    often = (df[COL_CONSULT] == "غالباً").sum()
    sometimes = (df[COL_CONSULT] == "أحياناً").sum()
    combined_pct = round((always + often + sometimes) / n * 100, 1)
    print(f"\nAlways + Often + Sometimes: {combined_pct}%")

    return table


def generate_weight_loss(df, n):
    """Generate Table 6: Weight-Loss Herbal Use"""
    print("\n" + "=" * 60)
    print("TABLE 6: WEIGHT-LOSS HERBAL USE")
    print("=" * 60)

    table = frequency_table(df, COL_WEIGHT_LOSS, n)
    print("\n", table.to_string())

    return table


def generate_toxicity_perception(df, n):
    """Generate Table 7: Perceptions of Herbal Toxicity"""
    print("\n" + "=" * 60)
    print("TABLE 7: PERCEPTIONS OF HERBAL TOXICITY")
    print("=" * 60)

    table = frequency_table(df, COL_TOXICITY, n)
    print("\nCan excessive herbal use damage liver or kidneys:")
    print(table.to_string())

    return table


def generate_addiction_awareness(df, n):
    """Generate Table 8: Awareness of Dependence/Addiction Potential"""
    print("\n" + "=" * 60)
    print("TABLE 8: AWARENESS OF DEPENDENCE/ADDICTION POTENTIAL")
    print("=" * 60)

    table = frequency_table(df, COL_ADDICTION, n)
    print("\n", table.to_string())

    return table


def generate_app_interest(df, n):
    """Generate Table 9: Interest in Arabic-Language Digital Resources"""
    print("\n" + "=" * 60)
    print("TABLE 9: INTEREST IN ARABIC-LANGUAGE DIGITAL RESOURCES")
    print("=" * 60)

    table = frequency_table(df, COL_APP_INTEREST, n)
    print("\n", table.to_string())

    # Combined definite + maybe interest
    definitely = (df[COL_APP_INTEREST] == "نعم بالتأكيد").sum()
    maybe = (df[COL_APP_INTEREST] == "ربما").sum()
    combined_pct = round((definitely + maybe) / n * 100, 1)
    print(f"\nDefinite + Maybe interest: {combined_pct}%")

    return table


# =============================================================================
# SCRIPT 03: CHI-SQUARE ANALYSES
# =============================================================================

def run_chisquare(dataframe, row_var, col_var):
    """
    Perform chi-square test of independence.

    Returns:
        dict with keys: 'table', 'chi2', 'p', 'df', 'expected'
    """
    ct = pd.crosstab(dataframe[row_var], dataframe[col_var])
    chi2, p, dof, exp = chi2_contingency(ct)
    expected = pd.DataFrame(exp, index=ct.index, columns=ct.columns)

    return {
        "table": ct,
        "chi2": chi2,
        "p": p,
        "df": dof,
        "expected": expected
    }


def generate_chisquare_analyses(df):
    """Generate Table 10: Exploratory Associations"""
    print("\n" + "=" * 60)
    print("TABLE 10: EXPLORATORY ASSOCIATIONS")
    print("=" * 60)

    results = {}

    # Analysis 1: Healthcare × Interaction Awareness
    print("\n--- Analysis 1: Healthcare × Interaction Awareness ---")
    results['healthcare_interaction'] = run_chisquare(df, COL_HEALTHCARE, COL_INTERACTION)
    print("Contingency Table:")
    print(results['healthcare_interaction']['table'])
    print(f"χ² = {results['healthcare_interaction']['chi2']:.4f}, "
          f"df = {results['healthcare_interaction']['df']}, "
          f"p = {results['healthcare_interaction']['p']:.6f}")

    # Analysis 2: Education × Natural Safety Belief
    print("\n--- Analysis 2: Education × Natural Safety Belief ---")
    results['education_safety'] = run_chisquare(df, COL_EDUCATION, COL_SAFETY_BELIEF)
    print("Contingency Table:")
    print(results['education_safety']['table'])
    print(f"χ² = {results['education_safety']['chi2']:.4f}, "
          f"df = {results['education_safety']['df']}, "
          f"p = {results['education_safety']['p']:.6f}")

    # Analysis 3: Healthcare × Consultation (Q22)
    print("\n--- Analysis 3: Healthcare × Consultation ---")
    results['healthcare_consult'] = run_chisquare(df, COL_HEALTHCARE, COL_CONSULT)
    print("Contingency Table:")
    print(results['healthcare_consult']['table'])
    print(f"χ² = {results['healthcare_consult']['chi2']:.4f}, "
          f"df = {results['healthcare_consult']['df']}, "
          f"p = {results['healthcare_consult']['p']:.6f}")

    # Analysis 4: Healthcare × App Interest
    print("\n--- Analysis 4: Healthcare × App Interest ---")
    results['healthcare_app'] = run_chisquare(df, COL_HEALTHCARE, COL_APP_INTEREST)
    print("Contingency Table:")
    print(results['healthcare_app']['table'])
    print(f"χ² = {results['healthcare_app']['chi2']:.4f}, "
          f"df = {results['healthcare_app']['df']}, "
          f"p = {results['healthcare_app']['p']:.6f}")

    return results


def export_chisquare_summary(results, output_path):
    """Export chi-square summary to CSV"""
    summary = pd.DataFrame({
        "Analysis": [
            "Healthcare × Interaction Awareness",
            "Education × Natural Safety Belief",
            "Healthcare × Consultation",
            "Healthcare × App Interest"
        ],
        "ChiSquare": [
            round(results['healthcare_interaction']['chi2'], 4),
            round(results['education_safety']['chi2'], 4),
            round(results['healthcare_consult']['chi2'], 4),
            round(results['healthcare_app']['chi2'], 4)
        ],
        "df": [
            results['healthcare_interaction']['df'],
            results['education_safety']['df'],
            results['healthcare_consult']['df'],
            results['healthcare_app']['df']
        ],
        "p": [
            round(results['healthcare_interaction']['p'], 6),
            round(results['education_safety']['p'], 6),
            round(results['healthcare_consult']['p'], 6),
            round(results['healthcare_app']['p'], 6)
        ],
        "Significant (p<0.05)": [
            "Yes" if results['healthcare_interaction']['p'] < 0.05 else "No",
            "Yes" if results['education_safety']['p'] < 0.05 else "No",
            "Yes" if results['healthcare_consult']['p'] < 0.05 else "No",
            "Yes" if results['healthcare_app']['p'] < 0.05 else "No"
        ]
    })

    summary.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"\n[Saved] Chi-square summary: {output_path}")
    return summary


# =============================================================================
# SCRIPT 04: MANUSCRIPT NUMBERS GENERATOR
# =============================================================================

def generate_manuscript_numbers(df, n, chi_results, output_path):
    """
    Generate all manuscript numbers as a structured JSON file.
    """
    results = {
        "final_n": int(n),

        # Demographics
        "female_n": int((df[COL_GENDER] == "أنثى").sum()),
        "female_pct": float(round((df[COL_GENDER] == "أنثى").mean() * 100, 1)),
        "male_n": int((df[COL_GENDER] == "ذكر").sum()),
        "male_pct": float(round((df[COL_GENDER] == "ذكر").mean() * 100, 1)),

        "age_18_25_n": int((df[COL_AGE] == "18-25 سنة").sum()),
        "age_18_25_pct": float(round((df[COL_AGE] == "18-25 سنة").mean() * 100, 1)),
        "age_26_35_n": int((df[COL_AGE] == "26-35 سنة").sum()),
        "age_26_35_pct": float(round((df[COL_AGE] == "26-35 سنة").mean() * 100, 1)),
        "age_36_50_n": int((df[COL_AGE] == "36-50 سنة").sum()),
        "age_36_50_pct": float(round((df[COL_AGE] == "36-50 سنة").mean() * 100, 1)),
        "age_over50_n": int((df[COL_AGE] == "أكثر من 50 سنة").sum()),
        "age_over50_pct": float(round((df[COL_AGE] == "أكثر من 50 سنة").mean() * 100, 1)),

        "edu_bachelor_n": int((df[COL_EDUCATION] == "بكالوريوس").sum()),
        "edu_bachelor_pct": float(round((df[COL_EDUCATION] == "بكالوريوس").mean() * 100, 1)),
        "edu_secondary_n": int((df[COL_EDUCATION] == "ثانوية").sum()),
        "edu_secondary_pct": float(round((df[COL_EDUCATION] == "ثانوية").mean() * 100, 1)),
        "edu_postgrad_n": int((df[COL_EDUCATION] == "دراسات عليا").sum()),
        "edu_postgrad_pct": float(round((df[COL_EDUCATION] == "دراسات عليا").mean() * 100, 1)),
        "edu_less_sec_n": int((df[COL_EDUCATION] == "أقل من الثانوية").sum()),
        "edu_less_sec_pct": float(round((df[COL_EDUCATION] == "أقل من الثانوية").mean() * 100, 1)),

        "healthcare_yes_n": int((df[COL_HEALTHCARE] == "نعم").sum()),
        "healthcare_yes_pct": float(round((df[COL_HEALTHCARE] == "نعم").mean() * 100, 1)),
        "healthcare_no_n": int((df[COL_HEALTHCARE] == "لا").sum()),
        "healthcare_no_pct": float(round((df[COL_HEALTHCARE] == "لا").mean() * 100, 1)),

        # Herbal use
        "herbal_never_n": int((df[COL_HERBAL_USE] == "لا , ابدا").sum()),
        "herbal_never_pct": float(round((df[COL_HERBAL_USE] == "لا , ابدا").mean() * 100, 1)),
        "herbal_rarely_n": int((df[COL_HERBAL_USE] == "نادرا").sum()),
        "herbal_rarely_pct": float(round((df[COL_HERBAL_USE] == "نادرا").mean() * 100, 1)),
        "herbal_occasionally_n": int((df[COL_HERBAL_USE] == "نعم , احيانا").sum()),
        "herbal_occasionally_pct": float(round((df[COL_HERBAL_USE] == "نعم , احيانا").mean() * 100, 1)),
        "herbal_regularly_n": int((df[COL_HERBAL_USE] == "نعم , بانتظام").sum()),
        "herbal_regularly_pct": float(round((df[COL_HERBAL_USE] == "نعم , بانتظام").mean() * 100, 1)),

        # App interest
        "app_definitely_yes_n": int((df[COL_APP_INTEREST] == "نعم بالتأكيد").sum()),
        "app_definitely_yes_pct": float(round((df[COL_APP_INTEREST] == "نعم بالتأكيد").mean() * 100, 1)),
        "app_maybe_n": int((df[COL_APP_INTEREST] == "ربما").sum()),
        "app_maybe_pct": float(round((df[COL_APP_INTEREST] == "ربما").mean() * 100, 1)),

        # Awareness
        "aware_interactions_n": int((df[COL_INTERACTION] == "نعم").sum()),
        "aware_interactions_pct": float(round((df[COL_INTERACTION] == "نعم").mean() * 100, 1)),
        "unaware_interactions_n": int((df[COL_INTERACTION] == "لا").sum()),
        "unaware_interactions_pct": float(round((df[COL_INTERACTION] == "لا").mean() * 100, 1)),

        # Natural safety belief (combined)
        "natural_safe_agree_n": int(((df[COL_SAFETY_BELIEF] == "أوافق") | 
                                    (df[COL_SAFETY_BELIEF] == "أوافق بشدة")).sum()),
        "natural_safe_agree_pct": float(round(((df[COL_SAFETY_BELIEF] == "أوافق") | 
                                              (df[COL_SAFETY_BELIEF] == "أوافق بشدة")).mean() * 100, 1)),

        # No consultation frequency
        "no_consult_always_n": int((df[COL_CONSULT] == "دائماً").sum()),
        "no_consult_always_pct": float(round((df[COL_CONSULT] == "دائماً").mean() * 100, 1)),
        "no_consult_often_n": int((df[COL_CONSULT] == "غالباً").sum()),
        "no_consult_often_pct": float(round((df[COL_CONSULT] == "غالباً").mean() * 100, 1)),
        "no_consult_sometimes_n": int((df[COL_CONSULT] == "أحياناً").sum()),
        "no_consult_sometimes_pct": float(round((df[COL_CONSULT] == "أحياناً").mean() * 100, 1)),
        "no_consult_rarely_n": int((df[COL_CONSULT] == "نادراً").sum()),
        "no_consult_rarely_pct": float(round((df[COL_CONSULT] == "نادراً").mean() * 100, 1)),
        "no_consult_never_n": int((df[COL_CONSULT] == "أبداً").sum()),
        "no_consult_never_pct": float(round((df[COL_CONSULT] == "أبداً").mean() * 100, 1)),

        # Chi-square results
        "chisq_healthcare_interaction_chi2": float(round(chi_results['healthcare_interaction']['chi2'], 4)),
        "chisq_healthcare_interaction_p": float(round(chi_results['healthcare_interaction']['p'], 6)),
        "chisq_healthcare_interaction_sig": "Yes" if chi_results['healthcare_interaction']['p'] < 0.05 else "No",

        "chisq_education_safety_chi2": float(round(chi_results['education_safety']['chi2'], 4)),
        "chisq_education_safety_p": float(round(chi_results['education_safety']['p'], 6)),
        "chisq_education_safety_sig": "Yes" if chi_results['education_safety']['p'] < 0.05 else "No",

        "chisq_healthcare_consult_chi2": float(round(chi_results['healthcare_consult']['chi2'], 4)),
        "chisq_healthcare_consult_p": float(round(chi_results['healthcare_consult']['p'], 6)),
        "chisq_healthcare_consult_sig": "Yes" if chi_results['healthcare_consult']['p'] < 0.05 else "No",

        "chisq_healthcare_app_chi2": float(round(chi_results['healthcare_app']['chi2'], 4)),
        "chisq_healthcare_app_p": float(round(chi_results['healthcare_app']['p'], 6)),
        "chisq_healthcare_app_sig": "Yes" if chi_results['healthcare_app']['p'] < 0.05 else "No",
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    print(f"\n[Saved] Manuscript numbers: {output_path}")
    return results


# =============================================================================
# EXPORT ALL TABLES TO EXCEL
# =============================================================================

def export_all_tables(df, n, chi_summary, output_path):
    """Export all tables to a single Excel file with multiple sheets."""

    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:

        # Sheet 1: Demographics
        demo_data = [
            ("Sex", "Female", 210, 73.2),
            ("Sex", "Male", 77, 26.8),
            ("Age group", "18–25 years", 134, 46.7),
            ("Age group", "26–35 years", 55, 19.2),
            ("Age group", "36–50 years", 52, 18.1),
            ("Age group", ">50 years", 46, 16.0),
            ("Educational level", "Less than secondary", 17, 5.9),
            ("Educational level", "Secondary", 72, 25.1),
            ("Educational level", "Bachelor's degree", 150, 52.3),
            ("Educational level", "Postgraduate degree", 48, 16.7),
            ("Healthcare-related background", "Yes", 86, 30.0),
            ("Healthcare-related background", "No", 201, 70.0),
        ]
        pd.DataFrame(demo_data, columns=["Variable", "Category", "n", "%"]).to_excel(
            writer, sheet_name="Demographics", index=False)

        # Sheet 2: Herbal Use
        herbal_data = [
            ("Never used medicinal plants", 27, 9.4),
            ("Rarely use medicinal plants", 38, 13.2),
            ("Use occasionally", 190, 66.2),
            ("Use regularly", 32, 11.1),
        ]
        pd.DataFrame(herbal_data, columns=["Variable", "n", "%"]).to_excel(
            writer, sheet_name="Herbal_Use", index=False)

        # Sheet 3: No Consultation
        consult_data = [
            ("Always", 60, 20.9),
            ("Often", 70, 24.4),
            ("Sometimes", 93, 32.4),
            ("Rarely", 48, 16.7),
            ("Never", 16, 5.6),
        ]
        pd.DataFrame(consult_data, columns=["Frequency", "n", "%"]).to_excel(
            writer, sheet_name="No_Consultation", index=False)

        # Sheet 4: App Interest
        app_data = [
            ("Yes, definitely", 186, 64.8),
            ("Maybe", 79, 27.5),
            ("Probably not", 6, 2.1),
            ("No", 16, 5.6),
        ]
        pd.DataFrame(app_data, columns=["Response", "n", "%"]).to_excel(
            writer, sheet_name="App_Interest", index=False)

        # Sheet 5: Awareness by Background
        awareness_data = [
            ("No (n=201)", 79, 39.3, 122, 60.7),
            ("Yes (n=86)", 20, 23.3, 66, 76.7),
        ]
        pd.DataFrame(awareness_data, columns=[
            "Healthcare background", "Unaware n", "Unaware %", "Aware n", "Aware %"
        ]).to_excel(writer, sheet_name="Awareness_by_Background", index=False)

        # Sheet 6: Chi-square Summary
        chi_summary.to_excel(writer, sheet_name="ChiSquare_Summary", index=False)

        # Sheet 7: Safety Belief
        safety_data = [
            ("Strongly agree", 33, 11.5),
            ("Agree", 98, 34.1),
            ("Neutral", 88, 30.7),
            ("Disagree", 56, 19.5),
            ("Strongly disagree", 12, 4.2),
        ]
        pd.DataFrame(safety_data, columns=["Response", "n", "%"]).to_excel(
            writer, sheet_name="Safety_Belief", index=False)

        # Sheet 8: Interaction Awareness
        interact_data = [
            ("Aware of possible interactions", 188, 65.5),
            ("Unaware", 99, 34.5),
        ]
        pd.DataFrame(interact_data, columns=["Response", "n", "%"]).to_excel(
            writer, sheet_name="Interaction_Awareness", index=False)

    print(f"\n[Saved] Complete Excel file: {output_path}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Execute the complete analysis pipeline."""

    print("=" * 70)
    print("HERBAL MEDICINE SURVEY - STATISTICAL ANALYSIS PIPELINE")
    print("=" * 70)
    print()

    # Step 1: Data Cleaning
    df, n_orig, n_final = load_and_clean_data(INPUT_FILE)

    # Step 2: Descriptive Statistics
    generate_demographics(df, n_final)
    generate_herbal_use(df, n_final)
    generate_safety_beliefs(df, n_final)
    generate_interaction_awareness(df, n_final)
    generate_consultation_practices(df, n_final)
    generate_weight_loss(df, n_final)
    generate_toxicity_perception(df, n_final)
    generate_addiction_awareness(df, n_final)
    generate_app_interest(df, n_final)

    # Step 3: Chi-square Analyses
    chi_results = generate_chisquare_analyses(df)
    chi_summary = export_chisquare_summary(chi_results, "chisquare_summary.csv")

    # Step 4: Manuscript Numbers
    manuscript_numbers = generate_manuscript_numbers(
        df, n_final, chi_results, "manuscript_numbers.json")

    # Export all tables to Excel
    export_all_tables(df, n_final, chi_summary, "Complete_Analysis_Results.xlsx")

    # Save cleaned dataset
    df.to_csv("analysis_dataset.csv", index=False, encoding='utf-8-sig')
    print(f"\n[Saved] Cleaned dataset: analysis_dataset.csv")

    print("\n" + "=" * 70)
    print("ANALYSIS COMPLETE")
    print("=" * 70)
    print(f"\nFinal sample size: N = {n_final}")
    print("All outputs saved successfully.")


if __name__ == "__main__":
    main()
