from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_VERSION_PREFIX}/token")

TokenDep = Annotated[str, Depends(oauth2_scheme)]
