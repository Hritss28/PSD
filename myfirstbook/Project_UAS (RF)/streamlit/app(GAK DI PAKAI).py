import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Klasifikasi Time Series BME", page_icon="📊", layout="wide")

@st.cache_resource
def load_model_and_scaler():
    try:
        model = joblib.load('models/model_rf_bme.pkl')
        scaler = joblib.load('models/scaler_bme.pkl')
        return model, scaler
    except FileNotFoundError as e:
        st.error(f"File model atau scaler tidak ditemukan: {e}")
        return None, None

model, scaler = load_model_and_scaler()

label_mapping = {
    1: 'Begin',
    2: 'Middle',
    3: 'End'
}

st.title("Klasifikasi Time Series Dataset BME")
st.markdown("---")
st.markdown("### Upload File CSV")

uploaded_file = st.file_uploader("Pilih file CSV yang ingin diklasifikasi", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success(f"File berhasil diupload! Jumlah data: {len(df)} baris, {df.shape[1]} kolom")
    
    with st.expander("Preview Data (5 baris pertama)"):
        st.dataframe(df.head())
    
    st.markdown("---")
    st.markdown("### Pilih Mode Klasifikasi")
    
    mode = st.radio(
        "Silakan pilih mode klasifikasi:",
        ["Klasifikasi Semua Data", "Klasifikasi Data Spesifik (Pilih Baris)"],
        index=0
    )
    
    st.markdown("---")
    
    if model is not None and scaler is not None:
        
        # MODE 1: Klasifikasi Semua Data
        if mode == "Klasifikasi Semua Data":
            st.markdown("### Klasifikasi Semua Data")
            
            if st.button("Mulai Klasifikasi Semua Data", type="primary"):
                with st.spinner("Sedang melakukan klasifikasi..."):
                    X = df.values
                    X_scaled = scaler.transform(X)
                    
                    predictions = model.predict(X_scaled)
                    predictions_label = [label_mapping[pred] for pred in predictions]
                    
                    result_df = df.copy()
                    result_df['Prediksi (Numerik)'] = predictions
                    result_df['Prediksi (Label)'] = predictions_label
                    
                    st.success(f"Klasifikasi selesai untuk {len(df)} data!")
                    
                    st.markdown("#### Hasil Klasifikasi")
                    st.dataframe(result_df[['Prediksi (Numerik)', 'Prediksi (Label)']])
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        begin_count = sum(predictions == 1)
                        st.metric("Begin", begin_count)
                    with col2:
                        middle_count = sum(predictions == 2)
                        st.metric("Middle", middle_count)
                    with col3:
                        end_count = sum(predictions == 3)
                        st.metric("End", end_count)
                    
                    csv = result_df.to_csv(index=False)
                    st.download_button(
                        label="Download Hasil Klasifikasi (CSV)",
                        data=csv,
                        file_name="hasil_klasifikasi_semua.csv",
                        mime="text/csv"
                    )
        
        # MODE 2: Klasifikasi Data Spesifik
        else:
            st.markdown("### Klasifikasi Data Spesifik")
            row_options = [f"Baris {i}" for i in range(len(df))]
            selected_row = st.selectbox(
                "Pilih baris data yang ingin diklasifikasi:",
                options=row_options,
                index=0
            )
            
            # Ambil index yang dipilih
            selected_idx = int(selected_row.split()[1])
            st.markdown(f"#### Data pada {selected_row}")
            selected_data = df.iloc[selected_idx]
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.dataframe(selected_data.to_frame().T)
            
            with col2:
                if st.button("Klasifikasi Data Ini", type="primary"):
                    with st.spinner("Sedang melakukan klasifikasi..."):
                        X = selected_data.values.reshape(1, -1)
                        X_scaled = scaler.transform(X)
                        
                        prediction = model.predict(X_scaled)[0]
                        prediction_label = label_mapping[prediction]
                        
                        st.markdown("---")
                        st.markdown("#### Hasil Prediksi")
                        
                        if prediction == 1:
                            color = "green"
                        elif prediction == 2:
                            color = "blue"
                        else:
                            color = "red"
                        
                        st.markdown(f"""
                        <div style="padding: 20px; border-radius: 10px; background-color: {color}; color: white; text-align: center;">
                            <h2>{prediction_label}</h2>
                            <p style="font-size: 18px;">Kelas: {prediction}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        st.info(f"Data pada **{selected_row}** diprediksi sebagai kelas **{prediction} ({prediction_label})**")
            
            # Visualisasi data yang dipilih
            st.markdown("---")
            st.markdown("#### Visualisasi Data Time Series")
            
            import matplotlib.pyplot as plt
            
            fig, ax = plt.subplots(figsize=(12, 4))
            ax.plot(selected_data.values, linewidth=2, color='steelblue')
            ax.set_title(f'Pola Time Series - {selected_row}', fontsize=14, fontweight='bold')
            ax.set_xlabel('Time Step', fontsize=12)
            ax.set_ylabel('Nilai', fontsize=12)
            ax.grid(True, alpha=0.3)
            ax.axhline(y=0, color='red', linestyle='--', alpha=0.5)
            plt.tight_layout()
            st.pyplot(fig)
    
    else:
        st.error("Model atau scaler tidak dapat dimuat. Pastikan file 'model_rf_bme.pkl' dan 'scaler_bme.pkl' tersedia.")

else:
    st.info("Silakan upload file CSV terlebih dahulu untuk memulai klasifikasi.")
    
    st.markdown("---")
    st.markdown("### Informasi")
    st.markdown("""
    **Format CSV yang dibutuhkan:**
    - File CSV harus berisi fitur time series (128 kolom: att1 sampai att128)
    - Tidak perlu menyertakan kolom 'target' (hanya data fitur saja)
    - Contoh: `BME_TEST_DEPLOY_NO_TARGET.csv`
    
    **Kelas Prediksi:**
    - **Begin (1)**: Pola puncak di awal time series
    - **Middle (2)**: Pola puncak di tengah time series  
    - **End (3)**: Pola puncak di akhir time series
    """)

st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>Klasifikasi Time Series BME dengan Random Forest | © 2025</div>",
    unsafe_allow_html=True
)