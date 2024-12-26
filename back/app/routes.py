"""Routes de l'API pour les entités."""
from flask import Blueprint, jsonify, request
from .models import Whisky, Distillery, Tasting, Negociant
from .repositories import DistilleryRepository, NegociantRepository, WhiskyRepository, TastingRepository
from .services import WhiskyService

api = Blueprint('v1', __name__)

@api.route('/api/distilleries', methods=['GET'])
def get_distilleries():
    """Récupère toutes les distilleries."""
    distilleries = DistilleryRepository.get_all()
    distilleries_with_whiskies = []
    for distillery in distilleries:
        distillery_dict = distillery.to_dict()
        distillery_dict['whiskies'] = [whisky.to_dict() for whisky in distillery.whiskies]
        distilleries_with_whiskies.append(distillery_dict)
    return jsonify(distilleries_with_whiskies)

@api.route('/api/distilleries/<distillery_id>', methods=['GET'])
def get_distillery(distillery_id):
    """Récupère une distillerie par son ID."""
    distillery = DistilleryRepository.get_by_id(distillery_id)
    if distillery:
        distillery_dict = distillery.to_dict()
        distillery_dict['whiskies'] = [whisky.to_dict() for whisky in distillery.whiskies]
        return jsonify(distillery_dict)
    return jsonify({'error': 'Distillery not found'}), 404

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

# Similar routes for Negociant, Whisky, and Tasting can be created following the same pattern

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
    TastingRepository.add(tasting)
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
    negociants_with_whiskies = []
    for negociant in negociants:
        negociant_dict = negociant.to_dict()
        negociant_dict['whiskies'] = [whisky.to_dict() for whisky in negociant.whiskies]
        negociants_with_whiskies.append(negociant_dict)
    return jsonify(negociants_with_whiskies)

@api.route('/api/negociants/<negociant_id>', methods=['GET'])
def get_negociant(negociant_id):
    """Récupère un négociant par son ID."""
    negociant = NegociantRepository.get_by_id(negociant_id)
    if negociant:
        negociant_dict = negociant.to_dict()
        negociant_dict['whiskies'] = [whisky.to_dict() for whisky in negociant.whiskies]
        return jsonify(negociant_dict)
    return jsonify({'error': 'Negociant not found'}), 404

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
    print(data)
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
