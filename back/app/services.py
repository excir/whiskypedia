"""Services pour les opérations complexes sur les entités."""
from .repositories import WhiskyRepository, DistilleryRepository, NegociantRepository, TastingRepository

class WhiskyService:
    """Service pour les opérations complexes sur les whiskies."""

    @staticmethod
    def get_whisky_with_dependencies(whisky_id: str) -> dict:
        """Récupère un whisky avec ses dépendances (distillerie, négociant, dégustations).

        Args:
            whisky_id (str): L'ID du whisky.

        Returns:
            dict: Un dictionnaire contenant les informations du whisky et ses dépendances.
        """
        whisky = WhiskyRepository.get_by_id(whisky_id)
        if not whisky:
            return {'error': 'Whisky not found'}

        whisky_dict = whisky.to_dict()
        whisky_dict.pop('distillery_id', None)
        whisky_dict.pop('negociant_id', None)

        distillery = DistilleryRepository.get_by_id(whisky.distillery_id)
        if distillery:
            whisky_dict['distillery'] = distillery.to_dict()

        if whisky.negociant_id:
            negociant = NegociantRepository.get_by_id(whisky.negociant_id)
            if negociant:
                whisky_dict['negociant'] = negociant.to_dict()

        tastings = TastingRepository.get_all()
        whisky_dict['tastings'] = [tasting.to_dict() for tasting in tastings if tasting.whisky_id == whisky_id]

        return whisky_dict
