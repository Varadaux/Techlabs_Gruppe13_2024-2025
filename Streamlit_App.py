#!/usr/bin/env python
# coding: utf-8

# In[1]:


I = 1


# In[2]:


import streamlit as st
import folium
from streamlit.components.v1 import iframe


# In[3]:


st.title("Displaying Münster’s socioeconomic and educational situation geographically")


# In[4]:


st.header("Münster's Socioeconomic Situation ")

with open("SchulDaten_Heatmap.html", 'r') as file:
    st.components.v1.html(file.read(), height=600)


# In[5]:


st.header("Münster's Educational Situation ")


# In[6]:


with open("SchulDaten_Heatmap.html", 'r') as file:
    st.components.v1.html(file.read(), height=600)

