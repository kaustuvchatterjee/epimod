#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 19:56:00 2020

@author: kaustuv
"""

import streamlit as st
from models import run_sir
from models import run_sird
from models import run_seird


st.title("Compartmental Models in Epidemiology")

## Sidebar Layout
models = ['SIR','SIRD', 'SEIRD']
model_opt = st.sidebar.selectbox("Select Model:", models)


if model_opt == models[0]:
    N = st.sidebar.number_input("Population:", value=1000000)
    r0 = st.sidebar.slider("Basic Reproduction Rate (R0):",0.0,10.0,2.5)
    infec_pd = st.sidebar.slider("Infectious Period (days):",1.0,20.0,10.0)
    days = st.sidebar.slider("Simulation Days:",1,730,250)
    
#    st.text(type(N))
    
    fig = run_sir(N,days,infec_pd,r0)
    st.plotly_chart(fig)
    

if model_opt == models[1]:
    N = st.sidebar.number_input("Population:", value=1000000)
    r0 = st.sidebar.slider("Basic Reproduction Rate (R0):",0.0,10.0,2.5)
    infec_pd = st.sidebar.slider("Infectious Period (days):",1.0,20.0,10.0)
    ifr = st.sidebar.slider("Fatality Rate (%):",0.01,3.0,0.15)
    days = st.sidebar.slider("Simulation Days:",1,730,250)
    
#    st.text(type(N))
    
    fig1, fig2 = run_sird(N,days,infec_pd,r0,ifr)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)

if model_opt == models[2]:
    N = st.sidebar.number_input("Population:", value=1000000)
    r0 = st.sidebar.slider("Basic Reproduction Rate (R0):",0.0,10.0,2.5)
    incub_pd = st.sidebar.slider("Incubation Period (days):",1.0,20.0,5.1)
    infec_pd = st.sidebar.slider("Infectious Period (days):",1.0,20.0,7.2)
    ifr = st.sidebar.slider("Fatality Rate (%):",0.01,3.0,0.15)
    days = st.sidebar.slider("Simulation Days:",1,730,250)
    
#    st.text(type(N))
    
    fig1, fig2 = run_seird(N,days,incub_pd,infec_pd,r0,ifr)
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)