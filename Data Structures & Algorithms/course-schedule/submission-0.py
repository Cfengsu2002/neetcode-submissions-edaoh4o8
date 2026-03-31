class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_schedule=defaultdict(list)
        for i in range(len(prerequisites)):
            course_schedule[prerequisites[i][0]].append(prerequisites[i][1])
        valid_course=set()
        is_valid=True
        current_taking=set()
        def dfs(current_course):
            nonlocal valid_course, is_valid
            if(current_course in current_taking):
                is_valid=False
                return
            if(current_course in valid_course):
                return
            if(course_schedule[current_course]==[]):
                valid_course.add(current_course)
                return 
            current_taking.add(current_course)
            for element in course_schedule[current_course]:
                dfs(element)
            current_taking.remove(current_course)
            return 
        for i in range(numCourses):
            dfs(i)
        return is_valid
            
            