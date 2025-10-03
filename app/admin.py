"""
PANEL DE ADMINISTRACIÓN WEB
===========================

Este archivo configura Flask-Admin para proporcionar un panel de administración
visual y completo accesible desde el navegador.

CARACTERÍSTICAS:
- Interfaz web visual para todas las tablas
- Protegido con autenticación (solo usuarios admin)
- CRUD completo: Create, Read, Update, Delete
- Búsqueda y filtros automáticos
- Paginación incluida

ACCESO: http://localhost:5000/admin
REQUIERE: Usuario con is_admin=True

FECHA: 2 de octubre de 2025
PROYECTO: Tax Calculator Pro - IIVTNU Alfafar
"""

from flask import redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from app import db
from app.models import User, People, Property, Transaction, TaxCalculation


# ==============================================================================
# SEGURIDAD: Vistas Protegidas con Autenticación
# ==============================================================================

class SecureModelView(ModelView):
    """
    Vista base SEGURA para todos los modelos.
    
    CONCEPTO: Herencia en POO
    -----------
    Esta clase hereda de ModelView (la clase base de Flask-Admin) y añade
    funcionalidad de seguridad. Todas nuestras vistas heredarán de esta clase.
    
    ¿QUÉ HACE?
    - Verifica que el usuario esté autenticado
    - Verifica que el usuario sea administrador (is_admin=True)
    - Redirige a login si no cumple los requisitos
    
    ¿CÓMO FUNCIONA?
    Flask-Admin llama a estos métodos antes de mostrar cualquier vista:
    1. is_accessible() → ¿Puede este usuario acceder?
    2. inaccessible_callback() → ¿Qué hacer si NO puede acceder?
    """
    
    def is_accessible(self):
        """
        Determina si el usuario actual puede acceder a esta vista.
        
        EXPLICACIÓN LÍNEA POR LÍNEA:
        - current_user.is_authenticated → ¿El usuario ha iniciado sesión?
        - current_user.is_admin → ¿El usuario tiene el flag is_admin=True?
        - and → Ambas condiciones deben ser True
        
        RETORNA: True si puede acceder, False si no.
        """
        return current_user.is_authenticated and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        """
        Se ejecuta cuando un usuario NO autorizado intenta acceder.
        
        EXPLICACIÓN:
        - Si el usuario NO está autenticado → redirige a login
        - Si está autenticado pero NO es admin → redirige a home
        - request.url almacena la URL que intentaba acceder
        - next=request.url permite redirigir de vuelta después del login
        """
        if not current_user.is_authenticated:
            # Usuario no autenticado → enviar a login
            return redirect(url_for('login', next=request.url))
        else:
            # Usuario autenticado pero no admin → enviar a home
            return redirect(url_for('home'))


class SecureAdminIndexView(AdminIndexView):
    """
    Vista SEGURA para la página principal del panel de admin.
    
    CONCEPTO: Página de Inicio Personalizada
    ----------------------------------------
    La página principal (/admin) también necesita protección.
    Esta clase personaliza la página de inicio del panel de administración.
    """
    
    @expose('/')
    def index(self):
        """
        Página principal del panel de administración.
        
        El decorador @expose('/') indica que esta función responde a la ruta /admin
        """
        # Primero verifica si el usuario puede acceder
        if not self.is_accessible():
            return self.inaccessible_callback('index')
        
        # Si puede acceder, muestra la página de inicio
        return super(SecureAdminIndexView, self).index()
    
    def is_accessible(self):
        """Misma lógica de seguridad que SecureModelView"""
        return current_user.is_authenticated and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        """Misma lógica de redirección que SecureModelView"""
        if not current_user.is_authenticated:
            return redirect(url_for('login', next=request.url))
        else:
            return redirect(url_for('home'))


# ==============================================================================
# VISTAS PERSONALIZADAS PARA CADA MODELO
# ==============================================================================

class UserAdmin(SecureModelView):
    """
    Vista de administración para la tabla User.
    
    PERSONALIZACIÓN:
    - column_list: columnas que se muestran en la lista
    - column_searchable_list: columnas donde se puede buscar
    - column_filters: columnas que pueden filtrarse
    - column_exclude_list: columnas que NO se muestran (ej: password)
    - form_excluded_columns: columnas que NO aparecen en formularios
    """
    # Columnas visibles en la tabla principal
    column_list = ['id', 'username', 'is_admin', 'is_active', 'last_login', 
                   'login_count', 'created_at', 'updated_at']
    
    # Columnas donde se puede buscar texto
    column_searchable_list = ['username']
    
    # Filtros disponibles
    column_filters = ['is_admin', 'is_active', 'created_at']
    
    # NO mostrar el password (seguridad)
    column_exclude_list = ['password']
    form_excluded_columns = ['password']
    
    # Etiquetas en español
    column_labels = {
        'username': 'Usuario',
        'is_admin': 'Administrador',
        'is_active': 'Activo',
        'last_login': 'Último Login',
        'login_count': 'Número de Logins',
        'created_at': 'Fecha Creación',
        'updated_at': 'Última Actualización'
    }


