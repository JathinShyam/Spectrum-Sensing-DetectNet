import streamlit as st
from PIL import Image
import pandas as pd


st.set_page_config(layout="wide")

st.title('Basic Concepts')

with st.expander('What is modulation?'):
    st.write('Modulation is the process of converting data into radio waves by adding information to an electronic or optical carrier signal. A carrier signal is one with a steady waveform - constant height, or amplitude, and frequency.')
    st.image('mod.jpg')

with st.expander('Why use modulation?'):
    st.write("The carrier wave used by radio frequency (RF) transmissions doesn't carry much information itself. To include speech or data, another wave has to be superimposed on the carrier wave, thus changing the shape of the carrier wave. The process of doing so is called modulation. To transmit sound, the audio signal must first be converted into an electric signal, using a transducer. After conversion, it is used to modulate a carrier signal.")
    
with st.expander('Analog vs. digital'):
    st.write("Modulation schemes can be analog or digital. An analog scheme has an input wave that varies continuously like a sine wave. In digital modulation scheme, voice is sampled at some rate and then compressed and turned into a bit stream, and this in turn is created into a particular kind of wave which is then superimposed on the carrier signal.")

with st.expander('SNR?'):
    st.write("The ‘Signal-to-Noise’ ratio or, SNR (in short), is a metric that describes the signal performance in the presence of wireless channel noise (interference). In the linear scale, the SNR is the ratio of the signal power to the noise power. The wireless channel is never noise-free.")

with st.expander("What Information does SNR Give Us?"):
    st.write("* When the signal power drops below a certain threshold, it cannot be detected and decoded faithfully by the receiver. \n * It tells us the strength of the signal when compared to the channel noise. \n * A positive SNR indicates that the signal power is greater than the noise power while a negative SNR indicates the opposite. \n * It is often a common practice to express the SNR in logarithm-based decibel (dB) scale.")    
