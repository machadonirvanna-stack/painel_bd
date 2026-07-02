from dataclasses import dataclass


@dataclass
class Config:

    DATABASE_URL = (
        "postgresql://postgres:YGQveroMXNLMLoPXsuMekkJHfQAPHqBq"
        "@shortline.proxy.rlwy.net:52249/railway"
    )

    PAGE_TITLE = "ATI Analytics"

    PAGE_ICON = "📊"

    LAYOUT = "wide"

    PRIMARY_COLOR = "#1E88E5"

    CACHE_MINUTES = 10