
# class LoginRequest(BaseModel):
#     email: str
#     password: str

# @router.post("/login", response_model=schemas.Token)
# async def login(request: schemas.LoginRequest, db: Session = Depends(get_db), firebase_auth: auth = Depends(get_firebase_auth)):
#     try:
#         decoded_token = firebase_auth.verify_id_token(request.token)
#         email = decoded_token["email"]
#         user = service.get_user_by_email(db, email)
#         if not user:
#             raise HTTPException(status_code=404, detail="User not found")
#         access_token = service.create_access_token(data={"sub": user.email})
#         return {"access_token": access_token, "token_type": "bearer"}
#     except auth.InvalidIdTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token")


# @router.post("/signup", response_model=schemas.User)
# async def signup(request: schemas.SignupRequest, db: Session = Depends(get_db), firebase_auth: auth = Depends(get_firebase_auth)):
#     try:
#         decoded_token = firebase_auth.verify_id_token(request.token)
#         email = decoded_token["email"]
#         user = service.get_user_by_email(db, email)
#         if user:
#             raise HTTPException(
#                 status_code=400, detail="Email already registered")
#         new_user = service.create_user(db, email, request.password)
#         return new_user
#     except auth.InvalidIdTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token")


#####################


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def create_user(db: Session, email: str, password: str):
#     new_user = models.User(email=email, password=password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user


# def create_access_token(data: dict):
#     # Use a JWT library to create and return an access token
#     # Example using PyJWT:
#     # import jwt
#     # access_token = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
#     # return access_token
#     pass
