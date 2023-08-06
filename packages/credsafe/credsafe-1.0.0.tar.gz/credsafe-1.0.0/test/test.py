from credsafe import Agent as AgentV2, AgentV1, EasyRSA
import time


app = "my app"
kp = EasyRSA(bits=1024).gen_key_pair()
print("save this kp or load it from a file, otherwise you cannot get(...) if you lose it")
print(kp)
id = "username"
pw = "passcode"

# credsafe_agent = AgentV1(app_name=app, key_pair=kp)
credsafe_agent = AgentV2(app_name=app, key_pair=kp)
print("agent created")
time.sleep(5)
credsafe_agent.set(id=id, pw=pw, k="phone", v=123456789)
credsafe_agent.set(id=id, pw=pw, k="config", v={"something": "secret"})
print("value set")
time.sleep(5)
print(credsafe_agent.get(id=id, pw=pw, k="phone"))
print(credsafe_agent.get(id=id, pw=pw, k="config"))
time.sleep(5)
credsafe_agent.rm(id=id, pw=pw, k="config")
print("value removed")
time.sleep(5)
try:
    print(credsafe_agent.get(id=id, pw=pw, k="config"))
except:
    print("KeyError")
print("agent destroyed")
credsafe_agent.destroy(id=id)
