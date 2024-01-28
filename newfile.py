import pandas as pd
import requests
import time


while True:
    sheet_id = "1QWe-MhGzMdeDma4i312n_bjXKhG0Cu5pV9m3AFf50Ts"
    
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv"

    df = pd.read_csv(url)
    df["Schedule Datetime"] = pd.to_datetime(df["Schedule Datetime"])
    df

    previous_minute = pd.datetime.now() + pd.Timedelta(minutes=-1)
    print(type(previous_minute))
    current_time = pd.datetime.now()
    print(type(current_time))
    df = df[(df["Schedule Datetime"] > previous_minute) &  (df["Schedule Datetime"]  < current_time)] 
    df


    def send_message(row):
        bot_id = "6439985184:AAFydohEu58QkmXR0KX7mJI7EHg83Ls5OXY"
        chat_id = "@testautorespone"
        message = row[0]
        url = f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={message}"

        return requests.get(url).json()

    if not df.empty:
        df['status'] = df.apply(send_message, axis=1)
    time.sleep(60)
    df