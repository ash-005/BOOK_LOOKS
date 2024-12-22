import streamlit as st
import joblib 
model = joblib.load('book_genre_clf.joblib')
vectorizer = joblib.load('vectorizer.pkl')
def book_genre_app():
    st.title('Booke Genre From Description')
    st.write('Enter a book description to predict its genre.')
    
    user_input = st.text_area('Enter book description', height=300)
    user_input_vectorized = vectorizer.transform([user_input])
    if st.button('Predict Genre'):
        if user_input:
            prediction = model.predict(user_input_vectorized)
            st.success(f'Predicted Genre: {prediction[0]}')
        else:
            st.error('Please enter a book description.')

if __name__ == '__main__':
    book_genre_app()