# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Import Libraries
#import streamlit as st
#import pandas as pd
import plotly.graph_objects as go
#from plotly.subplots import make_subplots
import numpy as np
import scipy.integrate as spi

#SIR Model
def sir(y,t,N,beta, gamma):
    S,I,R = y
    dSdt = -beta*S*I/N
    dIdt = beta*S*I/N - gamma*I
    dRdt = gamma*I
    return dSdt, dIdt, dRdt

def sird(y,t,N,beta, gamma,d):
    S,I,R,D = y
    dSdt = -beta*S*I/N
    dIdt = beta*S*I/N - gamma*I - d*gamma*I
    dRdt = gamma*I
    dDdt = d*gamma*I
    return dSdt, dIdt, dRdt, dDdt

def seird(y,t,N,e,beta,gamma,d,):
    S,E,I,R,D = y
    dSdt = -beta*S*I/N
    dEdt = beta*S*I/N - e*E
    dIdt =  e*E- gamma*I - d*gamma*I
    dRdt = gamma*I
    dDdt = d*gamma*I
    return dSdt, dEdt, dIdt, dRdt, dDdt


def run_sir(N, days, infectious_period, r0):
    gamma = 1/infectious_period
    beta = gamma*r0

    I0 = 1
    R0 = 0
    S0 = N-I0-R0

    t = np.linspace(0,days, days)
    # Initial coditions vector
    y0 = S0,I0,R0
     
    ret = spi.odeint(sir,y0,t,args=(N,beta,gamma))
    S,I,R = ret.T
    S = list(map(lambda x: round(x,0),S))
    I = list(map(lambda x: round(x,0),I))
    R = list(map(lambda x: round(x,0),R))
    
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t,y=S, mode="lines", name="Susceptibles", line={'dash': 'solid', 'color': 'blue'}))
    fig.add_trace(go.Scatter(x=t,y=I, mode="lines", name="Infected", line={'dash': 'solid', 'color': 'red'}))
    fig.add_trace(go.Scatter(x=t,y=R, mode="lines", name="Removed", line={'dash': 'solid', 'color': 'green'}))
    #X-Axis
    fig.update_xaxes(title_text='Days')
    
    #Y-axis
    fig.update_yaxes(title_text='Count')
    
    # Layout
    fig.update_layout(title={"text": "SIR Model","x": 0.5,"y": .95,"xanchor": "center","yanchor": "bottom"}, #Title
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

    
    return fig

def run_sird(N, days, infectious_period, r0, ifr):
    gamma = 1/infectious_period
    beta = gamma*r0
    ifr = ifr/100

    I0 = 1
    R0 = 0
    D0 = 0
    S0 = N-I0-R0-D0

    t = np.linspace(0,days, days)
    # Initial coditions vector
    y0 = S0,I0,R0,D0
     
    ret = spi.odeint(sird,y0,t,args=(N,beta,gamma, ifr))
    S,I,R,D = ret.T
    S = list(map(lambda x: round(x,0),S))
    I = list(map(lambda x: round(x,0),I))
    R = list(map(lambda x: round(x,0),R))
    D = list(map(lambda x: round(x,0),D))

    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=t,y=S, mode="lines", name="Susceptibles", line={'dash': 'solid', 'color': 'blue'}))
    fig1.add_trace(go.Scatter(x=t,y=I, mode="lines", name="Infected", line={'dash': 'solid', 'color': 'red'}))
    fig1.add_trace(go.Scatter(x=t,y=R, mode="lines", name="Recovered", line={'dash': 'solid', 'color': 'green'}))
    
    #X-Axis
    fig1.update_xaxes(title_text='Days')
    
    #Y-axis
    fig1.update_yaxes(title_text='Count')
    
    # Layout
    fig1.update_layout(title={"text": "SIRD Model","x": 0.5,"y": 0.95,"xanchor": "center","yanchor": "bottom"}, #Title
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
    fig1.add_annotation(text=max_text,
                       x=day_max_infected ,y=max_infected,
                       xref='x', yref='y',
#                       ax=0, ay=0,
                       showarrow=True)

    
    fig2 = go.Figure()
    fig2 = fig2.add_trace(go.Scatter(x=t,y=D, mode="lines", name='Deaths'))
     #X-Axis
    fig2.update_xaxes(title_text='Days')
    
    #Y-axis
    fig2.update_yaxes(title_text='Count')
    
    # Layout
    fig2.update_layout(title={"text": "SIRD Model - Deaths","x": 0.5,"y": 0.95,"xanchor": "center","yanchor": "bottom"}, #Title
                      width=740, height=420, #Figure size
                      margin=dict(r=20, b=10, l=10, t=30),
                      template = 'plotly_white', #Template {seaborn, plotly_white, dark}
                      showlegend = False
                      )     
    # Annotations
    max_D = max(D)
    max_pos = np.argmax(D)
    day_max_D = t[max_pos]
    txt = "Max Deaths: {a:.0f} on Day: {b:.0f}"
    max_text = txt.format(a=max_D, b=day_max_D)
    fig2.add_annotation(text=max_text,
                       x=day_max_D ,y=max_D,
                       xref='x', yref='y',
#                       ax=0, ay=0,
                       showarrow=True)    
    return fig1, fig2

def run_seird(N, days, incubation_period, infectious_period, r0, ifr):
    
    e = 1/incubation_period
    gamma = 1/infectious_period
    beta = gamma*r0
    ifr = ifr/100

    E0 = 1
    I0 = 0
    R0 = 0
    D0 = 0
    S0 = N-E0-I0-R0-D0

    t = np.linspace(0,days, days)
    # Initial coditions vector
    y0 = S0,E0,I0,R0,D0
     
    ret = spi.odeint(seird,y0,t,args=(N,e,beta,gamma, ifr))
    S,E,I,R,D = ret.T
    S = list(map(lambda x: round(x,0),S))
    E = list(map(lambda x: round(x,0),E))
    I = list(map(lambda x: round(x,0),I))
    R = list(map(lambda x: round(x,0),R))
    D = list(map(lambda x: round(x,0),D))

    
    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=t,y=S, mode="lines", name="Susceptibles", line={'dash': 'solid', 'color': 'blue'}))
    fig1.add_trace(go.Scatter(x=t,y=E, mode="lines", name="Exposed", line={'dash': 'solid', 'color': 'orange'}))
    fig1.add_trace(go.Scatter(x=t,y=I, mode="lines", name="Infected", line={'dash': 'solid', 'color': 'red'}))
    fig1.add_trace(go.Scatter(x=t,y=R, mode="lines", name="Recovered", line={'dash': 'solid', 'color': 'green'}))
    
    #X-Axis
    fig1.update_xaxes(title_text='Days')
    
    #Y-axis
    fig1.update_yaxes(title_text='Count')
    
    # Layout
    fig1.update_layout(title={"text": "SEIRD Model","x": 0.5,"y": 0.95,"xanchor": "center","yanchor": "bottom"}, #Title
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
    fig1.add_annotation(text=max_text,
                       x=day_max_infected ,y=max_infected,
                       xref='x', yref='y',
#                       ax=0, ay=0,
                       showarrow=True)
    
    fig2 = go.Figure()
    fig2 = fig2.add_trace(go.Scatter(x=t,y=D, mode="lines", name='Deaths'))
     #X-Axis
    fig2.update_xaxes(title_text='Days')
    
    #Y-axis
    fig2.update_yaxes(title_text='Count')
    
    # Layout
    fig2.update_layout(title={"text": "SEIRD Model - Deaths","x": 0.5,"y": 0.95,"xanchor": "center","yanchor": "bottom"}, #Title
                      width=740, height=420, #Figure size
                      margin=dict(r=20, b=10, l=10, t=30),
                      template = 'plotly_white', #Template {seaborn, plotly_white, dark}
                      showlegend = False
                      )     
    # Annotations
    max_D= max(D)
    max_pos = np.argmax(D)
    day_max_D = t[max_pos]
    txt = "Max Deaths: {a:.0f} on Day: {b:.0f}"
    max_text = txt.format(a=max_D, b=day_max_D)
    fig2.add_annotation(text=max_text,
                       x=day_max_D ,y=max_D,
                       xref='x', yref='y',
#                       ax=0, ay=0,
                       showarrow=True)     
    return fig1, fig2