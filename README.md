# Data Engineering Fundamentals

This repository contains hands-on implementations of fundamental **Data Engineering concepts using Python**. It includes problems related to data processing, file handling, text processing, data structures, algorithms, and other data engineering techniques.

The repository will continue to grow as I explore and implement new concepts.

## Problems

| Problem                                | File                     | Description                                                                                                                                                                                     |
| -------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Word Frequency Analysis Using Heap** | `word_frequency_heap.py` | Processes a text file to calculate the total frequency of each word and the number of lines containing that word. Words are ordered by descending frequency using a custom heap implementation. |

## 1. Word Frequency Analysis Using Heap

### Problem

Given a text file containing multiple lines, process the text and generate the following information for every unique word:

```text id="hpsf75"
word, total frequency, number of lines containing the word
```

Words are separated by any **non-alphanumeric character** and are treated as lowercase.

The final output is arranged in **descending order of total word frequency using a heap data structure**.

### Concepts Implemented

* File handling
* Text preprocessing
* Custom word parsing
* Frequency counting
* Max Heap
* Heapify
* Build Heap
* Heap-based sorting

## Repository Structure

```text id="f9mrmj"
data-engineering-fundamentals/
│
├── word_frequency_heap.py
├── data/
│   └── sample_text.txt
└── README.md
```

More problems and implementations will be added as the repository grows.

## Technologies

* Python 3

## Purpose

This repository documents my practical exploration of Data Engineering fundamentals through problem solving and implementation. The focus is on understanding how data is processed, transformed, organized, and analyzed while implementing important underlying algorithms and data structures from scratch.
