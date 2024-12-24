from app import db
from .models import Whisky, Distillery, Tasting, Negotiant
from flask import Blueprint, jsonify, request
from .repositories import DistilleryRepository, NegotiantRepository, WhiskyRepository, TastingRepository
from .services import WhiskyService

api = Blueprint('v1', __name__)

@api.route('/api/distilleries', methods=['GET'])
def get_distilleries():
    distilleries = DistilleryRepository.get_all()
    return jsonify([distillery.to_dict() for distillery in distilleries])

@api.route('/api/distilleries/<distillery_id>', methods=['GET'])
def get_distillery(distillery_id):
    distillery = DistilleryRepository.get_by_id(distillery_id)
    if distillery:
        return jsonify(distillery.to_dict())
    return jsonify({'error': 'Distillery not found'}), 404

@api.route('/api/distilleries', methods=['POST'])
def add_distillery():
    data = request.json
    distillery = Distillery(**data)
    DistilleryRepository.add(distillery)
    return jsonify(distillery.to_dict()), 201

@api.route('/api/distilleries/<distillery_id>', methods=['PUT'])
def update_distillery(distillery_id):
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
    distillery = DistilleryRepository.get_by_id(distillery_id)
    if distillery:
        DistilleryRepository.delete(distillery)
        return jsonify({'message': 'Distillery deleted'})
    return jsonify({'error': 'Distillery not found'}), 404

# Similar routes for Negotiant, Whisky, and Tasting can be created following the same pattern

@api.route('/api/whiskies', methods=['GET'])
def get_whiskies():
    whiskies = WhiskyRepository.get_all()
    return jsonify([WhiskyService.get_whisky_with_dependencies(whisky.id) for whisky in whiskies])

@api.route('/api/whiskies/<whisky_id>', methods=['GET'])
def get_whisky(whisky_id):
    whiskydict = WhiskyService.get_whisky_with_dependencies(whisky_id)
    if whiskydict:
        return jsonify(whiskydict)
    return jsonify({'error': 'Whisky not found'}), 404

@api.route('/api/whiskies', methods=['POST'])
def add_whisky():
    data = request.json
    whisky = Whisky(**data)
    WhiskyRepository.add(whisky)
    return jsonify(whisky.to_dict()), 201

@api.route('/api/whiskies/<whisky_id>', methods=['PUT'])
def update_whisky(whisky_id):
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
    whisky = WhiskyRepository.get_by_id(whisky_id)
    if whisky:
        WhiskyRepository.delete(whisky)
        return jsonify({'message': 'Whisky deleted'})
    return jsonify({'error': 'Whisky not found'}), 404

@api.route('/api/tastings', methods=['GET'])
def get_tastings():
    tastings = TastingRepository.get_all()
    return jsonify([tasting.to_dict() for tasting in tastings])

@api.route('/api/tastings/<tasting_id>', methods=['GET'])
def get_tasting(tasting_id):
    tasting = TastingRepository.get_by_id(tasting_id)
    if tasting:
        return jsonify(tasting.to_dict())
    return jsonify({'error': 'Tasting not found'}), 404

@api.route('/api/tastings', methods=['POST'])
def add_tasting():
    data = request.json
    tasting = Tasting(**data)
    TastingRepository.add(tasting)
    return jsonify(tasting.to_dict()), 201

@api.route('/api/tastings/<tasting_id>', methods=['PUT'])
def update_tasting(tasting_id):
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
    tasting = TastingRepository.get_by_id(tasting_id)
    if tasting:
        TastingRepository.delete(tasting)
        return jsonify({'message': 'Tasting deleted'})
    return jsonify({'error': 'Tasting not found'}), 404

@api.route('/api/negotiants', methods=['GET'])
def get_negotiants():
    negotiants = NegotiantRepository.get_all()
    return jsonify([negotiant.to_dict() for negotiant in negotiants])

@api.route('/api/negotiants/<negotiant_id>', methods=['GET'])
def get_negotiant(negotiant_id):
    negotiant = NegotiantRepository.get_by_id(negotiant_id)
    if negotiant:
        return jsonify(negotiant.to_dict())
    return jsonify({'error': 'Negotiant not found'}), 404

@api.route('/api/negotiants', methods=['POST'])
def add_negotiant():
    data = request.json
    negotiant = Negotiant(**data)
    NegotiantRepository.add(negotiant)
    return jsonify(negotiant.to_dict()), 201

@api.route('/api/negotiants/<negotiant_id>', methods=['PUT'])
def update_negotiant(negotiant_id):
    data = request.json
    negotiant = NegotiantRepository.get_by_id(negotiant_id)
    if negotiant:
        for key, value in data.items():
            setattr(negotiant, key, value)
        NegotiantRepository.update()
        return jsonify(negotiant.to_dict())
    return jsonify({'error': 'Negotiant not found'}), 404

@api.route('/api/negotiants/<negotiant_id>', methods=['DELETE'])
def delete_negotiant(negotiant_id):
    negotiant = NegotiantRepository.get_by_id(negotiant_id)
    if negotiant:
        NegotiantRepository.delete(negotiant)
        return jsonify({'message': 'Negotiant deleted'})
    return jsonify({'error': 'Negotiant not found'}), 404