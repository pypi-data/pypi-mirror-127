import unittest
from .context import jacobsjsondoc
from jacobsjsondoc.reference import JsonAnchor, ReferenceDictionary
from jacobsjsondoc.document import create_document, DocReference, DocObject, Document
from jacobsjsondoc.loader import PrepopulatedLoader
from jacobsjsondoc.options import ParseOptions, RefResolutionMode
import json

SAMPLE_DOCUMENT = {
    "$id": "http://example.com/schema.json",
    "type": "object",
    "properties": {
        "foo": {
            "$ref": "#fooprop",
        },
        "bar": {
            "$id": "#barprop",
            "type": "integer",
        }
    },
    "objects": {
        "fooProperty": {
            "$id": "#fooprop",
            "type": "string",
        }
    }
}

class TestJsonReferenceObject(unittest.TestCase):

    def test_reference_from_uri(self):
        uri = "http://example.com/schema.json#/definition/food"
        ref = JsonAnchor.from_string(uri)
        self.assertEqual(ref.uri, "http://example.com/schema.json")

    def test_references_equal(self):
        uri = "http://example.com/schema.json#/definition/food"
        ref1 = JsonAnchor.from_string(uri)
        ref2 = JsonAnchor.from_string(uri)
        self.assertEqual(ref1, ref2)
        ref3 = ref1.copy()
        self.assertEqual(ref2, ref3)

    def test_reference_buildup(self):
        base_uri = "http://example.com/myschema.json"
        ref = JsonAnchor.from_string(base_uri)
        change_path_id = "/other/schema.json"
        ref.change_to(JsonAnchor.from_string(change_path_id))
        self.assertEqual(ref.uri, "http://example.com/other/schema.json")
        add_fragment_id = "#func"
        ref.change_to(JsonAnchor.from_string(add_fragment_id))
        ref_repr = repr(ref)
        self.assertEqual(ref_repr, "http://example.com/other/schema.json#func")
        ref2 = JsonAnchor.from_string(ref_repr)
        self.assertEqual(ref, ref2)

class TestReferenceDictionary(unittest.TestCase):

    def setUp(self):
        self.data1 = {
            "A": {
                "B": 1,
                "C": [2,3,4,5]
            },
            "D": False
        }

    def test_reference_lookup(self):
        source_uri = "example"
        rd = ReferenceDictionary()
        rd.put(source_uri, self.data1)
        ref = JsonAnchor.from_string(source_uri)
        node_out = rd[ref]
        self.assertEqual(self.data1, node_out)
        ref.change_to(JsonAnchor.from_string("#A/B"))
        rd[ref] = self.data1['A']['B']
        fragment_uri = "example#A/B"
        self.assertEqual(rd.get(fragment_uri), 1)

class TestNotAReference(unittest.TestCase):

    def setUp(self):
        data = """{
            "A": {
                "B": 1,
                "$ref": {"C":true}
            },
            "D": false,
            "E": {
                "$ref": "#/A"
            },
            "F": [
                "G",
                "H"
            ],
            "J" : { "$ref": "#/F/1" }
        }"""
        ppl = PrepopulatedLoader()
        ppl.prepopulate("data", data)
        self.doc = create_document(uri="data", loader=ppl)

    def test_dollar_ref_is_a_reference(self):
        self.assertIsInstance(self.doc["E"], DocReference)

    def test_object_with_property_that_isnt_a_reference(self):
        self.assertNotIsInstance(self.doc["A"], DocReference)
        self.assertIsInstance(self.doc["A"], DocObject)

    def test_not_a_reference(self):
        self.assertNotIsInstance(self.doc["A"]["$ref"], DocReference)
        self.assertIsInstance(self.doc["A"]["$ref"], DocObject)

    def test_array_index_reference(self):
        self.assertIsInstance(self.doc["J"], DocReference)
        self.assertEqual(self.doc["J"].resolve(), "H")
class TestIdTagging(unittest.TestCase):

    def setUp(self):
        self.data = SAMPLE_DOCUMENT
        ppl = PrepopulatedLoader()
        ppl.prepopulate(self.data["$id"], json.dumps(self.data))
        self.doc = create_document(uri=self.data["$id"], loader=ppl)
    
    def test_root_has_correct_id(self):
        self.assertEqual(self.doc._dollar_id.uri, self.data["$id"])

    def test_bar_has_correct_id(self):
        self.assertEqual(self.doc['properties']['bar']._dollar_id, "http://example.com/schema.json#barprop")

    def test_fooproperty_has_correct_id(self):
        self.assertEqual(self.doc['objects']['fooProperty']._dollar_id, "http://example.com/schema.json#fooprop")

    def test_dictionary_contents(self):
        self.assertEqual(len(self.doc._ref_dictionary), 3)

    def test_dictionary_has_barprop(self):
        barprop = self.doc._ref_dictionary.get("http://example.com/schema.json#barprop")
        self.assertEqual(barprop['$id'], "#barprop")
        self.assertEqual(barprop['type'], "integer")
    
DOUBLE_REFERENCE_DOC = """
{
    "definitions": {
        "item": {
            "type": "array",
            "additionalItems": false,
            "items": [
                { "$ref": "#/definitions/sub-item" },
                { "$ref": "#/definitions/sub-item" }
            ]
        },
        "sub-item": {
            "type": "object",
            "required": ["foo"]
        }
    },
    "type": "array",
    "additionalItems": false,
    "items": [
        { "$ref": "#/definitions/item" },
        { "$ref": "#/definitions/item" },
        { "$ref": "#/definitions/item" }
    ]
}
"""

