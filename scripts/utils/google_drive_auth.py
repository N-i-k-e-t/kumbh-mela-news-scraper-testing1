from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate_google_drive():
    """Authenticate and return Google Drive instance."""
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

# If running as a standalone script
def main():
    drive = authenticate_google_drive()
    print("✅ Google Drive authentication successful!")

if __name__ == "__main__":
    main()
