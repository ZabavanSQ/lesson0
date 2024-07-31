immutable_var = (1, 2, 3, 'street', 5.5, True)
print(immutable_var)
# immutable_var[2] = 5 нелья изменить кортеж так как это не изменяемый элимент
mutable_list = [2, 4, 6, 'q', 'r', 'a', ('g','r')]
print(mutable_list)
mutable_list [3] = 'street'
mutable_list [-1] = 666
print(mutable_list)