jsonschema-pyref
================

This package adds support to
[jsonschema](https://pypi.org/project/jsonschema/)'s `RefResolver` for
resolving schema `$ref`s with two new custom URL schemes:

* `py-obj`: URLs with this scheme allow loading a schema from a dict in a
  Python module/class/etc.  This uses dotted attribute notation for the path
  to the schema.  For example `py-obj:package.submodule.Class.schema`
  resolves to a `schema` class attribute in the class `Class` in the module
  `package.submodule`.

* `py-pkgdata`: URLs with this scheme allow loading a schema from a file
  (currently only JSON and YAML are supported) in the package data installed
  with a Python package.  For example
  `py-pkgdata:package.subpackage/schema.json` loads the schema from the file
  `schema.json` under `package/subpackage` from wherever the package is
  installed.

Many JSON Schemas have an
[$id](https://json-schema.org/understanding-json-schema/basics.html#declaring-a-unique-identifier)
property declaring the unique identity of the schema.  Typically this is an
http(s) URL, but there is nothing *requiring* it to be.  Often this is just
used for namespacing, and the supplied URL does technically require to
exist.

In practice, if your Python package ships with a number of schemas used by
the package, and you would like to reference those schemas either from
another package, or relative to other schemas in the same package, the use
of the http scheme for schema `$id`s doesn't help with this.  It is
necessary to provide some kind of mapping between the URLs in the schema
`$id`s, and their actual location in the Python package.

The use of these custom URL schemes makes it implicit that this schema's
home is in a Python package or module (in the case of schemas declared
directly in Python code) and that it is not located on a network resource.

This gives an alternative way to declare the `$id`s of and `$ref` schemas
installed alongside Python code.


Examples
--------

```python
>>> import jsonschema
>>> from jsonschema_pyref import RefResolver
>>> schema = {
...     'properties': {
...         'a': {'$ref': 'py-obj:jsonschema_pyref.examples.schema1'},
...         'b': {'$ref': 'py-pkgdata:jsonschema_pyref.examples/schema1.json'},
...         'c': {'$ref': 'py-pkgdata:jsonschema_pyref.examples/schema2.yml'}
...      }
... }
>>> resolver = RefResolver.from_schema(schema)
>>> doc = {'a': 'hello', 'b': 'world', 'c': 123}
>>> jsonschema.validate(doc, schema, resolver=resolver) is None
True

```

As a convenience, `jsonschema_pyref.validate` is also provided as a drop-in
replacement for `jsonschema.validate` which uses the custom `RefResolver` by
default:

```python
>>> from jsonschema_pyref import validate
>>> validate(doc, schema) is None
True

```

Let's have a look at what's in the referenced schemas to see exactly
what we're validating the document against:

```python
>>> from pkgutil import get_data
>>> import jsonschema_pyref.examples
>>> jsonschema_pyref.examples.schema1
{'type': 'string'}
>>> def show_file(filename):
...     data = get_data('jsonschema_pyref.examples', filename)
...     print(data.decode('ascii').strip())
...
>>> show_file('schema1.json')
{"type": "string"}
>>> show_file('schema2.yml')
type: integer

```

These example schemas may be trivial, but you can easily confirm that this
would work all the same with a more complex schema.

Just to prove that the correct schemas are actually being loaded (and the
document is not just being trivially validated) we can also try some
counter-examples:

```python
>>> doc1 = dict(doc, a=123)
>>> jsonschema.validate(doc1, schema, resolver=resolver)
Traceback (most recent call last):
...
jsonschema.exceptions.ValidationError: 123 is not of type 'string'
...
Failed validating 'type' in schema['properties']['a']:
    {'type': 'string'}
...
On instance['a']:
    123

```

```python
>>> doc2 = dict(doc, b=123)
>>> jsonschema.validate(doc2, schema, resolver=resolver)
Traceback (most recent call last):
...
jsonschema.exceptions.ValidationError: 123 is not of type 'string'
...
Failed validating 'type' in schema['properties']['b']:
    {'type': 'string'}
...
On instance['b']:
    123

```

```python
>>> doc3 = dict(doc, c='hello')
>>> jsonschema.validate(doc3, schema, resolver=resolver)
Traceback (most recent call last):
...
jsonschema.exceptions.ValidationError: 'hello' is not of type 'integer'
...
Failed validating 'type' in schema['properties']['c']:
    {'type': 'integer'}
...
On instance['c']:
    'hello'

```

Here is a slightly more complex example demonstrating how relative refs
work with `py-pkgdata` URLs, as well as that fragments are correctly
resolved relative to each schema.

First we have `schema4.yml` which also contains an `$id` property, allowing
`jsonschema.RefResolver` to correctly determine the base URL against which
to resolve relative refs (in the case of `{"$ref": "schema3.json"}`):

```python
>>> show_file('schema4.yml')
$id: "py-pkgdata:jsonschema_pyref.examples/schema4.yml"
type: "object"
properties:
    foo: {"$ref": "schema3.json"}
    bar: {"$ref": "#/$defs/bar"}
additionalProperties: false
$defs:
    bar: {"type": "integer"}

```

And `schema3.json`:

```python
>>> show_file('schema3.json')
{
    "$id": "py-pkgdata:jsonschema_pyref.examples/schema3.json",
    "type": "object",
    "properties": {
        "foo": {"$ref": "#/$defs/foo"}
    },
    "additionalProperties": false,
    "$defs": {
        "foo": {"type": "string"}
    }
}

```

Here is a document that should validate against `schema4` which we'll
load also by `$ref`:

```python
>>> doc = {
...     'foo': {'foo': 'hello'},
...     'bar': 123
... }
...
>>> schema = {'$ref': 'py-pkgdata:jsonschema_pyref.examples/schema4.yml'}
>>> resolver = RefResolver.from_schema(schema)
>>> jsonschema.validate(doc, schema, resolver=resolver) is None
True

```

And again a couple counter-examples:

```python
>>> doc1 = dict(doc, foo={'foo': 123})
>>> jsonschema.validate(doc1, schema, resolver=resolver)
Traceback (most recent call last):
...
jsonschema.exceptions.ValidationError: 123 is not of type 'string'
...
Failed validating 'type' in schema['properties']['foo']['properties']['foo']:
    {'type': 'string'}
...
On instance['foo']['foo']:
    123
```

```python
>>> doc2 = dict(doc, bar='bar')
>>> jsonschema.validate(doc2, schema, resolver=resolver)
Traceback (most recent call last):
...
jsonschema.exceptions.ValidationError: 'bar' is not of type 'integer'
...
Failed validating 'type' in schema['properties']['bar']:
    {'type': 'integer'}
...
On instance['bar']:
    'bar'

```

API Documentation
-----------------

https://jsonschema-pyref.readthedocs.io/en/latest/api.html
