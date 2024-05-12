# -*- coding: utf-8 -*-

import jieba


str_a = "安徽救人牺牲消防员父母：两遭丧子之痛，炸十年油条为儿购婚房"
cut_words = jieba.cut(str_a)
print("/".join(cut_words))
