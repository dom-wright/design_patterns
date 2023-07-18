'''
Factory Method

Factory methods are used when the exact concrete implementation required for a task is not known until runtime. In the factory pattern, the required conditional if/else block to determine what is needed is delegated to a separate component to return the required implementation for use.

Examples: 
- An image processor, where the user can choose different filters on the base image.
- Incoming employee data from a db, where you must create objects of the correct type for each employee e.g. executive, manager, employee.

Example 1 - Choosing the right serializer based on the type requested.
Example 2 - Opening a document of the correct type based on user selection.
'''

import json
import xml.etree.ElementTree as et


# Example 1

class SerializerFactory:

    @staticmethod
    def get_serializer(self, song, format):
        if format == 'JSON':
            return JSONSerializer(song)
        elif format == 'XML':
            return XMLSerializer(song)
        else:
            raise ValueError(format)


class JSONSerializer:

    def __init__(self, song):
        self.song = song

    def serialize(self):
        song_info = {
            'id': self.song['song_id'],
            'title': self.song['title'],
            'artist': self.song['artist']
        }
        return json.dumps(song_info)


class XMLSerializer:

    def __init__(self, song):
        self.song = song

    def serialize(self):
        song_element = et.Element('song', attrib={'id': self.song['song_id']})
        title = et.SubElement(song_element, 'title')
        title.text = self.song['title']
        artist = et.SubElement(song_element, 'artist')
        artist.text = self.song['artist']
        return et.tostring(song_element, encoding='unicode')


song1 = {
    "song_id": "12621534",
    "title": "My Favourite Song",
    "artist": "The Magazines"
}


def song_client():
    factory = SerializerFactory()
    format = input("Enter the format you want for the serializer (JSON/XML): ")
    serializer = factory.get_serializer(song1, format)
    string = serializer.serialize()
    print(string)


if __name__ == '__main__':
    song_client()


# Example 2

class Document:
    def __init__(self, name):
        self.name = name

    def open(self):
        pass

    def save(self):
        pass


class TextDocument(Document):
    def open(self):
        print("Opening text document:", self.name)

    def save(self):
        print("Saving text document:", self.name)


class SpreadsheetDocument(Document):
    def open(self):
        print("Opening spreadsheet document:", self.name)

    def save(self):
        print("Saving spreadsheet document:", self.name)


class PresentationDocument(Document):
    def open(self):
        print("Opening presentation document:", self.name)

    def save(self):
        print("Saving presentation document:", self.name)


class DocumentFactory:
    @staticmethod
    def create_document(doc_type, name):
        if doc_type == "text":
            return TextDocument(name)
        elif doc_type == "spreadsheet":
            return SpreadsheetDocument(name)
        elif doc_type == "presentation":
            return PresentationDocument(name)
        else:
            raise ValueError("Invalid document type: " + doc_type)


# Usage example
factory = DocumentFactory()
doc1 = factory.create_document("text", "Document1.txt")
doc2 = factory.create_document("spreadsheet", "Document2.xlsx")
doc3 = factory.create_document("presentation", "Document3.pptx")

doc1.open()
doc1.save()

doc2.open()
doc2.save()

doc3.open()
doc3.save()
