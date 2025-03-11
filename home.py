#from sklearn.neighbors import KNeighborsClassifier  
import streamlit as st
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

st.title("🫀🫀🫀การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองข้อมูล🫀🫀🫀")

st.image('./img/Heart-Disease.jpg')
st.subheader("🫀🫀🫀🫀HeartDisease🫀🫀🫀🫀🫀")
c1,c2,c3=st.columns(3)
with c1:
    st.write("")
with c2 :
    st.image('./img/HeartDisease01.jpg')
with c3 :
    st.write("")

dt = pd.read_csv("./data/heart02.csv")
st.header("🫀🫀🫀Data HeartDisease🫀🫀🫀")
st.write(dt.head(10))
st.subheader("สถิติโรคหัวใจ")
st.write(dt.describe())
st.write("สถิติจำนวนเพศหญิง = 0 ชาย = 1")
st.write(dt.groupby('Sex')['Sex'].count())

st.subheader("data sex")
count_male = dt.groupby('Sex').size()[1]
count_female = dt.groupby('Sex').size()[0]
dx = [count_male, count_female]
dx2 = pd.DataFrame(dx, index=["Male", "Female"])
st.bar_chart(dx2)

st.subheader("average sex")
average_male_age = dt[dt['Sex'] == 1]['Age'].mean()
average_female_age = dt[dt['Sex'] == 0]['Age'].mean()

dxage = [average_male_age, average_female_age]
dxage2 = pd.DataFrame(dxage, index=["Male", "Female"])
st.bar_chart(dxage2)

