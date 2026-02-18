import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🔐 Siber Güvenlik Log Dashboard")

# Örnek veri (gerçek ortamda CSV'den okunabilir)
data = {
    "IP": ["192.168.1.1", "192.168.1.5", "10.0.0.3", "192.168.1.1", "10.0.0.8"],
    "Durum": ["Başarılı", "Başarısız", "Başarısız", "Başarılı", "Başarısız"],
    "Saldırı_Türü": ["Normal", "Brute Force", "SQL Injection", "Normal", "Brute Force"]
}

df = pd.DataFrame(data)

# Genel istatistikler
st.subheader("📊 Genel İstatistikler")

toplam = len(df)
basarisiz = len(df[df["Durum"] == "Başarısız"])

st.metric("Toplam İstek", toplam)
st.metric("Başarısız Giriş", basarisiz)

# IP dağılımı
st.subheader("🌍 IP Dağılımı")

ip_sayim = df["IP"].value_counts()
st.bar_chart(ip_sayim)

# Saldırı türü dağılımı
st.subheader("⚠ Saldırı Türleri")

saldiri_sayim = df["Saldırı_Türü"].value_counts()

fig, ax = plt.subplots()
ax.pie(saldiri_sayim, labels=saldiri_sayim.index, autopct="%1.1f%%")
st.pyplot(fig)

# Şüpheli IP (2'den fazla başarısız deneme)
st.subheader("🚨 Şüpheli IP'ler")

supheli = df[df["Durum"] == "Başarısız"]["IP"].value_counts()
supheli = supheli[supheli > 1]

st.write(supheli if not supheli.empty else "Şüpheli IP bulunamadı.")
