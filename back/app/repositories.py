from app import db
from .models import Distillery, Negotiant, Whisky, Tasting

class DistilleryRepository:
    @staticmethod
    def get_all() -> list[Distillery]:
        return Distillery.query.all()

    @staticmethod
    def get_by_id(distillery_id: int) -> Distillery:
        return Distillery.query.get(distillery_id)

    @staticmethod
    def add(distillery: Distillery) -> None:
        db.session.add(distillery)
        db.session.commit()

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(distillery: Distillery) -> None:
        db.session.delete(distillery)
        db.session.commit()

class NegotiantRepository:
    @staticmethod
    def get_all() -> list[Negotiant]:
        return Negotiant.query.all()

    @staticmethod
    def get_by_id(negotiant_id: int) -> Negotiant:
        return Negotiant.query.get(negotiant_id)

    @staticmethod
    def add(negotiant: Negotiant) -> None:
        db.session.add(negotiant)
        db.session.commit()

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(negotiant: Negotiant) -> None:
        db.session.delete(negotiant)
        db.session.commit()

class WhiskyRepository:
    @staticmethod
    def get_all() -> list[Whisky]:
        return Whisky.query.all()

    @staticmethod
    def get_by_id(whisky_id: int) -> Whisky:
        return Whisky.query.get(whisky_id)

    @staticmethod
    def add(whisky: Whisky) -> None:
        db.session.add(whisky)
        db.session.commit()

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(whisky: Whisky) -> None:
        db.session.delete(whisky)
        db.session.commit()

class TastingRepository:
    @staticmethod
    def get_all() -> list[Tasting]:
        return Tasting.query.all()

    @staticmethod
    def get_by_id(tasting_id: int) -> Tasting:
        return Tasting.query.get(tasting_id)

    @staticmethod
    def add(tasting: Tasting) -> None:
        db.session.add(tasting)
        db.session.commit()

    @staticmethod
    def update() -> None:
        db.session.commit()

    @staticmethod
    def delete(tasting: Tasting) -> None:
        db.session.delete(tasting)
        db.session.commit()
