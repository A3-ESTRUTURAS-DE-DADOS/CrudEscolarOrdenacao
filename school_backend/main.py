import os
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(
        port=os.getenv('PORT', 5000),
        host=os.getenv('IP', 'localhost'),
        debug=True
    )

'''
- Fazer o front da tabela
- Fazer as rotas http (controller)
- Fazer as rotas para puxar da api
- Fazer as tabelas pelo flask (models)
- Angular (views)
'''