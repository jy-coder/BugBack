import os
import firebase_admin
from firebase_admin import credentials
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, BasicAuthentication
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "bug-app-f83d2",
    "private_key_id": "31439f0658999802f2de9176b8c6694177f0924f",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDGpoAHVIbMlqqN\nXCyYomTI5cbBtwUMyNXQDs04O3lDujQIE021bW/+XyLqqqioVsLq5q5jKTKOaHyw\nuo8sFN4LIJXUIrpiK2nrTj77Xq0nbb77GSdnb4mUwCnLEmoG5NjOT+HT0JgwhE9m\n+8i+idzb1lGLmoK34qeqLhzo5H1cNC2KW2KZxj3ZU4bZMmaNSLsqHNi1AMMhsMKY\nSaO2LPLnbfwowscgtbGN2PwAFixjQEfng5pUVM8BRHrcyOAXKTQk3IV6I+uuLDtp\nnIm6OZYRPlipzRoOcMIykVk8hcjJjF0T6Naul6yrd1TRDmrUQg7ODUMyJsm4VdSC\n7Uiqq/fZAgMBAAECggEAUeGQdTUIqSzTWRgsw69wVoSr0+5CFR51T2DCg1K0bc/D\nIa7/QXC+EH4bcNnuUhENH/D84Z+6GIwGFXyYhiWFztVcHMhBxjQ54QVsHYXNXqq0\nZWDdZpvJfHhm4a8R6AyNNyEjJwFcsebfqcXP3YYK9MyW6THDftNco9+FCBQifg3D\nkXe0YmsS75cTcN5/z47eWO3nEjycoc9vUsG2hFTaeLlgSb9BJrrPBcp2g30UgV+Z\nSO0SESH67GunR4+hrqpjPNrbfDU4KwWk0UrsCsZM0FR1qwNhbWPhZ6MPzE/4KurH\ndi7104Z/xdfF5fdbT1BUuSEzEsOE02NxIb99BL+lBwKBgQDv+yT129SpXzSat9wE\nLjzsBvV/lTtmoW15n6xDSRFhLbe864IcD7Pb6FVElP7SuUrEy51M35BtZ9fD544Z\nVUERo8UHgUAWyLUWxyhjr+HNrJ2blN9IZnxTg47e9fSzcZ9bLQH2WaCTmIJy7V7H\nTA9NpN1HHyR3aSi2KbIgzsd8qwKBgQDT6RZio3ryXv0fj5+kfDf1GmKmG2tcqHtD\nTV/YqD+gGJ94NSFxfZn+2IJOaWdJYOlLjSSxWTotN7HtGeykoP5OeVubkUYoo9mn\nxjxRY9B34J+tXpw15zpld6Mrr6u2lPOpR9I9l7iXXNUDuU29zf904glqyWIlDwfG\ndtSemuPViwKBgQDOgGPblCC45g3UHOYcStVtnMdf08BbngkgIUAQXi2wW7DBxj4d\ne32fe5rz+uoT1hH6qeNfpPkYy8Sk9PoX3n6xeSUwQg4uDOOXCCU/MrexThoJKN/B\n4z6Udp5YSXkZeGpSALaxj4pXt2J5Frz57f81JuqqKqgsgLbhmZuIE6chJQKBgBaS\nnJzTNzR8I9Bp1yKJTNih/+Ibx5ruI3su0cfdXDGsjcgbOL3DGFVKMM8zcRoi5Zbz\nqPXvQEAyz5QnD8sVjyFC0hxHJEcN9RBnEGPHExzB46BvFIq1X8YRMWNk6hCf2zir\n+twuvi35aINmCL7wI4cK0N/8JaU27agZXlqquxwzAoGAVLD6J/68Mp6GvDXSJ+wW\nzMJhkGvTk5uc2WzMyHTp9hY0hUSgleeKgsAIvPCJvifkeQ7eT00WLTtA9H2W6wX8\ntkZOo0OhJl3GwDk2+KzvThm8/Cjvfs4NVrfsyCOesLYuwGFtLjGIgBUqUsgVuOaN\nLQkSt4K7Gono2mUm3JwbM2U=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-n1y5b@bug-app-f83d2.iam.gserviceaccount.com",
    "client_id": "115230172660692981715",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-n1y5b%40bug-app-f83d2.iam.gserviceaccount.com"
  })

default_app = firebase_admin.initialize_app(cred)




class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION")
        if not auth_header:
            raise NoAuthToken("No auth token provided")

        id_token = auth_header.split(" ").pop()
        decoded_token = None
        try:
            decoded_token = auth.verify_id_token(id_token)
        except Exception:
            raise InvalidAuthToken("Invalid auth token")

        if not id_token or not decoded_token:
            return None

        try:
            uid = decoded_token.get("uid")
        except Exception:
            raise FirebaseError()

        user, created = User.objects.get_or_create(username=uid)
        user.profile.last_activity = timezone.localtime()

        return (user, None)