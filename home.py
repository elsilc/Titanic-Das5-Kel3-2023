import streamlit as st
import pandas as pd
import streamlit.components.v1 as stc 
import joblib

from eda import run_eda_app
from prediction import run_predict_app


st.set_page_config(page_title="Titanic ML",
		   page_icon="🚢",
		   layout="wide")

html_temp = """
		<div style="background-color:#3872ab;padding:1px;border-radius:10px">
        <h3 style="color:white;text-align:center;font-family:arial;">TITANIC MACHINE LEARNING</h3>
        <h3 style="color:white;text-align:center;font-family:arial;">KELOMPOK 3 - PJJ DAS V 2023 </h3>
        </div>
		"""

def main():
    stc.html(html_temp)
    menu=["Home","EDA","Prediction"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        col1, col2 = st.columns([0.4,0.6])
        with col1:
            st.image('kapal.jpg')
        with col2:
            st.write('RMS Titanic adalah sebuah kapal penumpang super Britania Raya yang tenggelam di Samudra Atlantik Utara pada tanggal 15 April 1912 setelah menabrak sebuah gunung es pada pelayaran perdananya dari Southampton, Inggris ke New York City. Tenggelamnya Titanic mengakibatkan kematian sebanyak 1514 orang dalam salah satu bencana maritim masa dama paling mematikan sepanjang sejarah. Titanic merupakan kapal terbesar di dunia pada pelayaran perdananya. Satu dari tiga kapal samudra kelas Olympic dioperasikan oleh White Star Line. Kapal ini dibangun pada 1909 sampai 1911 oleh galangan kapal Harland and Wolff di Belfast. Kapal ini sanggup mengangkut 2,224 penumpang.')
        
        st.container()
        
        st.write('Berdasarkan Kejadian Titanic tersebut maka akan dilakukan Data Analytic atas Penumpang Kapal tersebut')

    elif choice == "EDA":
        run_eda_app()
    
    elif choice =="Prediction":
        run_predict_app()


if __name__=='__main__':
    main()
