"""Script pour importer des données JSON dans la base de données."""
import json
from datetime import datetime
from app import create_app, db
from app.models import Distillery, Negociant, Whisky, Tasting

app = create_app()
app.app_context().push()

with open('data.json', encoding='UTF-8') as f:
    data = json.load(f)

# for dist in data["distilleries"]:
#     db.session.add(Distillery(**dist))

for neg in data["negociants"]:
    db.session.add(Negociant(**neg))

# for whisky in data["whiskies"]:
#     db.session.add(Whisky(**whisky))

# for tasting in data["tastings"]:
#     tasting["tasting_date"] = datetime.strptime(tasting["tasting_date"], "%Y-%m-%d").date()
#     db.session.add(Tasting(**tasting))

db.session.commit()
