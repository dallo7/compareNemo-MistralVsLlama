# LLM Comparison App

[![I Love Open Source](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)                    
[![GitHub stars](https://img.shields.io/github/stars/YOUR-USERNAME/YOUR-REPOSITORY)](https://github.com/YOUR-USERNAME/YOUR-REPOSITORY) 
[![Machine Learning](https://img.shields.io/badge/Topic-Machine%20Learning-orange)](https://en.wikipedia.org/wiki/Machine_learning)
[![LLMs](https://img.shields.io/badge/Topic-LLMs-green)](https://en.wikipedia.org/wiki/Large_language_model)

This Dash application provides a side-by-side comparison of two Large Language Models (LLMs):

* **Llama-3.1-8B-Instruct**
* **Mistral-Nemo**

Users can input text, receive inferences from both models, and provide feedback to help improve their performance.

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
* ** Launch the App: Open a web browser and navigate to http://127.0.0.1:5050/ (or the address shown in your terminal when running the app).
* ** Enter Text: Type or paste your text into the input fields for each model.
* ** Click "Inference": Get responses from both LLMs.
* ** Provide Feedback: Use the "Like" and "Dislike" buttons to rate the outputs.
* ** Export Data: (Optional) Download the feedback data in Excel format.
  
6. License
This project is licensed under the MIT License.   

**Replace:**

- `dallo7` with your GitHub username.
- `https://github.com/dallo7/compareNemo-MistralVsLlama` with the name of your repository.

**Add:**

- A `LICENSE` file (MIT License is recommended for open-source projects).
- A `requirements.txt` file listing your project's dependencies.
