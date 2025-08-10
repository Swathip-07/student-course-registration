from django.apps import AppConfig

class CourseinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courseinfo'

    def ready(self):
        from django.contrib.auth.models import User
        from django.db.utils import OperationalError, ProgrammingError
        try:
            if not User.objects.filter(username='admin').exists():
                User.objects.create_superuser(
                    username='admin',
                    email='admin@example.com',
                    password='admin123'
                )
        except (OperationalError, ProgrammingError):
            # Happens during first migrate or if DB is not ready
            pass
