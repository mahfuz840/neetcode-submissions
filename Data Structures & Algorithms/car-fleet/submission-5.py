class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuples = []
        for i in range(len(position)):
            tuples.append((position[i], speed[i]))
        
        tuples_sorted = sorted(tuples, reverse = True)

        st = []
        ans = 0
        mx = -1

        for tup in tuples_sorted:
            rem = target - tup[0]
            rem_time = rem / tup[1]
            # print(tup[0], rem_time)

            new_fleet = False
            while st and mx < rem_time:
                new_fleet = True
                st.pop()
                # print('popping', st.pop())
            
            if new_fleet:
                ans += 1
            
            st.append(rem_time)
            mx = max(mx, rem_time)
        
        return ans + 1