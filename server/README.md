source venv/bin/activate

### SQL alchemy commands:

Get all elements of a model

```
from api import db
from models import Square
Square.query.all()
```

Delete an element of a models
```
square = Square.query.all()[0]
db.session.delete(square)
```

Filter on model
```
Square.query.filter_by(species=3).all()
```
