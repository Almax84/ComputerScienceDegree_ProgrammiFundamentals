def es2(fposts):
    with open(fposts, 'r', encoding='utf-8') as file:
        return_list = []

        splitted_text = ' '.join(file.read().splitlines())
        posts = list(map(lambda x: x.strip(' '), list(filter(lambda x: x != '', splitted_text.split("<post>")))))

        # get list of words
        words = set()
        post_dict = dict()
        for post in posts:
            post_splitted = post.split(" ")
            post_id = post_splitted[0]
            #words_post = list(filter( lambda x : x != '',post_splitted[1:]))
            words_post = [x for x in post_splitted[1:] if x != '']
            post_dict[post_id] = words_post
            words |= set(words_post)

        max_dict = dict()

        for word in words:

            occorrenze_parola_in_tutti_i_post = 0

            word_max_occurrence_in_post = 0

            posts_contenenti_parola = 0
            for id_post, splitted_post_no_id in post_dict.items():


                if word in splitted_post_no_id:
                    posts_contenenti_parola += 1
                    word_count = splitted_post_no_id.count(word)
                    occorrenze_parola_in_tutti_i_post += word_count
                else:
                    continue

                if word_count > word_max_occurrence_in_post or word_count == word_max_occurrence_in_post and max_dict.get(
                        word) is not None and id_post < \
                        max_dict.get(word)[1]:
                    max_dict[word] = [word_count, id_post]
                    word_max_occurrence_in_post = word_count

            word_dict = {"parola": word, "I1": occorrenze_parola_in_tutti_i_post, "I2": posts_contenenti_parola,
                         "I3": tuple((max_dict.get(word)[0], max_dict.get(word)[1]))}
            return_list.append(word_dict)

    return_list = sorted(return_list, key=sort_logic)
    return return_list


def sort_logic(k):
    return (-k['I1'], k['parola'], -int(k['I3'][1]),)

