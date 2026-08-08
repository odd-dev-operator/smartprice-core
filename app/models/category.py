from enum import Enum


class Category(str, Enum):
    AUDIO = "audio"
    TELEVISIONS = "televisions"
    COMPUTING = "computing"
    MOBILE = "mobile"
    APPLIANCES = "appliances"
    PHOTOGRAPHY = "photography"
    GAMING = "gaming"
    HOME = "home"
    TOOLS = "tools"
    SPORTS = "sports"
    MISC = "misc"