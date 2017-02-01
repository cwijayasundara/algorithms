from collections import deque

# chk if the name start with m
def person_is_seller(name):
    return name[0] == 'm'

graph = {} # hashtable
graph["you"] = ["tommy", "charlie", "simon","cham"]
graph["tommy"] = ["peter", "peg"]
graph["charlie"] = ["tim"]
graph["simon"] = ["thom", "mike"]
graph["peter"] = []
graph["peg"] = []
graph["thom"] = []
graph["mike"] = []
graph["cham"] = []
graph["tim"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    # searched people
    searched = []
    while search_queue:
        person = search_queue.popleft()
        # if person is not searched
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller!"
                return True
            else:
                search_queue += graph[person]
                # person is searched
                searched.append(person)
    return False

search("you")
