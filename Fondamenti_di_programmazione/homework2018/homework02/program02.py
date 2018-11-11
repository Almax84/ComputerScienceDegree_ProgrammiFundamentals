
def es2(fposts):
    with open(fposts, 'r', encoding='utf-8') as file:
        return_list = []
        
        splitted_text =' '.join(file.read().splitlines())
        posts = list(map(lambda x: x.strip(' '), list(filter(lambda x: x != '', splitted_text.split("<post>")))))

        # get list of words
        for post in posts:
            words = [x for x in post.split(" ")[1:] if x != '']

        analyzed_words = set()
        
        max_dict = dict()
        
        for post in posts:
            words_in_post = post.split(" ")

            for i in range(1, len(words_in_post)):
               word = words_in_post[i]
               
               if word == '' or word in analyzed_words:
                   continue
               
               occorrenze_parola_in_tutti_i_post = 0
               
               word_max_occurrence_in_post = 0
               
               if word and word != ' ' and word != '':
                   analyzed_words.add(word)
                   posts_parola = 0
                   for post in posts:
                       splitted_post = post.split(" ")
                       id_post = splitted_post[0]
                       splitted_post_no_id = [x for x in splitted_post[1:] if x != '']
                       word_count = splitted_post_no_id.count(word)
                       occorrenze_parola_in_tutti_i_post += word_count
                       if word in splitted_post_no_id:
                           posts_parola+=1
                                          
                       if word_count > word_max_occurrence_in_post:
                           max_dict[word] = [word_count, id_post]
                           word_max_occurrence_in_post = word_count
                       elif word_count == word_max_occurrence_in_post and max_dict.get(word) is not None and id_post < max_dict.get(word)[1]:
                           max_dict[word] = [word_count, id_post]
                    
            
               word_dict = {"parola":word,"I1":occorrenze_parola_in_tutti_i_post,"I2":posts_parola,"I3":tuple((max_dict.get(word)[0],max_dict.get(word)[1]))}
               return_list.append(word_dict)
                
                           
        return_list = sorted(return_list, key=sort_logic )       
                       
                      
                       
                   #print(occorrenze_parola, " per parola", word, " numero post in cui appare: " , posts_parola)
            
    
        return return_list


lista_di_prova = [{'parola': 'hw1', 'I1': 6, 'I2': 3, 'I3': (3, '30')}, {'parola': 'python', 'I1': 3, 'I2': 2, 'I3': (2, '30')}, {'parola': 'hw2', 'I1': 2, 'I2': 1, 'I3': (2, '1')}, {'parola': 'monti', 'I1': 1, 'I2': 1, 'I3': (1, '30')}, {'parola': 'sterbini', 'I1': 1, 'I2': 1, 'I3': (1, '21')}, {'parola': '30', 'I1': 1, 'I2': 1, 'I3': (1, '21')}, {'parola': 'spognardi', 'I1': 1, 'I2': 1, 'I3': (1, '1')}]

    
def sort_logic(k):
    return (-k['I1'],k['parola'], -int( k['I3'][1]),  )


#print(es2("fp2.txt"))
