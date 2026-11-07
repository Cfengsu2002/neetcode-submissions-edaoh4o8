class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        answer=[]
        courses_pre={}
        for i in range(numCourses):
            courses_pre[i]=[]
        for course, pre in prerequisites:
            courses_pre[course].append(pre)

        visited=set()
        no_cycle=False
        answer=[]
        def dfs(course, current_visiting):
            nonlocal no_cycle, visited, answer
            if course in visited:
                return
            if course in current_visiting:
                no_cycle=True
                return
            for pre in courses_pre[course]:
                current_visiting.add(course)
                dfs(pre, current_visiting)
                current_visiting.remove(course)
            visited.add(course)
            answer.append(course)
            return
        for i in range(numCourses):
            dfs(i, set())
        return answer if no_cycle!=True else []