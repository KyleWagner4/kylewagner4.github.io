---
title: SEC 10-K / 10-Q Analyzer
summary: Pulls XBRL filings from SEC EDGAR and normalizes them across reporting conventions into comparable three-statement financials.
order: 1
metric: { value: '10 yr', label: 'Trend history' }
draft: true
---

A Flask tool that reads structured XBRL data straight from EDGAR, maps each
company's tags to a common chart of accounts, and presents clean
three-statement financials with computed ratios, single-company or side by
side. The full case study is being written.
