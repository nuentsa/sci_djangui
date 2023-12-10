import math
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import BienImmo

def calcul_mensualite(taux_interet, taux_assurance, montant_financement, duree_annees):
    # Conversion des taux en valeurs décimales
    taux_interet_decimal = taux_interet / 100.0
    taux_assurance_decimal = taux_assurance / 100.0

    # Calcul du taux d'intérêt mensuel
    taux_interet_mensuel = taux_interet_decimal / 12.0

    # Calcul du nombre total de paiements mensuels
    nombre_paiements = duree_annees * 12.0

    # Calcul du facteur d'amortissement
    facteur_amortissement = (taux_interet_mensuel * math.pow(1 + taux_interet_mensuel, nombre_paiements)) / (math.pow(1 + taux_interet_mensuel, nombre_paiements) - 1)

    # Calcul du montant de l'assurance mensuelle
    montant_assurance_mensuelle = montant_financement * taux_assurance_decimal / 12.0

    # Calcul de la mensualité totale
    mensualite = montant_financement * facteur_amortissement + montant_assurance_mensuelle

     # Calcul du coût total du crédit
    cout_total_credit = mensualite * nombre_paiements - montant_financement

    return mensualite, montant_assurance_mensuelle, cout_total_credit

# Calculer le financement par credit bancaire ou apport personnel
def simuler_mensualites(bien): 
    enveloppe_globale = bien.enveloppe_financement() 
    apport_personnel = st.number_input("Avec un apport personnel de ", value=enveloppe_globale)
    montant_financement = st.number_input("J'emprunte", min_value=0.0, value=max(0.0,(enveloppe_globale - apport_personnel)), step=100.0, help="autres frais bancaires non pris en compte")
    col1, col2 = st.columns(2, gap="large")
    nombre_de_parts = col1.number_input("Nombre de parts de la SCI ", value=13010, step=10)
    apport_par_part = round(apport_personnel / nombre_de_parts, 2)
    col2.write(f"Apport initial par part: {apport_par_part}€ ")
    bien.ajouter_apport_personnel(nombre_de_parts, apport_par_part)
    if montant_financement > 0 :
        duree_annees = st.slider("Sur une durée de", min_value=2, max_value=25, value=20)
        taux_interet = st.slider("à un taux d'intérêt de ", min_value=0.0, max_value=8.0, value=4.5)
        taux_assurance = st.slider("et un taux d'assurance de  ", min_value=0.0, max_value=3.0, value=0.5)
        st.divider()
        mensualite_credit, assurance_mensuelle, cout_total_credit = calcul_mensualite(taux_interet, taux_assurance, montant_financement, duree_annees)
        st.write(f"Mensualite : {round(mensualite_credit, 2)}€, dont assurances : {round(assurance_mensuelle, 2)}€, Cout Total credit : {round(cout_total_credit, 2)}€")
        bien.ajouter_mensualite(mensualite_credit+assurance_mensuelle)
    return bien
