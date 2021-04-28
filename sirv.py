#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:23:19 2020

@author: kaustuv
"""
# Import Library
import numpy as np
import scipy.integrate as spi
import scipy.interpolate as spn
import plotly.graph_objects as go


def run_sirv(N, days, I0, R0, infectious_period, r0, pStart,pEnd,pFrac):
    gamma = 1/infectious_period
    beta = gamma*r0

    # I0 = 1
    # R0 = 0
    S0 = N-I0-R0

    t = np.linspace(1,days, days)
    # Initial coditions vector
    y0 = S0,I0,R0 
    
    # p
    p = np.zeros(days)
    a = pFrac/(pEnd-pStart)
    x = np.linspace(0,(pEnd-pStart),(pEnd-pStart)-1)
    p[0:pStart-1] = 0
    p[pStart:pEnd-1] = a*x
    p[pEnd-1:] = pFrac
    
    interp = spn.interp1d(t,p)

    # Model Deinition
    def sirv(t,y,N,beta, gamma):
        S,I,R = y
        p = interp(t)
        dSdt = -beta*(1-p)*S*I/N
        dIdt = beta*(1-p)*S*I/N - gamma*I
        dRdt = gamma*I
        return dSdt, dIdt, dRdt

    
    sol = spi.solve_ivp(sirv,(1,days),y0, args=(N,beta,gamma),t_eval=t, method='RK45')
    
    I = sol.y[1]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t,y=I, mode="lines", name="Active Cases", line={'dash': 'solid', 'color': 'red'}))
    #X-Axis
    fig.update_xaxes(title_text='Days')
    
    #Y-axis
    fig.update_yaxes(title_text='Count')
    
    # Layout
    fig.update_layout(title={"text": "SIR Model with Vaccination","x": 0.5,"y": .95,"xanchor": "center","yanchor": "bottom"}, #Title
                      width=740, height=420, #Figure size
                      margin=dict(r=20, b=10, l=10, t=30),
                      template = 'plotly_white', #Template {seaborn, plotly_white, dark}
                      showlegend = True
                      )     
    
    # Annotations
    max_infected = max(I)
    max_pos = np.argmax(I)
    day_max_infected = t[max_pos]
    txt = "Max Infected: {a:.0f} on Day: {b:.0f}"
    max_text = txt.format(a=max_infected, b=day_max_infected)
    fig.add_annotation(text=max_text,
                       x=day_max_infected ,y=max_infected,
                       xref='x', yref='y',
#                       ax=0, ay=0,
                       showarrow=True)
    
    fig.add_vrect(
    x0=pStart, x1=pEnd,
    y0=0,y1=1,
    yref="paper",
    fillcolor="Green", opacity=0.25,
    layer="above", line_width=0)
        
#    fig.add_vrect(
#    x0=pStart, x1=pEnd,
#    fillcolor="LightSalmon", opacity=0.5,
#    layer="below", line_width=0,
#),
    
    return fig
