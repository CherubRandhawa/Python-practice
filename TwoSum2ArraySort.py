def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        ans = [] * 2
        while i < j:
            summ = numbers[i] + numbers[j]
            if summ == target:
                i += 1
                j += 1
                ans.append(i)
                ans.append(j)
                return ans
            elif summ < target:
                i += 1
            else:
                j -= 1