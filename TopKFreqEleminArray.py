        maper = {}
        arr = []
        for i in range (0, len(nums)):
            if nums[i] in maper:
                maper[nums[i]] += 1
            else:
                maper[nums[i]] = 1
        for i in range(0, k):
            key = max(maper, key = maper.get)
            arr.append(key)
            del maper[key]
        return arr            
