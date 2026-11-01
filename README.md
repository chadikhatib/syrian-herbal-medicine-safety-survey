# Syrian Herbal Medicine Safety & Digital Health Survey: Reproducibility Pipeline (v2.1)

## Overview
This repository contains the complete reproducible analytical pipeline, anonymized dataset (N=287), bilingual questionnaire, codebook, statistical analysis plan, and supplementary appendices for the study:
"Exploratory Survey of Herbal Medicine Use and Safety Awareness among Digitally Connected Syrian Adults: Implications for Arabic Digital Health Resources" (Submitted to PLOS ONE, Revision R1).

## Repository Structure
- `Anonymized_Dataset_N_287.csv`: Primary analytical dataset (N = 287)
- `reproduce_analysis.py`: Executable Python 3.11 script reproducing all descriptive & inferential analyses
- `Codebook_and_Data_Dictionary_v2.1.docx`: Full variable mapping for Q1–Q30 and derived variables
- `Supplementary_Information_Appendices.docx`: S1–S4 and S6–S9 Appendices
- `Release_Notes_v2.1.docx`: Chronological archive changelog
- `requirements.txt`: Environment package dependencies

## Reproducibility Guide
1. Clone or download repository files.
2. Install Python 3.11+ dependencies: `pip install -r requirements.txt`
3. Run the analytical script: `python reproduce_analysis.py Anonymized_Dataset_N_287.csv`

## Ethics Approval
Approved by the Biomedical Ethics of the Syrian Herbs & Alternative Medicine Association (SHAMNA), Syria (Approval No. SHAMNA-26-04; 10 April 2026).
