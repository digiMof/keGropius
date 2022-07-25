import rdflib

gropiusCqs = rdflib.Graph()
gropiusCqs.parse("gropius.ttl",format="ttl")

cq1 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?expression
WHERE {
    ?ideas rdf:type mof:Idea .
    ?ideas mof:embodiedIn ?expression
}
'''

cq2 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?effect
WHERE {
    mof:Academia mof:produces ?effect .
    ?effect rdf:type mof:Effect
}

'''

cq3 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?dependance
WHERE {
    mof:ArchitectureDesign mof:dependsOn ?dependance .
    ?dependance rdf:type mof:Goal
}

'''

cq4 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?mainGoal
WHERE {
    mof:Bauhaus mof:aimsAt ?mainGoal .
    ?mainGoal rdf:type mof:MainGoal
}
'''

cq5 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?expression
WHERE {
    mof:ArchitectureDesign mof:reflects ?expression
}
'''

cq6 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?sublcasses
WHERE {
    ?subclasses rdfs:subClassOf mof:Work
}
'''

cq7 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?object
WHERE {
    mof:Person mof:mustRethink ?object
}
'''

cq8 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?substitutes
WHERE {
    ?academies rdf:type mof:Academy . 
    ?academies mof:changedInto ?substitutes
}
'''

cq9 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?quality
WHERE {
    mof:Vorlehre mof:improves ?quality
}
'''

cq10 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?person
WHERE {
    ?person mof:mustRethink mof:ArchitectureDesign
}
'''

cq11 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?course
WHERE {
    mof:Bauhaus mof:involves ?course .
    ?course rdf:type mof:BauhausCourse
}
'''

cq12 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?goal
WHERE {
    ?institution rdf:type mof:NewlyFormedInstitution .
    ?institution mof:aimsAt ?goal .
    ?goal rdf:type mof:Goal
}
'''

cq13 = '''
PREFIX mof: <http://www.semanticweb.org/bonif/ontologies/2022/5/ontoGropius#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?approach
WHERE {
    ?institution rdf:type mof:NewlyFormedInstitution .
    ?institution mof:involves ?approach .
    ?approach rdf:type ?methods .
    ?methods rdfs:subClassOf mof:NewApproach
}
'''
cqs = [cq1, cq2, cq3, cq4, cq5, cq6, cq7, cq8, cq9, cq10, cq11, cq12, cq13]


for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx+1) + ":")
    results = gropiusCqs.query(cq)
    for result in results:
        print(result)
