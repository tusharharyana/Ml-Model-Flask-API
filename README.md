# Deploy ML model using Flask on PythonAnywhere.
- To deploy your machine learning model, start by setting up Flask on `https://www.pythonanywhere.com/`.
- Create a Flask web application and define routes to handle model predictions.
- Upload your trained machine learning model to the server and load it within your Flask app.
- Configure your Flask app to process incoming requests and provide predictions by integrating Postman for testing and validation.
- Test your deployed model by sending sample data to the Flask endpoint and verifying the predictions.
- Once satisfied with the deployment, make sure to monitor the performance of your application and handle any potential issues.

# Project Structure
This project has four major parts :

- app.py - This contains Flask APIs that receives employee details through GUI or API calls, computes the predicted value based on our model and returns it.
- model.pkl - This contains code fot our Machine Learning model to predict employee salaries based on training data in `credit_rating.csv` file.
- imputer.pkl - Holds data imputation code or information necessary for preprocessing the input data.
- label_encoder.pkl - Stores code or information for label encoding, typically used for transforming categorical variables into numerical values for model input.

# Requirements
* Postman for testing and validating API endpoints `https://www.postman.com/`.
* PyCharm for development and management of the Flask application and machine learning model `https://www.jetbrains.com/pycharm/download/`.

# Get started

## Local Testing using Postman
1. Clone this GitHub repository to your local machine using Pycharm.
2. Make sure you have Python installed (recommended version is Python 3.7 or higher).
3. Install the required dependencies by running the following command:
   ```bash
   pip install numpy
   pip install pandas
   pip install scikit-learn==1.4
   ```
4. Run app.py using below command to start Flask API
   ```bash
   python app.py
   ```
5. Open Postman, set the request method to POST, and navigate to the body section, selecting the form option. Next, copy the URL `http://127.0.0.1:5000/predict` generated after running `app.py` and paste it after POST.
6. Enter key and values in the form for testing API.
7. After clicking the send button, you will receive the output in response, which will include the predicted values based on the input provided to the Flask API endpoint.

## Deploy API on pythonanywhere

- Indeed, PythonAnywhere is a convenient platform for deploying Flask APIs, making them accessible from anywhere.

1. First, create an account on PythonAnywhere and sign in. Then, navigate to the `Web` option and click on `Add a new web app`.
2. Upload files in `mysite` directory.
   * model.pkl
   * label_encoder.pkl
   * imputer.pkl
   * app.py
3. Add root directory to all `.pkl` files like ` pickle.load(open('/home/tusharharyana/mysite/model.pkl', 'rb'))` and save it.
4. Go to console and install all dependencies by running the following commands in Bash.
   ```bash
   pip install numpy
   pip install pandas
   pip install scikit-learn==1.4
   ```
5. Reload and click on configuration for `tusharharyana.pythonanywhere.com`
6. Copy the URL and paste it into Postman to verify that the API is functioning:`https://tusharharyana.pythonanywhere.com/predict`.
- If everything goes well, you should be able to see the predicted value.

# Accessing the Hosted Application
You can access the hosted application through our PythonAnywhere platform at https://tusharharyana.pythonanywhere.com/.

# Contact
If you have any questions or feedback, please don't hesitate to contact me at [haryanatushar@gmail.com](mailto:haryanatushar@gmail.com). I appreciate your interest and support!