"""OAuth 2.0 credential management for Google Drive API."""

import os
import pickle
from pathlib import Path

from dotenv import load_dotenv
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

load_dotenv()

TOKEN_PICKLE = Path(__file__).parent / "token.pickle"
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
TOKEN_URI = "https://oauth2.googleapis.com/token"


def get_credentials() -> Credentials:
    """Build and return a Google OAuth2 Credentials object that auto-refreshes."""
    token_path = TOKEN_PICKLE
    creds = None

    if token_path.exists():
        with open(token_path, "rb") as f:
            creds = pickle.load(f)

    if creds and creds.valid:
        return creds

    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        client_id = os.getenv("CLIENT_ID")
        client_secret = os.getenv("CLIENT_SECRET")
        refresh_token = os.getenv("REFRESH_TOKEN")

        if not all([client_id, client_secret, refresh_token]):
            raise EnvironmentError(
                "Missing credentials. Set CLIENT_ID, CLIENT_SECRET, and "
                "REFRESH_TOKEN as environment variables or in a .env file."
            )

        creds = Credentials(
            token=None,
            refresh_token=refresh_token,
            token_uri=TOKEN_URI,
            client_id=client_id,
            client_secret=client_secret,
            scopes=SCOPES,
        )
        creds.refresh(Request())

    with open(token_path, "wb") as f:
        pickle.dump(creds, f)

    return creds
