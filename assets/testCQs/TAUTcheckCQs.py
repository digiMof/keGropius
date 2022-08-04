import rdflib

tautCqs = rdflib.Graph()
tautCqs.parse("assets/testCQs/taut.ttl",format="ttl")

# cq1) What is the main goal?
cq1 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

# cq2) Which are the activities whose scope is of public nature?
cq2 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

# cq3) Which are the institutions to be dissolved?
cq3 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

#cq4)  What error should be replaced by freedom?
cq4 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

#cq5) What is responsible for education?
cq5 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

#cq6) What products need to be dissolved?
cq6 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

#cq7) What should government institutions guarantee?
cq7 = '''
PREFIX mof: <https://digimof.github.io/keGropius/ontoTaut#> 
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

# === Printing the results of the queries
cqs = [cq1, cq2, cq3, cq4, cq5, cq6, cq7]


for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx+1) + ":")
    results = tautCqs.query(cq)
    for result in results:
        print(result)
