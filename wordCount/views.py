from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'index.html', {'name': 'BY : S K GUPTA'})


def count_method(request):
    data = request.POST['completeText']
    word_list = data.split()
    list_length = len(word_list)

    dictionary = {}

    for word in word_list:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    sorted_list = sorted(dictionary.items(), key = operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fullText': data, 'words_count': list_length, 'dictionary': sorted_list})
