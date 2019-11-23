def repeatedString(s, n):

    # get length and count of string
    segment_length = len(s)
    segment_count = s.count("a")

    # get ratio between n and string length
    ratio = n // segment_length

    # get the remainder between n and string length
    remainder = segment_length - n % segment_length

    # calculate count - ratio * number of As in string
    count = ratio * segment_count

    # get count of remainder, remove remainder from s
    last_partial_segment_count = s.count("a", 0, segment_length - remainder)
    result = count + last_partial_segment_count

    return result
