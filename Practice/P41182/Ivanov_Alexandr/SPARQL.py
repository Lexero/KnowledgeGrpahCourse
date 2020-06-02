from rdflib import Graph

g = Graph()
g.parse("training2.owl", format='turtle')

# for subj, pred, obj in g:
#     if (subj, pred, obj) not in g:
#         raise Exception("he")
#     if g.label(subj):
#         print(g.label(subj))

#print("graph has {} statements.".format(len(g)))

res = g.query(
    """PREFIX : <http://www.semanticweb.org/alex/ontologies/2020/3/training#>
    SELECT ?num ?comment
    WHERE {?num a :Result ;
    ns1:gender "Male" ;
    ns1:age 22 ;
    ns1:height 190 ;
    ns1:weight 80 ;
    ns1:body_type "middle" ;
    ns1:diseases "no" ;
    ns1:goal "muscle gain" ;
    ns1:quantity_per_week 3 ;
    ns1:sports_equipment "horizontal bar, jump rope" ;
    ns1:sportsmanship "used to play sports" ;
    rdfs:comment ?comment.
    }""")

print('\nTraining 1\n')
for row in res:
    print(row[0], '\n', row[1])


res = g.query(
    """PREFIX : <http://www.semanticweb.org/alex/ontologies/2020/3/training#>
    SELECT ?num ?comment
    WHERE {?num a :Result ;
    ns1:gender "Male" ;
    ns1:age 50 ;
    ns1:height 178 ;
    ns1:weight 120 ;
    ns1:body_type "fat" ;
    ns1:diseases "Hernia, Osteochondrosis, Diastasis" ;
    ns1:goal "losing weight" ;
    ns1:quantity_per_week 3 ;
    ns1:sports_equipment "Barbell" ;
    ns1:sportsmanship "never sports before" ;
    rdfs:comment ?comment.
    }""")

print('\nTraining 2\n')
for row in res:
    print(row[0], '\n', row[1])


res = g.query(
    """PREFIX : <http://www.semanticweb.org/alex/ontologies/2020/3/training#>
    SELECT ?num ?comment
    WHERE {?num a :Result ;
    ns1:gender "female" ;
    ns1:age 30 ;
    ns1:height 175 ;
    ns1:weight 65 ;
    ns1:body_type "middle" ;
    ns1:diseases "Osteochondrosis" ;
    ns1:goal "losing weight" ;
    ns1:quantity_per_week 4 ;
    ns1:sports_equipment "Cardiovascular equipment, Dumbbells, Bench" ;
    ns1:sportsmanship "played sports before" ;
    rdfs:comment ?comment.
    }""")

print('\nTraining 3\n')
for row in res:
    print(row[0], '\n', row[1])
