import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import networkx as nx
from urllib.request import urlopen
import re
from datetime import datetime
import datetime as dt


st.set_page_config(layout="wide", page_title='PisazoCount')

pisazers = ['Irene', 'Eddie', 'Manolo', 'Bea', 'Manu']

combinations = []
for pisazer1 in pisazers:
    for pisazer2 in pisazers:
        if pisazer1 != pisazer2:
            combinations.append((pisazer1,pisazer2))

def plot_info():
    edges_and_debts = dict()
    for combination in combinations:
        edges_and_debts[combination] = float(input(f"{combination[0]}→{combination[1]}: ").replace(',', '.'))
    edges_and_debts

    debts = dict()
    for pisazer in pisazers:
        debts[pisazer] = 0
        for combination in list(edges_and_debts):
            if pisazer == combination[0]:
                debts[pisazer] -= edges_and_debts[combination]
            elif pisazer == combination[1]:
                debts[pisazer] += edges_and_debts[combination]
    for index in list(debts):
        debts[index] = round(debts[index], 2)

    pisazo = nx.DiGraph()
    labels = dict()
    edges = []
    debts_copy = debts.copy()

    for debtor in [x for x in list(debts_copy) if debts_copy[x]<0]:
        for creditor in [x for x in list(debts_copy) if debts_copy[x]>0]:
            pay = min(debts_copy[creditor], -debts_copy[debtor])
            if pay != 0:
                edges.append([debtor, creditor])
                debts_copy[creditor] -= pay
                debts_copy[debtor] += pay
                labels[(debtor, creditor)] = round(pay, 2)
    pisazo.add_edges_from(edges)
    pos = nx.spring_layout(pisazo)
    plt.figure()
    nx.draw_planar(pisazo, pos,
                with_labels='True', 
                node_color='blue',
                node_size=1000)
    
    return nx.draw_networkx_edge_labels(pisazo, pos, edge_labels=labels, font_color="red")

