"""Extension pour convertir un modèle en dictionnaire."""

class DictExtension:
    """Extension pour convertir un modèle en dictionnaire."""

    def to_dict(self):
        """Convertit l'objet en dictionnaire en excluant les attributs privés et les valeurs None.

        Returns:
            dict: Un dictionnaire représentant l'objet.
        """
        return {key: value for key, value in self.__dict__.items() if value is not None and not key.startswith('_')}
