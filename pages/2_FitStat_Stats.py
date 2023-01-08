import streamlit as st
from fitstat_functions import retrieve_todays_steps, retrieve_avg_steps, retrieve_max_steps, retrieve_money_spent, retrieve_money_available, retrieve_calorie_count_today, retrieve_avg_calorie_count

st.set_page_config(
    page_title="FitStat Stats",
    page_icon="🚶",
)

if "authentication_status" not in st.session_state.keys():
    st.write(" Please Login using Authentication Page to continue")
    st.stop()
else:
    if st.session_state["authentication_status"] != True:
        st.write(" Please Login using Authentication Page to continue")
        st.stop()

wch_colour_box_green = (137, 250, 192)
wch_colour_box_yellow = (237, 240, 168)
wch_colour_box_blue_sky = (198, 210, 245)
wch_colour_box_blue_light = (232, 197, 250)
wch_colour_box_orange = (245, 201, 223)
wch_colour_box_red = (250, 214, 207)
wch_colour_box_pink = (119, 105, 245)
wch_colour_box_color2 = (247, 229, 35)
wch_colour_box_color1 = (110, 187, 245)

wch_colour_font = (0,0,0)
fontsize = 18
valign = "left"
lnk = '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.12.1/css/all.css" crossorigin="anonymous">'

no_of_steps_today = retrieve_todays_steps()
no_of_steps_week = retrieve_avg_steps(6)
no_of_steps_month = retrieve_avg_steps(29)
no_of_steps_year = retrieve_avg_steps(364)
max_no_of_steps_month = retrieve_max_steps(29)
max_no_of_steps_year = retrieve_max_steps(364)
money_spent = retrieve_money_spent()
money_available = retrieve_money_available()
calorie_count_today = retrieve_calorie_count_today()
calorie_count_week = retrieve_avg_calorie_count(6)
calorie_count_month = retrieve_avg_calorie_count(29)
calorie_count_year = retrieve_avg_calorie_count(364)

#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

st.title ("FitStat Stats")

st.subheader('Day Stats')

htmlstr_number_of_steps_today = f"""<p style='background-color: rgb({wch_colour_box_green[0]}, 
                                              {wch_colour_box_green[1]}, 
                                              {wch_colour_box_green[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🚶</i> {no_of_steps_today}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Number of Steps Today</style></span></p>"""

htmlstr_calories_burned_today = f"""<p style='background-color: rgb({wch_colour_box_blue_light[0]}, 
                                              {wch_colour_box_blue_light[1]}, 
                                              {wch_colour_box_blue_light[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🍔</i> {calorie_count_today}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Calories Burned Today</style></span></p>"""

cc = st.columns(2)

with cc[0]:
    st.markdown(lnk + htmlstr_number_of_steps_today, unsafe_allow_html=True)

with cc[1]:
    st.markdown(lnk + htmlstr_calories_burned_today, unsafe_allow_html=True)

st.subheader('Average Step Stats')

cc = st.columns(3)

htmlstr_avg_steps_week = f"""<p style='background-color: rgb({wch_colour_box_yellow[0]}, 
                                              {wch_colour_box_yellow[1]}, 
                                              {wch_colour_box_yellow[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🚶</i> {no_of_steps_week}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Average Steps this week</style></span></p>"""

htmlstr_avg_steps_month = f"""<p style='background-color: rgb({wch_colour_box_orange[0]}, 
                                              {wch_colour_box_orange[1]}, 
                                              {wch_colour_box_orange[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🚶</i> {no_of_steps_month}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Average Steps this month</style></span></p>"""

htmlstr_avg_steps_year = f"""<p style='background-color: rgb({wch_colour_box_blue_sky[0]}, 
                                              {wch_colour_box_blue_sky[1]}, 
                                              {wch_colour_box_blue_sky[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🚶</i> {no_of_steps_year}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Average Steps this year</style></span></p>"""

