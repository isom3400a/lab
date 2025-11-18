import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Personal Expense Tracker")

if 'expenses' not in st.session_state:
  st.session_state.expenses=pd.DataFrame(columns=['Date', 'Category','Amount','Description'])

with st.form("expense_form"):
  st.subheader("Add New Expense")
  date=st.date_input("Date")
  category=st.selectbox["Category", "Transport", "Entertainment", "Bills", "Others"]
  amount=st.number_input("Amount", min_value=0.0, step=0.01)
  description=st.text_input("Description")

submitted=st.form_submit_button("Add Expense")
if submitted:
  new_expenses=pd.DataFrame({
    'Date':[date],
    'Category':[category],
    'Amount':[amount],
    'Description':[descripion]
  })
  st.session_state.expenses=pd.concat([st.session_state.expenses, new_expense], ignore_index=True)
  st.success("Expense added successfully!")
