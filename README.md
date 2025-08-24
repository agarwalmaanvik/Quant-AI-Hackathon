# Quant-AI: Automated Valuation with AI-Powered Foresight

**A hackathon project to automate financial valuation using a quantitative engine and an AI-powered qualitative insights engine.**

---

## The Problem: Analysis Paralysis in Finance

Financial valuation is a cornerstone of investment, yet the process is fundamentally broken. Analysts spend **80% of their time on manual data collection** and model building, leaving only 20% for the crucial task of analysis. Furthermore, existing models are adept at processing numbers but fail to systematically incorporate the vast, unstructured world of **qualitative data**. Critical insights from news, management sentiment, and industry trends are often integrated subjectively, leading to models that are slow, biased, and incomplete.

## The Solution: Quant-AI

Quant-AI is an automated platform designed to bridge the gap between quantitative rigor and qualitative foresight. Our system streamlines the entire valuation workflow, transforming a week of manual work into minutes of automated analysis.

### How It Works

1.  **Automated Modeling Engine:** The platform ingests a company's financial data via APIs to instantly generate a standardized three-statement financial model and a baseline Discounted Cash Flow (DCF) valuation.
2.  **Qualitative Insights Engine:** Using the OpenAI API, the platform scans and interprets real-time news, earnings call transcripts, and industry reports. It performs sentiment analysis and thematic extraction to identify risks and opportunities.
3.  **Dynamic Valuation:** The true innovation lies in the final step. The qualitative insights are used to generate **justifiable, data-driven recommendations** for adjusting the key assumptions in the DCF model, producing a more holistic and forward-looking valuation.

---

## Proof-of-Concept (POC) & Repository Structure

This repository contains the foundational code and financial models that prove the feasibility of the Quant-AI platform. It demonstrates a command of both the financial principles and the technical skills required for execution.

### 📂 `Financial Models (Excel)`

This directory contains the **architectural blueprints** for our platform's output. These are detailed, real-world financial models that serve as the structural templates for what our engine will generate automatically.

* **Key Files:** `TAMO - FS Analysis.xlsx`, `Beta.xlsx`
* **[Click here to explore the Financial Models](./Financial%20Models(Excel))**

### 📂 `Quantitative Scripts (Python)`

This directory contains the **functional building blocks** for our platform's backend. These Python scripts showcase the ability to perform the complex calculations needed for automated valuation and risk analysis.

* **Key Files:** `Beta.py`, `VAR/`
* **[Click here to explore the Quantitative Scripts](./Quantitative%20Scripts%20(Python))**

---

## Hackathon Goals

Our primary goal for this hackathon is to build a functional Minimum Viable Product (MVP) that:
1.  Takes a stock ticker as input.
2.  Builds a simplified, automated DCF model.
3.  Pulls the latest news headlines for that stock.
4.  Uses the OpenAI API to generate a "Sentiment Score."
5.  Displays the baseline valuation alongside the AI-driven sentiment score to prove the core concept.
