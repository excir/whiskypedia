"""Services pour les opérations complexes sur les entités."""
from .repositories import WhiskyRepository, DistilleryRepository, NegociantRepository, TastingRepository, LibraryRepository

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
            whisky_dict['distillery'] = DistilleryService.get_distillery_with_dependencies(distillery.id)

        if whisky.negociant_id:
            negociant = NegociantRepository.get_by_id(whisky.negociant_id)
            if negociant:
                whisky_dict['negociant'] = NegociantService.get_negociant_with_dependencies(negociant.id)
                
        if whisky.whisky_type_id:
            whisky_type = LibraryRepository.get_by_id(whisky.whisky_type_id)
            if whisky_type:
                whisky_dict['whisky_type'] = whisky_type.to_dict()

        tastings = TastingRepository.get_all()
        whisky_dict['tastings'] = [tasting.to_dict() for tasting in tastings if tasting.whisky_id == whisky_id]

        return whisky_dict

class DistilleryService:
    """Service pour les opérations complexes sur les distilleries."""

    @staticmethod
    def get_distillery_with_dependencies(distillery_id: str) -> dict:
        """Récupère une distillerie avec ses dépendances (whiskies).

        Args:
            distillery_id (str): L'ID de la distillerie.

        Returns:
            dict: Un dictionnaire contenant les informations de la distillerie et ses dépendances.
        """
        distillery = DistilleryRepository.get_by_id(distillery_id)
        if not distillery:
            return {'error': 'Distillery not found'}

        distillery_dict = distillery.to_dict()
        distillery_dict['whiskies'] = [whisky.to_dict() for whisky in distillery.whiskies]

        if distillery.country_id:
            country = LibraryRepository.get_by_id(distillery.country_id)
            if country:
                distillery_dict['country'] = country.to_dict()

        return distillery_dict

class NegociantService:
    """Service pour les opérations complexes sur les négociants."""

    @staticmethod
    def get_negociant_with_dependencies(negociant_id: str) -> dict:
        """Récupère un négociant avec ses dépendances (whiskies).

        Args:
            negociant_id (str): L'ID du négociant.

        Returns:
            dict: Un dictionnaire contenant les informations du négociant et ses dépendances.
        """
        negociant = NegociantRepository.get_by_id(negociant_id)
        if not negociant:
            return {'error': 'Negociant not found'}

        negociant_dict = negociant.to_dict()
        negociant_dict['whiskies'] = [whisky.to_dict() for whisky in negociant.whiskies]

        if negociant.country_id:
            country = LibraryRepository.get_by_id(negociant.country_id)
            if country:
                negociant_dict['country'] = country.to_dict()

        return negociant_dict
