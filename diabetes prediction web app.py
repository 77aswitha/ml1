import numpy as numpy
import pickle 
import streamlit as sp 

#loading the saved model
loaded_model=pickle.load(open(r'D:\deploying model\diabetes_model.sav','rb'))

# creating a functionfor prediction 

def diabetes_prediction(input_data):


    
    # changing the input_data to numpy array
     input_data_as_numpy_array = np.asarray(input_data)

     # reshape the array as we are predicting for one instance
     input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

     prediction = loaded_model.predict(input_data_reshaped)
     print(prediction)

     if(prediction[0] ==0):
         return 'the person is not diabetic'
     else:
         return 'the person is diabetic'

def main():

      # giving a title
     st.title('diabetes prediction Web App')

     # getting the input data from the user 
    

     pregnancies = st.text_input('Number of pregnancies')
     Glucose = st.text_input('Glucose levvel')
     BloodPressure = st.text_input('Blood Pressure value')
     SkinThickness = st.text_input('SkinThickness value')
     Insulin = st.text_input('Insulin value')
     BMI = st.text_input(' BMI value')
     DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
     Age = st.text_input('Age of the person')

     # code for prediction 
     diagnosis =''

     # creating a button for prediction 

     if st.button("Diabetes Test Result"):
         diagnosis = diabetes_prediction([pregnancies,Glucose,BloodPressure,SkinThickness, Insulin, BMI,DiabetesPedigreeFunction, Age])

         st.success(diagnosis)

     if __name__ == '__main__':
         main()

