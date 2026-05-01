class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cur_prev={}
        for i in range(numCourses):
            cur_prev[i] = []
        for cur, prev in prerequisites:
            cur_prev[cur].append(prev)
        
        print(cur_prev)
        current_visiting=set()
        allowed_courses=set()
        ans=[]
        is_true=True
        def dfs(cur):
            nonlocal current_visiting, allowed_courses, ans, is_true
            if(cur in current_visiting):
                return False
            if(cur in allowed_courses):
                return True
            current_visiting.add(cur)
            for course in cur_prev[cur]:
                if(not dfs(course)):
                    is_true=False
                    return False
            current_visiting.remove(cur)
            allowed_courses.add(cur)
            ans.append(cur)
            return True
        for i in range(numCourses):
            dfs(i)
        return ans if is_true else []