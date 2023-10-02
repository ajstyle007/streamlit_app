import streamlit as st
import pandas as pd

st.title(":blue[BMI INDEX CALCULATOR.]")
st.markdown("#### :violet[We need few details to calulate your BMI.]")
 
weight = st.slider("How much is your weight?", 0.0,150.0,70.0)
st.write("Your weight is ",weight,"Kg.")

feet1, inch1 = st.columns(2)

with feet1:

    height_feet = st.slider("How much is your Height in feet?", 4.00, 8.00, 5.00)
    
    
with inch1:
     
    inch = st.slider("How many inches?", 0.0,12.0,2.0)
    inch_into_feet = inch/12
 
height =  inch_into_feet+height_feet
st.write("Your height is ", round(height_feet,3),"feet", inch, "inches.")

#convert feet into meter
h_meter = height*0.3048 #or divide by 3.281
st.write("Your height in meters is ",round(h_meter,2),"m.")

BMI = weight / ((h_meter)*(h_meter))
r_bmi = round(BMI,2)
st.markdown( "## :green[Your BMI Index.]")

col1, col2 = st.columns(2)

with col1:
    st.subheader(r_bmi)

    if r_bmi<18.5:
        st.markdown("### :orange[Your are Underweight.]")
    elif r_bmi>18.5 and r_bmi<24.9:
            st.markdown("### :green[Your are normal weight.]")
    elif r_bmi>25 and r_bmi<29.9:
            st.markdown("### :red[Your are Over weight.]")
    elif r_bmi>30:
            st.markdown("### :rainbow[Your are Obese.]")
with col2:
    dict_bmi = {
        "Weight Catogory": ["Underweight","Normal weight","Overweight","Obesity"],
        "Values" :["18.5","18.5–24.9","25–29.9","BMI of 30 or greater"] 
     }         
    #df = pd.Series(dict_bmi)
    st.write("BMI chart." )

    #title_alignment= """ <style> # BMI chart. { text-align: center } </style> """
    #st.markdown(title_alignment, unsafe_allow_html=True)
    st.dataframe(dict_bmi, width=350)


#"""
#BMI Categories:
#Underweight = <18.5
#Normal weight = 18.5–24.9
#Overweight = 25–29.9
#Obesity = BMI of 30 or greater"""

        


        
 

