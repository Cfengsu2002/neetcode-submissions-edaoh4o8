class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_prev=defaultdict(list)
        visited=set()
        for courses in prerequisites:
            course, prev=courses
            course_prev[course].append(prev)
        can_take=True
        def dfs(course, current_taking):
            nonlocal can_take, visited
            if course in visited:
                return
            if course in current_taking:
                can_take=False
                return
            current_taking.add(course)
            for prev in course_prev[course]:
                dfs(prev, current_taking)
            current_taking.remove(course)
            visited.add(course)
            return
        for i in range(numCourses):
            dfs(i, set())
        return can_take