def main():
    st.write('''
# PisazoCount
''')

    c11, c12, c13, c14, c15, c16 = st.columns(6)
    c21, c22, c23, c24, c25, c26 = st.columns(6)
    c31, c32, c33, c34, c35, c36 = st.columns(6)
    c41, c42, c43, c44, c45, c46 = st.columns(6)
    c51, c52, c53, c54, c55, c56 = st.columns(6)
    c61, c62, c63, c64, c65, c66 = st.columns(6)

    with c12.container(border=True):
        st.write('Bea')
    with c13.container(border=True):
        st.write('Eddie')
    with c14.container(border=True):
        st.write('Irene')
    with c15.container(border=True):
        st.write('Manolo')
    with c16.container(border=True):
        st.write('Manu')

    with c21.container(border=True):
        st.write('Bea')
    with c31.container(border=True):
        st.write('Eddie')
    with c41.container(border=True):
        st.write('Irene')
    with c51.container(border=True):
        st.write('Manolo')
    with c61.container(border=True):
        st.write('Manu')

    edges_and_debts = dict()    

    edges_and_debts[('Bea', 'Eddie')] = c23.text_input('a', label_visibility='collapsed', value=0)
    edges_and_debts[('Bea', 'Irene')] = c24.text_input('b', label_visibility='collapsed', value=0)
    edges_and_debts[('Bea', 'Manolo')] = c25.text_input('c', label_visibility='collapsed', value=0)
    edges_and_debts[('Bea', 'Manu')] = c26.text_input('d', label_visibility='collapsed', value=0)

    edges_and_debts[('Eddie', 'Bea')] = c32.text_input('e', label_visibility='collapsed', value=0)
    edges_and_debts[('Eddie', 'Irene')] = c34.text_input('f', label_visibility='collapsed', value=0)
    edges_and_debts[('Eddie', 'Manolo')] = c35.text_input('g', label_visibility='collapsed', value=0)
    edges_and_debts[('Eddie', 'Manu')] = c36.text_input('h', label_visibility='collapsed', value=0)

    edges_and_debts[('Irene', 'Bea')] = c42.text_input('i', label_visibility='collapsed', value=0)
    edges_and_debts[('Irene', 'Eddie')] = c43.text_input('j', label_visibility='collapsed', value=0)
    edges_and_debts[('Irene', 'Manolo')] = c45.text_input('k', label_visibility='collapsed', value=0)
    edges_and_debts[('Irene', 'Manu')] = c46.text_input('l', label_visibility='collapsed', value=0)

    edges_and_debts[('Manolo', 'Bea')] = c52.text_input('m', label_visibility='collapsed', value=0)
    edges_and_debts[('Manolo', 'Eddie')]= c53.text_input('n', label_visibility='collapsed', value=0)
    edges_and_debts[('Manolo', 'Irene')] = c54.text_input('ñ', label_visibility='collapsed', value=0)
    edges_and_debts[('Manolo', 'Manu')] = c56.text_input('o', label_visibility='collapsed', value=0)

    edges_and_debts[('Manu', 'Bea')] = c62.text_input('p', label_visibility='collapsed', value=0)
    edges_and_debts[('Manu', 'Eddie')] = c63.text_input('q', label_visibility='collapsed', value=0)
    edges_and_debts[('Manu', 'Irene')] = c64.text_input('w', label_visibility='collapsed', value=0)
    edges_and_debts[('Manu', 'Manolo')] = c65.text_input('r', label_visibility='collapsed', value=0)

    for index in list(edges_and_debts):
        edges_and_debts[index] = float(edges_and_debts[index])

    debts = dict()
    for pisazer in pisazers:
        debts[pisazer] = 0
        for combination in list(edges_and_debts):
            if pisazer == combination[0]:
                debts[pisazer] -= edges_and_debts[combination]
            elif pisazer == combination[1]:
                debts[pisazer] += edges_and_debts[combination]
    for index in list(debts):
        debts[index] = round(debts[index], 2)

    pisazo = nx.DiGraph()
    labels = dict()
    edges = []
    debts_copy = debts.copy()

    for debtor in [x for x in list(debts_copy) if debts_copy[x]<0]:
        for creditor in [x for x in list(debts_copy) if debts_copy[x]>0]:
            pay = min(debts_copy[creditor], -debts_copy[debtor])
            if pay != 0:
                edges.append([debtor, creditor])
                debts_copy[creditor] -= pay
                debts_copy[debtor] += pay
                labels[(debtor, creditor)] = round(pay, 2)
    pisazo.add_edges_from(edges)
    pos = nx.spring_layout(pisazo)
    fig, ax = plt.subplots()
    nx.draw(pisazo, pos, with_labels='True', 
            node_color='white', node_size=1500, alpha=1)
    nx.draw_networkx_edge_labels(pisazo, pos, edge_labels=labels, 
                                 font_color="red")

    d1, d2 = st.columns(2)

    d1.table(debts)
    d2.pyplot(fig)

    try:
        url = 'https://scu.ugr.es'
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        text = html.split('\n')

        words = ['  DE  ', 'Menú 1', 'Menú 2', 'Primero', 'Segundo', 'Acompañamiento', 'Postre', 'Cremas y sopas', 'Ensaladas']

        for i in reversed(range(len(text))):
            line = text[i]
            if not any([x in line for x in words]):
                text.pop(i)
            else:
                text[i] = line.replace('\t', '').replace('<th class="leftalign" colspan="2"><strong>', '')\
                    .replace('</strong>  </th><th class="rightalign">  </th>', '')\
                    .replace('<td colspan="2"><strong>', '')\
                    .replace('</strong> </td><td><strong><em>Alérgenos</em></strong></td>', '')\
                    .replace('<td class="leftalign">', '')\
                    .replace('  </td><td class="leftalign"><strong>', '')\
                    .replace('</strong>  </th><th class="rightalign">  </th>', '')\
                    .replace('  </td><strong>', ': ')\
                    .replace('  ', ' ')
                text[i] = text[i].split('</strong>')[0]

        today = datetime.today().day

        for i in range(len(text)):
            if text[i] == text[0] and i != 0:
                text = text[0:i]
                break

        for i in range(len(text)):
            line = text[i]
            if f"{today+1} DE" in line:
                text = text[0:i]
                break

        for i in range(len(text)):
            line = text[i]
            if f"{today} DE" in line:
                text = text[i:]
                break
        text = text[1:]
        for i in range(len(text)):
            try:
                text[i] = text[i].split(': ')[1]
            except:
                pass
        menu1 = text[:text.index('Menú 2')]
        menu2 = text[text.index('Menú 2'):]


        menu1 = pd.DataFrame(menu1[1:], columns = [menu1[0]])
        menu2 = pd.DataFrame(menu2[1:], columns = [menu2[0]])
        df = pd.concat([menu1, menu2], axis=1).fillna('')
    
        with st.sidebar:
            st.markdown(df.style.hide(axis="index").to_html(), unsafe_allow_html=True)

    except:
        pass



if __name__=='__main__':
    main()
