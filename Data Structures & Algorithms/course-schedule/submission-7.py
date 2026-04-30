class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        current_prev_course={}
        for course in range(numCourses):   
            current_prev_course[course]=[]
        for current_course, prev_course in prerequisites:
            current_prev_course[current_course].append(prev_course)
        
        allowed_course=set()
        currently_taking=set()
        def dfs(current_course):
            nonlocal currently_taking, allowed_course
            if(current_course in allowed_course):
                return True
            if(current_prev_course[current_course]==[]):
                allowed_course.add(current_course)
                return True
                
            currently_taking.add(current_course)
            for prev_course in current_prev_course[current_course]:
                if(prev_course in currently_taking):
                    return False
                if(dfs(prev_course)):
                    allowed_course.add(prev_course)
                if not dfs(prev_course):
                    return False
            currently_taking.remove(current_course)
            return True
        
        
        
        
        
        for current_course in range(numCourses):
            if not dfs(current_course):
                return False
        return True
        print(current_prev_course)

