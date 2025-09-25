# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 19:56:55 2025

@author: Petra Izeboud
"""

import xlwings as xw
import pandas as pd


def main():
    """
    Vult eerste lege kolom in Excel met waarde uit externe excel file.
    
    Afhankelijk van de input in cel F6 in Excel wordt een keuze gemaakt
    uit welke Excel data wordt ingeladen en toegevoegd aan het excel bestand. 
    De keuze bestaat uit 'bejaarden' en 'studenten'.
    
    Als de keuze 'bejaarden' is dan wordt de input_bejaarden.xlsx ingelezen.
    Bij de keuze 'studenten' wordt de input_studenten.xlsx ingelezen.
    De data wordt toegevoegd aan de eerste lege kolom de 'calling' excel file. 
    
    Deze functie kan zowel vanuit python worden gebruikt, als vanuit Excel. 
    Als de functie vanuit Excel wordt geroepen, moet dat Excel bestand 
    DEZELFDE naam hebben als het python bestand. En deze moeten in dezelfde
    folder staan.
    """

    try:
        # Als het script vanuit Excel wordt aangeroepen halen we zo betstand op
        wb = xw.Book.caller()  # Works only when called from Excel
    except Exception:
        # If not called from Excel, open a workbook manually
        print("Running from Python")
        wb = xw.Book("voorbeeld_excel_pyton.xlsm")

    # # Connect met het Excel bestand dat de code oproept
    wb = xw.Book.caller()  
    
    # # kies de eerste sheet
    sheet = wb.sheets[0]
    
    sheet.range("A8").value = "Hello from Python -- staring wth main!"
    
    # Bekijk welke waarde de cel heeft die aangeeft uit welk excel bestand
    # we data gaan toevoegen
    keuze = sheet.range("F6").value
    if keuze == "bejaarden":
        # inlezen van de bijbehorende excel en invullen waardes in de actieve excel
        data = pd.read_excel(r"C:\Users\Petra Izeboud\MAMBA\course-material-master\course-material-master\practical_examples\14_Xlwings_Plugin_Excel\Python_Excel_plugin_uitleg\input_bejaarden.xlsx")
        keuze_col_naam = "Aantal bejaarden"
    elif keuze == "tieners":
        data= pd.read_excel(r"C:\Users\Petra Izeboud\MAMBA\course-material-master\course-material-master\practical_examples\14_Xlwings_Plugin_Excel\Python_Excel_plugin_uitleg\input_tieners.xlsx")
        keuze_col_naam = "Aantal tieners"
    else:
        sheet.range("F6").value = "Incorrect choice"
        # Met return stopt de rest van de code
        return None
    
    # Zoek de eerste lege kolom (op A1 na)
    col = 2
    while sheet.range((1, col)).value is not None:
        col += 1

    # onze data uit de ingelezen excel bestaat uit zoveel regels:
    nmbr_rows = len(data[keuze_col_naam])
    
    # Vul in de kolom naam in:
    sheet.range(1, col).value = keuze_col_naam
    # de Start_cell voor de data is de eerste lege cel op regel 2.
    start_cell = (2, col)  # Beginnen bij regel 2,  omdat op regel 1 de kolom naam staat
    end_cell = (nmbr_rows+1, col)  # Eindigen bij de regel afhankelijk van de lengte van je data
    
    # hiermee tover je de data om in een kolommen formaat (verticaal) ipv horizontaal
    data_to_fill = [[x] for x in data[keuze_col_naam].values]
    # Vul de data in
    sheet.range(start_cell, end_cell ).value = data_to_fill 
    
    # print een waarde
    sheet.range("A7").value = "end of main- completed succesfully!"

    
    