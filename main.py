import streamlit as st
import pandas as pd
import math

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
    st.title('Simulation Projet SCI')
    st.sidebar.header("Données pour la simulation")
    st.sidebar.subheader("Données du bien et Rentabilité brute")
    prix_bien = st.sidebar.number_input('Prix du bien', 100000.00)
    frais_notaire = prix_bien * 0.1
    travaux = st.sidebar.number_input('Montant des travaux', 10000)
    mobilier = st.sidebar.number_input("Mobilier", value=5000)
    frais_bancaires = 1000
    caution_credit = 0.015*prix_bien
    with st.sidebar.expander("Autres elements à financer "):
        st.text("Frais de notaire : {}".format(frais_notaire))
        st.text("Frais bancaires : {}".format(frais_bancaires))
        st.text("Caution de credit : {}".format(caution_credit))
    enveloppe_globale = prix_bien + frais_notaire + travaux + mobilier + frais_bancaires + caution_credit
    loyer_mensuel = st.sidebar.number_input("Loyer mensuel estimé", value=500, step=10)
    addresse_bien = st.sidebar.text_input("Addresse du bien")
    renta_brute = round(loyer_mensuel * 12 * 100 / enveloppe_globale, 2)
    if st.sidebar.button("Sauvegarder ce bien"):
        # Save this input data for further studies
        input_data = pd.DataFrame([dict(
            prix_bien = prix_bien,
            travaux = travaux, 
            mobilier = mobilier,
            loyer_mensuel = loyer_mensuel,
            enveloppe_globale = enveloppe_globale, 
            addresse_bien = addresse_bien,
            renta_brute = renta_brute
        )])

  
    st.subheader("Financement")
    st.text("Enveloppe de financement : {}".format(enveloppe_globale), help="incluant les frais annexes")
    montant_financement = st.number_input("J'emprunte", min_value=0.0, value=prix_bien, step=100.0)
    col1, col2 = st.columns(2, gap="large")
    with col1: 
        duree_annees = st.slider("Sur une durée de", min_value=2, max_value=25, value=20)
        taux_interet = st.slider("à un taux d'intérêt de ", min_value=0.0, max_value=8.0, value=4.5)
    with col2:
        taux_assurance = st.slider("et un taux d'assurance de  ", min_value=0.0, max_value=3.0, value=0.5)
        membres = st.slider("Membres de la SCI", value=3, min_value=3, max_value=14)

    st.divider()
    
    
    mensualite, montant_assurance_mensuelle, cout_total_credit = calcul_mensualite(taux_interet, taux_assurance, montant_financement, duree_annees)
    st.write(f"Mensualite : {round(mensualite, 2)}€, dont assurances : {round(montant_assurance_mensuelle, 2)}€, Cout Total credit : {round(cout_total_credit, 2)}€")
    effort_initial = max(enveloppe_globale - montant_financement, 0)
    effort_par_membre = round(effort_initial / membres, 2)
    simul_data = {
            "Achat (+travaux+mobilier)":   prix_bien + travaux + mobilier, 
            "Autres frais (Notaire, Frais bancaires)": frais_bancaires + frais_notaire + caution_credit,
            "Total financement": enveloppe_globale,
            "Montant à emprunter": montant_financement,
            "Apport Initial": max(enveloppe_globale - montant_financement, 0),
            "Apport Par Membre": effort_par_membre            
    }
    st.dataframe(simul_data)


if __name__ == "__main__":
    main()
