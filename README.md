# MultiModal Disaster Response Agent

## Overview
This repository contains the implementation of a **MultiModal Crisis Classification Model** that integrates text and images for disaster response analysis. The model is based on the research paper *"Towards MultiModal Disaster Response Agents"* and is designed to extract relevant disaster-related information from social media platforms, particularly Twitter.

## Problem Statement
The increasing frequency of natural disasters necessitates **efficient and real-time emergency response**. While social media provides real-time data, extracting relevant crisis-related information remains challenging. Traditional text-based classification models (e.g., AIDR) and image-based models have limitations. This project aims to enhance **situational awareness** by leveraging multimodal learning that fuses text and images.

## Approach
- The project uses the **CrisisMMD dataset**, a human-labeled multimodal dataset for disaster classification.
- We experiment with **multimodal fusion techniques** to improve disaster relevance classification, severity assessment, and humanitarian categorization.
- Initially, we tested a baseline multimodal model **without external knowledge infusion**, achieving a **training accuracy of 92.8% but validation/test accuracy of ~70%**, indicating overfitting.
- Future work will integrate **Visual Language Models (VLMs) for richer image-text interactions** and **Named Entity Recognition (NER) for location extraction**.

## Features
- **Multimodal Data Processing:** Leverages both text and image modalities for crisis classification.
- **Crisis Classification Tasks:**
  - **Task 1:** Identifies whether a social media post is informative or not.
  - **Task 2:** Categorizes the type of crisis-related information (e.g., injured people, infrastructure damage, missing persons, etc.).
  - **Task 3:** Assesses damage severity (severe, mild, or little/no damage).
- **Guided Cross Attention Mechanism:** Enhances feature fusion between text and image modalities.
- **Deep Learning Models Used:**
  - **Text Processing:** ELECTRA Transformer Encoder
  - **Image Processing:** DenseNet-based CNN

## Dataset
The model is trained on **CrisisMMD**, a dataset of **Twitter posts with text and image pairs** from real-world disasters such as:
- Hurricane Irma, Hurricane Harvey, Hurricane Maria
- Mexico Earthquake, California Wildfires, Iraq-Iran Earthquake
- Sri Lanka Floods

Preprocessing steps include:
- **Text Cleaning:** Removal of URLs, special characters, and redundant metadata.
- **Image Processing:** Resizing to a standard format.
- **Train-Test Split:** The dataset is divided into **train, validation, and test sets** to ensure robust evaluation.

## Installation (To be updated)
To set up the project environment, install dependencies:
```bash
pip install -r requirements.txt
```

## Usage (To be updated)
Run the model using the provided script:
```bash
python train.py --config config.yaml
```

## Results & Observations
- **Training Accuracy:** 92.8%
- **Validation Accuracy:** ~68%
- **Test Accuracy:** ~70%
- **Key Challenges:** Overfitting, lack of external knowledge infusion, feature extraction inefficiencies.
- **Next Steps:** Integration of VLMs for image interpretation and NER for location extraction.

## Future Work
- Improve **multimodal feature alignment**.
- Integrate **VLMs for richer image context**.
- Use **NER to extract and map disaster locations**.
- Enhance **generalization across different crisis types**.

## Contributors
- **Christine N. Muthee**
- **Keriane L. Nzabampema** 



---

