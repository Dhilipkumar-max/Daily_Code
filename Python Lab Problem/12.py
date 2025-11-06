def insertion_sort(scores): 
    for i in range(1, len(scores)): 
        key = scores[i] 
        j = i - 1 
        while j >= 0 and key < scores[j]: 
            scores[j + 1] = scores[j] 
            j -= 1 
        scores[j + 1] = key 
    return scores 
def selection_sort(scores): 
    n = len(scores) 
    for i in range(n): 
        min_index = i 
        for j in range(i+1, n): 
            if scores[j] < scores[min_index]: 
                min_index = j 
        scores[i], scores[min_index] = scores[min_index], scores[i] 
    return scores 
exam_scores = [72, 88, 53, 94, 78, 60] 
print("Original Exam Scores:", exam_scores) 
sorted_by_insertion = insertion_sort(exam_scores.copy()) 
print("Sorted by Insertion Sort:", sorted_by_insertion)
sorted_by_selection = selection_sort(exam_scores.copy()) 
print("Sorted by Selection Sort:", sorted_by_selection)