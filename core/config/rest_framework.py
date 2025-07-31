
REST_FRAMEWORK_APPS = [
    'rest_framework',
    # social django
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
]

REST_FRAMEWORK = {
    # 1. AUTENTICACIÓN: Le indicas a DRF que use JWT por defecto.
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    # 2. PERMISOS: Aquí defines los permisos por defecto para tus vistas.
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    #     # 'rest_framework.permissions.AllowAny', # Si necesitas permitir el acceso a todos
    # ),
}
