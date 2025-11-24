from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total_candies = n
        i = 1
        
        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue
            current_peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                current_peak += 1
                total_candies += current_peak
                i += 1
                
            if i==(n-1):
                return total_candies
            
            current_valley = 0
            while i < n and ratings[i] < ratings[i-1]:
                current_valley+=1
                total_candies += current_valley
                i+=1
            
            total_candies -= min(current_peak, current_valley)
        return total_candies

if __name__ == "__main__":
    # 實例化物件
    solver = Solution()
    
    # 測試案例 1: [1, 0, 2] -> 應回傳 5 (分配為 2, 1, 2)
    case1 = [1, 0, 2]
    result1 = solver.candy(case1)
    print(f"測試案例 1: {case1} -> 結果: {result1}")

    # 測試案例 2: [1, 2, 2] -> 應回傳 4 (分配為 1, 2, 1)
    case2 = [1, 2, 2]
    result2 = solver.candy(case2)
    print(f"測試案例 2: {case2} -> 結果: {result2}")
    
    # 測試案例 3 (複雜山坡): [1, 3, 2, 2, 1] -> 應回傳 7 (1, 2, 1, 2, 1)
    case3 = [1, 3, 2, 2, 1]
    result3 = solver.candy(case3)
    print(f"測試案例 3: {case3} -> 結果: {result3}")