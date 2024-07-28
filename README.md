# LLM Comparison App
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-v2-orange)](https://dash.plotly.com/)
[![I Love Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)                    
[![Machine Learning](https://img.shields.io/badge/Topic-Machine%20Learning-orange)](https://en.wikipedia.org/wiki/Machine_learning)
[![LLMs](https://img.shields.io/badge/Topic-LLMs-green)](https://en.wikipedia.org/wiki/Large_language_model)

This Dash application provides a side-by-side comparison of two Large Language Models (LLMs):

* **Llama-3.1-8B-Instruct**
* **Mistral-Nemo**

Users can input text, receive inferences from both models, and provide feedback to help improve their performance.

## Task

▶️  ***Extract email signature from an email address***
  
   * -- Both these models use the same prompt after a series of prompt-tunning seen on this colab 👉🏾 https://github.com/dallo7/compareNemo-MistralVsLlama/blob/70abf364d8e42618ff4e3ca2a6f5dc4b0830dfa0/tinkerIT.ipynb
   * -- I am parsing the same query to both the models and using Human Eval you can determine the better model
   * -- Also, I had to create a wrapper for the llama 3.1 8B to handle the model response
   * -- Use the custom Evaluation datasets to test the models performance 👉🏾 https://github.com/dallo7/compareNemo-MistralVsLlama/blob/70abf364d8e42618ff4e3ca2a6f5dc4b0830dfa0/Victor%20Email.pdf

* Check out the Demo Hosted here‼️ https://comparenemo-mistralvsllama-1.onrender.com/ 

## Sample Input

```bash
Test Case 1: Simple Email with Full Signature
Subject: Meeting follow-up

Hi Sarah,

I hope this email finds you well. I wanted to check in on your thoughts regarding the new marketing campaign. Please let me know if you have any questions or concerns.

Best,
John Smith
Marketing Manager
Acme Corporation
123 Main Street
Anytown, CA 12345
Phone: (555) 555-1212
Email: john.smith@acmecorp.com
Website: www.acmecorp.com

```


## Sample Output

```bash

**Full Name: John Smith                                                                                                     
**Email: john.smith@acmecorp.com 
**Company Name: Acme Corporation
**Location: 123 Main Street, Anytown, CA 12345
**Telephone Number: (555) 555-1212 
```

## Features

* **Interactive Interface:** User-friendly Dash interface for seamless model comparison.
* **Real-time Inference:**  Get prompt results from both LLMs instantly.
* **Feedback Collection:**  Users can rate outputs to contribute to reinforcement learning with human feedback (RLHF).
* **Data Export:** Export feedback data for further analysis.

## Technologies Used

* **Dash:**  Core framework for building the interactive web application.
* **Dash Bootstrap Components:** For styling and layout enhancements.
* **Pandas:** For data manipulation and storage of feedback.
* **Llama-3.1-8B-Instruct & Mistral-Nemo:** The Large Language Models being compared.
* **Gradio Client:**  Potentially for integrating with Gradio for model inference (if used in your `models.py`).

## Installation

1. **Clone the Repository:**
   ```bash
   git clone [invalid URL removed]
   ```
2. Install Dependencies:  
   ```bash
    pip install -r requirements.txt
   ```
3. Run the App
    ```bash
    python app.py
    ```
4. Usage
*  Launch the App: Open a web browser and navigate to ```bash http://127.0.0.1:5050/``` (or the address shown in your terminal when running the app).
*  Enter Text: Type or paste your text into the input fields for each model.
*  Click "Inference": Get responses from both LLMs.
*  Provide Feedback: Use the "Like" and "Dislike" buttons to rate the outputs.
*  Export Data: (Optional) Download the feedback data in Excel format.
  
6. License
This project is licensed under the MIT License.                    
  
