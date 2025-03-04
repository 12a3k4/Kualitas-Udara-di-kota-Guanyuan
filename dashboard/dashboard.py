import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')


# Membaca data dari CSV
all_df = pd.read_csv("./all_data.csv")

# Menggabungkan kolom "day", "month", dan "year" menjadi satu kolom datetime
all_df['day'] = pd.to_datetime(all_df[['year', 'month', 'day']])

# Mengurutkan dan mereset index
all_df.sort_values(by="day", inplace=True)
all_df.reset_index(drop=True, inplace=True)

# Mendapatkan nilai minimum dan maksimum dari kolom 'day'
min_day = all_df["day"].min()
max_day = all_df["day"].max()
    
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://www.chinadiscovery.com/assets/images/sichuan/guangyuan/guangyuan-sicahun.jpg")
    
    # Mengambil start_day & end_day dari date_input
    start_day, end_day = st.date_input(
        label='Date Filter',min_value=min_day,
        max_value=max_day,
        value=[min_day, max_day]
    )

st.header(':sparkles: Kualitas Udara di kota Guanyuan :sparkles:')
st.write("Proyek Analisis Data: Air Quality @Guanyuan")
st.write("Nama: Ali Akbar Said")
st.write("Email : aliakbarsaid@gmail.com")
st.write("ID Cohort : A001YBF001")
st.write("Program: Laskar AI 2025")

main_df = all_df[(all_df["day"] >= str(start_day)) & 
                (all_df["day"] <= str(end_day))]

st.subheader("PM2.5 Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["PM2.5"], label="PM2.5")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("PM10 Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["PM10"], label="PM10")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("SO2 Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["SO2"], label="SO2")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("NO2 Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["NO2"], label="NO2")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("CO Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["CO"], label="CO")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)

st.subheader("O3 Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["O3"], label="O3")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("CO Polution")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["CO"], label="CO")
plt.xlabel("Year")
plt.ylabel("Concentration (microgram/m3)")
plt.legend()
st.pyplot(fig)


st.subheader("Temperatur")
groupByYear = main_df.groupby("day").mean(numeric_only=True)


fig = plt.figure(figsize=(10,6))
plt.plot(groupByYear.index, groupByYear["TEMP"], label="TEMP")
plt.xlabel("Year")
plt.ylabel("°C")
plt.legend()
st.pyplot(fig)
