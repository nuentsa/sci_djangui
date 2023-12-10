
class Bien:
    def __init__(self, prix_bien, travaux, mobilier, frais_notaires, charges_copro, taxes_foncieres, superficie, loyer_mensuel, addresse, url_annonce):
        self.prix_bien = prix_bien
        self.travaux = travaux
        self.mobilier = mobilier
        self.frais_notaires = frais_notaires
        self.charges_copro = charges_copro
        self.taxes_foncieres = taxes_foncieres
        self.loyer_mensuel = loyer_mensuel
        self.superficie = superficie
        self.addresse = addresse
        self.url_annonce = url_annonce
    
    # Rajouter des frais bancaires eventuels
    def ajouter_frais_bancaires(self, frais_dossier, caution_credit):
        self.frais_dossier = frais_dossier
        self.caution_credit = caution_credit
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
    def to_dict_summary(self):
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
    def to_json_document():
        return