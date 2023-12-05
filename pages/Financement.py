import math
import streamlit as st


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

def main(): 
    st.subheader("Financement")
    if 'current_prop' not in st.session_state:
        st.write("Pas de bien en cours de simulation...")
        st.write("Selectionnez d'abord un bien sur la page d'accueil")

    property_details = st.session_state['current_prop']
    enveloppe_globale = sum(property_details["prix_achat"].values())
    montant_financement = st.number_input("J'emprunte", min_value=0.0, value=enveloppe_globale, step=100.0)
    apport_personnel = st.number_input("Avec un apport de ", value=max(0,(enveloppe_globale - montant_financement)))

    if montant_financement > 0 :
        col1, col2 = st.columns(2, gap="large")
        with col1: 
            duree_annees = st.slider("Sur une durée de", min_value=2, max_value=25, value=20)
            taux_interet = st.slider("à un taux d'intérêt de ", min_value=0.0, max_value=8.0, value=4.5)
        with col2:
            taux_assurance = st.slider("et un taux d'assurance de  ", min_value=0.0, max_value=3.0, value=0.5)
            
        mensualite, montant_assurance_mensuelle, cout_total_credit = calcul_mensualite(taux_interet, taux_assurance, montant_financement, duree_annees)
        st.write(f"Mensualite : {round(mensualite, 2)}€, dont assurances : {round(montant_assurance_mensuelle, 2)}€, Cout Total credit : {round(cout_total_credit, 2)}€")
    st.divider()

main()