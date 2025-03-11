#from sklearn.neighbors import KNeighborsClassifier  
import streamlit as st
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt

st.title("🫀🫀🫀HeartDisease🫀🫀🫀")
st.header("🫀🫀🫀การพยากรณ์โรคหัวใจล้มเหลวด้วยเทคนิคเหมืองข้อมูล")

st.image('./img/Heart-Disease.jpg')
st.subheader("🫀🫀🫀🫀HeartDisease🫀🫀🫀🫀🫀")

dt = pd.read_csv("./data/heart02.csv")
st.header("🫀🫀🫀HeartDisease🫀🫀🫀")
st.write(dt.head(10))

