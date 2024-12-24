class DictExtension:
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if value is not None and not key.startswith('_')}