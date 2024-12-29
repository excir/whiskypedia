"""Routes de l'API pour les entités."""
from flask import Blueprint, jsonify, request, send_file
from datetime import datetime
from .models import Whisky, Distillery, Tasting, Negociant, Library
from .repositories import DistilleryRepository, NegociantRepository, WhiskyRepository, TastingRepository, LibraryRepository
from .services import WhiskyService, DistilleryService, NegociantService
import os
from PIL import Image
from flask import current_app as app

api = Blueprint('v1', __name__)
UPLOAD_FOLDER = 'images'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@api.route('/api/distilleries', methods=['GET'])
def get_distilleries():
    """Récupère toutes les distilleries."""
    distilleries = DistilleryRepository.get_all()
    return jsonify([DistilleryService.get_distillery_with_dependencies(distillery.id) for distillery in distilleries])

@api.route('/api/distilleries/<distillery_id>', methods=['GET'])
def get_distillery(distillery_id):
    """Récupère une distillerie par son ID."""
    distillery_dict = DistilleryService.get_distillery_with_dependencies(distillery_id)
    if 'error' in distillery_dict:
        return jsonify(distillery_dict), 404
    return jsonify(distillery_dict)

@api.route('/api/distilleries', methods=['POST'])
def add_distillery():
    """Ajoute une nouvelle distillerie."""
    data = request.json
    distillery = Distillery(**data)
    DistilleryRepository.add(distillery)
    return jsonify(distillery.to_dict()), 201

@api.route('/api/distilleries/<distillery_id>', methods=['PUT'])
def update_distillery(distillery_id):
    """Met à jour une distillerie existante."""
    data = request.json
    distillery = DistilleryRepository.get_by_id(distillery_id)
    if distillery:
        for key, value in data.items():
            setattr(distillery, key, value)
        DistilleryRepository.update()
        return jsonify(distillery.to_dict())
    return jsonify({'error': 'Distillery not found'}), 404

@api.route('/api/distilleries/<distillery_id>', methods=['DELETE'])
def delete_distillery(distillery_id):
    """Supprime une distillerie par son ID."""
    distillery = DistilleryRepository.get_by_id(distillery_id)
    if distillery:
        DistilleryRepository.delete(distillery)
        return jsonify({'message': 'Distillery deleted'})
    return jsonify({'error': 'Distillery not found'}), 404

@api.route('/api/whiskies', methods=['GET'])
def get_whiskies():
    """Récupère tous les whiskies."""
    whiskies = WhiskyRepository.get_all()
    return jsonify([WhiskyService.get_whisky_with_dependencies(whisky.id) for whisky in whiskies])

@api.route('/api/whiskies/<whisky_id>', methods=['GET'])
def get_whisky(whisky_id):
    """Récupère un whisky par son ID."""
    whisky = WhiskyRepository.get_by_id(whisky_id)
    if whisky:
        return jsonify(whisky.to_dict())
    return jsonify({'error': 'Whisky not found'}), 404

@api.route('/api/whiskies/<whisky_id>/details', methods=['GET'])
def get_whisky_details(whisky_id):
    """Récupère les détails d'un whisky avec ses dépendances."""
    whiskydict = WhiskyService.get_whisky_with_dependencies(whisky_id)
    if whiskydict:
        return jsonify(whiskydict)
    return jsonify({'error': 'Whisky not found'}), 404

@api.route('/api/whiskies', methods=['POST'])
def add_whisky():
    """Ajoute un nouveau whisky."""
    data = request.json
    print(data)
    whisky = Whisky(**data)
    WhiskyRepository.add(whisky)
    return jsonify(whisky.to_dict()), 201

@api.route('/api/whiskies/<whisky_id>', methods=['PUT'])
def update_whisky(whisky_id):
    """Met à jour un whisky existant."""
    data = request.json
    whisky = WhiskyRepository.get_by_id(whisky_id)
    if whisky:
        for key, value in data.items():
            setattr(whisky, key, value)
        WhiskyRepository.update()
        return jsonify(whisky.to_dict())
    return jsonify({'error': 'Whisky not found'}), 404

@api.route('/api/whiskies/<whisky_id>', methods=['DELETE'])
def delete_whisky(whisky_id):
    """Supprime un whisky par son ID."""
    whisky = WhiskyRepository.get_by_id(whisky_id)
    if whisky:
        WhiskyRepository.delete(whisky)
        return jsonify({'message': 'Whisky deleted'})
    return jsonify({'error': 'Whisky not found'}), 404

@api.route('/api/tastings', methods=['GET'])
def get_tastings():
    """Récupère toutes les dégustations."""
    tastings = TastingRepository.get_all()
    return jsonify([tasting.to_dict() for tasting in tastings])

@api.route('/api/tastings/<tasting_id>', methods=['GET'])
def get_tasting(tasting_id):
    """Récupère une dégustation par son ID."""
    tasting = TastingRepository.get_by_id(tasting_id)
    if tasting:
        return jsonify(tasting.to_dict())
    return jsonify({'error': 'Tasting not found'}), 404

