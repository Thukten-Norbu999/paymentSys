
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import logout


class DoubleRoleCheckerMiddleware():
    def __init__(self):
        pass

    def __call__(self, ):
        pass


class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = timezone.now()
            last_activity = request.session.get('last_activity')

            if last_activity:
                elapsed_time = (current_time - last_activity).total_seconds()
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    logout(request)

            request.session['last_activity'] = current_time

        response = self.get_response(request)
        return response