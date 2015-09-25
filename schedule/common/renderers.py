import json

from rest_framework.renderers import JSONRenderer


class SelectJSONRenderer(JSONRenderer):
    # renders a list of objects formatted for x-editable select
    format = 'select'

    def render(self, data, *args, **kwargs):
        data = json.loads(super(SelectJSONRenderer, self).render(data, *args, **kwargs))
        if data: 
            assert 'id' in data[0]
            assert 'name' in data[0]
            assert 'value' not in data[0]
            assert 'text' not in data[0]
            data = [{'value': x['id'], 'text': x['name']} for x in data]
        return json.dumps(data)