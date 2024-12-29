"""Services pour les opérations complexes sur les entités."""
import io
import os
import zipfile
import json
from flask import send_file, current_app as app
from .models import Whisky, Distillery, Negociant, Tasting, Library
from .repositories import WhiskyRepository, DistilleryRepository, NegociantRepository, TastingRepository, LibraryRepository

UPLOAD_FOLDER = 'images'

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

class BackupService:
    """Service pour les opérations de sauvegarde et de réimport des données."""

    @staticmethod
    def create_backup():
        """Crée une sauvegarde des données et des images dans un fichier zip."""
        data = {
            'whiskies': [whisky.to_dict() for whisky in WhiskyRepository.get_all()],
            'distilleries': [distillery.to_dict() for distillery in DistilleryRepository.get_all()],
            'negociants': [negociant.to_dict() for negociant in NegociantRepository.get_all()],
            'tastings': [tasting.to_dict() for tasting in TastingRepository.get_all()],
            'libraries': [library.to_dict() for library in LibraryRepository.get_all()]
        }

        memory_file = io.BytesIO()
        with zipfile.ZipFile(memory_file, 'w') as zf:
            zf.writestr('data.json', json.dumps(data))
            for whisky in data['whiskies']:
                if whisky.get('photo'):
                    zf.write(os.path.join(app.root_path, "..", UPLOAD_FOLDER, whisky['photo']), whisky['photo'])
        memory_file.seek(0)
        return send_file(memory_file, download_name='backup.zip', as_attachment=True)

    @staticmethod
    def restore_backup(file):
        """Restaure les données et les images à partir d'un fichier zip."""
        with zipfile.ZipFile(file, 'r') as zf:
            data = json.loads(zf.read('data.json'))
            for whisky in data['whiskies']:
                existing_whisky = WhiskyRepository.get_by_id(whisky['id'])
                if existing_whisky:
                    for key, value in whisky.items():
                        setattr(existing_whisky, key, value)
                    WhiskyRepository.update()
                else:
                    WhiskyRepository.add(Whisky(**whisky))
            for distillery in data['distilleries']:
                existing_distillery = DistilleryRepository.get_by_id(distillery['id'])
                if existing_distillery:
                    for key, value in distillery.items():
                        setattr(existing_distillery, key, value)
                    DistilleryRepository.update()
                else:
                    DistilleryRepository.add(Distillery(**distillery))
            for negociant in data['negociants']:
                existing_negociant = NegociantRepository.get_by_id(negociant['id'])
                if existing_negociant:
                    for key, value in negociant.items():
                        setattr(existing_negociant, key, value)
                    NegociantRepository.update()
                else:
                    NegociantRepository.add(Negociant(**negociant))
            for tasting in data['tastings']:
                existing_tasting = TastingRepository.get_by_id(tasting['id'])
                if existing_tasting:
                    for key, value in tasting.items():
                        setattr(existing_tasting, key, value)
                    TastingRepository.update()
                else:
                    TastingRepository.add(Tasting(**tasting))
            for library in data['libraries']:
                existing_library = LibraryRepository.get_by_id(library['id'])
                if existing_library:
                    for key, value in library.items():
                        setattr(existing_library, key, value)
                    LibraryRepository.update(existing_library.id, library)
                else:
                    LibraryRepository.add(Library(**library))
            for file_name in zf.namelist():
                if file_name != 'data.json':
                    zf.extract(file_name, UPLOAD_FOLDER)
