# TransBus Terminal Management System

## Descripción
Sistema de gestión de terminales de buses que permite controlar el acceso, asignación de andenes y cobro de derechos de loza para diversas empresas de transporte terrestre en Chile.

## Requisitos
- Python 3.8+
- Django 5.x
- PostgreSQL
- Bootstrap 5

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/ManuArteaga2/Certificaci-n.git
cd Certificaci-n

### 2. Crear y activar un entorno virtual
```bash
python -m venv env
source env/bin/activate  # Unix/Mac
env\Scripts\activate     # Windows

### 3. Instalar las Dependencias:
pip install -r requirements.txt

### Acceso al panel de administración de Django
- Usuario: adminterminal
- Contraseña: Passadmin123
Operador
- Usuario: belkis
- Contraseña: manuela0902

### 4. Para generar el dump en postgres
pg_dump -U terminal_user -d terminales_db -F c -b -v -f terminales_db