@api.route('/api/tastings', methods=['POST'])
def add_tasting():
    """Ajoute une nouvelle dégustation."""
    data = request.json
    tasting = Tasting(**data)
    tasting.tasting_date = datetime.strptime(tasting.tasting_date, "%Y-%m-%dT%H:%M:%S.%fZ")
    tasting = TastingRepository.add(tasting)
    return jsonify(tasting.to_dict()), 201

@api.route('/api/tastings/<tasting_id>', methods=['PUT'])
def update_tasting(tasting_id):
    """Met à jour une dégustation existante."""
    data = request.json
    tasting = TastingRepository.get_by_id(tasting_id)
    if tasting:
        for key, value in data.items():
            setattr(tasting, key, value)
        TastingRepository.update()
        return jsonify(tasting.to_dict())
    return jsonify({'error': 'Tasting not found'}), 404

@api.route('/api/tastings/<tasting_id>', methods=['DELETE'])
def delete_tasting(tasting_id):
    """Supprime une dégustation par son ID."""
    tasting = TastingRepository.get_by_id(tasting_id)
    if tasting:
        TastingRepository.delete(tasting)
        return jsonify({'message': 'Tasting deleted'})
    return jsonify({'error': 'Tasting not found'}), 404

@api.route('/api/negociants', methods=['GET'])
def get_negociants():
    """Récupère tous les négociants."""
    negociants = NegociantRepository.get_all()
    return jsonify([NegociantService.get_negociant_with_dependencies(negociant.id) for negociant in negociants])

@api.route('/api/negociants/<negociant_id>', methods=['GET'])
def get_negociant(negociant_id):
    """Récupère un négociant par son ID."""
    negociant_dict = NegociantService.get_negociant_with_dependencies(negociant_id)
    if 'error' in negociant_dict:
        return jsonify(negociant_dict), 404
    return jsonify(negociant_dict)

@api.route('/api/negociants', methods=['POST'])
def add_negociant():
    """Ajoute un nouveau négociant."""
    data = request.json
    negociant = Negociant(**data)
    NegociantRepository.add(negociant)
    return jsonify(negociant.to_dict()), 201

@api.route('/api/negociants/<negociant_id>', methods=['PUT'])
def update_negociant(negociant_id):
    """Met à jour un négociant existant."""
    data = request.json
    negociant = NegociantRepository.get_by_id(negociant_id)
    if negociant:
        for key, value in data.items():
            setattr(negociant, key, value)
        NegociantRepository.update()
        return jsonify(negociant.to_dict())
    return jsonify({'error': 'Negociant not found'}), 404

@api.route('/api/negociants/<negociant_id>', methods=['DELETE'])
def delete_negociant(negociant_id):
    """Supprime un négociant par son ID."""
    negociant = NegociantRepository.get_by_id(negociant_id)
    if negociant:
        NegociantRepository.delete(negociant)
        return jsonify({'message': 'Negociant deleted'})
    return jsonify({'error': 'Negociant not found'}), 404


@api.route('/api/upload_image/<filename>', methods=['POST'])
def upload_image(filename):
    """Upload an image and save it to the images folder."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not file.filename.lower().endswith('.webp'):
        image = Image.open(file)
        filename = os.path.splitext(filename)[0] + '.webp'
        image.save(os.path.join(UPLOAD_FOLDER, filename), 'webp')
    else:
        file.save(os.path.join(UPLOAD_FOLDER, filename))
    
    return jsonify({'message': 'File uploaded successfully', 'filename' : filename}), 201

@api.route('/api/download_image/<filename>', methods=['GET'])
def download_image(filename):
    """Download an image from the images folder."""
    if filename.contains('..') or filename.contains('/'):
        return jsonify({'error': 'Invalid filename'}), 400
    file_path = os.path.join(app.root_path, "..", UPLOAD_FOLDER, filename)
    return send_file(file_path)

@api.route('/api/library', methods=['POST'])
def add_library():
    data = request.json
    library = Library(**data)
    LibraryRepository.add(library)
    return jsonify(library.to_dict()), 201

@api.route('/api/library', methods=['GET'])
def get_libraries():
    """Récupère toutes les bibliothèques."""
    libraries = LibraryRepository.get_all()
    return jsonify([library.to_dict() for library in libraries])

@api.route('/api/library/<library_id>', methods=['DELETE'])
def delete_library(library_id):
    """Supprime une bibliothèque par son ID."""
    library = LibraryRepository.get_by_id(library_id)
    if library:
        LibraryRepository.delete(library)
        return jsonify({'message': 'Library deleted'})
    return jsonify({'error': 'Library not found'}), 404

@api.route('/api/library/<library_id>', methods=['PUT'])
def update_library(library_id):
    """Met à jour une bibliothèque par son ID."""
    data = request.json
    library = LibraryRepository.update(library_id, data)
    if library:
        return jsonify(library.to_dict()), 200
    return jsonify({'error': 'Library not found'}), 404
