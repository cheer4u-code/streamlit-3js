import argparse
import streamlit as st
import streamlit.components.v1 as components

parser = argparse.ArgumentParser(description='Streamlit 3js')

st.set_page_config(
    page_title='Streamlit 3js',
    page_icon=None,
    layout='wide',
    initial_sidebar_state='auto',
)

def threejs(app):
    st.html(
        '''
        <style>
            .block-container {
                padding: 0 !important;
                margin: 0 !important;
                max-width: 100% !important;
                width: 100% !important;
            }
            iframe.stIFrame {
                width: 100vw;
                height: 100vh;
                display: block;
            }
        </style>
        ''');
    with open(app, 'r') as f:
        html = f.read()
    components.html(html, width=0, height=0)

def threejs_earth():
    threejs('earth.html')

def threejs_grid():
    threejs('grid.html')

pg = st.navigation([threejs_earth, threejs_grid])
pg.run()
