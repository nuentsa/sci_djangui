import streamlit as st
import pandas as pd
import serializer
from streamlit_extras.switch_page_button import switch_page
import BienImmo
import Financement
import math



def main():
    st.title("Simulation Express")
    st.subheader("Bien immobilier et Rentabilité brute")
    prix_bien = st.number_input('Prix du bien', step=500.0)
    frais_notaire = prix_bien * 0.1
    travaux = st.number_input('Montant des travaux', step=100.0)
    mobilier = st.number_input("Mobilier", step=100.0)
    superficie = st.number_input("Superficie", step=1)
    loyer_mensuel = st.number_input("Loyer mensuel estimé", step=10)
    with st.expander("Frais Notaires et Charges liées au bien"):
        frais_notaire = st.number_input("Frais de notaire", value=frais_notaire, step=100.0)
        charges_copro = st.number_input("Charges annuelles de copropriété", step=50.0)
        taxes_foncieres = st.number_input("Taxes Foncieres", step=50.0)
    with st.expander("Localisation et autre details"):
        addresse_bien = st.text_input("Addresse du bien")
        url_du_bien = st.text_input("Lien de l'annonce")
    
    # Details du bien pour sauvegarde et references futures
    bien = BienImmo.Bien(
        prix_bien=prix_bien, 
        travaux=travaux, 
        mobilier=mobilier,
        frais_notaires=frais_notaire, 
        charges_copro=charges_copro, 
        taxes_foncieres=taxes_foncieres, 
        superficie=superficie, 
        loyer_mensuel=loyer_mensuel, 
        addresse=addresse_bien, 
        url_annonce=url_du_bien)
    

    # L'enveloppe globale contient le prix du bien, des travaux, des frais bancaires eventuels et  autres frais annexes
    st.text("Enveloppe de financement : {}".format(bien.enveloppe_financement()))
    st.text("Rentabilité : {}".format(bien.rentabilite()), help="Rentabilité Nette, sans les eventuels frais bancaires")
    st.divider()
    if prix_bien == 0:
        return
    df = pd.DataFrame([bien.to_dict_summary()])
    st.write(df)
    
    with st.expander("Simulez le financement"):
        Financement.simuler_mensualites(bien)

    if st.button("Sauvegarder ce bien"):
        try: 
            serializer.enregistrer_bien(bien)
            st.success("Ce bien a été enregistré. Vous pouvez le comparer avec d'autres biens dans l'historique")
        except Exception as e:
            st.error("Error while saving the record")
            print("Error while saving the record {}".format(e))


main()

