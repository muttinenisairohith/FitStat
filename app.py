import streamlit as st
from streamlit_authenticator import SafeLoader

st.set_page_config(
    page_title="FitStat Home",
    page_icon="🚶",
)

if "authentication_status" not in st.session_state.keys():
    st.write(" Please Login using Authentication Page to continue")
    st.stop()
else:
    if st.session_state["authentication_status"] != True:
        st.write(" Please Login using Authentication Page to continue")
        st.stop()

st.write("# Welcome to FitStat! 🚶")
st.markdown(
    """
    Fitstat is an app exclusively developed to monitor my walking Activity.
    - This tool will record the steps that I make and provide various statistics.
    - Depending upon my step count in a month it will assign goals for the next month.
    - This tool will also showcase me the money that I can spend on junk food based on my work for fitness.
    - And at last like all other Fitness apps, this tool will also calculate the calories burned by me.
    ### Implemented Activities
    - FitStat Feeder - To feed step count and money spent w.r.t the date.
    - FitStat Stats - To showcase some stats related to step count, calories burnt and money spent.
    - Fitstat Snapshot - To provide a snapshot of Data available w.r.t the range selected.
    """
)
