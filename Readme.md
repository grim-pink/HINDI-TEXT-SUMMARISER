# Text Summarization for Indian Languages

## Authors

- Ritisha Singh (ritisha21089@iiitd.ac.in)
- Shruti Jha (shruti21289@iiitd.ac.in)

## Abstract

Indian languages have a rich linguistic diversity and are spoken by a large population, yet automatic text summarization for these languages has received little attention in academic research. This project tackles the challenges highlighted by the Indian Language Summarization Task (ILSUM) by developing tailored solutions for Indian English, Bengali, Hindi, and Gujarati. Our proposed approach combines Named Entity Recognition (NER) with advanced multilingual transformer models to generate semantically rich summaries. Additionally, we incorporate Optical Character Recognition (OCR) capabilities, enabling the processing of non-digital data formats.

## Introduction

In the fast-progressing field of natural language processing (NLP), text summarization serves many purposes. With the growing amount of digital content in various languages, efficient techniques are needed to summarize it while considering specific linguistic characteristics and difficulties. This project focuses on creating a summarization model for Hindi, one of the most spoken languages globally.

## Motivation

The research was driven by the requirement to tackle the difficulties of Hindi text summarization, such as code-mixing and script mixing, which make it hard for current techniques to summarize effectively. The rise of Hindi digital content on different platforms necessitates automated summarization tools that can quickly and effectively sort through large amounts of information.

## Literature Survey

Several works highlight the challenges and opportunities in automatic text summarization for Indian languages. These include various techniques such as extractive and abstractive summarization, graph-based methods, and rule-based approaches. The need for language-specific resources and deep learning architectures is emphasized to improve the quality of summarization.

## Methodology

### Dataset Overview

The dataset provided by ILSUM includes headings, articles, and summaries, aimed at generating fixed-length extractive or abstractive summaries for each news article. This dataset includes over 15,000 unique and relevant articles for each language, with features like code and script mixing, reflecting realistic scenarios.

### Proposed Architecture

Our model integrates several advanced functionalities beyond text summarization, such as NER and OCR. NER enhances the semantic richness of summaries by identifying and categorizing key entities. OCR enables the processing of non-digital data formats, broadening the application horizon of the proposed model.

### Model Fine-tuning

To achieve state-of-the-art performance, we fine-tuned two pre-trained language models: IndicBART and mT5-base. This allows leveraging their pre-existing knowledge and adapting them specifically to Hindi summarization.

## Results

The Google mT5 base model outperforms the IndicBart model across various evaluation metrics, achieving higher scores in ROUGE-1, ROUGE-2, ROUGE-L, and BERT Score F1. For NER, the model demonstrates promising results with an accuracy of 95.79%.

## Observations

For the combined tasks of summarization and NER, task synchronization challenges were encountered due to the disparate nature of the datasets. Expanding the NER model's dataset to encompass a broader vocabulary could potentially refine its classification capabilities and improve overall performance.

## Conclusion and Future Work

Future work includes developing a model from the ground up, using MUSE embeddings for bilingual embedding, and incorporating FastText embeddings to enhance semantic richness. Additionally, integrating pre-trained models like mT5 large can further enhance performance.

## Additional Resources

For more details, refer to the [project report](Report.pdf).

You can also find more information and related resources at this [Google Drive link](https://drive.google.com/file/d/1jC_Tz2vQ-hlBy3rpXiCiTGqw-FoaJmMO/view?usp=sharing).

