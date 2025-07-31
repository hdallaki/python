import yfinance as yf
import streamlit as st
import os
import psycopg2
from psycopg2 import sql
import pandas as pd

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# دانلود داده‌های سهام اپل
data = yf.download('AAPL', start='2020-01-01', end='2024-01-01')

# اضافه کردن عنوان
st.title('اولین تجربه من از فارسی نویسی در استریم‌لایت')
st.image('1.jpg')
# اضافه کردن متن
st.text('Streamlit is great')
st.button('Click')
st.slider('اسلایدر من', 0, 63, (25, 45))
st.write('---')
st.write('##')
st.date_input('تاریخ امروز')

# رسم نمودار: فقط ستون Close را رسم می‌کنیم
st.subheader('نمودار قیمت بسته شدن سهام AAPL')
st.line_chart(data['Close'])


# --- اتصال به PostgreSQL و نمایش داده‌ها ---
st.write('---')
st.subheader('داده‌های پایگاه داده PostgreSQL')

# رشته اتصال به دیتابیس
DATABASE_URL = "postgresql://test_pbp1_user:cTdbQ0gemjAQXPQFJWoquQTiUbSW0lj7@dpg-d25sg1k9c44c73edr3jg-a/test_pbp1"

try:
    # اتصال به دیتابیس
    conn = psycopg2.connect(DATABASE_URL)

    # ایجاد cursor
    cur = conn.cursor()

    # ایجاد جدول نمونه (در صورت عدم وجود)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            age INT,
            city VARCHAR(50)
        );
    """)

    # درج داده‌های نمونه (فقط یک بار یا اگر تکراری نباشند)
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        sample_data = [
            ('علی', 28, 'تهران'),
            ('زهرا', 34, 'مشهد'),
            ('رضا', 25, 'اصفهان'),
            ('نگین', 30, 'شیراز')
        ]
        for row in sample_data:
            cur.execute("INSERT INTO users (name, age, city) VALUES (%s, %s, %s)", row)
        conn.commit()

    # خواندن داده‌ها از جدول
    df = pd.read_sql_query("SELECT * FROM users", conn)

    # نمایش داده‌ها در استریم‌لایت
    st.write("اطلاعات کاربران:")
    st.dataframe(df)

    # بستن اتصال
    cur.close()
    conn.close()

except Exception as e:
    st.error(f"خطا در اتصال به دیتابیس: {e}")
