from resources.lib.utils.kodiutils import get_settings, show_settings, set_settings, get_setting_as_bool


class Settings:
    def __setitem__(self, key, value):
        set_settings(key, value)

    def __getitem__(self, key):
        return get_settings(key)

    @staticmethod
    def as_bool(key):
        return get_setting_as_bool(key)

    @staticmethod
    def show():
        show_settings()


settings = Settings()