class PeopleAdmin(SecureModelView):
    """Vista de administración para la tabla People (Personas)"""
    column_list = ['id', 'nif', 'name', 'surname', 'person_type', 
                   'notification_address', 'created_at']
    column_searchable_list = ['nif', 'name', 'surname']
    column_filters = ['person_type', 'created_at']
    
    column_labels = {
        'person_type': 'Tipo de Persona',
        'nif': 'NIF/CIF',
        'name': 'Nombre',
        'surname': 'Apellidos',
        'notification_address': 'Dirección de Notificación',
        'created_at': 'Fecha Creación',
        'updated_at': 'Última Actualización'
    }


class PropertyAdmin(SecureModelView):
    """Vista de administración para la tabla Property (Propiedades)"""
    column_list = ['id', 'cadastral_reference', 'address', 'town', 
                   'cadastral_value', 'created_at']
    column_searchable_list = ['cadastral_reference', 'address']
    column_filters = ['town', 'cadastral_value', 'created_at']
    
    column_labels = {
        'town': 'Municipio',
        'address': 'Dirección',
        'cadastral_reference': 'Referencia Catastral',
        'cadastral_value': 'Valor Catastral',
        'created_at': 'Fecha Creación',
        'updated_at': 'Última Actualización'
    }


class TransactionAdmin(SecureModelView):
    """Vista de administración para la tabla Transaction (Transacciones)"""
    column_list = ['id', 'transaction_type', 'transaction_date', 
                   'transaction_value', 'property_id', 'grantor_id', 'grantee_id']
    column_searchable_list = []
    column_filters = ['transaction_type', 'transaction_date', 'transaction_value']
    
    column_labels = {
        'transaction_type': 'Tipo de Transacción',
        'transaction_date': 'Fecha de Transacción',
        'transaction_value': 'Valor de Transacción',
        'property_id': 'ID Propiedad',
        'grantor_id': 'ID Vendedor',
        'grantee_id': 'ID Comprador',
        'decedent_id': 'ID Fallecido',
        'heir_id': 'ID Heredero'
    }


class TaxCalculationAdmin(SecureModelView):
    """Vista de administración para la tabla TaxCalculation (Cálculos Fiscales)"""
    column_list = ['id', 'transaction_id', 'taxable_base', 'gross_tax', 
                   'bonification', 'net_tax', 'tax_rate', 'created_at']
    column_searchable_list = []
    column_filters = ['tax_rate', 'created_at']
    
    column_labels = {
        'transaction_id': 'ID Transacción',
        'taxable_base': 'Base Imponible',
        'gross_tax': 'Cuota Íntegra',
        'bonification': 'Bonificación',
        'net_tax': 'Cuota Líquida',
        'tax_rate': 'Tipo de Gravamen',
        'coefficients': 'Coeficientes',
        'created_at': 'Fecha Creación',
        'updated_at': 'Última Actualización'
    }


# ==============================================================================
# FUNCIÓN DE INICIALIZACIÓN
# ==============================================================================

def init_admin(app):
    """
    Inicializa y configura Flask-Admin en la aplicación Flask.
    
    PARÁMETROS:
    - app: La instancia de Flask (tu aplicación)
    
    ¿QUÉ HACE?
    1. Crea el objeto Admin con configuración personalizada
    2. Registra todas las vistas de modelos
    3. Cada vista queda accesible en /admin
    
    RESULTADO:
    - /admin → Panel principal
    - /admin/user → Gestión de usuarios
    - /admin/people → Gestión de personas
    - /admin/property → Gestión de propiedades
    - /admin/transaction → Gestión de transacciones
    - /admin/taxcalculation → Gestión de cálculos fiscales
    """
    
    # Crear el objeto Admin
    admin = Admin(
        app,                                    # Tu aplicación Flask
        name='Tax Calculator Pro - Admin',     # Nombre que aparece en el panel
        template_mode='bootstrap4',            # Tema visual (Bootstrap 4)
        index_view=SecureAdminIndexView(),     # Vista de inicio personalizada (protegida)
        base_template='admin/custom_base.html' # Plantilla base personalizada (opcional)
    )
    
    # Registrar vistas para cada modelo
    # Sintaxis: admin.add_view(VistaPersonalizada(Modelo, Sesión, nombre='Nombre en menú'))
    
    admin.add_view(UserAdmin(User, db.session, name='Usuarios', endpoint='admin_users'))
    admin.add_view(PeopleAdmin(People, db.session, name='Personas', endpoint='admin_people'))
    admin.add_view(PropertyAdmin(Property, db.session, name='Propiedades', endpoint='admin_properties'))
    admin.add_view(TransactionAdmin(Transaction, db.session, name='Transacciones', endpoint='admin_transactions'))
    admin.add_view(TaxCalculationAdmin(TaxCalculation, db.session, name='Cálculos Fiscales', endpoint='admin_taxcalculations'))
    
    return admin

