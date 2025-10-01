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
import streamlit as st
import io

# navbar
with st.sidebar:
    st.header("🎶 Augmentation Audio and Speech Recognition 🎶")
    
    if st.button("Dashboard"):
        # ketika click langsung diarahkan ke page Upload_Audio
        st.switch_page("Dashboard.py")
        st.rerun()
    if st.button("Audio Augmentation"):
        # ketika click langsung diarahkan ke page Upload_Audio
        st.switch_page("pages/Audio_Augmentation.py")
        st.rerun()
    st.markdown("---") 

# ====================
# SPEECH TO TEXT
# ====================
st.title("😀 Speech To Text 💬")
file_path = st.file_uploader("Upload a WAV file", type=["wav"])

# load model manual dari URL
bundle = pipelines.WAV2VEC2_ASR_BASE_960H 

class CTCDecoder(torch.nn.Module):
        def __init__(self, labels, blank=0):
            super().__init__()
            self.labels = labels
            self.blank = blank

        def forward(self, emission: torch.Tensor) -> str:
            indices = torch.argmax(emission, dim=-1)  # ambil index maksimum per frame waktu
            indices = torch.unique_consecutive(indices, dim=-1)  # hapus duplikat berurutan
            indices = [i for i in indices if i != self.blank]  # hapus label blank
            return "".join([self.labels[i] for i in indices])
def speech_to_text(file_path):
    # load audio dari yang udah di upload
    audio_bytes = file_path.read()
    file_path.seek(0)  #reset file pointer
    file_path1 = io.BytesIO(audio_bytes)

    # load audio
    waveform, sample_rate = torchaudio.load(file_path1)
    
    model = bundle.get_model()

    # resample kalau sample rate tidak sesuai dengan model
    if sample_rate != bundle.sample_rate:
        waveform = F.resample(waveform, sample_rate, bundle.sample_rate)

    # ubah suara ke teks dengan model
    with torch.inference_mode():
        emission, _ = model(waveform)
        features, _ = model.extract_features(waveform)
        
    # decode hasil prediksi
    decoder = CTCDecoder(bundle.get_labels())
    transcript = decoder(emission[0])

    # ganti '|' dengan spasi
    transcript = transcript.replace("|", " ")

    return transcript


if file_path is not None:
    st.audio(file_path, format='audio/wav')

    st.markdown("---")
    if st.button("Predict Text from Audio"):
        with st.spinner("Processing audio..."):
            predicted_text = speech_to_text(file_path)
        st.success(f"Prediction Result: {predicted_text}")
        # st.markdown(f"""{predicted_text}""")
        # st.write(f"{predicted_text}")
        
else:

    st.info("Please upload your WAV file!")   
