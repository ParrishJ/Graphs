import random
import math
from collections import deque
class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # Generate all possible friendships between users, put them in a list
        # shuffle the list 
        # create friendships using add_friendship() from the irst N elements in that list
        possible_friendships = []
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # shuffle the list
        random.shuffle(possible_friendships)
        # create friendships using add_friendship from the first N elements in that list
        for i in range(math.floor(num_users * avg_friendships / 2)): 
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    # class demo - linear time populate graph linear
    def add_friendship_linear(self, user_id, friend_id):
        # Returns True if user_id and friend_id have successfully been added as friends
        if user_id == friend_id:
            return False
        # Check if friend_id and user_id are not already friends with each other
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True



    def populate_graph_linear(self, num_users, avg_friendships):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users (same as other graph)
        for i in range(num_users):
            self.add_user(f"User {i}")
        
        # Create rabdin friendships until we've hit the target number of friendships
        target_friendships = num_users * avg_friendships
        total_friendships = 0 
        collisions = 0 

        while total_friendships < target_friendships:
            # keep adding friendships
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f"Collisions: {collisions}")


    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
    
        connection_list = {}
        
        # Loop through the list of friendships
        for friend in self.friendships:
            # if the friend that you're on == user_id, we know that the path is equal to a list with the user_id in it
            if friend == user_id:
                connection_list[user_id] = [friend]
            
            # Else, visit each friend. If the bfs for that friend returns a path, append that path to our dictionary where the key is the id
            # the destination or friend we're trying to reach and the value is the path the search took to get to that friend. 
            else:
                if self.bfs(user_id, friend):
                    connection_list[friend] = self.bfs(user_id, friend)   
        return connection_list


        
        
    # A Standart bfs to use in the get all social paths function
    def bfs(self, starting_vertex, destination_vertex):
        visited = set()
        queue = deque()
        queue.append([starting_vertex])
        while len(queue) > 0:
            currentPath = queue.popleft()
            currentNode = currentPath[-1]
            if currentNode == destination_vertex:
                return currentPath
            if currentNode not in visited:
                visited.add(currentNode)
                for neighbor in self.friendships[currentNode]:
                    newPath = list(currentPath)
                    newPath.append(neighbor)
                    queue.append(newPath)

        """ visited[user_id] = visited
        return visited """

    # Implementation from class
    def get_all_social_paths_class_demo(self, user_id):
        visited = {}
        queue = deque()
        queue.append([user_id])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1]
            visited[currNode] = currPath
            for friend in self.friendships[currNode]:
                if friend not in visited:
                    newPath = currPath.copy()
                    newPath.append(friend)
                    queue.append(newPath)
        return visited



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph_linear(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths_class_demo(1)
    print(connections)


""" 
QUESTIONS 

1. To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?

You would have to call add_frindship 500 times. Because add_friendship creates a bi-directional edge / friendship for two people at once, calling
add_friendship 500 times would create 1000 friendships. 1000 friendships distributed among 100 friends would equate to an average of 10 friendships
per person.

2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social 
network? What is the average degree of separation between a user and those in his/her extended network?

My understanting is that a simple formula presented by Watts and Strogatz (ln(number of nodes) / ln(edges per node)) can be used to find the average
degees of separation here. When we use the numbers above, we get about 4.29 degrees of separation on average. Because each person has five friends
which is more than the average degrees of separation here, my understanding is that on average 100% of the users will be in each person's extended network.


Citation for formula:
Watts, Duncan J., and Strogatz, Steven H. “Collective Dynamics of ‘Small-World’ Networks.” Nature, vol. 393, June 1998, pp. 440–442

‌

"""