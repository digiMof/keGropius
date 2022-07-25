import rdflib

BauhausCqs = rdflib.Graph()
BauhausCqs.parse("assets/testCQs/bau.ttl", format="ttl")

# cq1) What is the main goal of newly formed institutions?
cq1 = '''
PREFIX mof: <http://www.semanticweb.org/orsola/ontologies/2022/6/ontoBau#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?institution ?mainGoal
WHERE {
?institution mof:aimsAt ?mainGoal .
?institution rdf:type mof:NewlyFormedInstitution .
?mainGoal rdf:type mof:SloganGoal
}
'''

# cq2) What different actions should be taken towards academies by different newly formed institutions?
cq2 = '''
PREFIX mof: <http://www.semanticweb.org/orsola/ontologies/2022/6/ontoBau#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?action ?newlyformed
WHERE { ?academy rdf:type mof:Academy .
{?academy ?action ?newlyformed . ?newlyformed rdf:type mof:NewlyFormedInstitution} 
UNION
{?academy ?action ?newlyformed . ?newlyformed rdf:type mof:NewlyFormed}
}

'''

# cq3) What is demanded of education programmes?
cq3 = '''
PREFIX mof: <http://www.semanticweb.org/orsola/ontologies/2022/6/ontoBau#> 
PREFIX owl: <http://www.w3.org/2002/07/owl#> 
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> 
PREFIX xml: <http://www.w3.org/XML/1998/namespace> 
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?demand
WHERE {
?demand mof:involvedBy ?education .
{?education rdf:type mof:EducationalProgram}
UNION
{?education rdf:type mof:NewApproach}
}

'''

# === Printing the results of the queries
cqs = [cq1, cq2, cq3]

for idx, cq in enumerate(cqs):
    print("Results for cq " + str(idx+1) + ":")
    results = BauhausCqs.query(cq)
    for result in results:
        print(result)
