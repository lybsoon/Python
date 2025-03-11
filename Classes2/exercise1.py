#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?

set_gene1 = {'SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1', 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4',
             'ANGC3', 'WELNT14', 'EOO1', 'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'}
set_gene2 = {'SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC1', 'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421',
             'ANGC3', 'WELNT14', 'EOO11', 'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'}

set_gene3 = {'SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3', 'GALNT14', 'ERCC11', 'LJS19A2', 'AKM7B', 'ELLB34',
             'FULR4', 'ANGC3', 'WELNT15', 'EOO1', 'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'}


all_gens = set_gene1 & set_gene2 & set_gene3
print("Wspolne geny dla wszystkich pacjentow: ",all_gens)

gens_2 =set_gene1 & set_gene2 and set_gene3 & set_gene1 and set_gene2 & set_gene3
print("Geny ktore są tylko wspólne dla 2 pacjentow ", gens_2)

unique_gens = set_gene1 - (set_gene2 | set_gene3) and set_gene2 - (set_gene1 | set_gene3) and set_gene3 - (set_gene1 | set_gene2)
print("Geny ktore wystepuja tylko w 1 chorobie: ", unique_gens)