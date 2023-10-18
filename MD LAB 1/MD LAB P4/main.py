# # 4. Truth table solver:
# from prettytable import PrettyTable
#
#
# def conv(a):
#     if a:
#         a = 1
#     else:
#         a = 0
#     return a
#
#
# pt = PrettyTable()
# ex = input()
# if ex.find('z') == -1:
#     if ex.find('y') == -1:
#         rows = 4
#         if ex.find('x') == -1:
#             rows = 2
#     else:
#         rows = 8
# else:
#     rows = 16
#
# tf = [1, 0]
# if rows == 2:
#     pt.field_names = ["k", ex]
#     for k in tf:
#         h = conv(eval(ex.replace('+', 'or').replace('*', 'and').replace('!', 'not ')))
#         pt.add_row([k, h])
#     print(pt)
# if rows == 4:
#     pt.field_names = ["k", "x", ex]
#     for k in tf:
#         for x in tf:
#             h = conv(eval(ex.replace('+', 'or').replace('*', 'and').replace('!', 'not ')))
#             pt.add_row([k, x, h])
#     print(pt)
# elif rows == 8:
#     pt.field_names = ["x", "y", "z", ex]
#     for k in tf:
#         for x in tf:
#             for y in tf:
#                 h = conv(eval(ex.replace('+', 'or').replace('*', 'and').replace('!', 'not ')))
#                 pt.add_row([k, x, y, h])
#     print(pt)
# elif rows == 16:
#     pt.field_names = ["x", "y", "z", "k", ex]
#     for k in tf:
#         for x in tf:
#             for y in tf:
#                 for z in tf:
#                     h = conv(eval(ex.replace('+', 'or').replace('*', 'and').replace('!', 'not ')))
#                     pt.add_row([k, x, y, z, h])
#     print(pt)

# from prettytable import PrettyTable
#
# pt = PrettyTable()
# ex = input()
# var = []
# for i in ex:
#     if i.isalpha() and len(i) == 1:
#         var.append(i)
# print(var)
# pt.field_names = var + [ex]
# ex = ex.replace('+', 'or').replace('*', 'and').replace('!', 'not ')
# print(ex)
# # pt = PrettyTable([x for x in var] + [ex])

# rows = 2 ** len(var)
# col = len(var)
# print(rows)
# print(col)
# print(pt)
# for i in range(rows)[::-1]:
#     lst = []
#     for j in range(1, col+1)[::-1]:
#         lst += (str(int((i % 2**j) < 2**j // 2)))
#     new = ex.replace(var[0], lst[0])
#     for k in range(len(var)):
#         new = new.replace(var[k], lst[k])
#         lst += str(int(eval(new)))
#         pt.add_row([x for x in lst])
#
# print(pt)


from prettytable import PrettyTable
#     rows = 2**len(var)
#     cols = len(var)
#     # for i in range(rows):
#     #     tf = []
#     #     tfl = 1
#     #     for j in range(rows):
#     #
#     # table.add_row([x for x in tf])
#     # for i in range(rows):
#     #     if i < rows/2:
#     #         k = 1
#     #     else:
#     #         k = 0
#     #     tf = []
#     #     for j in range(1, cols):
#     #
#     #     table.add_row([x for x in tf])
#     print(truth_table(ex))

# pt = PrettyTable()
# ex = input()
# var = []
# for i in ex:
#     if i.isalpha() and len(i) == 1:
#         var.append(i)
# print(var)
# pt.field_names = var
# ex = ex.replace('+', 'or').replace('*', 'and').replace('!', 'not ')
# print(ex)
# print(pt)
# rows = 2 ** len(var)
# col = len(var) - 1
# rowsl = []
# for i in range(rows):
#     rowsl.append(str(bin(i)))
#     # print(bin(i))
#     rowsl[i] = rowsl[i].replace('0b', '')
#     # print(rowsl[i])
#     for j in range(0, rows - len(rowsl[i])):
#         rowsl[i] = rowsl[i] + '0'
# print(rowsl)
# ghgfh = []
# for i in rowsl:
#     ghgfh.append(i[0:len(var)])
# print(ghgfh)
# varstf = []
# for i in ghgfh:
#     for x in i:
#         varstf.append(int(x))
# print(varstf)
# rowsforpt = []
# for i in range(0, rows):
#     rowspt = []
#     for tf in varstf[i:i+2]:
#         rowspt.append(varstf[i])
#     pt.add_row(rowspt)
# print(pt)