class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build prereq graph
        course_graph = {}
        for course, prereq in prerequisites:
            course_graph.setdefault(course, []).append(prereq)

        print(course_graph)

        path = set()

        def dfs_cycle(course):
            if course in path:
                return False #detect cycle

            if course not in course_graph:
                return True  # no prereqs
            
            path.add(course)
            for prereq in course_graph[course]:
                if not dfs_cycle(prereq):
                    return False
            
            path.remove(course) # done exploring this node
            course_graph[course] = [] # empty prereq graph
            return True 

        for n in range(numCourses):
            if not dfs_cycle(n):
                return False
        return True
        





# ######
# [a, b] [c, d] [a, d]

# a <-- b
#   <-- d
# c <-- d

# #1 - naive
# 1. build all prereq for each course ---> N
# 2. check each course-prereq pair until conflict ---> N^M

# #2 - graph optimized
# 1. build course graph by prereq relations ---> N
# [[pre0, pre1,..], [pre0, pre1], ...] -> [numCourse]
#  course0           course1

# 2. traverse to detect if there's a cycle in the graph
