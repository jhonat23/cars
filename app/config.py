import secrets
import data #file not updated in repository for security reasons

class Config():
    SECRET_KEY = secrets.token_hex(20)
    SQLALCHEMY_DATABASE_URI = f"mysql+mysqldb://admin:{data.PASSWORD}@{data.PUBLIC_IP_ADDRESS}/{data.DBNAME}?unix_socket=/cloudsql/{data.PROJECT_ID}:{data.INSTANCE_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True