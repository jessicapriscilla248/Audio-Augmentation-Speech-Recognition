# Audio Augmentation & Speech Recognition App
Aplikasi ini adalah project Streamlit yang membantu pengguna untuk melakukan beberapa hal berikut:           
### 1. Augmentasi Audio
    a. Mengatur Volume
    
    b. Mengatur Pitch

    c. Menambahkan efek fade in dan fade out

### 2. Mengubah Suara ke Teks

## Fitur Utama
### 1. Augmentasi Audio
    a. Mengatur besar dan kecil volume menggunakan satuan dB (decibel, ukuran relatif dari volume (loudness)).
                
        - + -> naik 2x

        - - -> turun setengahnya
    b. Mengatur nada suara menjadi lebih rendah ke lebih tinggi.

    c. Memberikan efek fade in dan fade out pada audio.
### 2. Speech Recognition
            
    a. Mengubah dari Speech to Text menggunakan CTC decoding.

    b. Proses transkripsi dilakukan secara real time.

    c. Adanya progress tracking untuk setiap proses yang dilakukan.

## Web Application
<img src="\screen\tampilan.JPG" alt="Preview" width="600"/>
<img src="\screen\tampilan_2.JPG" alt="Preview" width="600"/>
<img src="\screen\tampilan_3.JPG" alt="Preview" width="600"/>
Demo app: ada pada link portofolio

## Manajemen File
1. Upload audio dengan file WAV
2. Tersedia preview audio sebelum diubah
3. Menyimpan file audio yang telah diubah sesuai preferensi pengguna 

## Tools yang Digunakan
1. Streamlit - Framework aplikasi web
2. PyTorch - Backend deep learning
3. TorchAudio - Library pemrosesan audio
4. Librosa - Analisis dan manipulasi audio
5. PyDub - Manipulasi file audio

## Mesin Speech Recognition
1. Model: Wav2Vec2 dengan CTC decoding
2. Decoder: Class CTCDecoder custom untuk transkripsi teks yang akurat
3. Processing: dengan torch.inference_mode()

