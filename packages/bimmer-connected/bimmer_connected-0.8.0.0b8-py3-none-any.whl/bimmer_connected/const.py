"""URLs for different services and error code mapping."""

AUTH_URL = 'https://{gcdm_oauth_endpoint}/oauth/authenticate'
TOKEN_URL = 'https://{gcdm_oauth_endpoint}/oauth/token'
BASE_URL = 'https://{server}'
OAUTH_CONFIG_URL = BASE_URL + '/eadrax-ucs/v1/presentation/oauth/config'

VEHICLES_URL = BASE_URL + '/eadrax-vcs/v1/vehicles'

REMOTE_SERVICE_BASE_URL = BASE_URL + '/eadrax-vrccs/v2/presentation/remote-commands'
REMOTE_SERVICE_URL = REMOTE_SERVICE_BASE_URL + '/{vin}/{service_type}'
REMOTE_SERVICE_STATUS_URL = REMOTE_SERVICE_BASE_URL + '/eventStatus?eventId={event_id}'

VEHICLE_IMAGE_URL = BASE_URL + "/eadrax-ics/v3/presentation/vehicles/{vin}/images?carView={view}"
VEHICLE_POI_URL = BASE_URL + '/eadrax-dcs/v1/send-to-car/send-to-car'

VEHICLE_CHARGING_STATISTICS_URL = BASE_URL + '/eadrax-chs/v1/charging-statistics'
VEHICLE_CHARGING_SESSIONS_URL = BASE_URL + '/eadrax-chs/v1/charging-sessions'

SERVICE_PROPERTIES = 'properties'
SERVICE_STATUS = 'status'
SERVICE_CHARGING_STATISTICS_URL = 'CHARGING_STATISTICS'
SERVICE_CHARGING_SESSIONS_URL = 'CHARGING_SESSIONS'
SERVICE_CHARGING_PROFILE = 'CHARGING_PROFILE'

# Possible error codes, other codes are mapped to UNKNOWN_ERROR
ERROR_CODE_MAPPING = {
    401: 'UNAUTHORIZED',
    404: 'NOT_FOUND',
    405: 'MOBILE_ACCESS_DISABLED',
    408: 'VEHICLE_UNAVAILABLE',
    423: 'ACCOUNT_LOCKED',
    429: 'TOO_MANY_REQUESTS',
    500: 'SERVER_ERROR',
    503: 'SERVICE_MAINTENANCE',
}
