



def containsNearbyAlmostDuplicate(nums, k, t):
    """
    :type nums: List[int]
    :type k: int
    :type t: int
    :rtype: bool
    """
    if t < 0:
        return False
    cache = {}
    for i in range(len(nums)):
        if i-k > 0:
            bucket_id_to_delete = nums[i-k-1]//(t+1)
            del cache[bucket_id_to_delete]

        bucket_id = nums[i]//(t+1)
        condition1 = (bucket_id in cache)
        condition2 = ((bucket_id-1 in cache and abs(cache[bucket_id-1]-nums[i])<= t))
        condition3 = ((bucket_id+1 in cache and abs(cache[bucket_id+1]-nums[i])<= t))
        if condition1 or condition2 or condition3:
            return True
        cache[bucket_id] = nums[i]
    return False


if __name__ == '__main__':
    test = [1, 5, 9, 1, 5, 9, 8]

    k = 2
    t = 3

    ans = containsNearbyAlmostDuplicate(test, k, t)
    print("answer is ",ans)