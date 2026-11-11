# Tool Store Catalogue

**A public product catalogue with permission-controlled administration.**

Built for a Web Programming II assignment, this application serves an HTML/CSS/JavaScript frontend from Django and exposes categories and tools through Django REST Framework. Visitors browse the catalogue; authenticated staff with model permissions manage records.

**Django · Django REST Framework · Token authentication · SQLite · JavaScript**

## Capabilities

| Workflow | Behavior |
| --- | --- |
| Browse | Public category/tool lists |
| Search and order | Search by name, brand, or category; order tools by supported fields |
| Authenticate | Exchange username/password for a DRF token |
| Manage records | Django add/change/delete permissions checked per action |
| Validate prices | Negative prices rejected; zero-priced items remain allowed |

This is a catalogue/CRUD demonstration, not a checkout or payment system.

## Run locally

```bash
git clone https://github.com/joaovitormessias/lojaDeFerramentas.git
cd lojaDeFerramentas/loja_backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`. Open http://127.0.0.1:8000 and sign in using your local account. Use `/admin/` to configure normal-user permissions; authentication alone does not grant write access.

## API and code review

- `GET /api/categorias/` and `GET /api/ferramentas/`: public reads.
- `POST /api-token-auth/`: obtain a token.
- Write requests use `Authorization: Token <token>` plus the required model permission.

| File | Responsibility |
| --- | --- |
| [models.py](loja_backend/estoque/models.py) | Category/tool relationship and stock fields |
| [serializers.py](loja_backend/estoque/serializers.py) | API fields, category label, and price validation |
| [permissions.py](loja_backend/estoque/permissions.py) | Per-action write authorization |
| [views.py](loja_backend/estoque/views.py) | Search, ordering, and CRUD |
| [app.js](loja_backend/frontend/static/js/app.js) | Authentication state and catalogue rendering |

## Verify

From `loja_backend/`:

```bash
python manage.py check
python manage.py test estoque
```

The price regression test passed during review. Manually verify anonymous reads, denied anonymous writes, role-specific writes, and a zero-price item. Browser interaction and production deployment were not validated.

## Limits

Development settings allow all hosts and use a development secret. Browser tokens are stored in localStorage, with no expiry/rotation workflow. Category deletion cascades to tools. API validation is not a database price constraint, so direct ORM/admin writes need separate policy. Add permission regression tests, stronger deployment configuration, and a measured browser demo before presenting it as a deployed product.

[Maintainer](https://github.com/joaovitormessias)
