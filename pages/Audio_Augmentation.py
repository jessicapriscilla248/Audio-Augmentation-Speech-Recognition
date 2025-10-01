import torchaudio
import torch
import random
import librosa
import soundfile as sf
import speech_recognition as sr
from pydub import AudioSegment, utils
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio.functional as F
import torchaudio.pipelines as pipelines
import numpy as np
import streamlit as st
import io

# navbar
with st.sidebar:
    st.header("🎶 Augmentation Audio and Speech Recognition 🎶")
    
    if st.button("Dashboard"):
        # ketika click langsung diarahkan ke page Upload_Audio
        st.switch_page("Dashboard.py")
        st.rerun()
    if st.button("Speech to Text"):
        # ketika click langsung diarahkan ke page Upload_Audio
        st.switch_page("pages/Speech_To_Text.py")
        st.rerun()
    st.markdown("---") 

# ====================
# AUDIO AUGMENTATION
# ====================
st.title("Audio Augmentation")
file_path = st.file_uploader("Upload a WAV file", type=["wav"])

def change_volume(volume_db, file_path):
    # load audio dari yang udah di upload
    audio_bytes = file_path.read()
    file_path.seek(0)  #reset file pointer
    file_path1 = io.BytesIO(audio_bytes)
        
    # load audio dengan pydub
    audio = AudioSegment.from_wav(file_path1)

    # change volume
    audio = audio + volume_db
    
    st.markdown("---") 

    st.text("Your Changed Audio:")
    # buat cek aja
    st.audio(audio.export(format="wav").read(), format='audio/wav')

    return audio

def change_pitch(file_path, pitch_rate):
    # load audio dari yang udah di upload
    audio_bytes = file_path.read()
    file_path.seek(0)  #reset file pointer

    audio, sample_rate = librosa.load(io.BytesIO(audio_bytes), sr=None)
    audio = librosa.effects.pitch_shift(audio, sr=sample_rate, n_steps=pitch_rate)
    
    # buat cek aja
    st.audio(audio, sample_rate=sample_rate, format='audio/wav')

    # convert balik ke AudioSegment buat save audio, np ke audiosegment
    audio_int = (audio * 32767).astype(np.int16)
    audio = AudioSegment(
        audio_int.tobytes(),
        frame_rate=sample_rate,
        sample_width=audio_int.dtype.itemsize,
        channels=1
    )

    return audio

def apply_fade(file_path, fade_type, duration):
    # load audio dari yang udah di upload
    audio_bytes = file_path.read()
    file_path.seek(0)  #reset file pointer
    file_path1 = io.BytesIO(audio_bytes)
    
    # load audio dengan pydub
    audio = AudioSegment.from_wav(file_path)

    # apply fade
    # 1 second = 1000ms
    # jadi perlu kita kali nih duration dengan 1000, biar jd millisecond
    if fade_type == 1:
        audio = audio.fade_in(duration*1000)
    else :
        audio = audio.fade_out(duration*1000)
    
    # buat cek aja
    st.audio(audio.export(format="wav").read(), format='audio/wav')

    return audio

def save_file(audio, new_filename):
    wav_io = io.BytesIO()
    audio.export(wav_io, format="wav")
    wav_io.seek(0)
    
    st.success(f"Audio ready as {new_filename}")
    return wav_io

# menu tab untuk user
if file_path is not None:
    st.audio(file_path, format='audio/wav')
    
    tab1, tab2, tab3 = st.tabs(['Change Volume', 'Change Pitch', 'Apply Fade'])

    with tab1:
        st.subheader("Adjust Your Audio Volume")
        volume_value = st.slider(
            "Adjust Volume", 
            min_value=-40, 
            max_value=30, 
            value=0,
            step=1, 
            help="Swipe left = quieter, swipe right = louder"
        )

        if st.button("Apply Volume Change"):
            modified_audio = change_volume(volume_value, file_path)
            if modified_audio:
                # save
                new_filename = "changed_audio.wav"
                save = save_file(modified_audio, new_filename)
                
                st.download_button(
                    label="Download Volume Modified Audio",
                    data=save,
                    file_name=new_filename,
                    mime="audio/wav"
                )

    with tab2:
        st.subheader("Adjust Your Audio Pitch")
        
        pitch_rate = st.slider(
            "Pitch Change", 
            min_value=-10, 
            max_value=10, 
            value=0,
            step=1,
            help="Swipe left = lower voice, swipe right = lighter voice"
        )

        if st.button("Apply Pitch Change"):
            modified_audio = change_pitch(file_path, pitch_rate)
            if modified_audio:
            # save
                new_filename = "changed_audio.wav"
                save = save_file(modified_audio, new_filename)
                
                st.download_button(
                    label="Download Pitch Modified Audio",
                    data=save,
                    file_name=new_filename,
                    mime="audio/wav"
                )
    with tab3:
        st.subheader("Adjust Your Fade Effect")

        # fade in : 1
        # fade out: 0
        fade_type = st.radio("Fade Type", [0, 1], format_func=lambda x: 'In' if x else 'Out')
        duration = st.slider(
            "Fade Duration",
            min_value =1,
            max_value=5,
            value=1,
            step=1
        )

        if st.button("Apply Fade Effect"):
            modified_audio = apply_fade(file_path, fade_type, duration)
            if modified_audio:
                # save
                new_filename = "changed_audio.wav"
                save = save_file(modified_audio, new_filename)
                
                st.download_button(
                    label="Download Fade Modified Audio",
                    data=save,
                    file_name=new_filename,
                    mime="audio/wav"
                )
else: 
    st.info("Please upload your WAV file!")            
        

