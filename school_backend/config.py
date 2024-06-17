import os

class Config:
    """
    Essa classe é responsável por armazenar as configurações do banco de dados.
    
    SQLALCHEMY_DATABASE_URI é a URI do banco de dados, no caso, um banco de dados PostgreSQL, é ela que permite a conexão com o banco remoto
    SQLALCHEMY_TRACK_MODIFICATIONS é uma configuração que define se as modificações no banco de dados devem ser rastreadas

    OBS: a URI do banco de dados foi obtida no site do Supabase, que é um serviço de banco de dados PostgreSQL
    OBS: a URI do banco de dados contém o nome de usuário e a senha, que são necessários para acessar o banco de dados
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres.zpawzfahadpotbvyfnfh:postgres#123@aws-0-sa-east-1.pooler.supabase.com:6543/postgres''?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
