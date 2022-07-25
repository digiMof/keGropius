import rdflib

tautCqs = rdflib.Graph()
tautCqs.parse("taut.ttl",format="ttl")

cq1 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?maingoal
WHERE {
    ?maingoal rdf:type mof:SloganGoal
}
'''

cq2 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?activity
WHERE {
    ?activity mof:aimsAt mof:PublicNature
}

'''

cq3 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?institutions ?type
WHERE {
    ?institutions mof:replacedBy mof:NewlyFormedInstitutions .
    ?institutions rdf:type ?type
}

'''

cq4 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?error
WHERE {
    ?error mof:replacedBy mof:Freedom
}
'''

cq5 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?institution
WHERE {
    ?institution mof:responsibleFor mof:EducationalChange    
}

'''

cq6 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?product
WHERE {
    ?product rdf:type mof:Monument .
    mof:Dissolution mof:involves ?product
}
'''

cq7 = '''
PREFIX mof: <http://www.semanticweb.org/manuele/ontologies/2022/5/18/ontoTaut#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?goal
WHERE {
    ?goal mof:fosteredBy mof:GovernmentInstitution
}

'''

cqs = [cq1, cq2, cq3, cq4, cq5, cq6, cq7]


for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx+1) + ":")
    results = tautCqs.query(cq)
    for result in results:
        print(result)
