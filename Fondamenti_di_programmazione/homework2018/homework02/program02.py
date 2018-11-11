def es2(fposts):
    with open(fposts, 'r', encoding='utf-8') as file:
        return_list = []

        splitted_text = ' '.join(file.read().splitlines())
        posts = list(map(lambda x: x.strip(' '), list(filter(lambda x: x != '', splitted_text.split("<post>")))))

        # get list of words
        words = set()
        for post in posts:
            words_post =  {x for x in post.split(" ")[1:] if x != ''}
            words |= words_post


        max_dict = dict()

        for word in words:

            occorrenze_parola_in_tutti_i_post = 0

            word_max_occurrence_in_post = 0

            posts_parola = 0

            for post in posts:

                splitted_post = post.split(" ")
                id_post = splitted_post[0]
                splitted_post_no_id = [x for x in splitted_post[1:] if x != '']
                word_count = splitted_post_no_id.count(word)
                occorrenze_parola_in_tutti_i_post += word_count
                if word in splitted_post_no_id:
                    posts_parola += 1

                if word_count > word_max_occurrence_in_post:
                    max_dict[word] = [word_count, id_post]
                    word_max_occurrence_in_post = word_count
                elif word_count == word_max_occurrence_in_post and max_dict.get(word) is not None and id_post < \
                        max_dict.get(word)[1]:
                    max_dict[word] = [word_count, id_post]

            word_dict = {"parola": word, "I1": occorrenze_parola_in_tutti_i_post, "I2": posts_parola,
                         "I3": tuple((max_dict.get(word)[0], max_dict.get(word)[1]))}
            return_list.append(word_dict)

    return_list = sorted(return_list, key=sort_logic)
    return return_list



def sort_logic(k):
    return (-k['I1'], k['parola'], -int(k['I3'][1]),)

#print(es2("fp1.txt"))
