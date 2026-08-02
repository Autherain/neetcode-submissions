type Solution struct{}

func (s *Solution) Encode(strs []string) string {
    if len(strs) == 0 {
        return ""
    }

    var sizes []string
    for _, element := range strs {
        sizes = append(sizes, strconv.Itoa(len(element)))
    }

    return strings.Join(sizes, ",") + "%" + strings.Join(strs, "")
}

func (s *Solution) Decode(str string) []string {
    if len(str) == 0 {
        return []string{}
    }
    parts := strings.SplitN(str, "%", 2)
    sizes := strings.Split(parts[0], ",")

    var returnArray []string
    var length int
    i := 0
    for _, element := range sizes {
        if element == "" {
            continue
        }
        length, _ = strconv.Atoi(element) // Handle the error return value
        returnArray = append(returnArray, parts[1][i:i+length])
        i += length
    }

    return returnArray
}