class TestDoubleRef(unittest.TestCase):

    def setUp(self):
        self.data = DOUBLE_REFERENCE_DOC
        ppl = PrepopulatedLoader()
        ppl.prepopulate(1, self.data)
        self.doc = create_document(uri=1, loader=ppl)

    def test_is_a_reference(self):
        self.assertIsInstance(self.doc['items'][0], DocReference)
        resolved = self.doc['items'][0].resolve()
        self.assertEqual(resolved['type'], "array")
        self.assertIsInstance(resolved['items'], list)


ROOT_POINTER_REF = """
{
    "schema": {
        "properties": {
            "foo": {"$ref": "#"}
        },
        "additionalProperties": false
    }
}
"""

class TestRootPointerRef(unittest.TestCase):

    def setUp(self):
        self.data = ROOT_POINTER_REF
        ppl = PrepopulatedLoader()
        ppl.prepopulate(1, self.data)
        self.doc = create_document(uri=1, loader=ppl)

    def test_parses_root_pointer_ref(self):
        self.assertIsInstance(self.doc, Document)
        self.assertIn("schema", self.doc)
        self.assertIsInstance(self.doc["schema"]["properties"]["foo"], DocReference)

class TestIdTrouble(unittest.TestCase):

    def setUp(self):
        data_text = """
        "schema": {
            "definitions": {
                "id_in_enum": {
                    "enum": [
                        {
                          "id": "https://localhost:1234/my_identifier.json",
                          "type": "null"
                        }
                    ]
                },
                "real_id_in_schema": {
                    "id": "https://localhost:1234/my_identifier.json",
                    "type": "string"
                },
                "zzz_id_in_const": {
                    "const": {
                        "id": "https://localhost:1234/my_identifier.json",
                        "type": "null"
                    }
                }
            },
            "anyOf": [
                { "$ref": "#/schema/definitions/id_in_enum" },
                { "$ref": "https://localhost:1234/my_identifier.json" }
            ]
        }
        """
        ppl = PrepopulatedLoader()
        ppl.prepopulate(1, data_text)
        options = ParseOptions()
        options.ref_resolution_mode = RefResolutionMode.USE_REFERENCES_OBJECTS
        options.dollar_id_token = "id"
        self.doc = create_document(uri=1, loader=ppl, options=options)

    def test_ref_points_to_correct_id(self):
        first_anyof_ref = self.doc["schema"]["anyOf"][0]
        self.assertIsInstance(first_anyof_ref, DocReference)
        second_anyof_ref = self.doc["schema"]["anyOf"][1]
        self.assertIsInstance(second_anyof_ref, DocReference)

        first_resolved = first_anyof_ref.resolve()
        second_resolved = second_anyof_ref.resolve()


class TestBaseUriChange(unittest.TestCase):

    def setUp(self):
        data_text = """
        {
            "id": "http://localhost:1234/scope_change_defs2.json",
            "type" : "object",
            "properties": {
                "list": {"$ref": "#/definitions/baz/definitions/bar"}
            },
            "definitions": {
                "baz": {
                    "id": "baseUriChangeFolderInSubschema/",
                    "definitions": {
                        "bar": {
                            "type": "array",
                            "items": {"$ref": "folderInteger.json"}
                        }
                    }
                }
            }
        }
        """
        data_text_2 = """
        {
            "id": "http://localhost:1234/",
            "items": {
                "id": "baseUriChange/",
                "items": {"$ref": "folderInteger.json"}
            }
        }"""
        ppl = PrepopulatedLoader()
        ppl.prepopulate("1", data_text)
        ppl.prepopulate("2", data_text_2)
        options = ParseOptions()
        options.ref_resolution_mode = RefResolutionMode.USE_REFERENCES_OBJECTS
        options.dollar_id_token = "id"
        self.doc = create_document(uri="1", loader=ppl, options=options)
        self.doc2 = create_document(uri="2", loader=ppl, options=options)

    def test_types(self):
        self.assertIsInstance(self.doc["type"], str)
        self.assertIsInstance(self.doc["properties"]["list"], DocReference)
        self.assertIsInstance(self.doc["definitions"]["baz"]["definitions"]["bar"]["items"], DocReference)

        self.assertIsInstance(self.doc2["items"]["items"], DocReference)

    def test_dollar_ids(self):
        self.assertEqual(self.doc._dollar_id, "http://localhost:1234/scope_change_defs2.json")
        self.assertEqual(self.doc["definitions"]["baz"]["definitions"]._dollar_id, "http://localhost:1234/baseUriChangeFolderInSubschema/")

        self.assertEqual(self.doc2._dollar_id, "http://localhost:1234/")
        self.assertEqual(self.doc2["items"]["items"]._dollar_id, "http://localhost:1234/baseUriChange/")

    def test_list_reference_resolution(self):
        dereffed = self.doc["properties"]["list"].resolve()
        self.assertIsInstance(dereffed, DocObject)

    def test_items_reference_resolution(self):
        with self.assertRaises(KeyError) as context:
            # We don't really want to have to load the remote reference, so we'll just check that the
            # exception shows the correct URI to the remote.
            dereffed = self.doc["definitions"]["baz"]["definitions"]["bar"]["items"].resolve()
            self.assertIn("http://localhost:1234/baseUriChangeFolderInSubschema/folderInteger.json", str(context.exception))

    def test_doc2_items_resolution(self):
        with self.assertRaises(KeyError) as context:
            # We don't really want to have to load the remote reference, so we'll just check that the
            # exception shows the correct URI to the remote.
            dereffed = self.doc2["items"]["items"].resolve()
            self.assertIn("http://localhost:1234/baseUriChange/folderInteger.json", str(context.exception))
