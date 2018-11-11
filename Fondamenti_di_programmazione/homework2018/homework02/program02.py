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
            words_post = [x for x in post_splitted[1:] if x != '']
            post_dict[post_id] = words_post
            words |= set(words_post)

        for word in words:

            occorrenze_parola_in_tutti_i_post = 0

            word_max_occurrence_in_post = 0
            word_occurrence_by_post = []
            posts_contenenti_parola = 0
            max_dict = dict()
            for id_post, splitted_post_no_id in post_dict.items():


                if word in splitted_post_no_id:
                    posts_contenenti_parola += 1
                    word_count = splitted_post_no_id.count(word)
                    occorrenze_parola_in_tutti_i_post += word_count
                    word_occurrence_by_post.append(tuple((word_count, id_post)))
                else:
                    continue



            t = max(word_occurrence_by_post, key=lambda tupl: (tupl[0], -int(tupl[1])))
            word_dict = {"parola": word, "I1": occorrenze_parola_in_tutti_i_post, "I2": posts_contenenti_parola,
                         "I3": t}


            return_list.append(word_dict)

    return_list = sorted(return_list, key=sort_logic)
    return return_list


def sort_logic(k):
    return (-k['I1'], k['parola'], -int(k['I3'][1]),)

print(es2("fp3.txt"))