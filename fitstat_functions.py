import pandas as pd
import datetime
from pandas import Timedelta

def merge_or_update_feeder(new_list, processed_dataframe):
    if new_list[0] in processed_dataframe["Date"].values:
        if processed_dataframe[processed_dataframe["Date"] == new_list[0]]["steps"].item() != new_list[1] and new_list[1] != 0:
            index = processed_dataframe[processed_dataframe["Date"] == new_list[0]]["steps"].index.item()
            processed_dataframe.loc[index,"steps"] = new_list[1]
            processed_dataframe.loc[index,"money_generated"] = calculate_money_per_day(new_list[1])
            processed_dataframe.loc[index,"calories_burned"] = calculate_calories_per_day(new_list[1])
        if processed_dataframe[processed_dataframe["Date"] == new_list[0]]["money_spent"].item() != new_list[2] and new_list[2] != 0:
            index = processed_dataframe[processed_dataframe["Date"] == new_list[0]]["money_spent"].index.item()
            processed_dataframe.loc[index,"money_spent"] = new_list[2]
        if processed_dataframe[processed_dataframe["Date"] == new_list[0]]["Remarks"].item() != new_list[3] and new_list[3] != "":
            index = processed_dataframe[processed_dataframe["Date"] == new_list[0]]["Remarks"].index.item()
            processed_dataframe.loc[index,"Remarks"] = new_list[3]    
    else:
        new_list.append(calculate_money_per_day(new_list[1]))
        new_list.append(calculate_calories_per_day(new_list[1]))
        new_list = [new_list]
        processed_dataframe = processed_dataframe.append(pd.DataFrame(new_list, columns = processed_dataframe.columns),ignore_index = True)
    return processed_dataframe

def calculate_money_per_day(step_count):
    money_generated = 0
    if step_count != 0:
        if step_count >= 3000 and step_count < 5000 :
            money_generated = 3
        elif step_count >= 5000 and step_count < 8000:
            money_generated = 5
        elif step_count >= 8000 and step_count < 10000:
            money_generated = 8
        elif step_count >= 10000:
            n = (step_count - 10000) // 1000
            money_generated = 10 + n
    return money_generated

def calculate_calories_per_day(step_count):
    return int(step_count * 0.05)

def retrieve_calorie_count_today():
    today_date = retrieve_todays_date()
    stat_data = retrieve_stat_file()
    if today_date in stat_data["Date"].values:
        return stat_data[stat_data["Date"] == today_date]["calories_burned"].item()
    else:
        return "Still Data Not Entered"

def retrieve_avg_calorie_count(input_days):
    stat_data = retrieve_stat_file()
    stat_data["Date"] = pd.to_datetime(stat_data["Date"],format="%Y-%m-%d")
    max_date = stat_data["Date"].max()
    min_date = stat_data["Date"].min()
    offset = (max_date - min_date).days + 1
    if offset < input_days:
        input_days = offset
    min_date = max_date - Timedelta(days = input_days)
    total_no_of_calories = stat_data[stat_data["Date"] >= min_date]["calories_burned"].mean()
    return(int(total_no_of_calories))

def retrieve_todays_date():
    today = datetime.datetime.now()
    return(str(datetime.date(today.year,today.month,today.day)))

def retrieve_avg_steps(input_days):
    stat_data = retrieve_stat_file()
    stat_data["Date"] = pd.to_datetime(stat_data["Date"],format="%Y-%m-%d")
    max_date = stat_data["Date"].max()
    min_date = stat_data["Date"].min()
    offset = (max_date - min_date).days + 1
    if offset < input_days:
        input_days = offset
    min_date = max_date - Timedelta(days = input_days)
    total_no_of_steps = stat_data[stat_data["Date"] >= min_date]["steps"].mean()
    return(int(total_no_of_steps))

def retrieve_max_steps(input_days):
    stat_data = retrieve_stat_file()
    stat_data["Date"] = pd.to_datetime(stat_data["Date"],format="%Y-%m-%d")
    max_date = stat_data["Date"].max()
    min_date = stat_data["Date"].min()
    offset = (max_date - min_date).days + 1
    if offset < input_days:
        input_days = offset
    min_date = max_date - Timedelta(days = input_days)
    max_no_of_steps = stat_data[stat_data["Date"] >= min_date]["steps"].max()
    date_max = stat_data[stat_data["steps"] == max_no_of_steps]["Date"].item()
    return(str(max_no_of_steps) + "("+ str(date_max).split()[0]+")")

def retrieve_money_spent():
    stat_data = retrieve_stat_file()
    return stat_data["money_spent"].sum()

def retrieve_money_available():
    stat_data = retrieve_stat_file()
    money_spent = stat_data["money_spent"].sum()
    money_available = stat_data["money_generated"].sum() - stat_data["money_spent"].sum()
    return money_available

def retrieve_stat_file():
    data = pd.read_csv("data/fitstat_data.csv")
    return data

def retrieve_todays_steps():
    today_date = retrieve_todays_date()
    stat_data = retrieve_stat_file()
    if today_date in stat_data["Date"].values:
        return stat_data[stat_data["Date"] == today_date]["steps"].item()
    else:
        return "Still Data Not Entered"


def date_manipulation(date):
    return str(date).split(" ")[0]

def retrieve_data_in_range(input_days, buffer):
    stat_data = retrieve_stat_file()
    stat_data["Date"] = pd.to_datetime(stat_data["Date"],format="%Y-%m-%d")
    max_date = stat_data["Date"].max()
    min_date = stat_data["Date"].min()
    offset = (max_date - min_date).days + 1
    if offset < input_days:
        input_days = offset
    min_date = max_date - Timedelta(days = input_days)
    output_dataframe = stat_data[stat_data["Date"] >= min_date]
    output_dataframe = output_dataframe.sort_values(by=['Date'], ascending=False)
    output_dataframe["Date"] = output_dataframe["Date"].apply(date_manipulation)
    return(output_dataframe)


        
