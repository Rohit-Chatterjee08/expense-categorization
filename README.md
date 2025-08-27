# 💰 Expense Categorizer

An intelligent web application that uses Natural Language Processing (NLP) to automatically categorize your financial transactions.

## Live Demo

You can try the live application here: **https://huggingface.co/spaces/chatterjeerohit08/expense-categorization**

---

## Overview

Tired of manually sorting your expenses? This tool simplifies the process by taking a raw transaction description and instantly assigning it a relevant category like "Food," "Transport," or "Bills."

The application is powered by a `scikit-learn` pipeline that combines **TF-IDF Vectorization** and a **Multinomial Naive Bayes** classifier to understand and classify text.

**Key Features:**
-   **Automatic Categorization:** Instantly classifies expenses from plain text.
-   **Simple Interface:** Just type a description and click a button.
-   **Modern UI:** A clean, modern, and user-friendly interface built with Gradio and custom CSS.
-   **NLP-Powered:** Uses a classic and effective machine learning model for text classification.

---

## How to Use

1.  Simply type a transaction description into the input box.
2.  Click the "Categorize Expense" button.
3.  The app will display the predicted category in a styled tag.

**Example Inputs:**
-   `UBER TRIP PAYMENT`
-   `STARBUCKS COFFEE`
-   `MONTHLY RENT PAYMENT`

---

## Technology Stack

-   **Backend & Modeling:** Python, Scikit-learn
-   **Web Framework/UI:** Gradio
-   **Deployment:** Hugging Face Spaces

---

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [Your GitHub Repository URL]
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd [repository-name]
    ```
3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the application:**
    ```bash
    python app_expense.py
    ```
