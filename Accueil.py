import streamlit as st
import pandas as pd
import serializer
from streamlit_extras.switch_page_button import switch_page



def main():
    st.title("Simulation Express")
    st.subheader("Bien immobilier et Rentabilité brute")
    prix_bien = st.number_input('Prix du bien', value=50000.00, step=500.0)
    frais_notaire = prix_bien * 0.1
    travaux = st.number_input('Montant des travaux', step=100.0)
    mobilier = st.number_input("Mobilier", step=100.0)
    with st.expander("Autres elements à financer "):
        frais_bancaires = 1000.0 # TODO Define as constant
        caution_credit = 0.015*prix_bien # TODO define as constant
        frais_notaire = st.number_input("Frais de notaire", value=frais_notaire, step=100.0)
        frais_bancaires = st.number_input("Frais bancaires", value=frais_bancaires, step=100.0)
        caution_credit = st.number_input("Caution de credit", value=caution_credit, step=50.0)
    with st.expander("Charges liées au bien"):
        charges_copro = st.number_input("Charges annuelles de copropriété", step=50.0)
        taxes_foncieres = st.number_input("Taxes Foncieres", step=50.0)
    with st.expander("Localisation et autre details"):
        addresse_bien = st.text_input("Addresse du bien")
        url_du_bien = st.text_input("Lien de l'annonce")
    loyer_mensuel = st.number_input("Loyer mensuel estimé", step=10)
    
    property_details = dict(
        prix_achat = dict(
            prix_bien = prix_bien,
            travaux = travaux,
            mobilier = mobilier,
            frais_notaire = frais_notaire,
            frais_comptable = frais_bancaires,
            caution_credit = caution_credit
        ),
        charges_fixes = dict(
            charges_copro = charges_copro,
            taxes_foncieres = taxes_foncieres
        ),
        rentabilite = dict(
            loyer_mensuel = loyer_mensuel
        ),
        description = dict(
            addresse_bien = addresse_bien,
            url_du_bien = url_du_bien
        )
    )
    enveloppe_globale = sum(property_details["prix_achat"].values())
    property_details["rentabilite"]["brute"] = round(loyer_mensuel * 12 * 100 / enveloppe_globale, 2)
    
    st.text("Enveloppe globale de financement : {}".format(enveloppe_globale), help="incluant les frais annexes")
    st.text("Rentabilité brute : {}".format(property_details["rentabilite"]["brute"]))
    
    #if st.button("Sauvegarder ce bien"):
    serializer.save_property(property_details)
    st.write(property_details)

    
    if st.button("Calculer le financement"):
        if 'current_prop' not in st.session_state:
            st.session_state['current_prop']= property_details
        switch_page("Financement")
    
    

    st.divider()


main()

