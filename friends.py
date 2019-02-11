from __future__ import division

users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

def num_friends(user):
    '''
    Find number of friends for a given user
    '''
    return len(user["friends"])

def sort_by_num_friends(friends_totals):
    '''README.md
    Sort from "most friends" to "least friends"
    '''    
    return sorted(friends_totals, key=lambda id: id[1], reverse = True)

def mean_num_friends(x):
    total_friends = sum(row[1] for row in x)
    return total_friends/len(users)

def median_num_friends(x):
    lstLen = len(x)
    index = (lstLen - 1)//2

    if (lstLen % 2):
        return x[index][1]
    else:
        return (x[index][1] + x[index+1][1])/2.0
   

def main():
    for user in users:
        user ["friends"] = []
    
    for x, y in friendship:
        users[x]["friends"].append(users[y])
        users[y]["friends"].append(users[x])

    friends_totals = [(user["id"], num_friends(user))
                     for user in users]
    
    sorted_friends = sort_by_num_friends(friends_totals)
    
    #print(friends_totals)
    print(sorted_friends)
    print("Mean = {}".format(mean_num_friends(friends_totals)))
    print("Median = {}".format(median_num_friends(sorted_friends)))
    
          
if __name__ == "__main__":
    main()
