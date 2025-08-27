# app_expense.py

import gradio as gr
import joblib

# --- 1. Load the Trained NLP Pipeline ---
pipeline = joblib.load('expense_categorizer_pipeline.joblib')

# --- 2. Custom CSS for a Modern Finance App UI ---
custom_css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

/* Main theme and layout */
body, #expense-app {
    background-color: #f7f9fc;
    font-family: 'Inter', sans-serif;
}
#expense-app {
    border-radius: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

/* Header styling */
#header h1 {
    color: #1a202c;
    font-size: 2.5em;
    font-weight: 700;
}
#header p {
    color: #718096;
    font-size: 1.1em;
}

/* Input textbox styling */
.gradio-container .form-control {
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    background-color: #ffffff;
}

/* Button styling */
#categorize-button {
    background-color: #4299e1; /* Blue */
    color: white;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    transition: background-color 0.3s ease;
}
#categorize-button:hover {
    background-color: #2b6cb0; /* Darker Blue */
}

/* Custom styling for the output category tag */
.category-output-wrapper {
    padding: 20px;
    text-align: center;
}
.category-tag {
    display: inline-block;
    padding: 12px 24px;
    background-color: #4299e1;
    color: white;
    font-size: 1.2em;
    font-weight: 600;
    border-radius: 50px; /* Pill shape */
    box-shadow: 0 4px 10px rgba(66, 153, 225, 0.4);
}
"""

# --- 3. Define the Prediction Function ---
def categorize_expense(description):
    """
    Takes a text description, predicts the category, and returns it
    as a styled HTML component.
    """
    if not description:
        return "<div class='category-output-wrapper'>Please enter a description.</div>"
    
    # The pipeline expects a list of items to predict
    predicted_category = pipeline.predict([description])[0]
    
    # Format the output as an HTML div with our custom class
    html_output = f"""
    <div class='category-output-wrapper'>
        <p style='color: #718096; font-size: 1em;'>Predicted Category:</p>
        <div class='category-tag'>{predicted_category}</div>
    </div>
    """
    return html_output

# --- 4. Build the Gradio App with gr.Blocks ---
with gr.Blocks(css=custom_css, elem_id="expense-app") as app:
    with gr.Column(elem_id="header"):
        gr.Markdown("<h1>💰 Expense Categorizer</h1>")
        gr.Markdown("<p>Enter a transaction description to automatically assign a spending category.</p>")

    # Input section
    expense_input = gr.Textbox(
        label="Transaction Description",
        placeholder="e.g., UBER TRIP PAYMENT, STARBUCKS COFFEE"
    )
    
    # Button to trigger the prediction
    categorize_button = gr.Button("Categorize Expense", elem_id="categorize-button")
    
    # Output section using the HTML component
    category_output = gr.HTML(label="Category")
    
    # Connect the button to the function
    categorize_button.click(
        fn=categorize_expense,
        inputs=expense_input,
        outputs=category_output
    )

app.launch()