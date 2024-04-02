import json
from pylib.base.entity import Entity


class JsonUtil:
    @staticmethod
    def to_json(source:any) -> str:
        target = source
        if isinstance(source, list):
            elements = []
            for element in source:
                elements.append(JsonUtil.__to_json(element))
            target = elements
        else:
            target = JsonUtil.__to_json(source)
        return json.dumps(target, ensure_ascii=False)
    
    @staticmethod
    def __to_json(source:any):
        if isinstance(source, Entity):
            return source.to_dict()
        else:
            return source
