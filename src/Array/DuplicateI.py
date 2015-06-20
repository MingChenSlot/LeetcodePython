__author__ = 'mingchen'

# @param {integer[]} nums
# @param {integer} k
# @return {boolean}
def containsNearbyDuplicate_kn(self, nums, k):
    for (i, num) in enumerate(nums):
        for j in range(i + 1, min(i + k + 1, len(nums))):
            if num == nums[j]:
                return True
    return False


def containsNearbyDuplicate(self, nums, k):
    duplicate_map = {}
    for (i, num) in enumerate(nums):
        if num in duplicate_map:
            if i - duplicate_map[num] > k:
                duplicate_map[num] = i
            else:
                return True
        else:
            duplicate_map[num] = i
    return False


# @param {integer[]} nums
# @param {integer} k
# @param {integer} t
# @return {boolean}
def containsNearbyAlmostDuplicate_kn(self, nums, k, t):
    for (i, num) in enumerate(nums):
        for j in range(i + 1, min(i + k + 1, len(nums))):
            if abs(num - nums[j]) <= t:
                return True
    return False

def containsNearbyAlmostDuplicate(self, nums, k, t):
    if k < 1 or t < 0:
        return False

    duplicate_map = {}
    for (i, num) in enumerate(nums):
        bucket = remapNum(num) / (t + 1)
        if bucket in duplicate_map or \
            (bucket - 1 in duplicate_map and abs(duplicate_map[bucket - 1] - num) <= t) or \
            (bucket + 1 in duplicate_map and abs(duplicate_map[bucket + 1] - num) <= t):
            return True
        else:
            if len(duplicate_map) > k:
                del duplicate_map[remapNum(nums[i - k]) / (t + 1)]
            duplicate_map[bucket] = num
    return False

def remapNum(num):
    from sys import maxint
    return num + maxint / 2


