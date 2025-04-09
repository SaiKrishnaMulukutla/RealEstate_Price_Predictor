# Real Estate Price Predictor

## Description
Real Estate Price Predictor is a powerful and interactive web application built with **Streamlit** that allows users to estimate property prices in Bangalore based on various inputs like location, square footage, number of bedrooms (BHK), and number of bathrooms. The app is powered by a Machine Learning regression model trained on historical real estate data and engineered with domain knowledge, statistical techniques, and performance optimization strategies.

This app is ideal for home buyers, real estate investors, and property analysts looking to get quick and data-driven price estimates.

Check out the live app here:
🔗 https://realestate-price-predictor.streamlit.app/

---

## Demo Video
🎥 Watch the Real Estate Price Predictor in action!

https://github.com/user-attachments/assets/762261df-0f57-46ce-9e32-4952782babe0
## Key Features

- **Live Price Prediction**: Predicts house prices in Bangalore based on user inputs.
- **ML-Powered**: Uses a machine learning model trained via GridSearchCV and k-Fold Cross-Validation.
- **Clean & Simple UI**: Streamlit interface with intuitive input fields and styled headings.
- **Feature Engineering**: Robust preprocessing pipeline for outliers, missing values, and dimensionality reduction.
- **Location-Sensitive**: Location is encoded using one-hot encoding for better model accuracy.
- **Business Logic Filtering**: Smart logic to remove unrealistic data points and outliers.
- **Error Handling**: Handles missing values, incorrect inputs, and displays helpful messages.

---

## Technologies Used

- **Python** – Core programming language.
- **Streamlit** – Web interface framework for interactive deployment.
- **Scikit-learn** – For building and training the ML model.
- **Pandas & NumPy** – Data manipulation and cleaning.
- **Matplotlib/Seaborn** – Used during data exploration.
- **Joblib** – For model serialization.
- **Jupyter Notebook** – For EDA and experimentation.

---

## Process Flow

1. **User Input**: Select BHK, Bathrooms, Total Sqft, and Location.
2. **Data Cleaning**: Input is validated and passed to the preprocessed model.
3. **Model Prediction**: The ML model returns an estimated price (in Lakhs).
4. **Result Display**: Price is shown with helpful UI styling and formatting.

---

## 📸 Home Page
<img width="703" alt="Image" src="https://github.com/user-attachments/assets/fdae5252-7223-4ff1-905e-79edf6f0a310" />```

---

## Run Locally

Step-by-step instructions to run this app on your machine:

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/real-estate-price-predictor.git
cd real-estate-price-predictor
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Run the app**:

```bash
streamlit run app.py
```

---

## requirements.txt

```txt
streamlit>=1.30.0
scikit-learn>=1.1.0
pandas>=1.3.0
numpy>=1.21.0
joblib>=1.2.0
```

---

## Deployment

This app can be deployed easily on [Streamlit Cloud](https://streamlit.io/cloud).  
Just connect your GitHub repository and click **Deploy**.

---

## Future Enhancements

- Add interactive map view for location selection.
- Show visual breakdown of price vs features.
- Extend to other cities or countries.
- Add data export/download options.
- Allow filtering by amenities or property type.

---

## Acknowledgements

Thanks to:

- The open-source Python community  
- Streamlit for the easy deployment platform  
- Kaggle & real estate data providers  
- Scikit-learn & Pandas developers for incredible tools

---

## Contact

For questions, suggestions, or collaborations:

📧 **Email**: saikrishnamulukutla@gmail.com  
🔗 **LinkedIn**: https://www.linkedin.com/in/saikrishnamulukutla/
📁 **GitHub**: https://github.com/SaiKrishnaMulukutla/
