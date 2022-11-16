import mysql.connector
import tkinter.messagebox
db_server="85.215.172.165"
db_name="Projekt_X"
db_username="root"
db_userpass="root"
connection=""
cursor=""

#Datenbank neu erstellen
def db_erstellen():
    try:
        connection=mysql.connector.connect(host=db_server, user=db_username,passwd=db_userpass)
        cursor=connection.cursor()
        execution_string=f"CREATE DATABASE {db_name};"
        cursor.execute(execution_string)
        db_tab_make()
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim öffnen der Datenbank")

#Datenbank komplett löschen
def db_eliminator():
    try:
        connection=mysql.connector.connect(host=db_server, user=db_username,passwd=db_userpass)
        cursor=connection.cursor()
        execution_string=f"DROP DATABASE {db_name};"
        cursor.execute(execution_string)
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim löschen der Datenbank")

#Datenbank öffnen
def db_oeffnen():
    try:
        connection=mysql.connector.connect(host=db_server, user=db_username,passwd=db_userpass)
        cursor=connection.cursor()
        execution_string=f"USE {db_name};"
        cursor.execute(execution_string)
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim öffnen der Datenbank")

#Datenbank schliessen
def db_schliessen():
    try:
        connection.commit()
        connection.close()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim schliessen der Datenbank")

#Kundendaten-Tabelle erstellen
def db_tab_make():   
    try:
        db_oeffnen()
        execution_string = "CREATE TABLE kunden( \
        kdnr INTEGER AUTO_INCREMENT PRIMARY KEY, \
        kname VARCHAR(30), \
        kvname VARCHAR(30), \
        kstr VARCHAR(40), \
        khausnr VARCHAR(5), \
        kplz DECIMAL(5,0), \
        kort VARCHAR(30) \
        );"
        cursor.execute(execution_string)
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim erstellen der Tabelle (Kundendaten)")

#Produktdaten-Tabelle erstellen
    try:
        db_oeffnen()
        execution_string="CREATE TABLE produkte( \
        artnr INT AUTO_INCREMENT PRIMARY KEY, \
        artbez VARCHAR(50), \
        artpreis DECIMAL(3,2) \
        );"        
        cursor.execute(execution_string)
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim erstellen der Tabelle (Produkte)")

#Bestellungen-Tabelle erstellen
    try:
        db_oeffnen()
        execution_string="CREATE TABLE bestellungen( \
        onr INT AUTO_INCREMENT PRIMARY KEY, \
        omenge DECIMAL(3,0) \
        );"
        cursor.execute(execution_string)
        connection.c
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim erstellen der Tabelle (Bestellungen)")


#Neuen Kunden anlegen
def db_neu_kunde(k_name,k_vname,k_str,k_hnr,k_plz,k_ort):
    try:
        db_oeffnen()
        execution_string=f"INSERT INTO kunden VALUES(kname, kvname, kstr, khausnr, kplz, kort) {k_name}, {k_vname}, {k_str}, {k_hnr}, {k_plz}, {k_ort};"
        cursor.execute(execution_string)
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim erstellen der Tabelle (Bestellungen)")

#Neuen Artikel anlegen
def db_neu_art(artikel_bez, artikel_preis):
    try:
        db_oeffnen()
        execution_string=f"INSERT INTO artikel VALUES(artnr, artbez, artpreis) {a_nr}, {a_bez}, {a_preis};"
        cursor.execute(execution_string)
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim anlegen des neuen Artikels")

#Neue Bestellung anlegen
def db_neu_bestellung(artikel_nr,artikel_anz):
    try:
        db_oeffnen()
        execution_string=f"INSERT INTO bestellungen VALUES(onr, omenge) {o_nr}, {o_menge};"
        cursor.execute(execution_string)
        db_schliessen()
    except
        tkinter.messagebox.showerror(title=f"Fehler", message="Fehler beim anlegen der Bestellung")