with cc[0]:
    st.markdown(lnk + htmlstr_avg_steps_week, unsafe_allow_html=True)

with cc[1]:
    st.markdown(lnk + htmlstr_avg_steps_month, unsafe_allow_html=True)

with cc[2]:
    st.markdown(lnk + htmlstr_avg_steps_year, unsafe_allow_html=True)


st.subheader('Average Step Stats')

cc = st.columns(3)

htmlstr_avg_calories_week = f"""<p style='background-color: rgb({wch_colour_box_blue_light[0]}, 
                                              {wch_colour_box_blue_light[1]}, 
                                              {wch_colour_box_blue_light[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🍔</i> {calorie_count_week}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Average Calories this week</style></span></p>"""

htmlstr_avg_calories_month = f"""<p style='background-color: rgb({wch_colour_box_yellow[0]}, 
                                              {wch_colour_box_yellow[1]}, 
                                              {wch_colour_box_yellow[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🍔</i> {calorie_count_month}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Average Calories this month</style></span></p>"""

htmlstr_avg_calories_year = f"""<p style='background-color: rgb({wch_colour_box_green[0]}, 
                                              {wch_colour_box_green[1]}, 
                                              {wch_colour_box_green[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🍔</i> {calorie_count_year}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Average Calories this year</style></span></p>"""

with cc[0]:
    st.markdown(lnk + htmlstr_avg_calories_week, unsafe_allow_html=True)

with cc[1]:
    st.markdown(lnk + htmlstr_avg_calories_month, unsafe_allow_html=True)

with cc[2]:
    st.markdown(lnk + htmlstr_avg_calories_year, unsafe_allow_html=True)

st.subheader('Maximum Step Stats')

cc = st.columns(2)

htmlstr_max_steps_month = f"""<p style='background-color: rgb({wch_colour_box_red[0]}, 
                                              {wch_colour_box_red[1]}, 
                                              {wch_colour_box_red[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🚶</i> {max_no_of_steps_month}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Maximum Number of Steps on a day this month</style></span></p>"""

htmlstr_max_steps_year = f"""<p style='background-color: rgb({wch_colour_box_pink[0]}, 
                                              {wch_colour_box_pink[1]}, 
                                              {wch_colour_box_pink[2]}, 0.5); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>🚶</i> {max_no_of_steps_year}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Maximum Number of Steps on a day this year</style></span></p>"""

with cc[0]:
    st.markdown(lnk + htmlstr_max_steps_month, unsafe_allow_html=True)

with cc[1]:
    st.markdown(lnk + htmlstr_max_steps_year, unsafe_allow_html=True)

st.subheader('Money Stats')

cc = st.columns(2)

htmlstr_money_spent = f"""<p style='background-color: rgb({wch_colour_box_color1[0]}, 
                                              {wch_colour_box_color1[1]}, 
                                              {wch_colour_box_color1[2]}, 0.75); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>💵</i> {money_spent}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Money spent this month</style></span></p>"""

htmlstr_money_available = f"""<p style='background-color: rgb({wch_colour_box_color2[0]}, 
                                              {wch_colour_box_color2[1]}, 
                                              {wch_colour_box_color2[2]}, 0.5); 
                        color: rgb({wch_colour_font[0]}, 
                                   {wch_colour_font[1]}, 
                                   {wch_colour_font[2]}, 0.75); 
                        font-size: {fontsize}px; 
                        border-radius: 7px; 
                        padding-left: 12px; 
                        padding-top: 18px; 
                        padding-bottom: 18px; 
                        line-height:25px;'>
                        <i>💵</i> {money_available}
                        </style><BR><span style='font-size: 14px; 
                        margin-top: 0;'>Money available to spend</style></span></p>"""


with cc[0]:
    st.markdown(lnk + htmlstr_money_spent, unsafe_allow_html=True)

with cc[1]:
    st.markdown(lnk + htmlstr_money_available, unsafe_allow_html=True)