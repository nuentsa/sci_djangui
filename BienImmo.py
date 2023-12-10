import json

class Bien:

    # Constructor from dictionary
    def __init__(self, input_dict):
        self.__dict__.update(input_dict)
    
    def ajouter_apport_personnel(self, nombre_de_parts, apport_par_part):
        self.nombre_de_parts = nombre_de_parts
        self.apport_par_part = apport_par_part
    # Mensualite d'un eventuel credit bancaire, y compris les assurances
    def ajouter_mensualite(self, mensualite):
        self.mensualite = mensualite
    # Enveloppe de financement, excluant des frais bancaires eventuels
    def enveloppe_financement(self):
        return self.prix_bien + self.travaux + self.mobilier + self.frais_notaires
    
    # Retourne la rentabilité nette, 
    # ne tient compte que de l'enveloppe de financement et du loyer annuel
    # et pas d'eventuels frais bancaires
    def rentabilite(self):
        enveloppe_globale = self.enveloppe_financement()
        if enveloppe_globale != 0:
            return round(self.loyer_mensuel * 12 * 100 / enveloppe_globale, 2)
        return 0.0
    
    # Save the immo details to a more concise dictionary for display
    def to_summary(self):
        return {
            "Localisation": self.addresse,
            "Prix Achat": self.enveloppe_financement(),
            "Charges annuelles": self.charges_copro + self.taxes_foncieres,
            "Loyer Annuel": self.loyer_mensuel * 12,
            "Superficie": self.superficie,
            "Rentabilite": self.rentabilite(),
            "Apport par part": self.apport_par_part,
            "Lien Annonce": self.url_annonce
        }
    def financement(self, apport_personnel, mensualite, assurance_mensuelle):
        self.apport_personnel = apport_personnel
        self.mensualite = mensualite
        self.assurance_mensuelle = assurance_mensuelle
    def to_dict(self):
        # Use Builtin method for now
        return self.__dict__