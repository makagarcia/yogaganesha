from apps.core.models import BusinessSettings


def business_settings(request):
    """Context processor para hacer BusinessSettings disponible en todos los templates"""
    return {
        'settings': BusinessSettings.load()
    }
