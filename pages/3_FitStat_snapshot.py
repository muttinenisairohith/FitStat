import streamlit as st
import altair as alt
from fitstat_functions import retrieve_data_in_range

st.set_page_config(
    page_title="FitStat SnapShot",
    page_icon="🚶",
)

if "authentication_status" not in st.session_state.keys():
    st.write(" Please Login using Authentication Page to continue")
    st.stop()
else:
    if st.session_state["authentication_status"] != True:
        st.write(" Please Login using Authentication Page to continue")
        st.stop()

st.title("FitStat SnapShot")

option = st.selectbox(label = "Select Range: ", options = ["7 Days","30 Days","1 Year","5 years"])

def data_to_display(option):
    if option == "7 Days":
        input_days = 6
    elif option == "30 Days":
        input_days = 29
    elif option == "1 Year":
        input_days = 364
    elif option == "5 years":
        input_days = (365*5) - 1

    buffer = 0
    data_in_range = retrieve_data_in_range(input_days, buffer)

    

    st.markdown("Graphical Snapshot")
    chart = (
    alt.Chart(data_in_range)
    .mark_bar()
    .encode(
        alt.X("Date"),
        alt.Y("steps"),
        alt.Color("Date"),
        alt.Tooltip(["Date", "steps"]),
    )
    .interactive()
    )
    st.altair_chart(chart, use_container_width=True)
    #st.bar_chart(data_in_range, x="Date", y = "steps", width = 1000, height = 400)

    st.markdown("Snapshot of Data")
    st.dataframe(data_in_range, use_container_width = True)

data_to_display(option)
