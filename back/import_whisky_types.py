"""Script pour importer des types de whisky dans la base de données."""
from app import create_app, db
from app.models import Library

app = create_app()
app.app_context().push()

whisky_types = [
    'Single Malt Whisky',
    'Single Grain Whisky',
    'Blended Whisky',
    'Blended Malt Whisky',
    'Bourbon',
    'Rye Whisky',
    'Tennessee Whisky',
    'Irish Whiskey',
    'Scotch Whisky',
    'Japanese Whisky',
    'Canadian Whisky',
    'Corn Whisky',
]

for whisky_type in whisky_types:
    library_entry = Library(name="whisky_types", data=whisky_type)
    db.session.add(library_entry)

db.session.commit()