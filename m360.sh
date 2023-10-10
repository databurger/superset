TAG=3.0.0 docker-compose -f docker-compose-non-dev.yml pull
TAG=3.0.0 docker-compose -f docker-compose-non-dev.yml up -d
docker cp superset-frontend/src/assets/images/favicon-32x32.png superset_app:/app/superset/static/assets/images/
docker cp superset-frontend/src/assets/images/savista_logo.png superset_app:/app/superset/static/assets/images/