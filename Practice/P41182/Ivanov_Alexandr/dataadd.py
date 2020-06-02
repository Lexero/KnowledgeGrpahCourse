import json
from rdflib import Namespace, Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL

with open('training.json', encoding='utf-8-sig') as json_file:
    data = json.load(json_file)

ns = Namespace('http://www.semanticweb.org/alex/ontologies/2020/3/training#')

g = Graph()
g.parse("training.owl", format='turtle')


def add(data, category):
    if category == 'Training':
        for man in data[category]:
            name = URIRef(ns + man['Name'])
            gender = Literal(man['gender'])
            age = Literal(man['age'])
            weight = Literal(man['weight'])
            height = Literal(man['height'])
            sportsmanship = Literal(man['sportsmanship'])
            body_type = Literal(man['body_type'])
            diseases = Literal(man['diseases'])
            quantity_per_week = Literal(man['quantity_per_week'])
            sports_equipment = Literal(man['sports_equipment'])
            goal = Literal(man['goal'])
            Result = Literal(man['Result'])

            g.add((name, RDF.type, OWL.NamedIndividual))
            g.add((name, RDF.type, ns.Result))
            g.add((name, ns.gender, gender))
            g.add((name, ns.age, age))
            g.add((name, ns.height, height))
            g.add((name, ns.weight, weight))
            g.add((name, ns.sportsmanship, sportsmanship))
            g.add((name, ns.body_type, body_type))
            g.add((name, ns.diseases, diseases))
            g.add((name, ns.quantity_per_week, quantity_per_week))
            g.add((name, ns.sports_equipment, sports_equipment))
            g.add((name, ns.goal, goal))

            if (name, RDFS.comment, None) not in g:
                g.add((name, RDFS.comment, Result))

add(data, 'Training')

print(g.serialize(format="turtle").decode("utf-8"))

g.serialize(destination='training2.owl', format='turtle')