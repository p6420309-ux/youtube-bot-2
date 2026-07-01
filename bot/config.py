import os

class Config:
    # यहाँ अपना Telegram Bot Token डालें (जैसे: "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")
    BOT_TOKEN = "8955666230:AAEWGCBuDv9y94OaV0RUMqNZjArN2LO1Ljc"

    SESSION_NAME = "utube_bot"

    # API_ID नंबर होता है, इसलिए इसमें "" नहीं लगेगा
    API_ID = 33001782

    # API_HASH टेक्स्ट है, इसलिए यह "" के अंदर रहेगा
    API_HASH = "c2e205b6e5d630380bb83d4c69d5b977"

    CLIENT_ID = "251281373720-ug7q7906b479msc6p5h4ffud69u97f2f.apps.googleusercontent.com"

    CLIENT_SECRET = "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"

    # BOT_OWNER नंबर है, इसलिए "" नहीं लगेगा
    BOT_OWNER = 8783087041

    AUTH_USERS_TEXT = ""

    AUTH_USERS = [BOT_OWNER, 374321319] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = ""
    VIDEO_CATEGORY = 0
    VIDEO_TITLE_PREFIX = ""
    VIDEO_TITLE_SUFFIX = ""
    DEBUG = False

    UPLOAD_MODE = "private" 

    CRED_FILE = "auth_token.txt"
