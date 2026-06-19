SECRET_KEY=${secret_key}

AUTH0_CLIENT_ID=${auth0_client_id}
AUTH0_CLIENT_SECRET=${auth0_client_secret}

AUTH0_DOMAIN=${auth0_domain}
AUTH0_AUDIENCE=${auth0_audience}

AUTH0_M2M_CLIENT_ID=${auth0_m2m_client_id}
AUTH0_M2M_CLIENT_SECRET=${auth0_m2m_client_secret}
AUTH0_MANAGEMENT_API_AUDIENCE=${auth0_management_api_audience}

AUTH0_CALLBACK_URL=${alb_dns_name}/callback
APP_BASE_URL=${alb_dns_name}
ALLOWED_HOSTS=localhost,127.0.0.1,${alb_dns_name},${instance_private_ip}

DEBUG=False
DB_HOST=db