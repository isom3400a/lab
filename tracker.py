import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Personal Expense Tracker")

if 'expenses' not in st.session_state:
  st.session_state.expenses=pd.DataFrame(columns=['Date', 'Amount',"Description']
