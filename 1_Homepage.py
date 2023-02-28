import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Capstone Real Estate Consultants", page_icon=":house:", layout="wide", initial_sidebar_state="collapsed")

#--- Load Assets ----
img_crec_logo = Image.open("images/crec_logo.png")
img_data_home = Image.open("images/data_home_2.png")
img_seethru_green = Image.open("images/seethrugreen.png")
img_triangles = Image.open("images/triangles_home.png")
img_fuzz = Image.open("images/fuzz.jpg")
img_banner = Image.open("images/banner_grid.png")
img_buildings = Image.open("images/buildings.png")
img_crecddp = Image.open("images/CRECddp.png")
img_banner = Image.open("images/crec_banner.png")
crecddp_3 = Image.open("images/CRECddp_3.png")
title = Image.open("images/title.png")

#---- Header Section -----
st.image(crecddp_3, width=200)
st.write("- - -")

#--- Body Section ----
st.image(title)
st.write("##")
st.subheader("these areas of expertise converge into CREC's single-pane platform offering:")
st.write("##")

st.image(img_crecddp)

st.image(img_triangles)
st.write("- - -")
st.title("CREC's Mission")
st.subheader(":blue[To expedite real estate deals through application of state-of-the-art technology and custom-tailored data solutions.]")
	#st.write("- - -")
	
#--- Second Body ----
# st.write("##")
#---
