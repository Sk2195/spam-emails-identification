{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8c282e21",
   "metadata": {},
   "outputs": [],
   "source": [
    "import joblib\n",
    "from flask import Flask, render_template, request\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "\n",
    "\n",
    "# Load the trained Naive Bayes model\n",
    "model_file_path = \"spam_classifier_model.pkl\"\n",
    "spam_classifier_model = joblib.load(model_file_path)\n",
    "\n",
    "# Initialize the Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Initialize the CountVectorizer\n",
    "vectorizer = CountVectorizer()\n",
    "\n",
    "def classify(message):\n",
    "    # Preprocess the new message and convert it to numerical features (if using CountVectorizer)\n",
    "    # preprocess_message = vectorizer.transform([message])\n",
    "\n",
    "    # Use the trained model for classification\n",
    "    result = spam_classifier_model.predict([message])[0]\n",
    "    return result\n",
    "\n",
    "# Route for the home page\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n",
    "\n",
    "# Process user input and display the result\n",
    "@app.route('/classify', methods=['POST'])\n",
    "def classify_message():\n",
    "    message = request.form['message']\n",
    "    result = classify(message)\n",
    "    return render_template('result.html', message=message, result=result)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fd6177b0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
