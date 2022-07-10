from django.contrib.auth.models import User

def project_context(def):

    context = {
        'me' : User.objects.first(),

    }

    return context


