# pip install neo4j-driver

from neo4j import GraphDatabase, basic_auth

## DB에 접근하기 위해서 필요한 정보는 다음 네가지죠.
IP_ADDRESS ="localhost"
BOLT_PORT  = "7687"
USER_NAME = "neo4j"
PASSWORD = "adminuser"
##

# bolt protocol로 DB의 ip에 port로 접근하여, ID, PASSWORD를 입력합니다.
driver = GraphDatabase.driver(
    # bolt protocol로 내 DB의 IP에 BOLT_PORT로 접근하고 
    uri=f"bolt://{IP_ADDRESS}:{BOLT_PORT}", 
    # 주어진 USER_ID와 패스워드로 들어감.
    auth=basic_auth(
        user=USER_NAME, 
        password=PASSWORD)
    )

def run_query(input_query):
    """
    - input_query를 전달받아서 실행하고 그 결과를 출력하는 함수입니다.
    """
    # 세션을 열어줍니다.
    with driver.session() as session: 
        # 쿼리를 실행하고 그 결과를 results에 넣어줍니다.
        results = session.run(
            input_query,
            parameters={}
        )
        return results
####################################

# 쿼리를 작성합니다.
# 아래와 같은 Cypher 쿼리를 실행하면 그 결과로 테이블의 형태로 데이터가 리턴됩니다. 
# 그런데, 이 때, 아래 쿼리에서는 필요한 값만 가져온 것이 아니라, 모든 값을 그냥 그대로, 
# 그리고 AS와 같은 명령어로 칼럼의 이름을 확정하지도 않고 그대로 가져왔죠. 
# 이렇게 할 경우, 각 셀에 딕셔너리가 있는 형태가 되죠. 
print("=="*30)
cypher_query1 = '''
MATCH (p:Person)
RETURN p
'''
print("Cypher_query")
print(cypher_query1)
print("=="*30)
for i, each in enumerate(run_query(cypher_query1)):
    # each는 <class 'neo4j.Record'> 
    # 딕셔너리와 유사하다고 생각하면 됨.
    if i>=2:
        break
    print('--'*30)
    print(f"each              ==> {each}")
    print(f"each['p']         ==> {each['p']}")# 딕셔너리.
    print(f"each['p'].id      ==> {each['p'].id}")
    print(f"each['p'].labels  ==> {each['p'].labels}")
    # property는 다음의 형식으로
    print(f"each['p']['name'] ==> {each['p']['name']}")
print('=='*30)

# 만약, 이렇게 하지 않고, 일일이 원하는 칼럼에 대해서 이름을 명시해주면 더 깔끔하게 접근하는 것이 가능하죠.
cypher_query2 = '''
MATCH (p:Person)
RETURN p.name AS Name, p.born AS Born_year
'''
print("Cypher_query")
print(cypher_query2)
print("=="*30)
for i, each in enumerate(run_query(cypher_query2)):
    print("--"*30)
    if i>2:
        break
    print(f"each              ==> {each}")
    print(f"each['Name']      ==> {each['Name']}")
    print(f"each['Born_year'] ==> {each['Born_year']}")
print("=="*20)