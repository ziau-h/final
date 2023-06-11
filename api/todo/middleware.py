from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.conf import settings

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Rate limiting enabled and user is authenticated
        if settings.RATE_LIMIT_ENABLED and request.user.is_authenticated:
            cache_key = f'rate_limit:{request.user.id}:{request.META["REMOTE_ADDR"]}'
            request_count = cache.get(cache_key, 0)
            if request_count >= settings.RATE_LIMIT_REQUESTS:
                return HttpResponseForbidden("Rate limit exceeded. Try again later.")

            # Increment request count
            cache.incr(cache_key)
            cache.expire(cache_key, settings.RATE_LIMIT_DURATION)

        response = self.get_response(request)
        return response