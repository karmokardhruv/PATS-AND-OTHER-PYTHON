X=[25, 58, 12],[93, 32, 48],[22, 55, 73]
Y=[53, 61, 79, 82],[15, 21, 38, 42],[55, 61, 72, 99]
result=[[sum(a*b for a, b in zip(X_row, Y_col))
                for Y_col in zip(*Y)]
                        for X_row in X]
for r in result:
    print(r)