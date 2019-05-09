import csv
from owlready2 import*

onto = get_ontology("ontologiarelembrar.owl").load()

with open('populacao.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  next(csv_reader)
  for row in csv_reader:

    # criando instancia de Pessoa
    p1 = onto.Pessoa()
    p1.nome.append(row[0])
    p1.dataNascimento.append(row[1])
    p1.tipoFisico.append(row[2])
    p1.sexo.append(row[3])
    p1.alturaAproximada.append(row[4])
    p1.pesoAproximado.append(row[5])
    p1.corCabelo.append(row[6])
    p1.corPele.append(row[7])
    p1.corOlhos.append(row[8])
    p1.transtornoMental.append(row[9])
    p1.imagem.append(row[10])
    p1.marcaCaracteristica.append(row[11])

    # criando instancia de Local
    l1 = onto.Local()
    l1.latitude.append(row[12])
    l1.longitude.append(row[13])

    # criando instancia de Desaparecimento
    d1 = onto.Desaparecimento()
    d1.fonte.append(row[14])
    d1.ultimaHoraVista.append(row[15])
    d1.dataDesaparecimento.append(row[16])
    d1.informacoes.append(row[17])

    # criando instancia de Bairro
    b1 = onto.Bairro()
    b1.nomeBairro.append(row[18])

    # criando instancia de Cidade
    c1 = onto.Cidade()
    c1.nomeCidade.append(row[19])

    # criando instancia de UF
    uf = onto.UF()
    uf.sigla.append(row[20])

    # criando relacoes
    d1.estaAssociado = [p1]
    d1.ocorreuEm = [l1]

    l1.eUmPontoDe = [b1]
    b1.eBairroDe = [c1]
    c1.eCidadeDe = [uf]

# arquivo de saida
onto.save(file = "instancias.owl", format = "rdfxml")
      