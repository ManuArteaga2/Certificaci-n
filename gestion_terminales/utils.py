from django.contrib.auth.models import User

def es_administrador(user):
    return user.groups.filter(name='Administrador').exists()
