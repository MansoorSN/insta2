from instagrapi import Client
import streamlit as st

cl = Client()
cl.login("mansoords200", "Ottawa_22")

post_url=st.text_input("Paste the insta url")


post_id=cl.media_pk_from_url(post_url)
