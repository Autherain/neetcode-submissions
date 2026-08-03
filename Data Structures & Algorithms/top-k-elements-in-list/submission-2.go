import "slices"

func topKFrequent(nums []int, k int) []int {
    num := make(map[int]int)
    for _, elem := range nums {
        num[elem] = num[elem] + 1
    }
    
    // Initialize AFTER counting frequencies
    frequencySlice := make([][]int, len(nums)+1)
    
    for key, value := range num {
        frequencySlice[value] = append(frequencySlice[value], key)
    }
    
    // Méthode 1 : Slice vide
    res := []int{}
    for _, elem := range slices.Backward(frequencySlice) {
        for _, value := range elem {
            res = append(res, value)
            if len(res) == k {
                return res
            }
        }
    }
    return []int{}
}