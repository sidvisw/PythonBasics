# sentence_list=["This Is cool", "python is good", "python is not python snake"]
# search_dict={}
# user_input=input("Please input your query string\n")
# queries=user_input.split(" ")
# for sentence in sentence_list:
#     count=0
#     split_list=(sentence.lower()).split(" ")
#     for query in queries:
#         count+=(split_list.count(query.lower()))
#     if count!=0:
#         search_dict.update({sentence:count})
# search_dict_sorted={k: v for k, v in sorted(search_dict.items(), key=lambda item: item[1],reverse=True)}
# print(f"{len(search_dict_sorted)} results found:")
# i=1
# for key in search_dict_sorted.keys():
#     print(f"{i}. {key}")
#     i+=1

def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == '__main__':
    # matchingWords("This is good","python is good")
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "Subscribe to code with harry"]

    query=input("please enter the query string\n")
    scores=[matchingWords(query,sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore=[sentScore for sentScore in sorted(zip(scores,sentences),reverse=True)]
    # print(sortedSentScore)
    # a=[1,2,3]
    # b=[4,5,6]
    # zip(a,b)=[(1,4),(2,5),(3,6)]
    print(f"{len(sortedSentScore)} results found!")
    for score,item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}")