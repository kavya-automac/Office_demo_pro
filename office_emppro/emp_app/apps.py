from django.apps import AppConfig


class EmpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'emp_app'

#def ready(self):
#    import office_emppro.emp_app.signals