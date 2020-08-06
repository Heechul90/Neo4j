# pip install neo4j-driver
# python example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=basic_auth("neo4j", "adminuser"))
session = driver.session()

cypher_query = '''
MATCH (movie:Movie)<-[:ACTED_IN]-(actor)-[:ACTED_IN]->(rec:Movie)
WHERE movie.title IN $favorites
RETURN rec.title as title, count(*) as freq 
ORDER BY freq DESC LIMIT 5
'''

results = session.run(cypher_query,
  parameters={"favorites":["The Matrix"]})

for record in results:
  print(record['title'])

