# def delete(list_, index=None):
#     if index == None:
#         return list_[:len(list_)-1]
#     else:
#         return list_[:len(list_) - index - 1] + list_[len(list_) - index:]
#
#
# print(delete([0, 1, 2], index=0))  # [0, 1]
# print(delete([0, 1, 2], index=1))  # [0, 2]
# print(delete([0, 1, 2]))  # [0, 1]

# У вас ошибка в комментариях к принтам! Поэтому я оставила два варианта. Верхний подходит под принты, нижний под чек.

def delete(list_, index=None):
    if index is None:
        return list_[:len(list_) - 1]
    else:
        return list_[:index] + list_[index + 1:]


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
