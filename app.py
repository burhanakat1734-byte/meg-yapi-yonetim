import streamlit as st
from datetime import datetime

st.set_page_config(page_title="MEG Yapı Yönetim", page_icon="🧱", layout="wide")

st.session_state.setdefault("auth_ok", False)
def gate():
    if st.session_state["auth_ok"]:
        return True
    st.title("Giriş")
    pwd = st.text_input("Uygulama şifresi", type="password")
    if st.button("Giriş yap"):
        if pwd == "megdenal17":
            st.session_state["auth_ok"] = True
            st.rerun()
        else:
            st.error("Hatalı şifre")
    st.stop()
gate()

def topbar(role="Yönetici"):
    col_logo, col_title, col_role = st.columns([1, 3, 1])
    with col_logo:
        st.image("logo.png", width=56)
    with col_title:
        st.markdown("<h2 style='text-align:center;'>MEG Yapı Yönetim</h2>", unsafe_allow_html=True)
    with col_role:
        st.markdown(f"<div style='text-align:right; font-weight:600;'>{role}</div>", unsafe_allow_html=True)
    st.divider()

def sidebar_nav():
    st.sidebar.title("Menü")
    st.sidebar.caption("emlak yardımcım")
    page = st.sidebar.radio("Sayfalar",
        ["Araçlar", "Gelir/Gider", "İzinler", "Personeller", "Günlük Plan", "Raporlar"],
        label_visibility="collapsed",
    )
    return page

def page_araclar():
    st.subheader("Araçlar")
    st.write("Gider kalemleri: Tamir, Mazot, Bakım, Diğer")
    with st.form("arac_gider_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            plaka = st.text_input("Plaka")
        with col2:
            tur = st.selectbox("Tür", ["Tamir", "Mazot", "Bakım", "Diğer"])
        with col3:
            tutar = st.number_input("Tutar", min_value=0.0, step=0.5)
        aciklama = st.text_area("Açıklama")
        submitted = st.form_submit_button("Kaydet")
        if submitted:
            st.success(f"Kaydedildi: {plaka} | {tur} | {tutar} | {datetime.now()}")
    st.info("Liste ve filtreler burada görüntülenecek.")

def page_gelir_gider():
    st.subheader("Gelir/Gider")
    tab1, tab2 = st.tabs(["Gelir", "Gider"])
    with tab1:
        st.write("Gelir kayıt formu ve listesi")
    with tab2:
        st.write("Gider kayıt formu ve listesi")

def page_izinler():
    st.subheader("İzinler")
    st.write("Personel izinleri: kaç gün kaldı, aldı mı, mazeret, tarih aralığı")

def page_personeller():
    st.subheader("Personeller")
    st.caption("Danışman foto yükleme ve kişi kartları")
    st.write("Her danışmanın datası ayrı; tıklayınca sadece o danışman görünsün.")

def page_plan():
    st.subheader("Günlük Planlama")
    st.write("Günlük görevler, atamalar ve durum takibi")

def page_raporlar():
    st.subheader("Raporlar")
    st.write("Otomatik grafikleme: gelir/gider, araç gider dağılımı, izin kullanımı, iş sayıları")

def main():
    topbar(role="Yönetici")
    page = sidebar_nav()
    if page == "Araçlar":
        page_araclar()
    elif page == "Gelir/Gider":
        page_gelir_gider()
    elif page == "İzinler":
        page_izinler()
    elif page == "Personeller":
        page_personeller()
    elif page == "Günlük Plan":
        page_plan()
    elif page == "Raporlar":
        page_raporlar()

if __name__ == "__main__":
    main()
