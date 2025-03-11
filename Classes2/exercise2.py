# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście

lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']


if "FGFR4" in lista_gene1:
    print("FGFR4 ma index:",lista_gene1.index("FGFR4"))
else:
    print("FGFR4 nie zawiera sie w liscie")

if "FGERA4" in lista_gene1:
    print("FGERA4 ma index:",lista_gene1.index("FGERA4"))
else:
    print("FGERA4 nie zawiera sie w liscie")
