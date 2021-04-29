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
from sirv import run_sirv


st.title("Compartmental Models in Epidemiology")

## Sidebar Layout
models = ['SIR','SIRD', 'SEIRD', 'SIRV']
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

if model_opt == models[3]:
    N = st.sidebar.slider("Population:", 1, 1387000000, 1387000000,100000)
    I0 = st.sidebar.slider("Active Cases:", 1, 10000000, 1, 1000)
    R0 = st.sidebar.slider("Recovered:", 0, 1000000000, 0, 1000)
    r0 = st.sidebar.slider("Basic Reproduction Rate (R0):",0.0,10.0,2.5)
    infec_pd = st.sidebar.slider("Infectious Period (days):",1.0,20.0,10.0)
    days = st.sidebar.slider("Simulation Days:",1,365*5,365*2,100)
    pFrac = st.sidebar.slider("Fraction of Population Vaccinated:",0.0,1.0,0.5)
    pPeriod = st.sidebar.slider("Period over which vaccinated (days):",0,days,(30,90))
    pStart = pPeriod[0]
    pEnd = pPeriod[1]
#    st.text(type(N))
    
    fig = run_sirv(N, days, I0, R0, infec_pd, r0, pStart, pEnd, pFrac)
    st.plotly_chart(fig)