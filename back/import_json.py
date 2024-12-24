import json
from datetime import datetime
from app import create_app, db
from app.models import Distillery, Negotiant, Whisky, Tasting

app = create_app()
app.app_context().push()

with open('data.json') as f:
    data = json.load(f)

for dist in data["distilleries"]:
    db.session.add(Distillery(**dist))

for neg in data["negotiants"]:
    db.session.add(Negotiant(**neg))

for whisky in data["whiskies"]:
    db.session.add(Whisky(**whisky))

for tasting in data["tastings"]:
    tasting["tasting_date"] = datetime.strptime(tasting["tasting_date"], "%Y-%m-%d").date()
    db.session.add(Tasting(**tasting))
    
db.session.commit()
