import os


class Config:

    # पुराने फाइल से डाला गया BOT_TOKEN
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8955666230:AAEWGCBuDv9y94OaV0RUMqNZjArN2LO1Ljc")

    # पुराने फाइल से डाला गया SESSION_NAME
    SESSION_NAME = os.environ.get("SESSION_NAME", "utube_bot")

    # पुराने फाइल से डाला गया API_ID
    API_ID = int(os.environ.get("API_ID", "33001782"))

    # पुराने फाइल से डाला गया API_HASH
    API_HASH = os.environ.get("API_HASH", "c2e205b6e5d630380bb83d4c69d5b977")

    # पुराने फाइल से डाला गया CLIENT_ID
    CLIENT_ID = os.environ.get("CLIENT_ID", "251281373720-ug7q7906b479msc6p5h4ffud69u97f2f.apps.googleusercontent.com")

    # पुराने फाइल से डाला गया CLIENT_SECRET
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET", "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")

    # पुराने फाइल से डाला गया BOT_OWNER
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "8783087041"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG", False))

    # पुराने फाइल से डाला गया UPLOAD_MODE
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE", "private") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
