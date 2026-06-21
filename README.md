# Exploratory Survey of Herbal Medicine Use and Safety Awareness among Digitally Connected Syrian Adults: Statistical Analysis Pipeline

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

This repository contains the complete data management workflow, statistical analysis scripts, reproducible analysis pipeline, and supporting documentation for the study:

**"Exploratory Survey of Herbal Medicine Use and Safety Awareness among Digitally Connected Syrian Adults: Implications for Arabic Digital Health Resources."**

The study investigated patterns of herbal medicine use, safety awareness, perceptions of herbal toxicity, awareness of potential herb–drug interactions, consultation practices, information-seeking behaviors, and interest in Arabic-language digital health resources among Syrian adults.

Following eligibility screening and data cleaning, the final analytical dataset consisted of **287 participants aged 18 years and older**.

---
## Article Status

This repository accompanies the manuscript:

**Exploratory Survey of Herbal Medicine Use and Safety Awareness among Digitally Connected Syrian Adults: Implications for Arabic Digital Health Resources**

Submitted to **PLOS ONE (2026)**.

This repository serves as the official reproducibility archive and contains the anonymized dataset, questionnaire, codebook, statistical analysis plan, supplementary materials, and analysis scripts associated with the manuscript.

Current repository version: **v1.0 (submission version)**.
---

## Repository DOI

Zenodo Archive:

DOI: 10.5281/zenodo.20777941

The DOI provides permanent access to all study materials and archived repository versions.
---

## Study Objectives

The study aimed to:

1. Describe patterns of herbal medicine use among digitally connected Syrian adults.
2. Assess selected aspects of herbal medicine safety awareness.
3. Evaluate awareness of potential herb–drug interactions.
4. Explore consultation practices related to herbal medicine use.
5. Identify common sources of herbal medicine information.
6. Assess awareness of potential herbal toxicity and dependence-related concerns.
7. Evaluate interest in Arabic-language digital resources for medicinal plant information.
8. Generate exploratory evidence to support future health education and digital health initiatives.

---

## Study Design

**Design:** Exploratory cross-sectional online survey

**Study Period:** 15 April 2026 – 20 May 2026

**Survey Language:** Arabic

**Survey Platform:** Google Forms

**Sampling Method:** Non-probability convenience sampling

**Target Population:** Syrian adults aged 18 years and older

**Final Sample Size:** N = 287

---

## Data Processing Workflow

### Data Cleaning

The data processing pipeline includes:

* Importing raw survey responses
* Screening eligibility criteria
* Excluding participants younger than 18 years
* Reviewing incomplete and invalid records
* Creating the final analysis dataset
* Producing reproducible descriptive and inferential analyses
---
## Open Science Statement

In accordance with the PLOS Data Policy, all materials necessary to reproduce the findings reported in the manuscript are publicly available in this repository.

Available materials include:

- Anonymized dataset
- Arabic survey questionnaire
- English questionnaire translation
- Codebook and data dictionary
- Statistical Analysis Plan (SAP)
- Reproducibility Guide
- Statistical analysis scripts
- Ethics approval documentation
---

## Statistical Analyses

### Descriptive Analyses

Categorical variables were summarized using frequencies and percentages.

The analysis pipeline generates all manuscript tables:

* Table 1. Demographic Characteristics of Participants
* Table 2. Medicinal Plant Use Patterns
* Table 3. Awareness of Herbal Medicine Safety Concepts
* Table 4. Awareness of Herb–Drug Interactions
* Table 5. Consultation Practices
* Table 6. Weight-Loss Herbal Use
* Table 7. Perceptions of Potential Herbal Toxicity
* Table 8. Awareness of Dependence/Addiction Potential
* Table 9. Interest in Arabic-Language Digital Resources
* Table 10. Association between Healthcare Background and Awareness of Potential Herb–Drug Interactions

---

### Exploratory Inferential Analyses

Exploratory chi-square analyses were conducted to examine associations between selected participant characteristics and herbal medicine safety-related variables.

The primary association reported in the manuscript was:

* Healthcare background × awareness of potential herb–drug interactions

Additional exploratory analyses included:

* Educational level × belief that natural products are inherently safe
* Healthcare background × use of medicinal plants without professional consultation
* Healthcare background × interest in Arabic-language digital resources

Because the study employed an exploratory design and a non-probability sample, inferential findings should be interpreted as hypothesis-generating rather than confirmatory.

---

## Repository Structure

