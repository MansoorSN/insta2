from instagrapi import Client
import streamlit as st

cl = Client()
cl.login(st.secrets.USERNAME, st.secrets.PASSWORD)

post_url=st.text_input("Paste the insta url")

post_id=cl.media_pk_from_url(post_url)

if st.button("Download Post"):
  cl.photo_download(post_id)
