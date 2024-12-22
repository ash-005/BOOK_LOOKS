# BOOK_LOOKS 📚
A machine learning project aimed at classifying books into their primary genres based on their descriptions. This repository includes data preprocessing, model training, and a working Streamlit application to demonstrate the project.  

---

## 📄 Table of Contents  
- [Introduction](#introduction)  
- [Dataset](#dataset)  
- [Installation](#installation)  
- [Project Structure](#project-structure)  
- [Models Trained](#models-trained)  
- [Streamlit App](#streamlit-app)  
- [Results](#results)  
- [License](#license)  

---

## 📝 Introduction  
**BOOK_LOOKS** leverages machine learning techniques to predict the primary genre of a book based on its description. The project involves preprocessing textual data, training multiple classification models, and evaluating their performance.  

---

## 📚 Dataset  
The data used for this project is sourced from [Goodreads Best Books Ever Dataset](https://www.kaggle.com/datasets/arnabchaki/goodreads-best-books-ever/data).  

---

## ⚙️ Installation  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/yourusername/BOOK_LOOKS.git  
   cd BOOK_LOOKS  
   ```  

   ```  

2. Run the Streamlit app:  
   ```bash  
   streamlit run app.py  
   ```  

---

## 📂 Project Structure  
```
BOOK_LOOKS/  
├── app.py                     # Streamlit app for genre classification  
├── books_analysis.ipynb       # Exploratory data analysis and preprocessing  
├── test.ipynb                 # Testing and evaluation of models  
├── pipeline_final.ipynb       # Finalized pipeline for classification  
├── book_genre_working.webm    # Demonstration video of the Streamlit app  
└── README.md                  # Project documentation  
```  

---

## 🛠️ Models Trained  
1. Support Vector Classifier (SVC)  
2. Logistic Regression  
3. Naive Bayes  
4. Random Forest  

Each model was evaluated based on its accuracy, precision, and F1-score to determine the best-performing approach for this task.  

---

## 🌟 Streamlit App  
The Streamlit app provides an interactive interface where users can input a book description and receive a predicted primary genre.  
🎥 [Watch the Streamlit App in action](book_genre_working.webm)  

---

## 📊 Results  
The project achieved promising results, with the Random Forest model performing the best. Detailed results and comparisons can be found in `test.ipynb`.  

---

## 📝 License  
This project is licensed under the MIT License.  

---

Enjoy exploring **BOOK_LOOKS** and feel free to share feedback! 😊  