```text
├── data/
│   ├── raw_data.csv
│   ├── cleaned_data.csv
│   ├── data_dictionary.csv
│   └── codebook.csv
│
├── scripts/
│   ├── data_cleaning.py
│   ├── descriptive_analysis.py
│   ├── chi_square_analysis.py
│   ├── tables_generation.py
│   └── statistical_pipeline.py
│
├── outputs/
│   ├── Table1_DemographicCharacteristics.csv
│   ├── Table2_MedicinalPlantUsePatterns.csv
│   ├── Table3_HerbalMedicineSafetyConcepts.csv
│   ├── Table4_HerbDrugInteractionAwareness.csv
│   ├── Table5_ConsultationPractices.csv
│   ├── Table6_WeightLossHerbalUse.csv
│   ├── Table7_PotentialHerbalToxicity.csv
│   ├── Table8_DependenceAddictionAwareness.csv
│   ├── Table9_ArabicDigitalResourceInterest.csv
│   └── Table10_HealthcareBackground_HerbDrugInteraction.csv
│
├── SAP/
│   └── Statistical_Analysis_Plan.pdf
│
├── README.md
│
└── LICENSE
```
## Supplementary Materials

| Supplement | File |
|------------|------|
| S1 | Arabic Questionnaire |
| S2 | Response Bias Assessment |
| S3 | Psychometric Assessment |
| S4 | Qualitative Thematic Analysis |
| S5 | Medicinal Plant Safety Database |
| S6 | STROBE Checklist |
| S7 | Statistical Analysis Plan (SAP) |
| S8 | Data Dictionary & Codebook |
| S9 | Reproducibility Guide |
| S10 | Ethics Approval Documentation |
| S11 | Anonymized Dataset |

These materials are provided to support transparency, reproducibility, and secondary research use.

---

## Software Requirements

Analyses can be reproduced using:

### Python

* Python 3.11+
* pandas
* numpy
* scipy
* statsmodels
* openpyxl

### Alternative Software

Equivalent analyses can be reproduced using:

* IBM SPSS Statistics 29
* R (Version 4.0 or later)

---

## Ethical Approval

The study was conducted in accordance with the ethical principles of the Declaration of Helsinki (2013).

Ethical approval was obtained from the Biomedical Ethics Committee of the Syrian Herbs & Alternative Medicine Association (SHAMNA), Syria, in collaboration with the Faculty of Pharmacy, Manara University.

**Approval Number:** SHAMNA-26-04

**Approval Date:** 10 April 2026

All participants provided electronic informed consent prior to participation.

---

## Reproducibility

The repository is intended to facilitate transparent and reproducible research by providing:

* Data cleaning procedures
* Statistical analysis scripts
* Table generation workflows
* Documentation of variable coding and transformations
* Statistical Analysis Plan (SAP)

Researchers may reproduce all descriptive and exploratory analyses reported in the manuscript using the supplied code and data files.

---
## Repository Contents

This repository contains:

- Primary research data
- Metadata documentation
- Variable coding framework
- Statistical analysis workflow
- Supplementary methodological documents
- Reproducibility materials
- Ethics documentation

No personally identifiable participant information is included.

---

## Citation

If you use the analysis workflow, code structure, or accompanying materials, please cite:

```bibtex
@article{khatib2026herbal,
  title={Exploratory Survey of Herbal Medicine Use and Safety Awareness among Digitally Connected Syrian Adults: Implications for Arabic Digital Health Resources},
  author={Khatib, Chadi and Abo Kaf, Tasneim and Masri, Tasnim Haj F. and Mathbout, Nour and Zayat, Yaman},
  year={2026},
  note={Submitted to PLOS ONE, 2026}
}
```

---

## Correspondence

**Dr. Chadi Khatib**

Faculty of Pharmacy
Manara University
Syria

Email: [chadi.khatib@manara.edu.sy](mailto:chadi.khatib@manara.edu.sy)

---
## Data Sharing and Reuse

The anonymized dataset and accompanying materials are made available for academic, educational, and non-commercial research purposes.

Users are encouraged to cite the original study when reusing the data or materials.

No attempt should be made to identify individual participants.

---

## Disclaimer

The dataset was obtained through a non-probability convenience sample of digitally connected Syrian adults. Findings should therefore be interpreted within the context of the study design and are not intended to represent the entire Syrian population.

All inferential analyses are exploratory and should be interpreted as hypothesis-generating.
