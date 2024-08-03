
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_mod = list(students)
students_mod.sort()
n = grades.__len__()
print('Количество записей в журнале =' , n)
jurnal = dict({students_mod[0]: round(sum(grades[0]) / grades[0].__len__(),1)})
jurnal.update(dict({students_mod[1]: round(sum(grades[1]) / grades[1].__len__(),1)}))
jurnal.update(dict({students_mod[2]: round(sum(grades[2]) / grades[2].__len__(),1)}))
jurnal.update(dict({students_mod[3]: round(sum(grades[3]) / grades[3].__len__(),1)}))
jurnal.update(dict({students_mod[4]: round(sum(grades[4]) / grades[4].__len__(),1)}))
print('Журнал 5 "Ж":' , jurnal)
