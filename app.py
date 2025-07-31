import yfinance as yf
import streamlit as st
import os 
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

# رسم نمودار: فقط ستون Close را رسم می‌کنیم (یا می‌توانیم داده را ساده‌سازی کنیم)
# گزینه ۱: فقط قیمت بسته شدن (Close)
st.subheader('نمودار قیمت بسته شدن سهام AAPL')
st.line_chart(data['Close'])

# گزینه ۲ (اختیاری): اگر می‌خواهید چند ستون را رسم کنید، MultiIndex را حذف یا تغییر دهید
# مثلاً فقط Close و Volume را رسم کنیم (اما حواستان باشد که واحد‌ها خیلی متفاوت است)
# st.line_chart(data[['Close', 'Volume']])  # فقط اگر واحد‌ها مشابه یا نرمال شده باشند
