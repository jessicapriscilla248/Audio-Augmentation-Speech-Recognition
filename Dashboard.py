import streamlit as st

st.title("🎶 Audio Augmentation and Predict Text 🎶")

# navbar
with st.sidebar:
    st.header("🎶 Augmentation Audio and Predict Text 🎶")
    
    if st.button("Audio Augmentation"):
        # ketika click langsung diarahkan ke page Upload_Audio
        st.switch_page("pages/Audio_Augmentation.py")
        st.rerun()
    if st.button("Speech to Text"):
        # ketika click langsung diarahkan ke page Upload_Audio
        st.switch_page("pages/Speech_To_Text.py")
        st.rerun()
    st.markdown("---") 

st.markdown("""
    Aplikasi ini adalah project Streamlit yang membantu pengguna untuk melakukan beberapa hal berikut:
            
        1. Augmentasi Audio
            a. Mengatur Volume

            b. Mengatur Pitch

            c. Menambahkan efek fade in dan fade out

        2. Mengubah Suara ke Teks
""")
st.subheader("Fitur Utama")
st.markdown("""
        1. Augmentasi Audio
            
            a. Mengatur besar dan kecil volume menggunakan satuan dB (decibel, ukuran relatif dari volume (loudness)).
                
                - + -> naik 2x

                - - -> turun setengahnya
            b. Mengatur nada suara menjadi lebih rendah ke lebih tinggi.

            c. Memberikan efek fade in dan fade out pada audio.

        2. Speech Recognition
            
            a. Mengubah dari Speech to Text menggunakan CTC decoding.

            b. Proses transkripsi dilakukan secara real time.

            c. Adanya progress tracking untuk setiap proses yang dilakukan.
""")