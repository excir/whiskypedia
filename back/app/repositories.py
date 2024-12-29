"""Repositories pour les opérations CRUD sur les entités."""

from app import db
from .models import Distillery, Negociant, Whisky, Tasting, Library

class DistilleryRepository:
    """Repository pour les opérations CRUD sur les distilleries."""

    @staticmethod
    def get_all() -> list[Distillery]:
        """Récupère toutes les distilleries."""
        return Distillery.query.all()

    @staticmethod
    def get_by_id(distillery_id: int) -> Distillery:
        """Récupère une distillerie par son ID."""
        return Distillery.query.get(distillery_id)

    @staticmethod
    def add(distillery: Distillery) -> None:
        """Ajoute une nouvelle distillerie."""
        db.session.add(distillery)
        db.session.commit()

    @staticmethod
    def update() -> None:
        """Met à jour une distillerie existante."""
        db.session.commit()

    @staticmethod
    def delete(distillery: Distillery) -> None:
        """Supprime une distillerie."""
        db.session.delete(distillery)
        db.session.commit()

class NegociantRepository:
    """Repository pour les opérations CRUD sur les négociants."""

    @staticmethod
    def get_all() -> list[Negociant]:
        """Récupère tous les négociants."""
        return Negociant.query.all()

    @staticmethod
    def get_by_id(negociant_id: int) -> Negociant:
        """Récupère un négociant par son ID."""
        return Negociant.query.get(negociant_id)

    @staticmethod
    def add(negociant: Negociant) -> None:
        """Ajoute un nouveau négociant."""
        db.session.add(negociant)
        db.session.commit()

    @staticmethod
    def update() -> None:
        """Met à jour un négociant existant."""
        db.session.commit()

    @staticmethod
    def delete(negociant: Negociant) -> None:
        """Supprime un négociant."""
        db.session.delete(negociant)
        db.session.commit()

class WhiskyRepository:
    """Repository pour les opérations CRUD sur les whiskies."""

    @staticmethod
    def get_all() -> list[Whisky]:
        """Récupère tous les whiskies."""
        return Whisky.query.all()

    @staticmethod
    def get_by_id(whisky_id: int) -> Whisky:
        """Récupère un whisky par son ID."""
        return Whisky.query.get(whisky_id)

    @staticmethod
    def add(whisky: Whisky) -> None:
        """Ajoute un nouveau whisky."""
        db.session.add(whisky)
        db.session.commit()

    @staticmethod
    def update() -> None:
        """Met à jour un whisky existant."""
        db.session.commit()

    @staticmethod
    def delete(whisky: Whisky) -> None:
        """Supprime un whisky."""
        db.session.delete(whisky)
        db.session.commit()

class TastingRepository:
    """Repository pour les opérations CRUD sur les dégustations."""

    @staticmethod
    def get_all() -> list[Tasting]:
        """Récupère toutes les dégustations."""
        return Tasting.query.all()

    @staticmethod
    def get_by_id(tasting_id: int) -> Tasting:
        """Récupère une dégustation par son ID."""
        return Tasting.query.get(tasting_id)

    @staticmethod
    def add(tasting: Tasting) -> Tasting:
        """Ajoute une nouvelle dégustation."""
        db.session.add(tasting)
        db.session.commit()
        db.session.refresh(tasting)
        return tasting


    @staticmethod
    def update() -> None:
        """Met à jour une dégustation existante."""
        db.session.commit()

    @staticmethod
    def delete(tasting: Tasting) -> None:
        """Supprime une dégustation."""
        db.session.delete(tasting)
        db.session.commit()

class LibraryRepository:
    """Repository pour les opérations CRUD sur les bibliothèques de données."""

    @staticmethod
    def get_by_id(library_id: int) -> Library:
        """Récupère une bibliothèque par son ID."""
        return Library.query.get(library_id)
    
    @staticmethod
    def get_all() -> list[Library]:
        """Récupère toutes les bibliothèques."""
        return Library.query.all()

    @staticmethod
    def add(library: Library) -> Library:
        """Ajoute une nouvelle bibliothèque."""
        db.session.add(library)
        db.session.commit()
        db.session.refresh(library)
        return library


    @staticmethod
    def delete(library: Library) -> None:
        """Supprime une bibliothèque."""
        db.session.delete(library)
        db.session.commit()

    @staticmethod
    def update(library_id: str, data: dict) -> Library:
        """Met à jour une bibliothèque existante."""
        library = Library.query.get(library_id)
        if library:
            for key, value in data.items():
                setattr(library, key, value)
            db.session.commit()
            db.session.refresh(library)
        return library