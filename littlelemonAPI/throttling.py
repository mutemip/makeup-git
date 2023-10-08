from rest_framework.throttling import UserRateThrottle

# a custome throttle policy named 'scope'
class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'