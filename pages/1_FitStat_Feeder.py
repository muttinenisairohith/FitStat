import streamlit as st
import pandas as pd
from fitstat_functions import merge_or_update_feeder

st.set_page_config(
    page_title="FitStat Feeder",
    page_icon="🚶",
)

if "authentication_status" not in st.session_state.keys():
    st.write(" Please Login using Authentication Page to continue")
    st.stop()
else:
    if st.session_state["authentication_status"] != True:
        st.write(" Please Login using Authentication Page to continue")
        st.stop()

fitstat_path = "data/fitstat_data.csv"

existing_df = pd.read_csv(fitstat_path)

st.title ("Fitstat Feeder")

Date = st.date_input('Date')
Step_count = st.number_input('Step count',value = 0, step = 1000)
Money_spent = st.number_input('Money Spent',value = 0, step = 5)
Moments = st.text_input('Moments(optional)')
Button = st.button('Add log')

if (Button):
    if Date == "":
        st.error("Error, Date cannot be Null. Please reload and enter correct values")
    elif Step_count == 0 and Money_spent == 0:
        st.error("Error, Both Step count and Money spent cannot be Null. Please reload and enter correct values")
    else:
        new_list = [str(Date), Step_count, Money_spent, Moments]
        processed_df = merge_or_update_feeder(new_list,existing_df)
        processed_df.to_csv(fitstat_path, mode="w", index=None, header=True)
        st.success("Log Added Successfully. Reload to see the changes.")
